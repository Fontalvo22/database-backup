from src.settings import POSTGRE_SETTINGS, DATABASE_TYPE, DATABASE_NAME
import subprocess
import os
import psycopg2

class PostgreSql:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PostgreSql, cls).__new__(cls)
            cls._instance.connect(POSTGRE_SETTINGS)

        return cls._instance

    def connect(self, credentials):
        try:
            self.client = psycopg2.connect(f"dbname={DATABASE_NAME} user={credentials['username']} password={credentials['password']} host={credentials['host']}")
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
                ["pg_dump", "-h", POSTGRE_SETTINGS['host'], "-U", POSTGRE_SETTINGS['username'], "-d", DATABASE_NAME, "-f", f"{project_root}/backups/{DATABASE_TYPE}/{DATABASE_NAME}/{DATABASE_NAME}.sql"],
                check=True,
                capture_output=True,
                text=True,
                env={"PGPASSWORD": POSTGRE_SETTINGS['password']}
            )

            print("Backup successful!")
        except subprocess.CalledProcessError as e:
            print("Error during backup:", e.stderr)
