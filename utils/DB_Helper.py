import os
import psycopg2
from psycopg2 import OperationalError
from abc import ABC, abstractmethod

class DatabaseHelper(ABC):
    @abstractmethod
    def get(self, query, params=None):
        pass

    @abstractmethod
    def set(self, query, params=None):
        pass

    @abstractmethod
    def close(self):
        pass


class DBHelper(DatabaseHelper):
    def __init__(self):
        self.conn = None
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.conn = psycopg2.connect(
                dbname='HospitalMangmentSystem',
                user=os.getenv('postgree') ,
                password=os.getenv('Deem1425') ,
                host='localhost',
                port='5433'
            )
            print("Database connection established")
        except OperationalError as e:
            print(f"Error connecting to database: {e}")
            self.conn = None

    def get(self, query, params=None):
        self.check_connection()
        return self.fetch_all(query, params)

    def set(self, query, params=None):
        self.check_connection()
        self.execute_query(query, params)

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed")

    def check_connection(self):
        if self.conn is None or self.conn.closed != 0:
            print("Re-establishing database connection...")
            self.connect_to_db()

    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, params)
            self.conn.commit()
        except Exception as e:
            print(f"Query execution error: {e}")
            self.conn.rollback()
        finally:
            cursor.close()

    def fetch_all(self, query, params=None):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except Exception as e:
            print(f"Fetch error: {e}")
            return []
        finally:
            cursor.close()
