import subprocess

from dotenv import load_dotenv
import os
load_dotenv()

import mysql.connector

class MySql:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MySql, cls).__new__(cls)
            cls._instance.connect()

        return cls._instance

    def connect(self):
        try:
            self.client = mysql.connector.connect(host=os.getenv('MYSQL_HOST'), user=os.getenv('MYSQL_USERNAME'), passwd=os.getenv('MYSQL_PASSWORD'), database=os.getenv('MYSQL_DB_NAME'))
            self.cursor = self.client.cursor()
            # self.database = self.client[MONGO_DB_SETTINGS['db_name']]
            # self.database.get_collection("products")
        except Exception as error:
            print(error)
            exit()
    
    def backup(self):
        try:      
            project_root = project_root = os.getcwd()
            
            if not os.path.exists(f"{project_root}/backups/{os.getenv('DATABASE_TYPE')}/{os.getenv('MYSQL_DB_NAME')}"):
                os.makedirs(f"{project_root}/backups/{os.getenv('DATABASE_TYPE')}/{os.getenv('MYSQL_DB_NAME')}")
            
            subprocess.run(
                ["mysqldump", "-h", os.getenv('MYSQL_USERNAME'), "-u", os.getenv('MYSQL_USERNAME'), f"-p{ os.getenv('MYSQL_PASSWORD')}", "shop", "--result-file", f"{project_root}/backups/{ os.getenv('DATABASE_TYPE')}/{os.getenv('MYSQL_DB_NAME')}/{os.getenv('MYSQL_DB_NAME')}.sql"],
                check=True,
                capture_output=True,
                text=True
            )            
            
            print("Backup successful!")
        except subprocess.CalledProcessError as e:
            print("Error during backup:", e.stderr)
