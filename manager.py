from tkinter import *
from venta import VentaFrame
from inventario import InventarioFrame

BACK = "#CACACA"


class Manager(Tk):
    def __init__(self):
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

    def open_window(self, FrameClass):
        if self.current_toplevel:
            self.current_toplevel.destroy()

        ventana = Toplevel(self)
        frame = FrameClass(ventana)
        frame.pack(fill='both', expand=True)
        ventana.title(str(frame))
        ventana.geometry('1000x500+1000+250')
        ventana.resizable(False, False)
        self.current_toplevel = ventana


def main():
    app = Manager()
    app.mainloop()


if __name__ == "__main__":
    main()
