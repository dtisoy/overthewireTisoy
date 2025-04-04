import sqlite3
from typing import Union, Dict


class DBManager:
    @classmethod
    def create_database(cls):
        """Create database overthewire and bandit_levels table."""
    
        try:
            connection = sqlite3.connect("overthewire.db")
            cursor = connection.cursor()
    
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS bandit_levels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    level INTEGER NOT NULL CHECK (level >= 0 AND level <= 35),
                    flag VARCHAR(500) NOT NULL
                )
            """)
    
            connection.commit()
            connection.close()
    
            print("Database and Tables successfully created.")
    
        except sqlite3.Error as error:
            print("Error while creating the database:", error)
    
    def insert_level(self, level, flag):
        """Insert a new level in bandit levels table."""
        connection = self.__create_connection()
        if connection is None:
            return
    
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO bandit_levels (level, flag) VALUES (?, ?)", (level, flag))
            connection.commit()
            print(f"Level {level} inserted succesfully.")
        except sqlite3.Error as error:
            print("Error while trying to insert level:", error)
            connection.rollback()
        finally:
            connection.close()

    def get_last_level(self) -> Union[Dict, None]:
        """Get the last record added in bandit_levels table."""
        connection = self.__create_connection()
        if connection is None:
            return None

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT level, flag FROM bandit_levels ORDER BY id DESC LIMIT 1")
            resultado = cursor.fetchone()
            if resultado:
                return resultado
            else:
                return None
        except sqlite3.Error as error:
            print("Error al obtener el último nivel:", error)
            return None
        finally:
            connection.close()

    # database connection and settings 
    @staticmethod
    def __dict_factory(cursor, row):
        fields = [column[0] for column in cursor.description]
        return {key: value for key, value in zip(fields, row)} 

    def __create_connection(self):
        
        """Create a connection to overthewire.db."""
        try:
            connection = sqlite3.connect("overthewire.db")
            connection.row_factory = self.__dict_factory
            return connection
        except sqlite3.Error as error:
            print("Error while trying to connect to the database:", error)
            return None

    
