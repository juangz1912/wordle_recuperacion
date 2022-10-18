from colorama import init, Fore, Back, Style
import random

#Hecho por JUAN MANUEL GOMEZ Y JUAN JOSE GIRALDO
class Queue:
  def __init__(self):
    self.queue = []

  def print_queue(self):
    print(self.queue)
  def enqueue(self, e):
    self.queue.append(e)

  def dequeue(self):
    if(self.is_empty()):
      raise Exception("Cola vacía...")
    return self.queue.pop(0)


  def first(self):
    if(self.is_empty()):
      raise Exception("Cola vacía...")
    return self.queue[0]

  def is_empty(self):
    return len(self.queue)==0

  def __len__(self):
    return len(self.queue)

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
      "Si la letra aparece en,", (Fore.GREEN + "verde"),
      Fore.RESET + ", es porque la has acertado y está en la palabra, y también está en la casilla correcta de la palabra.\n",
      "Si la letra aparece en", (Fore.YELLOW + "amarillo"),
      Fore.RESET + ", es porque está en la palabra, pero no está en la casilla correcta.\n",
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
            intentos = 0


            cont = 7
            while intentos < 6:
                cont += -1
                print("Tienes", int(cont), "intentos")
                palabrausuario = ""

                palabrausuario = input("Ingrese una palabra de 5 letras: ").upper()
                while len(palabrausuario) < 5 or len(palabrausuario) > 5:
                    print("La palabra debe ser de CINCO letras.")
                    palabrausuario = input("Ingrese una palabra de 5 letras: ").upper()

                intentos += 1
                colores = [0, 0, 0, 0, 0]
                ganaste = [1, 1, 1, 1, 1]
                contador = 0

                # Se añade a la cola 1 letra por letra la palabra escogida aleatoriamente por el programa
                for i in range(5):
                    letra = palabraAleatoria[i]
                    palabra2.enqueue(letra)

                # se añade a la cola la palabra que ingresa el usuario
                for i in range(5):
                    try:
                        letra = palabrausuario[i]
                        palabraU.enqueue(letra)
                    except IndexError:
                        pass

                # se evalua si las letras están en la posicion correcta
                for i in range(5):
                    if palabra2.first() == palabraU.first():
                        colores[i] = 1
                        palabra2.dequeue()
                        palabraU.dequeue()
                    else:
                        palabra1.enqueue(palabra2.dequeue())
                        palabraU.dequeue()

                # se añade toda la palabra del usuario a la cola vacia
                for i in range(5):
                    letra = palabrausuario[i]
                    palabraU.enqueue(letra)

                if colores == ganaste:
                    for i in range(5):
                        print(Fore.GREEN + palabraU.dequeue() + Fore.RESET)
                    print(Fore.GREEN + "¡¡¡¡¡GANASTE!!!!!" + Fore.RESET)
                    break

                # se evalua si las letras de la palabraU están en la palabra1
                while not palabra1.is_empty():
                    if palabra1.first() == palabraU.first():
                        if colores[0] != 1:
                            colores[0] = 2
                        palabra1.dequeue()
                        break
                    else:
                        palabra2.enqueue(palabra1.dequeue())

                palabraU.dequeue()
                while not palabra1.is_empty():
                    palabra2.enqueue(palabra1.dequeue())

                while not palabra2.is_empty():
                    if palabra2.first() == palabraU.first():
                        if colores[1] == 1:
                            pass
                        else:
                            colores[1] = 2
                        palabra2.dequeue()
                        break
                    else:
                        palabra1.enqueue(palabra2.dequeue())

                palabraU.dequeue()
                while not palabra2.is_empty():
                    palabra1.enqueue(palabra2.dequeue())

                while not palabra1.is_empty():
                    if palabra1.first() == palabraU.first():
                        if colores[2] == 1:
                            pass
                        else:
                            colores[2] = 2
                        palabra1.dequeue()
                        break
                    else:
                        palabra2.enqueue(palabra1.dequeue())

                palabraU.dequeue()
                while not palabra1.is_empty():
                    palabra2.enqueue(palabra1.dequeue())

                while not palabra2.is_empty():
                    if palabra2.first() == palabraU.first():
                        if colores[3] == 1:
                            pass
                        else:
                            colores[3] = 2
                        palabra2.dequeue()
                        break
                    else:
                        palabra1.enqueue(palabra2.dequeue())

                palabraU.dequeue()
                while not palabra2.is_empty():
                    palabra1.enqueue(palabra2.dequeue())

                while not palabra1.is_empty():
                    if palabra1.first() == palabraU.first():
                        if colores[0] == 1:
                            pass
                        else:
                            colores[4] = 2
                        palabra1.dequeue()
                        break
                    else:
                        palabra2.enqueue(palabra1.dequeue())

                palabraU.dequeue()
                while not palabra1.is_empty():
                    palabra2.enqueue(palabra1.dequeue())

                # se añade toda la palabra aleatoria a la cola vacia
                for i in range(5):
                    letra = palabraAleatoria[i]
                    palabra1.enqueue(letra)

                # se añade toda la palabra del usuario a la cola vacia
                for i in range(5):
                    letra = palabrausuario[i]
                    palabraU.enqueue(letra)

                # se imprimen las letras con su color correspondiente
                if intentos == 6:
                    for i in range(5):
                        print(Fore.RED + palabraU.dequeue() + Fore.RESET)
                    print("")
                    print(Fore.RED + "!Ah no muchachos!" + Fore.RESET)
                    print(f"La palabra era: {palabraAleatoria}.")
                    break
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
                    if not palabra1.is_empty():
                        palabra1.dequeue()
                    if not palabra2.is_empty():
                        palabra2.dequeue()

        else:
            break
