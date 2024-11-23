from abc import ABC, abstractmethod

import psycopg2
from PySide6 import QtWidgets, QtSql


class DbTemplate(ABC):

    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def execute_query(self, sql_query, query_values=None):
        pass

    @abstractmethod
    def get_auto_increment_type(self):
        pass

    @abstractmethod
    def get_prepared_placeholder(self):
        pass


class SqLiteTemplate(DbTemplate):
    def __init__(self):
        super(SqLiteTemplate, self).__init__()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('../data/local/avia_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database", "Click cancel to exit...",
                                           QtWidgets.QMessageBox.Cancel)
            return False

        print('Connected to the SQlite database.')
        return True

    def execute_query(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def get_auto_increment_type(self):
        return 'integer primary key AUTOINCREMENT'

    def get_prepared_placeholder(self):
        return '?'


class PostgresqlTemplate(DbTemplate):
    def __init__(self):
        super(PostgresqlTemplate, self).__init__()
        self.connection = None

    def create_connection(self):
        postgres_host = '127.0.0.1'
        postgres_port = 5432
        account_db_user = 'postgres'

        try:
            with psycopg2.connect(user=account_db_user,
                                  host=postgres_host,
                                  port=str(postgres_port),
                                  database='postgres') as connect:
                print('Connected to the PostgreSQL server.')
                self.connection = connect
                self.connection.autocommit = True
                return True
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
            return False

    def execute_query(self, sql_query, query_values=None):
        cursor = self.connection.cursor()
        cursor.execute(sql_query, query_values)
        return cursor

    def close_connection(self):
        self.connection.close()

    def get_auto_increment_type(self):
        return 'serial primary key'

    def get_prepared_placeholder(self):
        return '%s'


class PSQLTemplate(DbTemplate):
    def __init__(self):
        super(PSQLTemplate, self).__init__()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase("QPSQL")
        print("Available drivers", db.drivers())

        db.setHostName("localhost")
        db.setDatabaseName("postgres")
        db.setUserName("postgres")
        db.setPort(5432)

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database", "Click cancel to exit...",
                                           QtWidgets.QMessageBox.Cancel)

            print('Last error', db.lastError().text())
            return False

        return True

    def execute_query(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def get_auto_increment_type(self):
        return 'serial primary key'
