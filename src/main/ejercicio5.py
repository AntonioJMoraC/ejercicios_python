try:
    precio = float(input("Introduce el precio sin IVA: "))
except ValueError:
    print("Introduce un precio en numeros")
    print("En caso de tener decimales, usa '.'")

try:
    iva = int(input("Introduce el tipo de IVA a aplicar (4, 10, 21): "))
except ValueError:
    print("Introduce un IVA en numeros")

total = precio * (1 + iva / 100)

print(f"El precio final es de {total:.2f}")