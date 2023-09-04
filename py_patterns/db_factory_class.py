import sqlite3
from typing import Self

class MemDB:
    """Memory Database class"""
    mem_db_instance: object = None
    mem_con: sqlite3.Connection = sqlite3.connect(':memory:')

    def __new__(cls) -> Self:
        """ Mem DB class single instance  """
        return_mem_db_obj: Self
        if cls.mem_db_instance is None:
            cls.mem_db_instance = super().__new__(cls)
        return_mem_db_obj = cls.mem_db_instance # type: ignore
        return return_mem_db_obj

class NormalDB:
    """Normal Database class """
    normal_db_instance: object = None
    db_con: sqlite3.Connection = sqlite3.connect('C:\\Data\\temp_database.db')

    def __new__(cls) -> Self:
        """ Normal DB class single instance  """
        return_normal_db_obj: Self
        if cls.normal_db_instance is None:
            cls.normal_db_instance = super().__new__(cls)
        return_normal_db_obj = cls.normal_db_instance # type: ignore
        return return_normal_db_obj

class DbFactory:
    """Database factory """
    db_factory_instance: object = None
    mem_db_instance: MemDB = MemDB()
    normal_db_instance: NormalDB = NormalDB()

    def __new__(cls) -> Self:
        """ Database factory class single instance  """
        return_db_factory_obj: Self
        if cls.db_factory_instance is None:
           cls.db_factory_instance = super().__new__(cls)
        return_db_factory_obj = cls.db_factory_instance # type: ignore
        return return_db_factory_obj

    def get_db_instance(self, db_type: str) -> object:
        """Get database or in memory database instance """
        db_instance: object = None
        if db_type != '':
            match db_type:
                case 'memory': db_instance = self.mem_db_instance
                case 'db': db_instance = self.normal_db_instance
                case _: pass
        return db_instance

if __name__ == '__main__':
    db_factory_instance =  DbFactory()
    db_factory_instance_two =  DbFactory()
    print(db_factory_instance is db_factory_instance_two)


    db_instance_one: object = None
    db_instance_one = db_factory_instance.get_db_instance('memory')
    if not db_instance_one is None:
       print(type(db_instance_one).__name__)

    db_instance_two: object = None
    db_instance_two = db_factory_instance.get_db_instance('memory')
    if not db_instance_two is None:
       print(type(db_instance_two).__name__)
       print(db_instance_one is db_instance_two)

    db_instance_one = None

    db_instance_one = db_factory_instance.get_db_instance('db')
    if not db_instance_one is None:
       print(type(db_instance_one).__name__)

    db_instance_two = None

    db_instance_two = db_factory_instance.get_db_instance('db')
    if not db_instance_two is None:
       print(type(db_instance_two).__name__)
       print(db_instance_one is db_instance_two)


