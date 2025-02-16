import psycopg2
from utils.InformationMessages import DATABASE_CONNECTED, DATABASE_CLOSED, QUERY_EXECUTED
from utils.ErrorMessages import DATABASE_CONNECTION_ERROR
from utils.SlackHelper import SlackHelper

class PostgresHelper:
    def __init__(self, host, db_name, user, password, port=5432, slack_helper=None):
        self.slack_helper = slack_helper
        try:
            self.connection = psycopg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.cursor = self.connection.cursor()
            print(DATABASE_CONNECTED)
            if self.slack_helper:
                self.slack_helper.send_notification(DATABASE_CONNECTED)
        except Exception as e:
            print(f"{DATABASE_CONNECTION_ERROR}: {e}")
            if self.slack_helper:
                self.slack_helper.send_notification(f"{DATABASE_CONNECTION_ERROR}: {e}")

    def execute_query(self, query, params=None):
        """Execute a query and send a Slack notification if successful."""
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print(QUERY_EXECUTED)
            if self.slack_helper:
                self.slack_helper.send_notification(QUERY_EXECUTED)
        except Exception as e:
            print(f"Error executing query: {e}")

    def fetch_query(self, query, params=None):
        """Execute a query and fetch results."""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        """Close the connection and send a Slack notification."""
        self.cursor.close()
        self.connection.close()
        print(DATABASE_CLOSED)
        if self.slack_helper:
            self.slack_helper.send_notification(DATABASE_CLOSED)
