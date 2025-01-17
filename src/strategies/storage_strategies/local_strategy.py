from src.strategies.storage_strategies.storage_strategy import StorageStrategy
import os
import shutil

class LocalStrategy(StorageStrategy):
    
    def __init__(self):
        project_root = os.getcwd()
        self.path = f"{project_root}/backups/{ os.getenv('DATABASE_TYPE')}"
        
    def save(self):
        
        databases_cases = {
                "mysql": "MYSQL_",
                "postgre": "POSTGRE_",
                "mongodb": "MONGO_DB_"
            }

        database_name = databases_cases[os.getenv('DATABASE_TYPE')]+"DB_NAME"

        self.package(os.getenv(database_name), os.getenv('DATABASE_TYPE'))+".zip"


    def load(self) -> str:
        with open(self.path, 'r') as file:
            return file.read()