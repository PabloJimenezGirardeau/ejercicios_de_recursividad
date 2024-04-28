'''Este código implementa un algoritmo para ordenar una lista de fichas que pueden ser de tres colores:
 rojo (R), verde (V) y azul (B). El objetivo es ordenar las fichas de modo que todos los rojos estén al
principio, seguidos por los verdes y finalmente los azules, todo en una sola pasada por la lista.'''
def permutar(fichas):
    i = 0  # Inicio de la sección roja
    j = 0  # Explorador que recorre la lista
    k = len(fichas) - 1  # Final de la sección azul
    while j <= k:
        if fichas[j] == 'R':  # Si encuentra una ficha roja
            fichas[i], fichas[j] = fichas[j], fichas[i]  # La mueve al inicio
            i += 1  # Avanza el límite de la sección roja
            j += 1  # Continúa al siguiente elemento
        elif fichas[j] == 'V':  # Si encuentra una ficha verde
            j += 1  # Solo avanza el explorador, el verde está en su lugar
        else:  # Si encuentra una ficha azul
            fichas[k], fichas[j] = fichas[j], fichas[k]  # La mueve al final
            k -= 1  # Retrocede el límite de la sección azul
    return fichas  # Devuelve la lista ordenada

def input_fichas():
    while True:
        entrada = input(f"Introduce una lista de fichas (R, V, B) separadas por comas \n (no hace falta que esten ordenadas): ")
        fichas = entrada.split(',')
        fichas = [f.strip().upper() for f in fichas]  # Limpiar y normalizar el input
        if all(f in {'R', 'V', 'B'} for f in fichas):
            return fichas
        else:
            print("Error: Solo se permiten los caracteres 'R', 'V', 'B'. Intenta de nuevo.")

# Solicitar input al usuario
fichas_usuario = input_fichas()
print("Antes de ordenar:","".join(fichas_usuario))
fichas_ordenadas = permutar(fichas_usuario)
print("Después de ordenar:", "".join(fichas_ordenadas))
