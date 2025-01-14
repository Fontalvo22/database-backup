from src.settings import MONGO_DB_SETTINGS
from src.strategies.database_strategies.database_strategy import DatabaseStrategy
from src.database_entities.mongo_db import MongoDB

class MongoStrategy(DatabaseStrategy):
    client = None
    def connect(self):
        pass

    
    def backup(self):
        database = MongoDB()
        database.backup()
