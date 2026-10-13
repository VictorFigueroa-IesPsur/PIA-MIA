#E4.5 · Clase abstracta Figura con area() y perimetro(); implementa Circulo, Rectangulo y Cuadrado.

from abc import ABC, abstractmethod
from math import pi

class Figura(ABC):

    @abstractmethod
    def area(self):...
    def perimetro(self):...

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pi * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base + self.altura) * 2 
    
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

pcirculo=Circulo(5)
print(f"{pcirculo.area()}")
prectangulo=Rectangulo(10,2)
print(f"{prectangulo.area()}")
pcuadrado=Cuadrado(3)
print(f"{pcuadrado.area()}")