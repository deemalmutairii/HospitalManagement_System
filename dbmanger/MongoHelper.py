from pymongo import MongoClient

class MongoHelper:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="testdb"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert(self, collection_name, data):
        self.db[collection_name].insert_one(data)

    def get(self, collection_name, query=None):
        if query is None:
            query = {}
        return self.db[collection_name].find(query)

    def close(self):
        self.client.close()
