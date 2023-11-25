import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('users.db')

# Создание таблицы users, если она не существует
conn.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 first_name TEXT NOT NULL);''')

# Ввод имени пользователя
first_name = input("Введите имя пользователя: ")

# Вставка записи в таблицу users
conn.execute(f"INSERT INTO users (first_name) VALUES ('{first_name}');")

# Подтверждение изменений в базе данных
conn.commit()

# Закрытие подключения к базе данных
conn.close()
