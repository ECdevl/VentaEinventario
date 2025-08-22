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
        products_frame.place(x=0, y=0, width=500, height=350)

        info_frame = Frame(self, relief='sunken', bd=2)
        info_frame.place(x=0, y=350, width=500, height=150)

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
        Button(products_frame, text="Editar", command=self.edit_article, bg='orange').pack(side="top", pady=2)

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

    def edit_article(self):
        selected = self.table.selection()
        if not selected:
            self.info_label.config(text="Selecciona un artículo para editar", fg="red")
            return
        if len(selected) > 1:
            self.info_label.config(text="Selecciona solo un artículo para editar", fg="red")
            return

        item = selected[0]
        try:
            selected_id = int(self.table.item(item, "values")[0])
        except (ValueError, TypeError):
            self.info_label.config(text="Id inválido", fg="red")
            return

        # buscar índice en la lista por id
        index = None
        articulo = None
        for idx, a in enumerate(articulos_instance.get_all()):
            if a.get("id") == selected_id:
                index = idx
                articulo = a
                break

        if articulo is None:
            self.info_label.config(text="Artículo no encontrado en inventario", fg="red")
            return

        # ventana de edición
        win = Toplevel(self)
        win.title("Editar Artículo")
        win.geometry("360x260")

        Label(win, text="Producto:", font=('Arial', 12)).pack(anchor='w', padx=8, pady=(8,0))
        e_nombre = Entry(win)
        e_nombre.pack(fill='x', padx=8)
        e_nombre.insert(0, articulo.get("nombre", ""))

        Label(win, text="Cantidad:", font=('Arial', 12)).pack(anchor='w', padx=8, pady=(8,0))
        e_cantidad = Entry(win)
        e_cantidad.pack(fill='x', padx=8)
        e_cantidad.insert(0, str(articulo.get("cantidad", "")))

        Label(win, text="Costo:", font=('Arial', 12)).pack(anchor='w', padx=8, pady=(8,0))
        e_costo = Entry(win)
        e_costo.pack(fill='x', padx=8)
        e_costo.insert(0, str(articulo.get("costo", "")))

        Label(win, text="Codigo:", font=('Arial', 12)).pack(anchor='w', padx=8, pady=(8,0))
        e_codigo = Entry(win)
        e_codigo.pack(fill='x', padx=8)
        e_codigo.insert(0, str(articulo.get("codigo", "")))

        lbl_error = Label(win, text="", fg="red")
        lbl_error.pack(pady=(6,0))

        def guardar_edicion():
            nombre = e_nombre.get().strip()
            cantidad = e_cantidad.get().strip()
            costo = e_costo.get().strip()
            codigo = e_codigo.get().strip()

            if not nombre:
                lbl_error.config(text="El nombre no puede estar vacío")
                return
            if not cantidad.isdigit():
                lbl_error.config(text="Cantidad debe ser un entero")
                return

            nuevo = {
                "id": selected_id,
                "nombre": nombre,
                "cantidad": int(cantidad),
                "costo": costo,
                "codigo": codigo
            }

            articulos_instance.edit(index, nuevo)
            self.load_articles()
            self.info_label.config(text="Artículo editado correctamente", fg="green")
            win.destroy()

        btn_frame = Frame(win)
        btn_frame.pack(fill='x', padx=8)
        Button(btn_frame, text="Guardar", command=guardar_edicion, bg='green').pack(side='left', expand=True, fill='both')
        Button(btn_frame, text="Cancelar", command=win.destroy, bg='gray').pack(side='right', expand=True, fill='both')

    def load_articles(self):

        for row in self.table.get_children():
            self.table.delete(row)
        for a in articulos_instance.get_all():
            self.table.insert('', 'end', values=(a["id"], a["nombre"], a["cantidad"], a["costo"], a["codigo"]))
