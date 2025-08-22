from textwrap import fill
from tkinter import *
from tkinter import ttk
from tkinter.tix import ComboBox
from jsonManager import JsonManager 
from caja import Caja
import locale
locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')  # Configura la localización a español

class VentaFrame(Frame):


    def __init__(self,parent):
        
        super().__init__(parent)
        self.root = parent
        

        self.articulos = []
        self.json_manager = JsonManager("inventario.json")
        self.articulos=self.json_manager.load()
        self.contenido()
        



    def __str__(self):
        return "Ventas"
    def contenido(self):
        
        self.config(bg="#CACACA")
        titulo = Label(self,text="VENTAS",font=('Consolas',20,'bold'))
        titulo.pack(side='top')
        add_frame = Frame(self)
        tabla_frame = Frame(self)
        add_frame.place(x=0,y=0,width=500,height=500)
        tabla_frame.place(x=500,y=0,width=500,height=500)
        

        self.lbl_warn = Label(add_frame,text='',font=('Arial',12),fg='red')
        self.lbl_warn.pack(side='top')
        lbl_producto = Label(add_frame,text="Producto:",font=('Arial',15))
        lbl_producto.pack(side='top')
        self.combobox_product = ttk.Combobox(add_frame, values=[articulo['nombre'] for articulo in self.articulos], font=('Arial',15))
        self.combobox_product.pack(side='top')
        self.combobox_product.bind('<Return>', lambda event: self.check_values(self.combobox_product.get(), self.entry_codigo.get()))
        lbl_codigo = Label(add_frame,text="Código:",font=('Arial',15))
        lbl_codigo.pack(side='top')
        self.entry_codigo = Entry(add_frame,font=('Arial',15))
        self.entry_codigo.pack(side='top')
        self.entry_codigo.bind('<Return>', lambda event: self.check_values(self.combobox_product.get(), self.entry_codigo.get()))
        lbl_cantidad = Label(add_frame,text="Cantidad:",font=('Arial',15))
        lbl_cantidad.pack(side='top')
        self.entry_cantidad = Entry(add_frame,font=('Arial',15))
        self.entry_cantidad.insert(0,'1')
        self.entry_cantidad.bind('<Return>', lambda event: self.check_values(self.combobox_product.get(), self.entry_codigo.get()))
        self.entry_cantidad.pack(side='top')
        btn_add = Button(add_frame, text="Agregar", font=('Arial',15), command=lambda: self.check_values(self.combobox_product.get(), self.entry_codigo.get()))
        
        btn_add.pack(side='top')
        btn_remove = Button(add_frame, text="Eliminar", font=('Arial',15), command=self.remove_article)
        btn_remove.pack(side='top')
        self.checkout_btn = Button(add_frame, text="Finalizar Compra", font=('Arial',15), command=self.finalizar_compra)
        self.checkout_btn.pack(side='top')

        self.metodo_pago = ttk.Combobox(add_frame, values=["Efectivo", "Tarjeta", "Transferencia"])
        self.metodo_pago.set("Transferencia")  # Valor por defecto
        self.metodo_pago.pack(side='top')

        total_frame = Frame(add_frame,relief='sunken', bd=5)
        total_frame.place(x=0,y=400,width=500,height=100)
        self.lbl_number = Label(total_frame,text='$0',font=('Consolas',30), fg='green')
        self.lbl_number.pack(side='bottom')
        lbl_tabla = Label(tabla_frame,text="Articulos a vender",font=('Arial',20))
        lbl_tabla.pack(side='top')
        columns = ('id', 'Producto', 'Cantidad', 'Costo', 'Codigo')
        self.productos_agregados = ttk.Treeview(tabla_frame, columns=columns, show='headings')
        for col in columns:
            self.productos_agregados.heading(col, text=col.upper())
            if col == 'id':
                self.productos_agregados.column(col, width=10)
            else:
                self.productos_agregados.column(col, width=100)
        self.productos_agregados.pack(side='top', fill='both', expand=True)

    def finalizar_compra(self):
        if not self.productos_agregados.get_children():
            self.lbl_warn.config(text="No hay artículos en la tabla.")
            return
        if self.metodo_pago.get() not in ["Efectivo", "Tarjeta", "Transferencia"]:
            self.lbl_warn.config(text="Selecciona un metodo de pago.")
            return
        if self.metodo_pago.get() == 'Efectivo':
            Caja.ganancias_efectivo += self.update_total()
        else:
            Caja.ganancias_transferencia += self.update_total()
        # Restar cantidades en self.articulos según lo que haya en la tabla
        for child in self.productos_agregados.get_children():
            values = self.productos_agregados.item(child, 'values')
            Caja.productos_vendidos.append({
                'nombre': values[1],
                'cantidad': int(values[2]),
                'codigo': values[4]
            })
            try:
                pid = int(values[0])
                qty = int(values[2])
            except (ValueError, TypeError):
                continue

            # buscar el artículo en el inventario por id
            for art in self.articulos:
                try:
                    art_id = int(art.get("id", -1))
                except (ValueError, TypeError):
                    art_id = -1

                if art_id == pid:
                    try:
                        current = int(art.get("cantidad", 0))
                    except (ValueError, TypeError):
                        current = 0
                    new_qty = current - qty
                    if new_qty < 0:
                        new_qty = 0
                    art["cantidad"] = new_qty
                    break
            else:
                # no se encontró el artículo en el inventario
                self.lbl_warn.config(text=fill(f"Artículo con id {pid} no encontrado en inventario."))

        # Guardar cambios en el JSON
        try:
            self.json_manager.save(self.articulos)

        except Exception as e:
            self.lbl_warn.config(text=f"Error al guardar inventario: {e}")
            return

        # Limpiar la tabla de venta y actualizar total
        for child in list(self.productos_agregados.get_children()):
            self.productos_agregados.delete(child)
        self.update_total()

        self.lbl_warn.config(text="Compra finalizada con éxito.")


    def remove_article(self):
        selected_item = self.productos_agregados.selection()
        if not selected_item:
            self.lbl_warn.config(text="Por favor, selecciona un artículo para eliminar.")
            return

        for item in selected_item:
            self.productos_agregados.delete(item)

        self.update_total()

    def check_values(self,product,code):
        if not product and not code:
            self.lbl_warn.config(text=fill("Por favor, introduce almenos un nombre o codigo de barras."))
            return
        self.lbl_warn.config(text="")
        if not code:
            self.load_specific_article(product)
        else:
            self.load_specific_article(code)

    def update_total(self):
        total = 0
        for child in self.productos_agregados.get_children():
            values = self.productos_agregados.item(child, 'values')
            total += float(values[3]) * int(values[2])

        self.lbl_number.config(text=locale.currency(total, grouping=True, international=True,symbol=True))
        return total

    def check_stock(self, product, add_qty):
        if not product:
            self.lbl_warn.config(text="Producto no encontrado en inventario.")
            return False

        try:
            add_qty = int(add_qty)
        except (ValueError, TypeError):
            add_qty = 0

        available = int(product.get("cantidad", 0))

        # sumar las cantidades ya añadidas en la tabla para este producto (comparando por id o nombre)
        current_in_table = 0
        for child in self.productos_agregados.get_children():
            values = self.productos_agregados.item(child, 'values')
            # values fields: (id, nombre, cantidad, costo, codigo)
            try:
                item_id = int(values[0])
            except (ValueError, TypeError):
                item_id = None
            item_name = str(values[1]).lower()
            try:
                item_qty = int(values[2])
            except (ValueError, TypeError):
                item_qty = 0

            if (item_id is not None and item_id == int(product.get("id", -1))) or (item_name == str(product.get("nombre","")).lower()):
                current_in_table += item_qty

        if current_in_table + add_qty > available:
            self.lbl_warn.config(text=fill(f"No hay suficiente stock de {product.get('nombre')}. Stock actual: {available} — en venta: {current_in_table} + {add_qty}"))
            return False

        return True


    def load_specific_article(self, article):
        producto = None
        for i in self.articulos:
            if i["codigo"] == article:
                producto = i
                break
            elif i["nombre"].lower() == str(article).lower():
                producto = i
                break

        if not producto:
            self.lbl_warn.config(text="Artículo no encontrado.")
            return

        # parsear cantidad solicitada (entry_cantidad puede no ser numérico)
        try:
            qty = int(self.entry_cantidad.get())
            if qty <= 0:
                raise ValueError
        except ValueError:
            self.lbl_warn.config(text="Cantidad inválida. Introduce un entero > 0.")
            return

        if not self.check_stock(producto, qty):
            return

        # si alcanza el stock, añadir o sumar en la tabla usando qty
        for i in self.productos_agregados.get_children():
            values = self.productos_agregados.item(i, 'values')
            if str(values[1]).lower() == producto["nombre"].lower():
                new_qty = int(values[2]) + qty
                self.productos_agregados.item(i, values=(values[0], values[1], str(new_qty), values[3], values[4]))
                break
        else:
            self.productos_agregados.insert('', 'end', values=(producto["id"], producto["nombre"], str(qty), producto["costo"], producto["codigo"]))

        self.update_total()


