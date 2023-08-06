from typing import Dict, List, Union
from bs4.element import Tag

from sqlparse.sql import Function, Identifier, IdentifierList, Parenthesis, Values
from sqlparse.tokens import Keyword, Punctuation, _TokenType
from .autocompleter import Autocompleter
import re
from .completion_engine import suggest_type, last_word
import sqlparse
from bs4 import BeautifulSoup
import pandas


def first_word(text):
    if not text:  # Empty string
        return ""
    else:
        regex = re.compile(r"^(\w+)")
        matches = regex.search(text)
        if matches:
            return matches.group(0)
        else:
            return ""


def convert_help_text_to_beautiful_html(text):
    regex_for_url = r"(https://.+/)"
    result = re.sub(
        regex_for_url,
        r"<a href='\1' target='_blank'>\1</a>",
        text,
        flags=re.MULTILINE | re.IGNORECASE,
    )

    regex_for_header = r"^Name:.+\nDescription:"
    result = re.sub(regex_for_header, "", result, flags=re.MULTILINE | re.IGNORECASE)
    header_style = "style='color:#0045ad;margin:0'"
    regex_for_syntax_header = r"^Syntax"
    result = re.sub(
        regex_for_syntax_header,
        f"<h3 {header_style}>Syntax</h3>",
        result,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    regex_for_description_header = r"^Description"
    result = re.sub(
        regex_for_description_header,
        f"<h3 {header_style}>Description</h3>",
        result,
        flags=re.MULTILINE | re.IGNORECASE,
    )

    regex_for_examples_header = r"^Examples"
    result = re.sub(
        regex_for_examples_header,
        f"<h3 {header_style}>Examples</h3>",
        result,
        flags=re.MULTILINE | re.IGNORECASE,
    )

    regex_for_dashes = r"^[-]+"
    result = re.sub(regex_for_dashes, "", result, flags=re.MULTILINE)

    result = result.replace("\n\n", "\n").lstrip("\n").replace("\n", "<br/>")

    return result


class Introspector:
    def get_instropection(
        self, code: str, cursor_pos: int, autocompleter: Autocompleter
    ):
        completer = autocompleter.completer
        # return word's type and word's text
        last_partial_token_right = first_word(code[cursor_pos:])
        last_partial_token_left = last_word(code[:cursor_pos:])
        word = last_partial_token_left + last_partial_token_right

        # get word start's position and end's position
        start_position = cursor_pos - len(last_partial_token_left)
        end_position = cursor_pos + len(last_partial_token_right)
        suggestion = suggest_type(code, code[:start_position])
        suggest_dict = {}
        for suggest in suggestion:
            type = suggest.get("type")
            if type:
                suggest_dict[type] = suggest
        print(f"suggest_dict: {suggest_dict}")
        # Need to check it is being suggested and it exists or not
        # priority: column_hint -> column -> table -> database -> function -> keyword
        if suggest_dict.get("column_hint"):
            # for statement like 「insert into t1 (a int, b int, c int) VALUES (」 would provide column hint
            parsed_before_cursor = sqlparse.parse(code[:end_position])
            if len(parsed_before_cursor) > 0:
                tokens: List[_TokenType] = parsed_before_cursor[0].tokens
                last_match_token_text: str = ""
                hint = ""  # based on the text before 「VALUES」 and after 「insert into」 to get hint
                value_index = 0
                table_name = ""
                for token in tokens[::-1]:
                    if token.ttype == Punctuation and str(token) == "(":
                        last_match_token_text = str(token).lower()
                    elif (
                        last_match_token_text == "("
                        and token.ttype == Keyword
                        and str(token).lower() == "values"
                    ) or isinstance(token, Values):
                        last_match_token_text = "values"
                    elif (
                        last_match_token_text == "values"
                        and token.ttype == Keyword
                        and str(token).lower() == "into"
                    ):

                        last_match_token_text = str(token).lower()
                        next_token = parsed_before_cursor[0].token_next(
                            parsed_before_cursor[0].token_index(token)
                        )
                        if next_token != (None, None) and next_token and next_token[1]:
                            table_name = next_token[1].get_name()
                    elif (
                        last_match_token_text == "into"
                        and str(token).lower() == "insert"
                    ):
                        return {
                            "type": "column_hint",
                            "hint": hint,
                            "value_index": value_index,
                            "table_name": table_name,
                        }
                    elif last_match_token_text == "values":
                        # accumulate text between 「insert into」 and 「values (」
                        # !!! sqlparse sometimes would resolve Column to Function
                        if isinstance(token, Function):
                            for t in token.tokens:
                                if isinstance(t, Parenthesis):
                                    for in_parenthesis_token in t.tokens:
                                        # (a) => [<Punctuation '(' at 0x7F5AB584EFA0>, <Identifier 'a' at 0x7F5AB5841DD0>, <Punctuation ')' at 0x7F5AB58510A0>]
                                        # (a, b, c) => [<Punctuation '(' at 0x7FE26C6120A0>, <IdentifierList 'a, b, c' at 0x7FE26C603D60>, <Punctuation ')' at 0x7FE26C6123A0>]
                                        if isinstance(
                                            in_parenthesis_token, IdentifierList
                                        ):
                                            cols: List[str] = []
                                            cur_col_text = ""
                                            for curToken in in_parenthesis_token.tokens:
                                                if (
                                                    curToken.ttype == Punctuation
                                                    and str(curToken) in "()"
                                                ):
                                                    continue
                                                if (
                                                    curToken.ttype == Punctuation
                                                    and str(curToken) == ","
                                                ):
                                                    cols.append(cur_col_text.lstrip())
                                                    cur_col_text = ""
                                                else:
                                                    cur_col_text += str(curToken)
                                            cols.append(cur_col_text.lstrip().rstrip())
                                            if value_index >= len(cols):
                                                return {
                                                    "type": "column_hint",
                                                    "hint": "out of column",
                                                }
                                            hint = cols[value_index].lstrip().rstrip()
                                        elif isinstance(
                                            in_parenthesis_token, Identifier
                                        ):
                                            if value_index >= 1:
                                                return {
                                                    "type": "column_hint",
                                                    "hint": "out of column",
                                                }
                    # VALUES (1 ,       => <Keyword 'VALUES' at 0x7F01FBB76FA0>, <Whitespace ' ' at 0x7F01FBB9F040>, <Punctuation '(' at 0x7F01FBB9F0A0>, <Integer '1' at 0x7F01FBB9F100>, <Whitespace ' ' at 0x7F01FBB9F160>, <Punctuation ',' at 0x7F01FBB9F1C0>]
                    # VALUES (1, 2      => <Keyword 'VALUES' at 0x7F01FBB92F40>, <Whitespace ' ' at 0x7F01FBB8DCA0>, <Punctuation '(' at 0x7F01FBB8DD60>, <IdentifierList '1 , 2' at 0x7F01DDDF4660>]
                    # VALUES (1, 2, 3   => <Keyword 'VALUES' at 0x7F01FBB92F40>, <Whitespace ' ' at 0x7F01FBB8DCA0>, <Punctuation '(' at 0x7F01FBB8DD60>, <IdentifierList '1 , 2' at 0x7F01DDDF4660>], <Punctuation ',' at 0x7F3CB98F92E0>]
                    if last_match_token_text == "" and str(token) == ",":
                        value_index += 1
                    if isinstance(token, IdentifierList):
                        for t in token.tokens:
                            if t.ttype == Punctuation and str(t) == ",":
                                value_index += 1
        if suggest_dict.get("column"):
            # check this is function or not
            parsed_after_cursor = sqlparse.parse(code[end_position:])
            if len(parsed_after_cursor) > 0:
                parsed_tokens = parsed_after_cursor[0].tokens
                print(f"parsed_tokens : {parsed_tokens}")
                if len(parsed_tokens) > 0:
                    if suggest_dict.get("function") and isinstance(
                        parsed_tokens[0], Parenthesis
                    ):
                        if word in [
                            function.lower() for function in completer.functions
                        ]:
                            return {"word": word, "type": "function"}

            # if suggest_dict's column has tables not empty, use that as table
            tables = suggest_dict["column"].get("tables")
            curDB: Union[Dict, None] = completer.dbmetadata["tables"].get(
                completer.dbname
            )
            if len(tables) > 0:
                if tables[0][1] != None and curDB:
                    if curDB.get(tables[0][1]) and (
                        word in curDB[tables[0][1]]
                        or f"`{word}`" in curDB[tables[0][1]]
                    ):
                        return {
                            "word": word,
                            "type": "column",
                            "database": completer.dbname,
                            "table": tables[0][1],
                        }
            # search all table for finding which table contains this column
            if curDB:
                for key in curDB.keys():
                    if word in curDB[key] or f"`{word}`" in curDB[key]:
                        # maybe this is wrong
                        return {
                            "word": word,
                            "type": "column",
                            "database": completer.dbname,
                            "table": key,
                        }
            # actively fetch system table's column
            if len(tables) > 0:
                database = tables[0][0]
                table = tables[0][1]
                if database and table:
                    database_table_dict = completer.dbmetadata["tables"].get(database)
                    if database_table_dict is None:
                        # fetch the table's column
                        column_list = (
                            autocompleter.executor.get_specific_table_columns_list(
                                table, database
                            )
                        )
                        if word.lower() in [column.lower() for column in column_list]:
                            return {
                                "word": word,
                                "type": "column",
                                "database": database,
                                "table": table,
                            }
        if suggest_dict.get("table"):
            # If suggest_dict's table has schema field. Regard that as the database, which table belongs
            if suggest_dict["table"].get("schema"):
                table_dbName = suggest_dict["table"].get("schema")
                for t in completer.database_tables:
                    if t[0] == table_dbName and (t[1] == word or t[1] == f"`{word}`"):
                        return {"word": word, "type": "table", "database": table_dbName}
            else:
                table_dbName = completer.dbname
                curDB = completer.dbmetadata["tables"].get(table_dbName)
                if curDB:
                    if curDB.get(word) or curDB.get(f"`{word}`"):
                        return {"word": word, "type": "table", "database": table_dbName}
        if suggest_dict.get("database") and word in completer.databases:
            return {"word": word, "type": "database"}
        if suggest_dict.get("function") and word.lower() in [
            function.lower() for function in completer.functions
        ]:
            return {"word": word, "type": "function"}
        if suggest_dict.get("keyword") and word.lower() in [
            keyword.lower() for keyword in completer.keywords
        ]:
            return {"word": word, "type": "keyword"}

    def render_doc_header(self, name: str):
        return f"<h2 style='color: #0045ad'>{name}</h2>"

    def inspect(
        self, code: str, cursor_pos: int, autocompleter: Autocompleter
    ) -> Union[str, None]:
        autocompleter.sync_data()

        result = self.get_instropection(code, cursor_pos, autocompleter)
        if result:
            word_type = result.get("type")
            word = result.get("word")
            if word_type == "keyword":
                # some special keyword would provide more information
                # such as `user` keyword would list all user in database.
                if word:
                    if word == "user":
                        # would show all user list
                        users = autocompleter.executor.users(html=True)
                        df = re.sub(
                            " +",
                            "",
                            pandas.read_html(users)[0].to_string(
                                index=False, header=False
                            ),
                        )
                        plain_mime = "Users:" + "\n" + df.strip("\n")
                        return users, plain_mime

                return "", ""
            elif word_type == "function":
                if word:
                    plain_help = autocompleter.executor.get_help_text(word)
                    # convert text to html and beautify plain_help
                    html = convert_help_text_to_beautiful_html(plain_help)
                    return (
                        f"{self.render_doc_header('Function')}{''.join(html)}",
                        plain_help,
                    )
                return f"{self.render_doc_header('function')}", ""
            elif word_type == "database":
                if word:
                    tables_html = autocompleter.executor.get_tables_in_db_html(word)

                    try:
                        df = re.sub(
                            " +",
                            "",
                            pandas.read_html(tables_html)[0].to_string(
                                index=False, header=False
                            ),
                        )
                        plain_mime = "Tables:" + "\n" + df.strip("\n")
                    except:
                        plain_mime = ""

                    return (
                        f"{self.render_doc_header('Database')}{tables_html}",
                        plain_mime,
                    )
                else:
                    return f"{self.render_doc_header('database')}", ""
            elif word_type == "table":
                db_name = result.get("database")
                if word and db_name:
                    table_html = autocompleter.executor.get_table_schema_html(
                        word, db_name
                    )
                    limit_num = 5
                    table_rows_html = autocompleter.executor.get_partial_table_row_html(
                        word, db_name, limit_num
                    )

                    plain_mime = (
                        f"{word} table\n\nPlease expand to see more information."
                    )

                    return (
                        f"""{self.render_doc_header('Table')}
                               <b>First {limit_num} rows of the {word} table</b><br/>
                               {table_rows_html}
                               <b>Table Schema</b><br/>
                               {table_html}""",
                        plain_mime,
                    )
                else:
                    return f"{self.render_doc_header('table')}", ""
            elif word_type == "column":
                table_name = result.get("table")
                db_name = result.get("database")
                if word and db_name and table_name:
                    column_html = autocompleter.executor.get_column_type_html(
                        word, table_name, db_name
                    )
                    limit_num = 5
                    column_rows_html = autocompleter.executor.get_column_row_html(
                        word, table_name, db_name, limit_num
                    )

                    try:
                        df_column = re.sub(
                            " +",
                            "",
                            pandas.read_html(column_html)[0].to_string(
                                index=False, na_rep="NULL", justify="left", header=False
                            ),
                        )
                        df_rows = re.sub(
                            " +",
                            "",
                            pandas.read_html(column_rows_html)[0].to_string(
                                index=False, na_rep="NULL", justify="left"
                            ),
                        )
                        plain_mime = (
                            f"Datatype:"
                            + "\n"
                            + df_column.strip("\n")
                            + "\n\n"
                            + f"First {limit_num} rows of the {word} column:"
                            + "\n"
                            + df_rows.strip("\n")
                        )
                    except:
                        plain_mime = ""

                    return (
                        f"""{self.render_doc_header('Column')}
                               {column_html}<br/>
                               <b>First {limit_num} rows of the {word} column</b><br/>
                               {column_rows_html}""",
                        plain_mime,
                    )
                else:
                    return f"{self.render_doc_header('column')}", ""
            elif word_type == "column_hint":
                hint = result.get("hint")
                value_index = result.get("value_index")
                table_name = result.get("table_name")
                if (
                    hint != "out of column"
                    and value_index != None
                    and table_name != None
                ):
                    result = autocompleter.executor.get_column_type_list(
                        table_name, autocompleter.completer.dbname
                    )
                    if hint == "":
                        # ex: insert into t1 VALUES (1,2,
                        if int(value_index) >= len(result):
                            hint = "out of column"
                        else:
                            for i, item in enumerate(result):
                                if i == value_index:
                                    hint = item.name + " " + item.type
                    else:
                        for item in result:
                            if item.name == hint:
                                hint = item.name + " " + item.type
                return hint, hint

        return "", ""
