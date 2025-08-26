#Esta clase se usa puramente para poder administrar los json
# tiene metodos para gurdar y cargar datos, se usan como metodos de clase para que sea mas eficaz y economico
#en cuanto a codigo
import json
from tkinter import Tk, Toplevel, Label, messagebox
from tkinter import ttk
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
            messagebox.showwarning(title="Advertencia", message="El archivo de inventario no existe. Se ha creado uno nuevo.\nNo lo elimine.")
            return []
        except json.JSONDecodeError:
            messagebox.showwarning(title="Advertencia", message="El archivo está corrupto. Se reinició vacío.")
            return []

    @classmethod
    def save(cls, data):
        with open(cls.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)




