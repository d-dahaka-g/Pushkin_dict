import sqlite3
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

googleauth = GoogleAuth()
googledrive = GoogleDrive(googleauth)
googleauth.LoadCredentialsFile('credentials.json')

if googleauth.credentials is None:
    googleauth.LocalWebserverAuth()
    googleauth.SaveCredentialsFile('credentials.json')
elif googleauth.access_token_expired:
    googleauth.Refresh()
    googleauth.SaveCredentialsFile('credentials.json')
else:
    googleauth.Authorize()

# file = googledrive.CreateFile(
#     {
#         'title': 'enter.txt'
#     }
# )
# file.SetContentString('это текст')
# file.Upload()

# path = 'СЯП_А-Б — копия.pdf'
# file = googledrive.CreateFile(
#     {
#         'title': 'СЯП_А-Б — копия копии.pdf'
#     }
# )
# file.SetContentFile(path)
# file.Upload()

# file = googledrive.CreateFile(
#     {
#         'id': '1LX9IAXnotccLtIpdx2h0ONYcW9okas43'
#     }
# )
# file.GetContentFile('Гарусова Д. А. переводческая практика.docx')

# items = googledrive.ListFile().GetList()
# for item in items:
#     print(f'название: {item['title']}, id: {item['id']}, size: {item.get('fileSize', 'нет размера')}')

# connection = sqlite3.connect('vocab.db')
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS [База данных словаря] ([ID слова] INTEGER PRIMARY KEY NOT NULL)" )
