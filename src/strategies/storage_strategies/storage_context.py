from src.strategies.storage_strategies.local_strategy import LocalStrategy

class StorageContext:
    def __init__(self, strategy):
        if strategy == 'local':
            self.strategy = LocalStrategy()
    
    def save(self):
        self.strategy.save()