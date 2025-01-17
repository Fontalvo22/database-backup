import subprocess

from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()



class MongoDB:
    _instance = None
    
    _mongo_uri = f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_HOST')}:{ os.getenv('MONGO_DB_PORT')}/?authSource={os.getenv('MONGO_DB_AUTH_SOURCE')}"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls)
            cls._instance.connect()
        return cls._instance

    def connect(self):
        try:
            self.client = MongoClient(self._mongo_uri)


            self.database = self.client[os.getenv('MONGO_DB_NAME')]
            self.database.get_collection("products")


        except Exception as error:
            print(error)
            exit()
    
    def backup(self):
        try:
            project_root = os.path.dirname(os.path.abspath(__file__))
            subprocess.run(
                ["mongodump", "--uri", self._mongo_uri, "--db", os.getenv('MONGO_DB_NAME'), "--out", f"{project_root}/../../backups/{os.getenv('DATABASE_TYPE')}"],
                check=True,
                capture_output=True,
                text=True
            )

            print("Backup successful!")
        except subprocess.CalledProcessError as e:
            print("Error during backup:", e.stderr)
