import mysql.connector

def upload_image(image_path):
    with open(image_path, 'rb') as file:
        image_data = file.read()

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Smirnovav.d69',
        database='image_db'
    )

    cursor = connection.cursor()
    query = "INSERT INTO images (image_data) VALUES (%s)"
    cursor.execute(query, (image_data,))

    connection.commit()
    cursor.close()
    connection.close()
    print(f"Изображение {image_path} успешно загружено в базу данных.")

# Пример использования
upload_image('C:\Diplom\image\i1.png')
upload_image('C:\Diplom\image\i2.png')
upload_image('C:\Diplom\image\i3.jpg')
upload_image('C:\Diplom\image\i4.png')
upload_image('C:\Diplom\image\i5.png')
upload_image('C:\Diplom\image\i6.png')

