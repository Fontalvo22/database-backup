from src.strategies.database_strategies.database_strategy import DatabaseStrategy
from src.database_entities.mysql import MySql

class MySqlStrategy(DatabaseStrategy):
    def connect(self, *args, **kwargs):
        pass
    
    def backup(self):
        database = MySql()
        database.backup()