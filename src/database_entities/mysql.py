from src.settings import MYSQL_SETTINGS, DATABASE_TYPE, DATABASE_NAME
import subprocess
import os
import mysql.connector

class MySql:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MySql, cls).__new__(cls)
            cls._instance.connect(MYSQL_SETTINGS)

        return cls._instance

    def connect(self, credentials):
        try:
            self.client = mysql.connector.connect(host=credentials['host'], user=credentials['username'], passwd=credentials['password'], database=DATABASE_NAME)
            self.cursor = self.client.cursor()
            # self.database = self.client[MONGO_DB_SETTINGS['db_name']]
            # self.database.get_collection("products")
        except Exception as error:
            raise error
    
    def backup(self):
        try:      
            project_root = project_root = os.getcwd()
            
            if not os.path.exists(f"{project_root}/backups/{DATABASE_TYPE}/{DATABASE_NAME}"):
                os.makedirs(f"{project_root}/backups/{DATABASE_TYPE}/{DATABASE_NAME}")
            
            subprocess.run(
                ["mysqldump", "-h", MYSQL_SETTINGS['host'], "-u", MYSQL_SETTINGS['username'], f"-p{MYSQL_SETTINGS['password']}", "shop", "--result-file", f"{project_root}/backups/{DATABASE_TYPE}/{DATABASE_NAME}/{DATABASE_NAME}.sql"],
                check=True,
                capture_output=True,
                text=True
            )            
            
            print("Backup successful!")
        except subprocess.CalledProcessError as e:
            print("Error during backup:", e.stderr)
