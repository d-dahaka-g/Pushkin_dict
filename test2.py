import pdfplumber
import re

with pdfplumber.open("СЯП_А-Б — копия.pdf") as pdf:
    words = []
    for i in range(26, 218):
        page = pdf.pages[i]
        x0, y0, x1, y1 = page.bbox

        # Левая колонка (безопасный bbox)
        left_bbox = (x0, y0, x1 / 2, y1 - 0.001)  # Чуть уменьшаем y1
        left_text = str(page.crop(left_bbox).extract_text())
        # words.append(re.findall(r'([А-ЯЁ]+\d?)(?:\s*\(([А-ЯЁ]+)\))?\s*\(\d+\)\.', left_text))
        pattern = re.compile(
            r'(?<!\S)([А-ЯЁ][А-ЯЁ0-9-]*)'  # Слово начинается с заглавной и может содержать цифры/дефисы
            r'(?:\s*\([А-ЯЁ0-9-]+\))?'  # Необязательный вариант в скобках
            r'(?:\s*\[[^\]]+\])?'  # Игнорируем текст в квадратных скобках
            r'\s*\(\d+\)\.'  # Номер статьи в скобках
            r'(?=\s|[А-ЯЁ]|\||\n|\Z)',  # Условия окончания
            re.MULTILINE
        )

        words.append(pattern.findall(left_text))
        # Результат: [('АБШИД', '15'), ('АВГУСТ1', '61'), ('АВГУСТ2', '62')]
        # words.append(re.findall(r'([А-ЯЁ]+)(?:\s*\([А-ЯЁ]+\))?\s*\((\d+)\)\.(?=\s+[А-Я]|\Z)', left_text))

        # Правая колонка
        right_bbox = (x1 / 2, y0, x1, y1 - 0.001)
        right_text = page.crop(right_bbox).extract_text()
        words.append(pattern.findall(right_text))

flat_list = sum(words, [])
# print("Левая колонка:", left_text)
# print()
# print("Правая колонка:", right_text)
print(flat_list)