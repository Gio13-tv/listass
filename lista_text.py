import os
os.system("cls")

class ListaNombres:
    def __init__(self):
        self.nombres = []
    
    def pedir_nombres(self):
        otro_nombre = 's'
        while otro_nombre == 's':
            nombre = input("Ingresa un nombre: ")
            self.nombres.append(nombre)
            otro_nombre = input("¿Otro nombre? (s/n): ")
    
    def guardar_archivo(self):
        with open("nombres.txt", "w") as archivo:
            for nombre in self.nombres:
                archivo.write(nombre + "\n")
        print("Archivo creado")

lista = ListaNombres()
lista.pedir_nombres()
lista.guardar_archivo()

print("\nNombres ingresados:")
for nombre in lista.nombres:
    print(nombre)