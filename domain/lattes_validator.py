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
            print(
                "\U0001F916 Credenciais de configuração do Banco de dados MySQL", db_config)
            cnx = mysql.connector.connect(
                user=db_config['user'],
                password=db_config['password'],
                host=db_config['host'],
                port=int(db_config['port']),
                database=db_config['database']
            )
            cursor = cnx.cursor()
            print("\U0001F916 Conexão com o banco de dados estabelecida com sucesso!")

            # Busca no banco de dados MySQL
            query = "SELECT idLattes FROM lattes WHERE idLattes = %s"
            cursor.execute(query, (lattes_number,))
            result = cursor.fetchone()
            if result is not None:
                print("\u2705 Lattes válido")
                return True
            cursor.close()
            cnx.close()

        except:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            print(
                "\U0001F6AB Não foi possível estabelecer conexão com o banco de dados MYSQL")
            print(
                "\U0001F916 Acesse o arquivo db_config e corrija para as configurações corretas")
            print(
                f"Path: {dir_path}\LATTES-IDENTIFIER-API\config\db_config.txt")

        return False

    def search_lattes_in_csv(self, lattes_number):
        print("\U0001F916 Iniciando validação do arquivo CSV")
        df = pd.read_csv('./' + 'assets' + '/' + r'lattes.csv', sep=';')
        if df["NRO_ID_CNPQ"].isin([lattes_number]).any():
            print("\u2705 Lattes válido")
            return True
        print("\U0001F6AB Lattes não encontrado no arquivo CSV")
        return False

    def validate_lattes(self, lattes_number):
        if self.search_lattes_in_mysql(lattes_number) or self.search_lattes_in_csv(lattes_number):
            return True
        return False
