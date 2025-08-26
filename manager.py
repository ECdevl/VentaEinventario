#En esta clase es donde empieza el programa y se usa para acceder a los demas modulos
from tkinter import *
from venta import VentaFrame
from inventario import InventarioFrame
from caja import Caja

BACK = "#CACACA"


class Manager(Tk):
    def __init__(self):
        #se inicializa y se configura la ventana principal
        super().__init__()
        self.title("Caja registradora")
        self.geometry("800x400+150+250")
        self.resizable(False, False)
        self.configure(bg="#C6D9E3")
        self.container = Frame(self, bg=BACK)
        self.container.pack(fill='both', expand=True)
        self.current_toplevel = None
        self.init_ui()

    def init_ui(self):
        Label(self.container, text="CAJA REGISTRADORA", font=('Arial', 24, 'bold'), bg=BACK).pack(side='top')
        Button(self.container, text="Ventas", command=lambda: self.open_window(VentaFrame), bg="#006AC7").place(x=200, y=200, width=200, height=50)
        Button(self.container, text="Inventario", command=lambda: self.open_window(InventarioFrame), bg="#10741D").place(x=400, y=200, width=200, height=50)
        Button(self.container,text='Hacer Caja',bg="#743510", command=Caja.hacer_caja).place(x=300,y=250,width=200,height=50)

    # Esta funcion crea un ToplLevel para poder abrir una ventana nueva del modulo al que se desea entrar
    
    def open_window(self, FrameClass):
        # Se asegura que haya solo una ventana abierta para evitar errores por duplicacion
        if self.current_toplevel:
            self.current_toplevel.destroy()

        ventana = Toplevel(self)
        frame = FrameClass(ventana)
        frame.pack(fill='both', expand=True)
        ventana.title(str(frame))
        ventana.geometry('1000x500+1000+250')
        ventana.resizable(False, False)
        self.current_toplevel = ventana


#Inicia el mainloop de TTK
def main():
    app = Manager()
    app.mainloop()


if __name__ == "__main__":
    main()
