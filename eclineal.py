import math
class EcuacionCuadratica:
    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c
    def get_a(self) -> float:
        return self._a
    def get_b(self) -> float:
        return self._b
    def get_c(self) -> float:
        return self._c
    def getDiscriminante(self) -> float:
        return (self._b ** 2) - (4 * self._a * self._c)
    def getRaiz1(self) -> float:
        disc = self.getDiscriminante()
        if disc < 0:
            return 0.0
        return (-self._b + math.sqrt(disc)) / (2 * self._a)
    def getRaiz2(self) -> float:
        disc = self.getDiscriminante()
        if disc < 0:
            return 0.0
        return (-self._b - math.sqrt(disc)) / (2 * self._a)
if __name__ == "__main__":
    try:
        entrada = input("Ingrese a, b, c: ")
        valores = [float(x) for x in entrada.split()]  
        if len(valores) != 3:
            print("Error: Debe ingresar exactamente 3 números.")
        else:
            a, b, c = valores
            ecuacion = EcuacionCuadratica(a, b, c)
            discriminante = ecuacion.getDiscriminante()
            if discriminante > 0:
                r1 = ecuacion.getRaiz1()
                r2 = ecuacion.getRaiz2()
                print(f"La ecuación tiene dos raíces {r1} y {r2}")
            elif discriminante == 0:
                r1 = ecuacion.getRaiz1()
                print(f"La ecuación tiene una raíz {r1}")
            else:
                print("La ecuación no tiene raíces reales")
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar números válidos separados por espacios.")
