import os
import subprocess
import psycopg2

from dotenv import load_dotenv

load_dotenv()

class PostgreSql:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PostgreSql, cls).__new__(cls)
            cls._instance.connect()

        return cls._instance

    def connect(self):
        try:
            self.client = psycopg2.connect(
                dbname=os.getenv('POSTGRE_DB_NAME'),
                user=os.getenv('POSTGRE_USERNAME'),
                password=os.getenv('POSTGRE_PASSWORD'),
                host=os.getenv('POSTGRE_HOST'),
                port=os.getenv('POSTGRE_PORT')
            )
            self.cursor = self.client.cursor()
        except Exception as error:
            print(error)
            exit()

    def backup(self):
        try:
            project_root = os.getcwd()
            backup_dir = os.path.join(project_root, 'backups', os.getenv('DATABASE_TYPE'), os.getenv('POSTGRE_DB_NAME'))

            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)

            backup_file = os.path.join(backup_dir, f"{os.getenv('POSTGRE_DB_NAME')}.sql")
            result = subprocess.run(
                ["pg_dump", "-h", os.getenv('POSTGRE_HOST'), "-U", os.getenv('POSTGRE_USERNAME'), "-d", os.getenv('POSTGRE_DB_NAME'), "-f", backup_file],
                check=True,
                capture_output=True,
                text=True,
                env={"PGPASSWORD": os.getenv('POSTGRE_PASSWORD')}
            )

            print("Backup successful:", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error during backup:", e.stderr)