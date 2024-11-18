# Ejercicio 1: Cálculo de edades (Ejercicio Resuelto 4)
edadJuan = int(input("Ingrese la edad de Juan: "))  # Solicita la edad de Juan al usuario

# Calcula las edades basándose en la proporción indicada
edadDeAlberto = int(edadJuan * (2 / 3))  # Edad de Alberto
edadDeAna = int(edadJuan * (4 / 3))  # Edad de Ana
edadDeMama = int(edadJuan + edadDeAlberto + edadDeAna)  # Edad de la mamá

# Muestra los resultados
print("La edad de Juan es:", edadJuan)
print("La edad de Alberto es:", edadDeAlberto)
print("La edad de Ana es:", edadDeAna)
print("La edad de Mamá es:", edadDeMama)