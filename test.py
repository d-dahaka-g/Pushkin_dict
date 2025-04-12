import pdfplumber
import re
import json

with pdfplumber.open("СЯП_В-Г — копия.pdf") as pdf:
    words = []
    l = 383
    for i in range(l):
        page = pdf.pages[i]
        x0, y0, x1, y1 = page.bbox
        left_bbox = (x0, y0, x1 / 2, y1 - 0.001)
        left_text = str(page.crop(left_bbox).extract_text())
        pattern = re.compile(
            r'(?<!\S)([А-ЯЁ][А-ЯЁ0-9-]*)'  
                r'(?:\s*\([А-ЯЁ0-9-]+\))?'     
                r'(?:\s*\[[^\]]+\])?'          
                r'\s*\((\d+)\)\.'              
                r'(?=\s|[А-ЯЁ]|\||\n|\Z)',
            re.MULTILINE
        )
        words.append(pattern.findall(left_text))
        right_bbox = (x1 / 2, y0, x1, y1 - 0.001)
        right_text = page.crop(right_bbox).extract_text()
        words.append(pattern.findall(right_text))

flat_list = sum(words, [])

with open('словник.json', 'r') as file:
    data = json.loads(file.read())

with open('словник.json', 'w') as f:
    for i in flat_list:
        data[i[0]] = i[1]
    json.dump(data, f, ensure_ascii=False, indent=4)
