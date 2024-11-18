# Ejercicio 5: Cálculo de área y perímetro de un círculo (Ejercicio Propuesto 17)
import math  # Importamos la librería math para trabajar con el valor de pi

radio = float(input("Ingrese el radio: "))  # Permite que el usuario ingrese el valor del radio

area_circulo = math.pi * (radio**2)  # Calcula el área de la circunferencia
perimetro_circulo = 2 * math.pi * radio  # Calcula el perímetro de la circunferencia

print("El valor del área del círculo es:", area_circulo)
print("El valor del perímetro del círculo es:", perimetro_circulo)
