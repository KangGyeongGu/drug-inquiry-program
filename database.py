# database.py
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, port, database, user, password):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=host,
                port=port,
                database=database,
                user=user,
                password=password
            )
        except Error as e:
            raise e

    def execute_query(self, query, params=None, fetch=False, fetchall=False):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            if fetch:
                return cursor.fetchone()
            if fetchall:
                return cursor.fetchall()
            self.connection.commit()
        except Error as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
