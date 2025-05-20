import sqlite3
import json

connection = sqlite3.connect('vocab.db')
cursor = connection.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS [База данных словаря] ([ID слова] INTEGER PRIMARY KEY NOT NULL, [Слово] TEXT, [Количество употреблений] INTEGER, [Информация по слову] TEXT)" )

with open('словник(а-б).json', 'r', encoding='utf-8') as f:
    data:dict = json.load(f)

for key, value in data.items():
    cursor.execute('''INSERT INTO [База данных словаря] ([Слово],  [Количество употреблений], [Информация по слову]) VALUES (?, ?, ?)
    ''', (key, value[0], value[1]))
    connection.commit()

connection.close()

