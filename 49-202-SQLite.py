import sqlite3

DB_NAME = "my_database.db"

# Создание файла базы данных:
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(sqlite3.version)

# Создание таблицы в файле:
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         student_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)


# Добавление данных в таблицу:
# inf = [
#     (100, "JS", 20),
#     (101, "Java", 5),
#     (102, 'c++', 2),
#     (103, 'php', 7),
# ]
#
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?)"
#     for cour in inf:
#         sqlite_conn.execute(sql_request, cour)
#     sqlite_conn.commit()


# Чтение данных из таблицы:
with sqlite3.connect(DB_NAME) as conn:
    query = "SELECT * FROM courses WHERE id > 200"
    cursor = conn.execute(query)
    print(cursor)
    for i in cursor:
        print(i)

# Удаление файла
from pathlib import Path
db = Path("my_database.db")
db.unlink()