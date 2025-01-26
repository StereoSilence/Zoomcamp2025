import os
import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine

def download_csv(url, csv_name):
    if not url:
        raise ValueError("URL is required to download the file.")
    print(f"Downloading {url} to {csv_name}...")
    result = os.system(f"curl -sSL {url} -o {csv_name}")
    if result != 0:
        raise Exception(f"Failed to download file from {url}")
    print("Download complete!")

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'  # Локальное имя файла, в который будет сохранён CSV

    # Загружаем CSV
    download_csv(url, csv_name)

    # Устанавливаем соединение с базой данных
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Читаем файл батчами
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    # Обрабатываем первую порцию данных
    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Создаем таблицу в базе данных
    print(f"Creating table {table_name}...")
    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')
    print(f"Table {table_name} created.")

    # Загружаем первую порцию данных
    df.to_sql(name=table_name, con=engine, if_exists='append')

    # Обрабатываем остальные данные
    while True:
        try:
            df = next(df_iter)
        except StopIteration:
            print("Data ingestion complete.")
            break

        t_start = time()

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name, con=engine, if_exists='append')
        t_end = time()
        print(f"Inserted another chunk..., took {t_end - t_start:.3f} seconds.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the result to')
    parser.add_argument('--url', help='url of the csv file', default=None)

    args = parser.parse_args()

    main(args)
