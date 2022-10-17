from colorama import init, Fore, Back, Style
import random


class Queue:
    def __init__(self):
        self.queue = []

    def print_queue(self):
        print(self.queue)

    def enqueue(self, e):
        self.queue.append(e)

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Cola vacía...")
        return self.queue.pop(0)

    def first(self):
        if (self.is_empty()):
            raise Exception("Cola vacía...")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def _len_(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, new):
        self.stack.append(new)

    def pop(self):
        if self.is_empty():
            raise Exception("Pila vacía...")
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            raise Exception("Pila vacía...")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def len(self):  # dunder method
        return len(self.stack)


rojo = Fore.RED
verde = Fore.GREEN
amarillo = Fore.YELLOW
reset = Style.RESET_ALL

palabras = ["PLATO", "ARBOL", "BOLSO", "BLUSA", "ANDES", "ANIMO", "CAJAS", "CHILE", "CUBOS", "CLAVO", "FUMAR", "MANGO",
            "PATOS", "JAPON", "MINAR", "MINAS", "PESOS", "PECES", "MUROS", "MULAS", "MULTA", "PUMAS", "PRADO", "SUDAR",
            "CIEGO", "SIRIA", "SEDAN", "VACAS", "VIAJE", "ICONO", "VOTOS", "VINOS", "ATOMO", "TOMAR", "BEBER",
            "BEBES"]  # 36 palabras

menu = True
print("Bienvenido a Wordle by: Juan Jose Giraldo")
print("")
print("Es sencillo, tienes que escribir una palabra y ver las letras que has acertado,\n",
"que tendrán diferente color dependiendo de si acertaste: \n",
"Si la letra aparece en,", (Fore.GREEN + "verde"), Fore.RESET +", es porque la has acertado y está en la palabra, y también está en la casilla correcta de la palabra.\n",
"Si la letra aparece en", (Fore.YELLOW + "amarillo"), Fore.RESET +", es porque está en la palabra, pero no está en la casilla correcta.\n" ,
"Si la letra aparece en blanco es porque no has acertado, y no está en la palabra que tienes que adivinar.")
print("")
while menu:
    opcion = 0

    print("Ingrese:")
    print("1. Para iniciar el juego.")
    print("2. Para salir del juego.")

    opcion = input(": ")
    if opcion != "1" and opcion != "2":
        print("Ingrese una opción valida.")
    else:
        opcion = int(opcion)
        if opcion == 1:
            palabraAleatoria = palabras[random.randint(0, 35)]
            palabra1 = Queue()
            palabra2 = Queue()

            palabraU = Queue()
            letraU = Queue()
            intentos = 0

            # Se añade a la cola 1 letra por letra la palabra escogida aleatoriamente por el programa
            for i in range(5):
                letra = palabraAleatoria[i]
                palabra1.enqueue(letra)
            cont = 6
            while intentos < 5:
                cont += -1
                print("")
                print("Si pones 1 letra extra o una letra menos pierdes un intento")
                print("")
                print("tienes",int(cont),"intentos")
                palabrausuario = input("Ingrese una palabra de 5 letras: ").upper()
                if len(palabrausuario) < 5:
                    print("")
                    print("Numero equivocado de letras, pierdes un intento, tr lo advertí :).")
                    print("")
                    continue
                intentos += 1
                colores = [0, 0, 0, 0, 0]
                contador = 0

                # se añade a la cola la palabra que ingresa el usuario
                for i in range(5):
                    try:
                        letra = palabrausuario[i]
                        palabraU.enqueue(letra)
                    except IndexError:
                        pass
                # se evalua si las letras de la palabraU están en la palabra1
                for j in range(5):

                    while not palabra1.is_empty():
                        # se evalua la primera letra ingresada por el usuario en toda la palabra 1
                        if palabra1.first() == palabraU.first():
                            colores[j] = 2
                        palabra1.dequeue()
                    # Se cambia a la siguiente letra ingresada por el usuario
                    palabraU.dequeue()

                    # se añade otra vez la palabra aleatoria a una cola vacia para evaluarla toda por la letra
                    # siguiente ingresada por el usuario
                    for m in range(5):
                        letra = palabraAleatoria[m]
                        palabra1.enqueue(letra)

                # se añade toda la palabra del usuario a la cola vacia
                for i in range(5):
                    letra = palabrausuario[i]
                    palabraU.enqueue(letra)

                # se evalua si las letras están en la posicion correcta y se vacian las colas
                for i in range(5):
                    if palabra1.dequeue() == palabraU.dequeue():
                        colores[i] = 1

                # se añade toda la palabra aleatoria a la cola vacia
                for i in range(5):
                    letra = palabraAleatoria[i]
                    palabra1.enqueue(letra)

                # se añade toda la palabra del usuario a la cola vacia
                for i in range(5):
                    letra = palabrausuario[i]
                    palabraU.enqueue(letra)

                # se imprimen las letras con su color correspondiente
                for i in range(5):
                    if colores[i] == 0:
                        print(palabraU.dequeue())
                    elif colores[i] == 1:
                        print(verde + palabraU.dequeue() + reset)
                    elif colores[i] == 2:
                        print(amarillo + palabraU.dequeue() + reset)

                # se vacia la cola para evitar errores con otros intentos del usuario
                for i in range(5):
                    if not palabraU.is_empty():
                        palabraU.dequeue()

            palabra1.print_queue()
            print("")
            print("quieres volver a Jugar??")

        else:
            break
