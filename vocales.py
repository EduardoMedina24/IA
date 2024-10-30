# Programa para contar vocales en una frase y almacenarlas en un arreglo

# Solicitar al usuario que ingrese una frase
frase = input("Ingresa una frase: ")

# Inicializar el contador y el arreglo para almacenar las vocales
contador_vocales = 0
vocales_encontradas = []

# Definir las vocales en minúsculas y mayúsculas para búsqueda
vocales = "aeiouAEIOU"

# Recorrer cada letra en la frase
for letra in frase:
    # Si la letra es una vocal
    if letra in vocales:
        contador_vocales += 1
        vocales_encontradas.append(letra)

# Mostrar resultados
print(f"Cantidad de vocales encontradas: {contador_vocales}")
print(f"Vocales específicas encontradas: {vocales_encontradas}")
