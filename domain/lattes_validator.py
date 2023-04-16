import pandas as pd
import mysql.connector
import os
from config.service import read_txt


class LattesValidator:
    def __init__(self):
        pass

    def search_lattes_in_mysql(self, lattes_number):
        try:
            db_config = read_txt("./config/db_config.txt")
            cnx = mysql.connector.connect(
                user=db_config['user'],
                password=db_config['password'],
                host=db_config['host'],
                port=int(db_config['port']),
                database=db_config['database']
            )
            cursor = cnx.cursor()
            print("Connection to the database established successfully!")
            
            query = "SELECT idLattes FROM lattes WHERE idLattes = %s"
            cursor.execute(query, (lattes_number,))
            result = cursor.fetchone()
            if result is not None:
                print("\u2705 Valid lattes")
                return True
            cursor.close()
            cnx.close()

        except:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            print("Could not establish connection to MYSQL database")
            print("Database credentials:", db_config)
            print("Access the db_config file and correct to the correct settings")
            print(
                f"Path: {dir_path}\LATTES-IDENTIFIER-API\config\db_config.txt")

        return False

    def search_lattes_in_csv(self, lattes_number):
        print("Starting CSV file validation")
        df = pd.read_csv('./' + 'assets' + '/' + r'lattes.csv', sep=';')
        if df["NRO_ID_CNPQ"].isin([lattes_number]).any():
            print("\u2705 Valid lattes")
            return True
        print("\U0001F6AB Lattes not found in CSV file")
        return False

    def validate_lattes(self, lattes_number):
        if self.search_lattes_in_mysql(lattes_number) or self.search_lattes_in_csv(lattes_number):
            return True
        return False
