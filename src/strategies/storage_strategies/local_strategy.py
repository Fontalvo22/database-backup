from src.strategies.storage_strategies.storage_strategy import StorageStrategy
from src.settings import DATABASE_NAME, DATABASE_TYPE
import os
import shutil

class LocalStrategy():
    
    def __init__(self):
        project_root = os.getcwd()
        self.path = f"{project_root}/backups/{DATABASE_TYPE}"

    def save(self):
        
        backup_zip = f"{self.path}/{DATABASE_NAME}"

        shutil.make_archive(backup_zip, 'zip', backup_zip)
        shutil.rmtree(backup_zip)
        print(f"Backup compressed to {backup_zip}")


    def load(self) -> str:
        with open(self.path, 'r') as file:
            return file.read()