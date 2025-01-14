BACKUP_FRECUENCY = "daily"

DATABASE_TYPE = "postgre"

MONGO_DB_SETTINGS = {
    'host': 'host.docker.internal',
    'port': 27018,
    'db_name': 'shop',
    'username': 'root',
    'password': 'example',
    'authSource': 'admin'
}

MYSQL_SETTINGS = {
    'host': 'mysql',
    'port': 3306,
    'db_name': 'shop',
    'username': 'root',
    'password': 'example'
}

POSTGRE_SETTINGS = {
    'host': 'postgres',
    'port': 5432,
    'db_name': 'shop',
    'username': 'root',
    'password': 'example'
}

DATABASE_NAME = 'shop'

MONGO_URI = f"mongodb://{MONGO_DB_SETTINGS['username']}:{MONGO_DB_SETTINGS['password']}@{MONGO_DB_SETTINGS['host']}:{MONGO_DB_SETTINGS['port']}/?authSource={MONGO_DB_SETTINGS['authSource']}"

STORAGE_TYPE = "local"


# mongodb://root:example@localhost:27018/?authSource=admin