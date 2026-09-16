import math
class AlgebraVectorial:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def producto_escalar(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z
    def producto_vectorial(self, v):
        rx = self.y * v.z - self.z * v.y
        ry = self.z * v.x - self.x * v.z
        rz = self.x * v.y - self.y * v.x
        return AlgebraVectorial(rx, ry, rz)
    def es_perpendicular(self, v, opcion=3):
        if opcion == 3:
            return abs(self.producto_escalar(v)) < 1e-6
        elif opcion == 4:
            suma = AlgebraVectorial(self.x + v.x, self.y + v.y, self.z + v.z)
            return abs(suma.modulo()**2 - (self.modulo()**2 + v.modulo()**2)) < 1e-6
        return "Es completamente falso"
    def es_paralela(self, v, opcion=2):
        if opcion == 2:
            pv = self.producto_vectorial(v)
            return pv.modulo() < 1e-6
        return "Es FALSO"
    def proyeccion_a_sobre_b(self, b):
        factor = self.producto_escalar(b) / (b.modulo()**2)
        return AlgebraVectorial(b.x * factor, b.y * factor, b.z * factor)
    def componente_a_en_b(self, b):
        return self.producto_escalar(b) / b.modulo()
    def mostrar(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
v1 = AlgebraVectorial(1, 0, 0)
v2 = AlgebraVectorial(0, 1, 0)
print("Vector 1:", v1.mostrar())
print("Vector 2:", v2.mostrar())
print("¿Son perpendiculares (a.b=0)?", v1.es_perpendicular(v2, 3))
print("Componente de v1 en v2:", v1.componente_a_en_b(v2))
