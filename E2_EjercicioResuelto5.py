# Ejercicio 2: Operaciones con números (Ejercicio Resuelto 5)
suma1 = float(input("Añade el valor 1 de la suma: "))  # Permite al usuario ingresar el primer valor de la operación
valorX = float(input("Añade el valor 2 de la suma: "))  # Permite al usuario ingresar el segundo valor
valorY = float(input("Añade el valor 3 de la operación: "))  # Permite al usuario ingresar el tercer valor

suma1 = suma1 + valorX  # Suma el valor de suma1 con valorX y actualiza suma1
valorX = valorX + valorY**2  # Suma valorX con el cuadrado de valorY y actualiza valorX
suma1 = suma1 + valorX / valorY  # Realiza la división entre valorX y valorY y lo suma a suma1

print("El valor de la suma es:", suma1)
