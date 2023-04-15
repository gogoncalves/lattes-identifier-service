import pandas as pd
import mysql.connector
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'config/db_config.txt', 'r') as f:
    db_config = {}
    for line in f:
        try:
            key, value = line.strip().split('=')
            db_config[key] = value
        except:
            pass

class LattesValidator:
    def __init__(self):
        pass

    def search_lattes_in_mysql(self, lattes_number):
        """
        Realiza a busca do id Lattes no banco de dados MySQL.
        """
        print("\U0001F916 Credenciais de configuração do Banco de dados MySQL",db_config)
        try:
            # Conexão com o banco de dados MySQL
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
            print("\U0001F6AB Não foi possível estabelecer conexão com o banco de dados MYSQL")
            print("\U0001F916 Acesse o arquivo db_config e altere para as configurações corretas do seu DB")
            print(f"\U0001F5FA  Adress: {dir_path}\config\db_config.txt")

        return False

    def search_lattes_in_csv(self, lattes_number):
        """
        Realiza a busca do id Lattes no arquivo CSV.
        """
        print("\U0001F6AB Iniciando validação do arquivo CSV")
        df = pd.read_csv(dir_path + '/' + r'lattes.csv', sep=';')
        if df["NRO_ID_CNPQ"].isin([lattes_number]).any():
            print("\u2705 Lattes válido")
            return True
        print("\U0001F6AB Lattes não encontrado no arquivo CSV")
        return False

    def validate_lattes(self, lattes_number):
        """
        Valida um número de identificação Lattes.
        """
        if self.search_lattes_in_mysql(lattes_number) or self.search_lattes_in_csv(lattes_number):
            return True
        return False