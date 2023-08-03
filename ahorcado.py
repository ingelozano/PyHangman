import random
from colorama import init, Fore, Style
# Representación del muñeco en ASCII

ahorcado = [
    "  +---+",
    "  |   |",
    "  O   |",
    " /|\  |",
    " / \  |",
    "      |",
    "========="
]

# Inicializar colorama para trabajar con colores en la consola
init(autoreset=True)

# Lista de palabras para adivinar
palabras = ["python", "programacion", "juego", "ahorcado", "divertido", "colorama", "emoji", "computadora", "programador", "python", "inteligencia",
    "artificial", "algoritmo", "desarrollo", "web", "datos", "tecnologia", "seguridad", "videojuego", "android", "smartphone", "criptomoneda", "nube",
    "aplicacion", "robotica", "inteligente", "internet", "redes", "virtual", "software", "hardware", "sistema", "ingenieria", "electronicos", "proyecto",
    "innovacion", "hamburguesa", "paraguas", "felicidad", "fotografia", "elefante", "bicicleta", "guitarra", "universidad", "mariposa", "chocolate",
    "reloj", "naturaleza", "aventura", "futbol", "viaje", "globo", "estrella", "emocion", "musica", "escritura", "fantasia", "montaña", "amistad",
    "sabiduria", "oasis", "equilibrio", "creatividad", "armonia", "magia", "independencia", "abrazo", "plenitud", "florecer", "paz",
    "silencio", "soledad", "fortaleza", "sueño", "inspiracion"]

# Función para obtener una palabra aleatoria
def obtener_palabra():
    return random.choice(palabras)

# Función para mostrar el estado actual del juego
def mostrar_tablero(palabra_oculta, intentos):
    print(Fore.BLUE + "Ahorcado:")
    print(Fore.YELLOW + " ".join(palabra_oculta))
    print(Fore.RED + f"Intentos restantes: {6 - intentos}")
    print(Fore.GREEN + "===================")

# Función principal del juego
def jugar():
    palabra = obtener_palabra()
    palabra_oculta = ["_"] * len(palabra)
    intentos = 0
    letras_adivinadas = []

    while intentos < 6:
        mostrar_tablero(palabra_oculta, intentos)
        letra = input(Fore.CYAN + "Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print(Fore.RED + "¡Ingresa una sola letra!")
            continue

        if letra in letras_adivinadas:
            print(Fore.RED + "¡Ya has ingresado esa letra antes!")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            for i, char in enumerate(palabra):
                if char == letra:
                    palabra_oculta[i] = letra
        else:
            intentos += 1

        if "_" not in palabra_oculta:
            print(Fore.GREEN + "¡Felicidades! ¡Has adivinado la palabra!")
            break

    else:
        print(Fore.RED + "  +---+")
        print(Fore.RED + "  |   |")
        print(Fore.RED + "  O   |")
        print(Fore.RED + " /|\  |")
        print(Fore.RED + " / \  |")
        print(Fore.RED + "      |")
        print(Fore.RED + "=========")
        print(Fore.RED + f"¡Perdiste! La palabra era: {palabra} ")

if __name__ == "__main__":
    print(Fore.MAGENTA + "Bienvenido al Juego del Ahorcado!")
    jugar()
