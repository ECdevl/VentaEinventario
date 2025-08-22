import json
from tkinter import Tk, Toplevel, Label
from textwrap import fill

class JsonManager:
    filename = 'inventario.json'
    def __init__(self):
        pass

    @classmethod
    def load(cls):
        try:
            with open(cls.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            with open(cls.filename, "w", encoding="utf-8") as f:
                json.dump([], f)
            JsonWarn("El archivo de inventario no existe. Se ha creado uno nuevo.\nNo lo elimine.")
            return []
        except json.JSONDecodeError:
            JsonWarn("El archivo está corrupto. Se reinició vacío.")
            return []

    @classmethod
    def save(cls, data):
        with open(cls.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

class JsonWarn(Toplevel):
    def __init__(cls,msg):
        super().__init__()
        cls.title("Advertencia")
        cls.geometry("100x200")

        cls.init_ui(msg)

    def init_ui(cls,msg):
        cls.create_widgets(msg)

    def create_widgets(cls,msg):
        lbl_titulo = Label(cls, text=fill(msg, width=35), font=('Arial', 24, 'bold'))
        lbl_titulo.pack(side='top', pady=10)


