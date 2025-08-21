import json
from tkinter import Tk, Toplevel, Label
from textwrap import fill

class JsonManager:
    def __init__(self, filename: str):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([], f)
            self._show_warning("El archivo de inventario no existe. Se ha creado uno nuevo.\nNo lo elimine.")
            return []
        except json.JSONDecodeError:
            self._show_warning("El archivo está corrupto. Se reinició vacío.")
            return []

    def save(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def _show_warning(self, message: str):
        warn = Toplevel()
        warn.title("Advertencia")
        warn.geometry("300x100+200+200")
        Label(warn, text=fill(message, width=35)).pack(pady=10)
