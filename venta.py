from tkinter import *

class VentaFrame(Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.contenido()


    def __str__(self):
        return "Ventas"
    def contenido(self):
        
        self.config(bg="#C6D9E3")
        titulo = Label(self,text="VENTAS",font=('Consolas',20,'bold'))
        titulo.pack(side='top')


