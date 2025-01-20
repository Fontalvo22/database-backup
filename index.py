
from src.strategies.database_strategies.database_context import DatabaseContext
from src.strategies.storage_strategies.storage_context import StorageContext
from src.strategies.frecuency_strategies.frecuency_context import FrecuencyContext

from dotenv import load_dotenv
import os


load_dotenv()


database = DatabaseContext(os.getenv('DATABASE_TYPE'))
database.backup()

# storage = StorageContext(os.getenv('STORAGE_TYPE'))
# storage.save()

frecuency = FrecuencyContext(os.getenv('BACKUP_FREQUENCY'))
frecuency.set_frecuency()