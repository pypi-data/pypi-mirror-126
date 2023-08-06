from logging import Logger
import threading
from typing import Callable, List
from mycli.packages.special.main import COMMANDS
from .sql_analyze import SQLAnalyze
from .sql_fetch import SqlFetch
from mariadb_kernel.mariadb_client import MariaDBClient
from mariadb_kernel.client_config import ClientConfig
from prompt_toolkit.document import Document
from threading import Thread, Event


class Refresher(object):
    def __init__(self, executor: SqlFetch, log: Logger) -> None:
        self.executor = executor
        self.fetch_keywords = self.executor.keywords()
        self.fetch_functions = self.executor.sql_functions()
        self.log = log

        self.completer = None
        self.refresh_thread = None
        self.stop_condition = Event()

    def stop_and_wait(self):
        # No previous refresh sequence was executed
        if not self.refresh_thread:
            return
        self.stop_condition.set()
        self.refresh_thread.join()
        self.stop_condition.clear()

    def wait_for_results(self):
        self.refresh_thread.join()
        return self.completer

    def refresh_databases(self):
        self.completer.extend_database_names(self.executor.databases())

    def refresh_schemata(self):
        # schemata - In MySQL Schema is the same as database. But for mycli
        # schemata will be the name of the current database.
        self.completer.extend_schemata(self.executor.dbname)
        self.completer.set_dbname(self.executor.dbname)

    def refresh_tables(self):
        self.completer.extend_relations(self.executor.tables(), kind="tables")
        self.completer.extend_columns(self.executor.table_columns(), kind="tables")

    def refresh_users(self):
        self.completer.extend_users(self.executor.users())

    def refresh_functions(self):
        self.completer.extend_functions(self.executor.functions())

    def refresh_special(self):
        self.completer.extend_special_commands(COMMANDS.keys())

    def refresh_show_commands(self):
        self.completer.extend_show_items(self.executor.show_candidates())

    def refresh_database_tables(self):
        self.completer.extend_tables(self.executor.database_tables())

    def refresh_variables(self):
        self.completer.extend_global_variables(self.executor.global_variables())
        self.completer.extend_session_variables(self.executor.session_variables())

    def refresh_all(self):
        self.completer = SQLAnalyze(self.log, True)
        refresh_func_list: List[Callable] = [
            self.refresh_databases,
            self.refresh_schemata,
            self.refresh_tables,
            self.refresh_users,
            self.refresh_functions,
            self.refresh_special,
            self.refresh_show_commands,
            self.refresh_database_tables,
            self.refresh_variables,
        ]
        for refresh_func in refresh_func_list:
            refresh_func()
            if self.stop_condition.is_set():
                return

        self.completer.set_keywords(self.fetch_keywords)
        self.completer.set_functions(self.fetch_functions)

    def refresh(self):
        self.refresh_thread = Thread(target=self.refresh_all)
        self.refresh_thread.start()


class Autocompleter(object):
    def __init__(
        self,
        mariadb_client: MariaDBClient,
        config: ClientConfig,
        log: Logger,
    ) -> None:
        self.log = log

        self.completer = SQLAnalyze(log, True)

        # A client connection is already established, so things shouldn't go wrong here
        # But in case the unexpected happens, there's nothing we can do here, exception
        # needs to be propagated upwards
        self.log.info("Starting a client connection used in code completion")
        self.completion_mariadb_client = MariaDBClient(log, config)
        self.completion_mariadb_client.start()

        self.executor = SqlFetch(self.completion_mariadb_client, log)
        self.code_block_executor = SqlFetch(mariadb_client, log)

        self.refresher = Refresher(self.executor, log)

        self.refresh()

    def refresh(self):
        code_block_db_name = self.code_block_executor.get_db_name()
        if self.executor.dbname != code_block_db_name and code_block_db_name != "":
            self.completion_mariadb_client.run_statement(
                f"use {code_block_db_name}"
            )  # TODO: to be replaced with SQLFetch functionality
            self.executor.dbname = code_block_db_name

        # Stop any previous refresh operation and wait for child thread to die
        self.refresher.stop_and_wait()

        # Dispatch refresh sequence again
        self.refresher.refresh()

    # Sync with refresher to get an up-to-date SQLAnalyze object
    def sync_data(self):
        new_completer = self.refresher.wait_for_results()
        self.completer.reset_completions(new_completer)

    def get_suggestions(self, code: str, cursor_pos: int):
        self.sync_data()

        result = self.completer.get_completions(
            document=Document(text=code, cursor_position=cursor_pos),
            complete_event=None,
            executor=self.executor,
            smart_completion=True,
        )
        return list(result)

    def shutdown(self):
        self.log.info("Shutting down code completion client connection")
        self.completion_mariadb_client.stop()
