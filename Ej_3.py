##Un programa que convierta divisas (dolares a quetzales)

print("**Bienvenido usuario**")

dolares = float(input("Ingresa la cantidad en $: "))

## Tasa de cambio fija 
tasa_cambio = 7.82

## Calcular la cantidad equivalente en quetzales
quetzales = dolares * tasa_cambio

## Mostrar el resultado
print(f"$ {dolares} equivalen a Q {quetzales}")

print("************************")