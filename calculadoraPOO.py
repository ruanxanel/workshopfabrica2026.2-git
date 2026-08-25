class Calculadora:
    def __init__(self):
        self.resultado = 0

    def somar(self, a, b):
        self.resultado = a + b
        return self.resultado

    def subtrair(self, a, b):
        self.resultado = a - b
        return self.resultado

    def multiplicar(self, a, b):
        self.resultado = a * b
        return self.resultado

    def dividir(self, a, b):
        if b != 0:
            self.resultado = a / b
            return self.resultado
        else:
            print("Divisão por zero não é permitida.")


a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
calculadora = Calculadora()
print("Resultado da soma:", calculadora.somar(a, b))
print("Resultado da subtração:", calculadora.subtrair(a, b))
print("Resultado da multiplicação:", calculadora.multiplicar(a, b))
print("Resultado da divisão:", calculadora.dividir(a, b))