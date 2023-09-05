"""Module for Database factory """
from .memdb_class import MemDB
from .normaldb_class import NormalDB
from typing import Self

class DbFactory:
    """Database factory """
    db_factory_instance: object = None
    name: str = 'Database factory'
    mem_db_instance: MemDB = MemDB()
    normal_db_instance: NormalDB = NormalDB()

    def __new__(cls) -> Self:
        """ Database factory class single instance  """
        return_db_factory_obj: Self
        if cls.db_factory_instance is None:
            cls.db_factory_instance = super().__new__(cls)

        return_db_factory_obj = cls.db_factory_instance # type: ignore
        return return_db_factory_obj

    def get_factory_name(self)-> str:
        """Get factory name"""
        return self.name

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
    db_factory_instance.get_factory_name()

    db_factory_instance_two =  DbFactory()
    db_factory_instance_two.get_factory_name()

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
