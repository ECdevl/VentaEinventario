import datetime
from tkinter import *
from tkinter import ttk
import tkcalendar
from textwrap import fill
from jsonManager import JsonManager


class Articulos:
    def __init__(self, filename="inventario.json"):
        self.json_manager = JsonManager(filename)
        self.articulos = self.json_manager.load()

    def add(self, articulo: dict):
        articulo["id"] = self._next_id()
        self.articulos.append(articulo)
        self.save()

    def edit(self, index: int, articulo: dict):
        self.articulos[index] = articulo
        self.save()

    def delete_by_ids(self, ids):
        self.articulos = [a for a in self.articulos if a["id"] not in ids]
        self.save()

    def get_all(self):
        return self.articulos

    def save(self):
        self.json_manager.save(self.articulos)

    def _next_id(self):
        if not self.articulos:
            return 1
        return max(a["id"] for a in self.articulos) + 1


articulos_instance = Articulos()


class InventarioFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.table = None
        self.contenido()
        self.load_articles()

    def __str__(self):
        return "Inventario"

    def contenido(self):
        Label(self, text="INVENTARIO", font=('Consolas', 20, 'bold')).pack(side='top')

        # Frames
        lblframe = LabelFrame(self, text="Lista de Articulos", font=('Arial', 15, 'bold'))
        lblframe.place(x=500, y=0, width=500, height=500)

        products_frame = Frame(self)
        products_frame.place(x=0, y=0, width=500, height=250)

        info_frame = Frame(self, relief='sunken', bd=2)
        info_frame.place(x=0, y=250, width=500, height=250)

        # Tabla
        columns = ('id', 'Producto', 'Cantidad', 'Costo', 'Codigo')
        self.table = ttk.Treeview(lblframe, columns=columns, show='headings')
        for col in columns:
            self.table.heading(col, text=col.upper())
            if col == 'id':
                self.table.column(col, width=10)
            else:
                self.table.column(col, width=100)
        self.table.pack(expand=True, fill='both', padx=10, pady=10)

        # Entradas
        self.entry_producto = self._create_entry(products_frame, "Producto")
        self.entry_cantidad = self._create_entry(products_frame, "Cantidad")
        self.entry_costo = self._create_entry(products_frame, "Costo")
        self.entry_codigo = self._create_entry(products_frame, "Codigo")

        Button(products_frame, text="Agregar", command=self.add_article, bg='green').pack(side="top", pady=2)
        Button(products_frame, text="Eliminar", command=self.delete_article, bg='red').pack(side="top", pady=2)

        # Info
        self.info_label = Label(info_frame, text="", font=('Consolas', 15))
        self.info_label.pack(side="top")

    def _create_entry(self, frame, text):
        Label(frame, text=f"{text}: ", font=('Arial', 15, 'bold')).pack(side="top")
        entry = Entry(frame)
        entry.pack(side="top")
        return entry

    def add_article(self):
        nombre = self.entry_producto.get().strip()
        cantidad = self.entry_cantidad.get().strip()
        costo = self.entry_costo.get().strip()
        codigo = self.entry_codigo.get().strip()

        if not nombre or not cantidad.isdigit():
            self.info_label.config(text="Introduce un nombre y cantidad válida", fg="#FF0000")
            return

        articulos_instance.add({
            "nombre": nombre,
            "cantidad": int(cantidad),
            "costo": costo,
            "codigo": codigo
        })
        self.load_articles()
        self.info_label.config(text="Artículo agregado", fg="green")

    def delete_article(self):
        selected = self.table.selection()
        if not selected:
            self.info_label.config(text="Selecciona uno o más elementos", fg="red")
            return

        ids = [int(self.table.item(item, "values")[0]) for item in selected]
        articulos_instance.delete_by_ids(ids)
        self.load_articles()
        self.info_label.config(text="Eliminado con éxito", fg="green")


    def load_articles(self):

        for row in self.table.get_children():
            self.table.delete(row)
        for a in articulos_instance.get_all():
            self.table.insert('', 'end', values=(a["id"], a["nombre"], a["cantidad"], a["costo"], a["codigo"]))
