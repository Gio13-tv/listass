import os
os.system("cls")

class ListaNombres:
    def __init__(self):
        self.nombres = []
    
    def pedir_nombres(self):
        otro_nombre = 's'
        while otro_nombre.lower() == 's':
            nombre = input("Ingresa un nombre: ")
            self.nombres.append(nombre.strip())  
            otro_nombre = input("¿Deseas agregar otro nombre? (s/n): ")
    
    def guardar_archivo(self):
        with open("nombres.txt", "w", encoding="utf-8") as archivo:
            archivo.write("Lista de nombres:\n")
            for nombre in self.nombres:
                archivo.write(nombre + "\n")
        print("\n Archivo 'nombres.txt' creado correctamente.")

if __name__ == "__main__":
    lista = ListaNombres()
    lista.pedir_nombres()
    lista.guardar_archivo()

    print("\nNombres ingresados:")
    for nombre in lista.nombres:
        print(f"- {nombre}")
