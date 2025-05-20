import customtkinter as ctk

import colours


class Frame(ctk.CTkFrame):
    def __init__(self, master, colour, width, height, x, y, corner_radius):
        super().__init__(master=master, width=width, height=height, corner_radius=corner_radius, fg_color=colour)
        self.place(x=x, y=y, anchor='center')


class Label(ctk.CTkLabel):
    def __init__(self, master, text, text_colour, x, y, image=None, anchor='w', font=None):
        super().__init__(master=master, text=text, text_color=text_colour, image=image, font=font)
        self.place(x=x, y=y, anchor=anchor)


class Button(ctk.CTkButton):
    def __init__(self, master, colour, hover_colour, width, height, text, x, y, font=None, hover=False, command = None, image=None):
        super().__init__(master=master, fg_color=colour, hover_color=hover_colour, width=width, height=height, text=text,
                         text_color='#C0C8D1', font=font, command=command, hover=hover, image=image)
        self.place(x=x, y=y, anchor='center')


    def change_colour(self, colour):
        self.configure(hover_color=colours.bottom_colour)
        self.configure(fg_color=colour)

class Entry(ctk.CTkEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.place(x=args[0], y=args[1], anchor='center')

