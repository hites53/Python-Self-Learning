from abc import ABCMeta, abstractmethod


class DBHandler(metaclass=ABCMeta):

    @abstractmethod
    def connect(self):
        return 

    @abstractmethod
    def select(self):
        return

    @abstractmethod
    def insert_or_update(self):
        return        



class PostgresDBHandler(DBHandler):

    def connect(self):
        print('Connecting to Postgres DB Server')
        return 

    def select(self):
        print('fetching records from Postgres')
        return

    def insert_or_update(self):
        print('Adding or updating records to Postgres')
        return 


class SQLServerDBHandler(DBHandler):

    def connect(self):
        print('Connecting to SQL Server')
        return 

    def select(self):
        print('fetching records from SQL Server')
        return

    def insert_or_update(self):
        print('Adding or updating records to SQL Server')
        return        


class DBFactory:
    # def __init__(self,name,*args,**kwargs):
    #     self.name = name

    @staticmethod
    def get_db_connector(name):
        from register import regitered_db

        all_classes = DBHandler.__subclasses__()
        for cls in all_classes:
            if cls.__name__ == regitered_db.get(name.lower()):
                return cls()
            



db = DBFactory.get_db_connector('sqlserver')
if db : db.connect()