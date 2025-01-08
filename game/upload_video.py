import mysql.connector

def upload_video(file_path):
    # Чтение видеофайла в бинарном формате
    with open(file_path, 'rb') as file:
        video_data = file.read()

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Smirnovav.d69',
        database='image_db'
    )

    cursor = connection.cursor()

    # Вставка видеофайла в базу данных
    query = "INSERT INTO video_files (file_name, video_data) VALUES (%s, %s)"
    cursor.execute(query, (file_path.split('/')[-1], video_data))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Файл {file_path} успешно загружен в базу данных.")

# Пример использования
upload_video('C:/Diplom/video/screen_load.mp4')  # Укажите путь к вашему видеофайлу
