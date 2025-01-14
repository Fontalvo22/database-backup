from src.strategies.database_strategies.database_strategy import DatabaseStrategy
from src.database_entities.postgresql import PostgreSql

class PostgreStrategy(DatabaseStrategy):
    def connect(self, *args, **kwargs):
        pass
    
    def backup(self):
        database = PostgreSql()
        database.backup()