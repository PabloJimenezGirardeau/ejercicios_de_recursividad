def dicotomia(tabla, t):
    if not tabla:
        return 'AUSENTE'
    if t < tabla[0] or t > tabla[-1]:  # Verifica los límites de la tabla
        return 'AUSENTE'
    return dicotomia_recursiva(tabla, t, 0, len(tabla) - 1)

def dicotomia_recursiva(tabla, t, inicio, fin):
    if inicio > fin:
        return 'AUSENTE'
    m = (inicio + fin) // 2
    if tabla[m] == t:
        return m
    elif tabla[m] < t:
        return dicotomia_recursiva(tabla, t, m + 1, fin)
    else:
        return dicotomia_recursiva(tabla, t, inicio, m - 1)

def solicitar_valor_tabla(tabla):
    while True:
        try:
            valor = int(input("Por favor, ingrese un valor para buscar en la tabla: "))
            if valor in tabla:
                return valor
            else:
                print("El valor ingresado no está en la tabla. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida.")

# Ejemplo de uso
tabla = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Tabla ordenada
print("Tabla:", tabla)
t = solicitar_valor_tabla(tabla)
resultado = dicotomia(tabla, t)
print(f"El índice de {t} en la tabla es: {resultado}")
