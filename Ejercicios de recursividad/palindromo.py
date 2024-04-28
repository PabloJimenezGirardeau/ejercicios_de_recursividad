def sin_acentos(texto):
    #Reemplaza los caracteres acentuados por sus equivalentes sin acento. 
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'À': 'A', 'È': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'Â': 'A', 'Ê': 'E', 'Î': 'I', 'Ô': 'O', 'Û': 'U',
        'ñ': 'n', 'Ñ': 'N', 'ç': 'c', 'Ç': 'C'
    }
    return ''.join(acentos.get(c, c) for c in texto)

def filtrar_alfanumericos(texto):
    #Filtra y conserva solo los caracteres alfanuméricos del texto.
    return ''.join(c for c in texto if c.isalnum())

def es_palindromo(frase):
    #Determina si la frase es un palíndromo. 
    if frase is None:
        return False
    frase_filtrada = filtrar_alfanumericos(sin_acentos(frase))
    frase_filtrada = frase_filtrada.upper()  # Convierte a mayúsculas
    return frase_filtrada == frase_filtrada[::-1]  # Compara con su imagen reflejada

def verificar_palindromos_ejemplos():
    """ Verifica ejemplos predefinidos de palíndromos. """
    ejemplos = [
        "Dábale arroz a la zorra el abad",
        "Logré ver gol",
        "Salas",
        "1754571",
        "10000000000000000001",
        "Oso",
        "no es palindromo"
    ]

    for ejemplo in ejemplos:
        es_pal = es_palindromo(ejemplo)
        print(f"'{ejemplo}' es palíndromo?: {es_pal}")

def verificar_palindromo_usuario():
    #Solicita al usuario ingresar una frase y verifica si es un palíndromo. 
    frase_usuario = input("Por favor, ingrese una frase para verificar si es un palíndromo: ")
    if es_palindromo(frase_usuario):
        print("La frase ingresada es un palíndromo.")
    else:
        print("La frase ingresada no es un palíndromo.")

# Verificar los ejemplos predefinidos
verificar_palindromos_ejemplos()

# Luego verificar la entrada del usuario
verificar_palindromo_usuario()
