import tkinter as tk

class Mycalculator:
    def __init__(self) :
        
        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text='eyyy',font=('arial',24))
        self.label.pack()

        self.button = tk.Button(self.root, text='กดสิอิสัส')
        self.button.place(x=20, y=30)

        self.root.mainloop()

Mycalculator()
