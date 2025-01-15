import os
import shutil

class StorageStrategy:

    def save():
        pass

    def load():
        pass

    def package(self, database_name, database_type):

        project_root = os.getcwd()
        self.path = f"{project_root}/backups/{database_type}"

        backup_zip = f"{self.path}/{database_name}"
        shutil.make_archive(backup_zip, 'zip', backup_zip)
        shutil.rmtree(backup_zip)
        print(f"Backup compressed to {backup_zip}")

        return backup_zip