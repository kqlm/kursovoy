import runpy
import mysql.connector
import os

def fetch_images(output_directory):
    # Убедитесь, что директория существует
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

def connect_to_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Smirnovav.d69',
        database='image_db'
    )
    return connection

def fetch_audio(audio_id):
    connection = connect_to_database()
    cursor = connection.cursor()
    
    # Извлечение аудиофайла по ID
    cursor.execute("SELECT file_name, audio_data FROM audio_files WHERE id = %s", (audio_id,))
    result = cursor.fetchone()

    if result:
        file_name, audio_data = result
        with open(os.path.join(output_directory, "data", file_name), 'wb') as file:
            file.write(audio_data)
        print(f"Файл {file_name} успешно извлечен из базы данных.")
    else:
        print("Аудиофайл не найден.")

    cursor.close()
    connection.close()

if __name__ == "__main__":    
    output_directory = 'C:/renpy/RenpyNew/game/audio'
    fetch_audio(output_directory)