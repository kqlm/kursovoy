import mysql.connector

def upload_audio(file_path):
    # Чтение аудиофайла в бинарном формате
    with open(file_path, 'rb') as file:
        audio_data = file.read()

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Smirnovav.d69',
        database='image_db'
    )

    cursor = connection.cursor()

    # Вставка аудиофайла в базу данных
    query = "INSERT INTO audio_files (file_name, audio_data) VALUES (%s, %s)"
    cursor.execute(query, (file_path.split('/')[-1], audio_data))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Файл {file_path} успешно загружен в базу данных.")

# Пример использования
upload_audio('C:\Diplom\paudio\spokoynaya.mp3')  # Укажите путь к вашему аудиофайлу