import sys

try:
    horas = int(input("Introduzca las horas trabajadas: "))

except ValueError:
    print("Introduce las horas en numeros enteros")
    sys.exit(1)

try:
    coste = float(input("Introduce el coste por hora: "))

except ValueError:
    print("Introduce el coste de las horas en numeros separados por '.'")
    sys.exit(1)

total = horas * coste
print(f"Importe total: {total}")