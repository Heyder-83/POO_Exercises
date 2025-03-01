"""
Herencia en Python
"""

class Animal:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def respirar(self):
        print("El animal respira")

class Perro(Animal):
    def __init__(self, peso, altura, raza):
        super().__init__(peso, altura)
        self.raza = raza

    def ladrar(self):
        print("El perro ladra")

perro1 = Perro(20, 1.5, "Chihuahua")
animal1 = Animal(30, 1.5)

perro1.respirar()
print(f"El perro mide {perro1.altura} Metros")