from dbmanger.PostgresHelper import PostgresHelper
from dbmanger.MongoHelper import MongoHelper
from utils.ErrorMessages import DATABASE_CONNECTION_ERROR


class DatabaseHelper:
    def __init__(self, db_type, config, slack_helper=None):
        """Initialize the appropriate database helper based on the provided type."""
        self.db_type = db_type.lower()
        self.slack_helper = slack_helper

        try:
            if self.db_type == 'postgres':
                self.db = PostgresHelper(
                    host=config.get('host', 'localhost'),
                    db_name=config.get('db_name', 'hospital_db'),
                    user=config.get('user', 'postgres_user'),
                    password=config.get('password', 'securepassword'),
                    port=config.get('port', 5432),
                    slack_helper=self.slack_helper
                )
            elif self.db_type == 'mongo':
                self.db = MongoHelper(
                    uri=config.get('uri', 'mongodb://localhost:27017/'),
                    db_name=config.get('db_name', 'hospital'),
                    slack_helper=self.slack_helper
                )
            else:
                raise ValueError("Unsupported database type. Please choose 'postgres' or 'mongo'.")

        except Exception as e:
            print(f"{DATABASE_CONNECTION_ERROR}: {e}")
            if self.slack_helper:
                self.slack_helper.send_notification(f"{DATABASE_CONNECTION_ERROR}: {e}")

    def execute_query(self, query, params=None):
        """Execute a query (Postgres only)."""
        if self.db_type == 'postgres':
            return self.db.execute_query(query, params)
        else:
            raise NotImplementedError("execute_query is only available for Postgres.")

    def fetch_query(self, query, params=None):
        """Fetch query results (Postgres only)."""
        if self.db_type == 'postgres':
            return self.db.fetch_query(query, params)
        else:
            raise NotImplementedError("fetch_query is only available for Postgres.")

    def insert(self, collection_name, data):
        """Insert a document (MongoDB only)."""
        if self.db_type == 'mongo':
            self.db.insert(collection_name, data)
        else:
            raise NotImplementedError("insert is only available for MongoDB.")

    def get(self, collection_name, query=None):
        """Fetch documents from a collection (MongoDB only)."""
        if self.db_type == 'mongo':
            return self.db.get(collection_name, query)
        else:
            raise NotImplementedError("get is only available for MongoDB.")

    def close(self):
        """Close the database connection."""
        self.db.close()
