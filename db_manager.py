import sqlite3

def extraction():
    connection = sqlite3.connect('vocab.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM [База данных словаря]')
    data = cursor.fetchall()
    connection.close()
    return data