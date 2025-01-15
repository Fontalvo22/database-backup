from src.strategies.storage_strategies.storage_strategy import StorageStrategy
from src.settings import DATABASE_NAME, DATABASE_TYPE
import boto3


class CloudStrategy(StorageStrategy):

    def save(self):
        s3 = boto3.resource('s3')

        backup_zip = self.package(DATABASE_NAME, DATABASE_TYPE)+".zip"

        print(backup_zip)
        with open(backup_zip, 'rb') as data:
            result = s3.Bucket('franklinfontalvo').put_object(Key=f"{DATABASE_NAME}-{DATABASE_TYPE}.zip", Body=data)
        
        print(result)


    def load(self) -> str:
        with open(self.path, 'r') as file:
            return file.read()