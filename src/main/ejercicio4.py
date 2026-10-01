import sys

try:
    celsius = float(input("Introduce la temperatura en grados celsius: "))

except ValueError:
    print("Introduce una temperatura con numeros enteros")
    print("En caso de tener decimales introducelo con '.'")
    sys.exit(1)

conversion = celsius * 1.8 + 32
print(f"La temperatura es de: {conversion:.2f} ºF")