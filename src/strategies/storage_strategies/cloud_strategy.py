from src.strategies.storage_strategies.storage_strategy import StorageStrategy
import boto3

from dotenv import load_dotenv
import os

load_dotenv()


class CloudStrategy(StorageStrategy):

    def save(self):
        try:
            s3 = boto3.resource('s3')

            databases_cases = {
                "mysql": "MYSQL_",
                "postgre": "POSTGRE_",
                "mongodb": "MONGO_DB"
            }

            database_name = databases_cases[os.getenv('DATABASE_TYPE')]+"_NAME"

            backup_zip = self.package(os.getenv(database_name), os.getenv('DATABASE_TYPE'))+".zip"


            with open(backup_zip, 'rb') as data:
                result = s3.Bucket(os.getenv('AWS_BUCKET_NAME')).put_object(Key=f"{os.getenv(database_name)}-{os.getenv('DATABASE_TYPE')}.zip", Body=data)
                print("Backup saved succesfully to cloud!")
        except Exception as e:
            print(f"An error occurred: {e}")


    def load(self) -> str:
        with open(self.path, 'r') as file:
            return file.read()