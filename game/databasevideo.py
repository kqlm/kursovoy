import runpy
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

def fetch_video(video_id):
    connection = connect_to_database()
    cursor = connection.cursor()
    
    # Извлечение видеофайла по ID
    cursor.execute("SELECT file_name, video_data FROM video_files WHERE id = %s", (video_id,))
    result = cursor.fetchone()

    if result:
        file_name, video_data = result
        # Укажите путь для сохранения файла в папке проекта
        file_path = os.path.join(runpy.config.game_directory, "data", file_name)  # Путь для сохранения файла
        with open(file_path, 'wb') as file:
            file.write(video_data)
        print(f"Файл {file_name} успешно извлечен из базы данных.")
        return file_path  # Возвращаем путь к сохраненному файлу
    else:
        print("Видео не найдено.")
        return None

    cursor.close()
    connection.close()
