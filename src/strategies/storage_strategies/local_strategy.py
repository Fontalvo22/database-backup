from src.strategies.storage_strategies.storage_strategy import StorageStrategy
import os
import shutil

class LocalStrategy(StorageStrategy):
    
    def __init__(self):
        project_root = os.getcwd()
        self.path = f"{project_root}/backups/{ os.getenv('DATABASE_TYPE')}"
        
    def save(self):
        
        try:
            s3 = boto3.resource('s3')

            databases_cases = {
                "mysql": "MYSQL_",
                "postgre": "POSTGRE_",
                "mongodb": "MONGO_DB"
            }

            database_name = databases_cases[os.getenv('DATABASE_TYPE')]+"_NAME"

            self.package(os.getenv(database_name), os.getenv('DATABASE_TYPE'))+".zip"
            print("Backup saved succesfully to local storage!")
            
        except Exception as e:
            print(f"An error occurred: {e}")

    def load(self) -> str:
        with open(self.path, 'r') as file:
            return file.read()