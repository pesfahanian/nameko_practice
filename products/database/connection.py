from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database

from settings import DB_PATH

Base = declarative_base()


class SQLite:
    def __init__(self):
        database_url = f'sqlite:///{DB_PATH}'
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        Session = sessionmaker(bind=self.engine)
        self.session = scoped_session(Session)
