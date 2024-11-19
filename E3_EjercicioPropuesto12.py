# Ejercicio 3: Cálculo de salario (Ejercicio Propuesto 12)
horas_trabajadas=float(input("Ingrese el número de horas trabajadas: ")) #Ingreso horas 
                                                                         #trabajadas
#Permite al usuario ingresar las horas trabajadas
valor_hora=float(input("Ingrese el valor de la hora: "))  #Permite al usuario
                                                          #ingresar el valor por hora
retefuente=float(input("ReteFuente en decimales, separado por un punto: ")) 
#Permite ingresar la retefuente como decimal

salario_bruto=float(valor_hora * horas_trabajadas)  # Calcula el salario bruto
valor_retefuente=float(salario_bruto * retefuente)  # Calcula el valor de la retefuente
salario_neto=float(salario_bruto - valor_retefuente)  # Calcula el salario neto

print("El valor del salario bruto es:", salario_bruto)
print("El valor de la retefuente es:", valor_retefuente)
print("El valor del salario neto es:", salario_neto)