import random
import time
class Cronometro:
    def __init__(self):
        self._tiempo_inicio = 0.0
        self._tiempo_fin = 0.0
    def inicia(self):
        self._tiempo_inicio = time.time() * 1000
    def detener(self):
        self._tiempo_fin = time.time() * 1000
    def lapso_de_tiempo(self) -> float:
        return self._tiempo_fin - self._tiempo_inicio
def ordenacion_seleccion(arr: list):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
if __name__ == "__main__":
    TAMANO = 10000 
    arreglo = [random.randint(0, 999999) for _ in range(TAMANO)]
    crono = Cronometro()
    crono.inicia()
    ordenacion_seleccion(arreglo)
    crono.detener()
    print(f"Tiempo de ordenación por selección: {crono.lapso de tiempo():.2f} ms")
