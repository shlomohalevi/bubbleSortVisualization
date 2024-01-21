
from turtle import Turtle,Screen
import os
import tkinter as tk

IMAGES_FOLDER_PATH = r'data structure\bubsort_images'
class BubbleSortGui():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width = 0.7, height = 0.7)
        self.screen.colormode(255)
        self.screen.bgcolor(11, 99,220)
        self.screen.onkey(self.on_escape, "Escape")
        self.screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", self.on_escape)
        # Listen for key events
        self.screen.listen()
        self.root = self.screen._root
        self.labeltxt = tk.Label(self.root,text='please insert only numbers seperated by a coma',fg='blue', font=("Helvetica", 16))
        self.labeltxt.pack(pady=10)
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)
        self.btn = tk.Button(self.root,text='insert numbers')
        self.btn.pack(pady=10)

    def on_escape(self):
        try:
            for file in os.listdir(IMAGES_FOLDER_PATH):
                file_path = os.path.join(IMAGES_FOLDER_PATH, file)
                os.remove(file_path)
        except Exception as e:
            print(e)
        try:
            self.screen.bye()  
        except self.screen.Terminator as e:
            print(e)
            pass  
   
        
