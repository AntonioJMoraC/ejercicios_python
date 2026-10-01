nombre = input("Introduce tu nombre: ")
while nombre.isdigit():
    nombre = input("Introduce tu nombre: ")

nombre = nombre.capitalize()
print(f"Hola, {nombre}")