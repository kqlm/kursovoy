import mysql.connector
import os

def connect_to_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Smirnovav.d69',
        database='image_db'
    )
    return connection

def register_user(username, email, password):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # Проверка, существует ли уже пользователь или email
        cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        if cursor.fetchone() is not None:
            return False  # Пользователь или email уже существует

        # Регистрация нового пользователя с ролью 'user'
        cursor.execute("INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)", 
                       (username, email, password, 'user'))
        connection.commit()
        return True  # Регистрация успешна
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        cursor.close()
        connection.close()

def check_user(username, password):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    connection.close()
    return user is not None  # Вернуть True, если пользователь найден
