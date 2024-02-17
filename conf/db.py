import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URI: postgresql://username:password@host.port/database

file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
host = config.get('DEV_DB', 'DOMAIN')
port = config.get('DEV_DB', 'PORT')
db = config.get('DEV_DB', 'DB_NAME')

URI = f'postgresql://{user}:{password}@{host}:{port}/{db}'

engine = create_engine(URI, echo=False, pool_size=5, max_overflow=0)  # pool_size кол соед к базе данных
DBSession = sessionmaker(bind=engine)
session = DBSession()

# USER=postgres
# PASSWORD=zimzim
# DB_NAME=mydata
# DOMAIN=localhost
# PORT=5432
