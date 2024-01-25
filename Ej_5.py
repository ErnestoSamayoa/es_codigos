##Un programa que indique en que tipo de dato se debe ingresar esa variable.

print("**Bienvenido usuario**")

# Solicitar al usuario ingresar un valor
Type = input("Ingresa una variable: ")

# Verificar si es un número
if Type.isdigit():
    print("Has Ingresado un número")

# Verificar si es un solo carácter
elif len(Type) == 1:
    print("Has ingresado un carácter")

# Verificar si es un booleano (considerando mayúsculas y minúsculas)
elif Type.lower() in ["true", "false"]:
    print("Has ingresado un booleano")

# Si no cumple ninguna de las condiciones anteriores, asumir que es un texto
else:
    print("Has ingresado un texto")

    print("************************")