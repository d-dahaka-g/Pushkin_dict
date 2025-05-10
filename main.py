import customtkinter as ctk

import colours
import images
import widgets
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
app.geometry(f'{width}x{height}+{x-width//2}+{y-height//2}')


top = widgets.Frame(master=app, width=width, height=100, colour=colours.top_colour, corner_radius=0, x=width//2, y=50)
bottom = widgets.Frame(master=app, width=width, height=380, colour=colours.bottom_colour, corner_radius=0, x=width//2, y=290)


title = widgets.Label(master=top, text='', text_colour='#FAFAFA', image=images.title_pic, x=20, y=40)

first_button = widgets.Button(master=top, text='Главная', colour=colours.bottom_colour, hover_colour=colours.top_colour, width=140, height=40, x=95, y=85, font=('Roboto', 15), command=lambda: selected(first_button, [second_button]))
first_button.bind('<Enter>', command=lambda event: first_button.configure(text_color='#FAFAFA'))
first_button.bind('<Leave>', command=lambda event: first_button.configure(text_color='#C0C8D1'))
first_button.change_colour(colours.bottom_colour)

second_button = widgets.Button(master=top, text='Примечания', colour=colours.top_colour, hover_colour=colours.top_colour, width=140, height=40, x=240, y=85, font=('Roboto', 15), command=lambda: selected(second_button, [first_button]))
second_button.bind('<Enter>', command=lambda event: second_button.configure(text_color='#FAFAFA'))
second_button.bind('<Leave>', command=lambda event: second_button.configure(text_color='#C0C8D1'))







app.mainloop()