import datetime
from tkinter import *
from tkinter import ttk
import locale

locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')

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
            CajaWindow()


        # Reiniciar valores
        cls.ganancias_transferencia = 0
        cls.ganancias_efectivo = 0
        cls.productos_vendidos = []

class CajaWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Reporte")
        self.geometry("500x200")

        self.init_ui()

    def init_ui(self):
        self.create_widgets()

    def create_widgets(self):
        lbl_titulo = Label(self, text="Reporte de Caja", font=('Arial', 24, 'bold'))
        lbl_titulo.pack(side='top', pady=10)

        self.lbl = Label(self, text="Registro de caja guardado correctamente", font=('Arial', 18))
        self.lbl.pack(side='top', pady=10)


