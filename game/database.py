
import mysql.connector
import os

def fetch_images(output_directory):
    # Убедитесь, что директория существует
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Smirnovav.d69',
        database='image_db'
    )

    cursor = connection.cursor()
    cursor.execute("SELECT id, image_data FROM images")

    for row in cursor.fetchall():
        image_id = row[0]
        image_data = row[1]

        # Сохраняем изображение
        file_path = os.path.join(output_directory, f'image_{image_id}.png')
        with open(file_path, 'wb') as file:
            file.write(image_data)
        print(f"Изображение image_{image_id}.png извлечено и сохранено в {output_directory}.")

    cursor.close()
    connection.close()

# Пример использования
if __name__ == "__main__":
    output_directory = 'C:/renpy/RenpyNew/game/images'
    fetch_images(output_directory)