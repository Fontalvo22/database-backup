from src.strategies.storage_strategies.local_strategy import LocalStrategy
from src.strategies.storage_strategies.cloud_strategy import CloudStrategy
class StorageContext:
    def __init__(self, strategy):
        if strategy == 'local':
            self.strategy = LocalStrategy()
        if strategy == 'cloud':
            print('holas')
            self.strategy = CloudStrategy()
    
    def save(self):
        self.strategy.save()