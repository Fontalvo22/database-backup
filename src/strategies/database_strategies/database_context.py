# context class
from src.strategies.database_strategies.mongo_strategy import MongoStrategy
from src.strategies.database_strategies.mysql_strategy import MySqlStrategy
from src.strategies.database_strategies.postgree_sql import PostgreStrategy

class DatabaseContext:
    strategy = None

    def __init__(self, strategy):
        if strategy == 'MongoDB':
            self.strategy = MongoStrategy()

        if strategy == 'mysql':
            self.strategy = MySqlStrategy()
        if strategy == 'postgre':
            self.strategy = PostgreStrategy()
            
    def set_strategy(self, strategy):
        self.strategy = strategy

    def connect(self):
        return self.strategy.connect()
    
    def backup(self):
        return self.strategy.backup()

    