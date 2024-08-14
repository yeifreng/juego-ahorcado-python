import random

# Funcion para que tome una palabra de manera aleatoria
def obtener_palabra_secreta():
    palabras = ['python', 'javascript', 'angular', 'react', 'laravel', 'typescript']
    return random.choice(palabras)

#Funcion para ir colocando la letra en cada posicion de acuerdo a la letra adivinada

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += '-'
    return adivinado

# Funcion que realiza el juego
def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()  #Guarda la palabra secreta de la primera funcion
    letras_adivinadas = [] #Variable que guardara en una lista, las letras adivinadas
    intentos = 10 #Intentos validos para jugar
    juego_terminado = False #Variable que sacara del while si se completo la palabra
    
    print('Bienvenido al juego del ahorcado')
    print(f'tienes {intentos} intentos para adivinar la palabra')
    #Cargar por pirmera vez las letras adivinadas de la palabra secreta
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), 'la cantidad de letras de la palabra es: ', len(palabra_secreta) )
    
    #Mientras el juego sea true y los intentos mayores a 0, sigue el juego
    while not juego_terminado and intentos > 0:
        adivinanza = input('introduce una letra: ').lower()
        if len(adivinanza) !=1 or not adivinanza.isalpha(): #el metodo isalpha nos devuelve true si el caracter es alfabetico
            print('por favor introduzca una letra valida(Solo escribir una letra)')
        elif adivinanza in letras_adivinadas:
            print('ya has utilizado esa letra, prueba otra')
        else:
            letras_adivinadas.append(adivinanza)
            
            if adivinanza in palabra_secreta:
                print(f'muy bien, la letra {adivinanza} esta presente en la palabra secreta')
            else:
                print(f'lo siento, la letra {adivinanza} no esta presente en la palabra secreta')
                intentos -= 1
                print(f'Te quedan {intentos} intentos')
                
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)
        
        if '-' not in progreso_actual:
            juego_terminado = True
            print(f'Felicidades has ganado, la palabra completa es {palabra_secreta}')
            
    if intentos == 0:
        print(f'Lo sientos, has llegado al limite de los intentos, la palabra secreta es {palabra_secreta}')
        
        
juego_ahorcado()