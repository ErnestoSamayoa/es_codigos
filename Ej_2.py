## Un programa que calcule al ingresar la hora indique cuantos segundos han trascurido del dia.

print("**Bienvenido usuario**")

hora_t = input("Ingresa la hora en formato HH:MM:SS: ")

##Proceso
hora, minutos, segundos = map(int, hora_t.split(':'))

## Calcular los segundos transcurridos desde el inicio del día
segundos_totales = hora * 3600 + minutos * 60 + segundos

## Mostrar el resultado
print(f"Han transcurrido {segundos_totales} segundos desde el inicio del día hasta las {hora_t}.")

print("************************")