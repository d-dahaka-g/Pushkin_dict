import customtkinter as ctk

import colours
import images
import widgets
import db_manager
import random

ctk.set_widget_scaling(1.0)
ctk.set_window_scaling(1.0)


def selected(button: widgets.Button, others: list[widgets.Button]):
    for widget in others:
        widget.change_colour(colours.top_colour)
    button.configure(fg_color=colours.bottom_colour)


app = ctk.CTk()
app.title('Словарь языка Пушкина')
app.resizable(False, False)
width = 720
height = 480
x = app.winfo_screenwidth() // 2
y = app.winfo_screenheight() // 2
app.geometry(f'{width}x{height}+{x - width // 2}+{y - height // 2}')

top = widgets.Frame(master=app, width=width, height=100, colour=colours.top_colour, corner_radius=0, x=width // 2, y=50)
bottom = widgets.Frame(master=app, width=width, height=380, colour=colours.bottom_colour, corner_radius=0, x=width // 2,
                       y=290)

title = widgets.Label(master=top, text='', text_colour='#FAFAFA', image=images.title_pic, x=20, y=40)

first_button = widgets.Button(master=top, text='Главная', colour=colours.bottom_colour, hover_colour=colours.top_colour,
                              width=140, height=40, x=95, y=85, font=('Roboto', 15),
                              command=lambda: selected(first_button, [second_button, third_button, fourth_button]))
first_button.bind('<Enter>', command=lambda event: first_button.configure(text_color='#FAFAFA'))
first_button.bind('<Leave>', command=lambda event: first_button.configure(text_color='#C0C8D1'))
first_button.change_colour(colours.bottom_colour)

second_button = widgets.Button(master=top, text='Предисловия', colour=colours.top_colour,
                               hover_colour=colours.top_colour, width=140, height=40, x=240, y=85, font=('Roboto', 15),
                               command=lambda: selected(second_button, [first_button, third_button, fourth_button]))
second_button.bind('<Enter>', command=lambda event: second_button.configure(text_color='#FAFAFA'))
second_button.bind('<Leave>', command=lambda event: second_button.configure(text_color='#C0C8D1'))

third_button = widgets.Button(master=top,
                              text='Содержание', colour=colours.top_colour, hover_colour=colours.top_colour, width=140,
                              height=40, x=385, y=85, font=('Roboto', 15),
                              command=lambda: selected(third_button, [first_button, second_button, fourth_button]))
third_button.bind('<Enter>', command=lambda event: third_button.configure(text_color='#FAFAFA'))
third_button.bind('<Leave>', command=lambda event: third_button.configure(text_color='#C0C8D1'))

fourth_button = widgets.Button(master=top,
                               text='Сокращения', colour=colours.top_colour, hover_colour=colours.top_colour, width=140,
                               height=40, x=530, y=85, font=('Roboto', 15),
                               command=lambda: selected(fourth_button, [first_button, second_button, third_button]))
fourth_button.bind('<Enter>', command=lambda event: fourth_button.configure(text_color='#FAFAFA'))
fourth_button.bind('<Leave>', command=lambda event: fourth_button.configure(text_color='#C0C8D1'))


main_frame = widgets.Frame(master=bottom, width=width, height=380, colour=colours.bottom_colour, corner_radius=0, x=width // 2,
                       y=190)

search = widgets.Entry(360, 25, master=main_frame, placeholder_text='Введите слово', placeholder_text_color='#93989D',
                       text_color=colours.top_colour, fg_color='#C0C8D1', width=670, height=34, border_color=colours.top_colour, corner_radius=20)

search_button = widgets.Button(master=search, text='', image=images.search_pic, x=635, y=17, colour='#C0C8D1', hover_colour='#C0C8D1', height=30, width=25)

wod_label = widgets.Label(master=bottom, text='Слово дня', text_colour='#C0C8D1', x=30, y=70, font=('Roboto', 20))

header_word = widgets.Label(master=bottom, text='Слово', text_colour='#C0C8D1', x=30, y=110, font=('Roboto', 20))
header_quantity = widgets.Label(master=bottom, text='Частота', text_colour='#C0C8D1', x=140, y=110, font=('Roboto', 20))
header_info = widgets.Label(master=bottom, text='Информация по слову', text_colour='#C0C8D1', x=220, y=110, font=('Roboto', 20))

random_word = random.choice(db_manager.extraction())
dirty_info = random_word[3].split()
length = len(dirty_info[0])
result = dirty_info[0]
counter = 1
while length < 45:
    l = len(dirty_info[counter])
    result += " " + dirty_info[counter]
    length += l
    counter += 1


word = widgets.Label(master=bottom, text=random_word[1], text_colour='#C0C8D1', x=30, y=150, font=('Roboto', 15))
quantity = widgets.Label(master=bottom, text=str(random_word[2]), text_colour='#C0C8D1', x=140, y=150, font=('Roboto', 15))
info = widgets.Label(master=bottom, text=result, text_colour='#C0C8D1', x=220, y=150, font=('Roboto', 15))

# print(random.choice(db_manager.extraction()))

app.mainloop()
