import customtkinter
from PIL import Image


title_pic = Image.open('title.png').resize((240, 135), Image.LANCZOS)
title_pic = customtkinter.CTkImage(title_pic, size=(240, 135))