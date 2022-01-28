from os import getenv

from pymongo import MongoClient
from dotenv import load_dotenv


class MongoDB:
    """ CRUD """
    load_dotenv()

    def __init__(self, cluster: str, table: str):
        self.cluster = cluster
        self.table = table

    def _connect(self):
        return MongoClient(getenv("MONGO_URL"))[self.cluster][self.table]

    def create(self, data: dict):
        self._connect().insert_one(dict(data))

    def read(self, query: dict):
        return self._connect().find(query, {"_id": False})

    def update(self, query: dict, update_data: dict):
        self._connect().update_many(query, {"$set": update_data})

    def delete(self, query: dict):
        self._connect().delete_many(query)


if __name__ == '__main__':
    mongo = MongoDB("TestCluster", "TestTable")
    # mongo.delete({})
    # mongo.create({
    #     "id": 987654321,
    #     "Name": "Tony Stark",
    # })
    # mongo.update({"id": 987654321}, {"Name": "Ironman"})
    # mongo.create({'id': 123456789, 'Name': 'Steve Rodgers'})
    print(*mongo.read({}))
