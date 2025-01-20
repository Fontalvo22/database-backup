from src.strategies.frecuency_strategies.frecuency_strategy import FrecuencyStrategy


class FrecuencyContext:
    def __init__(self, strategy):
        self.strategy = FrecuencyStrategy()
    
    def set_frecuency(self):
        return self.strategy.set_frecuency()