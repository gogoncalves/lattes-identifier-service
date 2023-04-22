import pandas as pd
import mysql.connector
import os
import urllib.request
import zipfile
import time
import requests
from config.config_service import read_txt
import re
import dask.dataframe as dd
from tqdm import tqdm


class LattesService:
    def __init__(self):
        pass

    def search_lattes_file(self, url, destination_path):
        # Change the file name to the name of the file that comes in the ZIP file
        extract_path = os.path.join(destination_path, 'R358737.csv')
        new_file_path = os.path.join(destination_path, 'lattes_processed.csv')

        os.makedirs(destination_path, exist_ok=True)

        response = requests.get(url, stream=True)
        if response.status_code != 200:
            print('Download failed')
            return False
        
        print('Download started')
        content_disp = response.headers.get('Content-Disposition', '')
        filename = re.findall('filename="(.+)"', content_disp)[0]
        caminho_zip = os.path.join(destination_path, filename)

        if os.path.exists(caminho_zip) and os.path.isfile(caminho_zip):
            os.remove(caminho_zip)
            print(f'File {caminho_zip} removed')
        if os.path.exists(extract_path) and os.path.isfile(extract_path):
            os.remove(extract_path)
            print(f'File {extract_path} removed')
        if os.path.exists(new_file_path) and os.path.isfile(new_file_path):
            os.remove(new_file_path)
            print(f'File {new_file_path} removed')

        with tqdm(unit='B', unit_scale=True, desc='Download progress', leave=True, miniters=1, ncols=100) as t:
            urllib.request.urlretrieve(url, caminho_zip, reporthook=lambda blocks_read,
                                        block_size, total_size: t.update(block_size * blocks_read))
            
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.extractall(destination_path)

        os.remove(caminho_zip)

        print(f'File {caminho_zip} removed')

        if os.path.exists(extract_path) and os.path.isfile(extract_path):
            df = pd.read_csv(extract_path, sep=',')
            df.to_csv(new_file_path, sep=';', index=False)
            time.sleep(2)
            os.remove(extract_path)
            time.sleep(2)
            print('Process performed successfully!')
        else:
            print('File not found or invalid!')

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

            query = "SELECT idLattes FROM lattes WHERE idLattes = %s;"
            cursor.execute(query, (lattes_number,))
            result = cursor.fetchone()
            if result is not None:
                print("\u2705 Valid lattes in MySQL database")
                return True

            cursor.close()
            cnx.close()

        except mysql.connector.Error as error:
            print(f"Error: {error}")

        except Exception as e:
            print(
                "An unexpected error occurred while trying to connect to the MySQL database")
            print(f"Error: {e}")

        return False

    def search_lattes_in_csv(self, lattes_number):
        print("Starting CSV file validation")

        csv_files = [f for f in os.listdir('./static') if f.endswith('.csv')]

        for csv_file in csv_files:
            df = dd.read_csv('./static/' + csv_file, sep=';')
            if (df["NRO_ID_CNPQ"] == lattes_number).any().compute():
                print("\u2705 Valid lattes in CSV file")
                return True

        print("\U0001F6AB Lattes not found in CSV files")
        return False

    def validate_lattes(self, lattes_number):
        if self.search_lattes_in_mysql(lattes_number) or self.search_lattes_in_csv(lattes_number):
            return True
        return False
