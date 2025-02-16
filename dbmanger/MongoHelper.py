from pymongo import MongoClient
from utils.information_messages import DATABASE_CONNECTED, DOCUMENT_INSERTED, DATABASE_CLOSED
from utils.error_messages import DATABASE_CONNECTION_ERROR, SLACK_NOTIFICATION_FAILED
from utils.slack_helper import SlackHelper

class MongoHelper:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="testdb", slack_helper=None):
        self.slack_helper = slack_helper
        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            print(DATABASE_CONNECTED)
            if self.slack_helper:
                self.slack_helper.send_notification(DATABASE_CONNECTED)
        except Exception as e:
            print(f"{DATABASE_CONNECTION_ERROR}: {e}")
            if self.slack_helper:
                self.slack_helper.send_notification(f"{DATABASE_CONNECTION_ERROR}: {e}")

    def insert(self, collection_name, data):
        """Insert a document and send a Slack notification."""
        try:
            self.db[collection_name].insert_one(data)
            print(DOCUMENT_INSERTED)
            if self.slack_helper:
                self.slack_helper.send_notification(DOCUMENT_INSERTED)
        except Exception as e:
            print(f"Error inserting document: {e}")
            if self.slack_helper:
                self.slack_helper.send_notification(f"{SLACK_NOTIFICATION_FAILED.format(500)}: {e}")

    def get(self, collection_name, query=None):
        """Fetch documents from a collection."""
        if query is None:
            query = {}
        return self.db[collection_name].find(query)

    def close(self):
        """Close the connection and send a Slack notification."""
        self.client.close()
        print(DATABASE_CLOSED)
        if self.slack_helper:
            self.slack_helper.send_notification(DATABASE_CLOSED)
