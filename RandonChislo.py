import random
import sqlite3
rand_num = random.randint(1, 5)
attempts = 0
def insert_varible_into_table(PlayerName, attempts):
    try:
        sqlite_connection = sqlite3.connect('my_db_users.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                             PlayerName TEXT,
                             attempts INTEGER
                            )""")

        sqlite_insert_with_param = """INSERT INTO users
                              (PlayerName, attempts)
                              VALUES (?, ?);"""

        data_tuple = (PlayerName, attempts)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу sqlitedb_developers")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

while True:
    answer = int(input("Угадай число: "))
    if answer == rand_num:
        attempts += 1
        print("Угадал")
        print(f'Тебе понадобилось {attempts} попыток')
        PlayerName = input('Введи своё имя: ')
        insert_varible_into_table(PlayerName, attempts)
        break
    elif answer < rand_num:
        print("Число слишком маленькое")
        attempts += 1

    elif answer > rand_num:
        print("Число слишком большое")
        attempts += 1


