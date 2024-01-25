##Un programa que opere la formula cuadrática.

import cmath  # Necesario para manejar raíces cuadradas de números negativos

print("**Bienvenido usuario**")

# Solicitar al usuario ingresar los coeficientes
a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

# Calcular el discriminante
d = cmath.sqrt(b**2 - 4*a*c)

# Calcular las soluciones
x1 = (-b + d) / (2*a)
x2 = (-b - d) / (2*a)

##Resultados
print(f"Las soluciones son: {x1} y {x2}")

print("*********************")