from sqlalchemy import create_engine
from sqlalchemy.engine import CursorResult
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import Union


class DatabaseConnection:

    def __init__(self, driver: str, username: str, password: str, host: str, name: str, port: Union[int, str] = 5432):
        self.driver = driver
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.name = name
        self.db_path = self.__set_database()
        self.engine = self.__set_engine()

    def __set_database(self):
        return '{}://{}:{}@{}:{}/{}'.format(self.driver, self.username, self.password, self.host, self.port, self.name)

    def __set_engine(self):
        return create_engine(self.db_path, pool_size=20, max_overflow=0)

    def execute(self, sql_query: str, params: dict = None) -> CursorResult:
        sql_query = text(sql_query)

        with self.engine.connect() as conn:
            with Session(bind=conn) as session:
                result = session.execute(statement=sql_query, params=params)

                session.commit()

        return result
