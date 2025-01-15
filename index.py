
from src.strategies.database_strategies.database_context import DatabaseContext
from src.strategies.storage_strategies.storage_context import StorageContext
from src.settings import DATABASE_TYPE, STORAGE_TYPE

database = DatabaseContext(DATABASE_TYPE)

database.backup()

storage = StorageContext(STORAGE_TYPE)
storage.save()

