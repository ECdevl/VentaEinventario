import datetime

class Caja:
    ganancias_transferencia = 0
    ganancias_efectivo = 0
    productos_vendidos = []

    def __init__(self):
        pass
    
    @classmethod
    def hacer_caja(cls):
        total = cls.ganancias_transferencia + cls.ganancias_efectivo
        with open(f"{str(datetime.date.today())}.txt", "w") as file:
            file.write(f"Ganancias por transferencia: {cls.ganancias_transferencia}\n")
            file.write(f"Ganancias por efectivo: {cls.ganancias_efectivo}\n")
            file.write(f"Ganancias totales: {total}\n")
            file.write("Productos vendidos:\n")
            for producto in cls.productos_vendidos:
                file.write(f" - {producto['nombre']} ({producto['codigo']}): {producto['cantidad']} unidades\n")
            

        # Reiniciar valores
        cls.ganancias_transferencia = 0
        cls.ganancias_efectivo = 0
        cls.productos_vendidos = []
