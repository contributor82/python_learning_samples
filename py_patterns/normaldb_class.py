"""Module for normal database"""
import sqlite3
from typing import Self


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