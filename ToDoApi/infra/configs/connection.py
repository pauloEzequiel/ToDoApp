from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infra.configs.base import Base
import os

class DBConnectionHandler:

    def __init__(self) -> None:
        #db_path = "database/"
        #self.__create_database_dir(db_path)
        self.__connection_string = 'mysql+mysqldb://usr_todo:usr_todo@db:3306/bd_todo'
        self.__engine = self.__create_database_engine()
        self.__create_Bd()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine
   
    def __create_database_dir(self,db_path):
        if not os.path.exists(db_path):
          os.makedirs(db_path)

    def __create_Bd(self):
        if not database_exists(self.__engine.url):
          create_database(self.__engine.url) 
 
        Base.metadata.create_all(self.__engine)

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()