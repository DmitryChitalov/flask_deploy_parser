import configparser as cfg
import time
import sys
import sys
import os
import unittest
import json

sys.path.append(os.path.join(os.getcwd(), '..'))
import sys
import os
import unittest
import json
# sys.path.append(os.path.join(os.getcwd(), '..'))
# print(1, os.path.join(os.getcwd()))

from .process_request import read_requests, process_request
from .database import db_session


#print("хуец")
def main():
    print("хуец")
    # Читаем конфигурационные параметры
    config = cfg.ConfigParser()
    config.read("./flask_parser/hh_config.ini")
    sqlite_db = config["SQLite"]["path"]
    file_folder = config["Json"]["path"]

    i_cycle = 0
    while True:
        # Читаем записи со статусом 0 из БД
        rows = read_requests(db_session)
        print(f" я тут {rows}")
        if rows:
            # Если записи найдены, то начинаем обработку
            for row_request in rows:
                print(
                    f"\nОбработка запроса: {row_request.region} {row_request.text_request} начата.")
                process_request(db_session, file_folder, row_request)
                print(
                    f"Обработка запроса: {row_request.region} {row_request.text_request} завершена.")

        else:
            ## Переходим в режим ожидания
            time.sleep(0.1)
            sys.stdout.write("\r")
            sys.stdout.write(f"Новых запросов не найдено. Цикл {i_cycle}")
        i_cycle += 1

# if __name__ == "__main__":

# main()
