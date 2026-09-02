import math
def promedio(datos: list) -> float:
    n = len(datos)
    if n == 0:
        return 0.0
    return sum(datos) / n
def desviacion(datos: list) -> float:
    n = len(datos)
    if n <= 1:
        return 0.0
    prom = promedio(datos)
    suma_cuadrados = sum((x - prom) ** 2 for x in datos)
    return math.sqrt(suma_cuadrados / (n - 1))
def main():
    entrada = input("Ingrese 10 números: ")
    numeros = [float(x) for x in entrada.split()]
    prom_val = promedio(numeros)
    desv_val = desviacion(numeros)
    print(f"El promedio es {prom_val:.2f}")
    print(f"La desviación estándar es {desv_val:.5f}")
if __name__ == "__main__":
    main()