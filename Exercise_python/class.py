"""
POO in Python
"""

class Carro:  # Clase
    def __init__(self, color, velocidad):  # Función de construcción
        self.color = color
        self.velocidad = velocidad

    def acelerar(self):  # self accede a las propiedades de la clase
        print(f"La velocidad paso de {self.velocidad}") 
        self.velocidad +=10
        print(f"a {self.velocidad} km/h")



mi_carro = Carro("negro", 90)
carro_vecino = Carro("Azul", 50)

mi_carro.acelerar()
mi_carro.acelerar()
carro_vecino.acelerar()
carro_vecino.acelerar()
