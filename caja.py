#clase de caja
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import locale

locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')
#Toma las ganancias de transferencia y efectivo de la clase VentasFrame
#luego las muestra en un documento.txt con la fecha y hora actual
#junto al total de ganancias y los productos que se vendieron
class Caja:
    ganancias_transferencia = 0
    ganancias_efectivo = 0
    productos_vendidos = []

    def __init__(self):
        pass
    
    @classmethod
    def hacer_caja(cls):
        total = cls.ganancias_transferencia + cls.ganancias_efectivo
        with open(f"{str(datetime.date.today())} hs:{str(datetime.datetime.now().time().replace(second=0,microsecond=0))}.txt", "w") as file:
            file.write(f"Ganancias por transferencia: {locale.currency(cls.ganancias_transferencia, grouping=True)}\n")
            file.write(f"Ganancias por efectivo: {locale.currency(cls.ganancias_efectivo, grouping=True)}\n")
            file.write(f"Ganancias totales: {locale.currency(total, grouping=True)}\n")
            file.write("Productos vendidos:\n")
            for producto in cls.productos_vendidos:
                file.write(f" - {producto['nombre']} ({producto['codigo']}): {producto['cantidad']} unidades\n")
            messagebox.showinfo("Reporte de Caja", f"Registro de caja guardado correctamente como: {file.name}", icon='info')


        # Reiniciar valores
        cls.ganancias_transferencia = 0
        cls.ganancias_efectivo = 0
        cls.productos_vendidos = []



