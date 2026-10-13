#E4.1 · Clase CuentaBancaria con saldo privado, ingresar, retirar (valida saldo suficiente) y propiedad saldo de solo lectura.
class SaldoInsuficiente(Exception):
    """ """

class CuentaBancaria:

    def __init__(self,titular,saldo=0.0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    def retirar(self,cantidad):
        if cantidad > self._saldo :
            print("")
            raise SaldoInsuficiente(f"Saldo insuficiente para retirar, su saldo es de : {self.saldo}€")
        else:
            restante= self._saldo - cantidad
            print(f"Usted tiene en la cuenta despues de retirar: {restante}€")

    def ingresar(self,cantidad):
        nuevosaldo= self._saldo + cantidad
        print(f"Usted ha ingresado: {cantidad}€, su saldo es ahora de : {nuevosaldo}€")

prueba1= CuentaBancaria("Juanjo",100.50)

print(f"Hola {prueba1.titular}")
prueba1.retirar(5)
