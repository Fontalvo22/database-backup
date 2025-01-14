from src.settings import MONGO_DB_SETTINGS, MONGO_URI, DATABASE_TYPE
import subprocess
import os

from pymongo import MongoClient

class MongoDB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls)
            cls._instance.connect(MONGO_URI)
        return cls._instance

    def connect(self, mongo_uri):
        try:
            self.client = MongoClient(mongo_uri)


            self.database = self.client[MONGO_DB_SETTINGS['db_name']]
            self.database.get_collection("products")


        except Exception as error:
            raise error
    
    def backup(self):
        try:
            project_root = os.path.dirname(os.path.abspath(__file__))
            subprocess.run(
                ["mongodump", "--uri", MONGO_URI, "--db", MONGO_DB_SETTINGS['db_name'], "--out", f"{project_root}/../../backups/{DATABASE_TYPE}"],
                check=True,
                capture_output=True,
                text=True
            )

            print("Backup successful!")
        except subprocess.CalledProcessError as e:
            print("Error during backup:", e.stderr)
