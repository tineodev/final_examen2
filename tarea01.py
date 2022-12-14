import pandas as pd
import os

# Debe utilizar: colecciones (listas, tuplas, etc), 
# funciones y clases de Python.

class Libro():

    def __init__(self):
        self.libros = pd.read_csv('libros.csv')
        self.opciones = ["Listar todos los libros", "Editar libro", "Eliminar libro", "Agregar libro","Buscar por número de autores", "Buscar por ..."]
        self.filtrar = ["TITULO","GENERO","ISBN","EDITORIAL","AUTORES"]
        self.cantidad = len(self.libros.index)



    def preguntar_funcionalidad(self):
        ''' Pregunta al usuario que accion quiere realizar'''
        print("\nFuncionalidades: ")
        contador = 0
        for i in self.opciones:
            print(f"{contador+1}) {i}")
            contador +=1
        opcion = fuera_rango(contador, "Opción", 0)
        opcion -=1 # type: ignore
        opcion_escogida = self.opciones[opcion]
        print(f" Opcion escogida: {opcion_escogida}\n")
        
        # * Ejecutar funcion
        if opcion ==0:
            self.listarLibros()
        if opcion == 1:
            self.seleccionar_libro(self.cantidad, "actualizar") 
        elif opcion == 2:
            self.seleccionar_libro(self.cantidad, "eliminar") 
        elif opcion == 3:
            self.agregarLibro()
        elif opcion == 4:
            self.buscar_num_Autores()
        elif opcion == 5:
            self.buscarLibro()
        else:
            exit()



    def leer(self):
        self.libros = pd.read_csv('libros.csv', sep=';')
        return self.libros



    def listarLibros(self):
        print(self.libros.sort_values(by="TITULO", ascending=True).head(3))



    def buscarLibro(self):
        '''
        Buscar libros por autor, editorial o género. 
        Se deben sugerir las opciones y listar los resultados.
        '''
        print("Modo búsqueda:")
        for i in self.filtrar:
            print(f"* {i}")
        columna = input("Ingrese una opcion: ").upper().strip()
        celda = input(f"Ingrese una opcion de {columna}: ").strip()

        try: 
            match columna:
                case 'ISBN':
                    dataFrame = self.libros[self.libros['ISBN'] == celda]
                    print(dataFrame)
                case _:
                    dataFrame = self.libros[self.libros[columna].str.contains(celda)]
                    print(dataFrame)
        except:
            print(f"No se ha encontrado {celda} en {columna}, inténtelo de nuevo.")



    def buscar_num_Autores(self):
        flag = False
        while True:
            try:
                num = int(input("Buscar libros por número de autores: "))
            
            except ValueError:
                print("Debe ser un número.")
            except Exception:
                print("ERROR: Vuelva a intentarlo.")
            else:
                break

        for x in self.libros["AUTORES"].items():
            if (x[1].count("|")+1) == num:
                print(self.libros["TITULO"][int(x[0])]) #type: ignore
                flag = True

        if not(flag):
            print(f"No existen libros con {num} autor(es)")


    def agregarLibro(self):

        self.ultimoDig = int(self.libros['ID'].tail(1)) #type: ignore
        while True:
            self.titulo = str(input("Ingresar TITULO del libro: "))
            if (self.titulo != ""): break
        while True:
            self.genero = str(input("Ingresar GENERO del libro: "))
            if (self.genero != ""): break
        while True:
            self.isbn = str(input("Ingresar ISBN del libro: "))
            if (self.isbn != ""): break
        while True:
            self.editorial = str(input("Ingresar EDITORIAL del libro: "))
            if (self.editorial != ""): break
        while True:
            self.autores = str(input("Ingresar AUTOR del libro [Si son más de 2, separar con '|']: "))
            if (self.autores != ""): break
            
        agregar = {
            'ID': self.ultimoDig+1,
            'TITULO': self.titulo,
            'GENERO': self.genero,
            'ISBN': self.isbn,
            'EDITORIAL': self.editorial,
            'AUTORES': self.autores
        }

        self.libros = self.libros.append(agregar,ignore_index=True)

        self.guardaLibro()

    def seleccionar_libro(self, pm_limite:int, pm_opcion):
        ''' * Indica indice del libro '''
        print(self.libros)
        indice = fuera_rango(pm_limite, "Índice del libro", -1)
        try:
            try:
                if pm_opcion == "actualizar":
                    self.actualizar_libro(indice)
                elif pm_opcion =="eliminar":
                    self.eliminar_libro(indice)
            except:
                print("Libro no encontrado, pruebe otra vez")
        except:
            limpiar_consola()
            print(self.libros)
            self.preguntar_funcionalidad()



    def actualizar_libro(self,pm_libro):
        '''Editar o actualizar datos de un libro 
        (título, género, ISBN, editorial y autores).
        '''
        print("Modo edición\n")
        unidad = self.libros.iloc[pm_libro]
        print(unidad)

        def actualizar_unidad(pm_libro):
            lista = list(unidad)   # type: ignore
            # Opciones
            lista_items = ["ID","TITULO","GENERO","ISBN","EDITORIAL","AUTORES"]
            print("ID - TITULO - GENERO - ISBN - EDITORIAL - AUTORES")

            # Preguntar item a editar
            while True:
                pregunta = input("(EXIT para salir) ¿Qué item desea editar? ").upper().strip()
                if pregunta == "EXIT":
                    limpiar_consola()
                    break
                elif pregunta not in lista_items:
                    print("Ingrese un valor correcto o escriba EXIT\n")
                else:
                    if pregunta == lista_items[5]:
                        print("Formato:\n\tAutor 1|Autor 2|Autor3 ...")
                    index = lista_items.index(pregunta)
                    cambiar = input(f"Cambiar '{lista[index]}' por: ")
                    print(f"Se cambió {pregunta}")
                    self.libros._set_value(pm_libro, pregunta, cambiar)
                    self.libros.to_csv('libros.csv', encoding='utf-8', index=False)

        # Preguntar Editar el libro
        while True:
            pregunta = input("\n¿Desea editar este libro? (Y/N) ").lower().strip()
            if pregunta == "y":
                print()
                print("Modo Edición")
                actualizar_unidad(pm_libro)
                break
            elif pregunta == "n":
                limpiar_consola()
                print("Modo vista")
                self.preguntar_funcionalidad()
                break
            else:
                print("Intentelo de nuevo")
        print(self.libros)



    def guardaLibro(self):
        ''' Guardar libros en archivo de disco duro (.txt o csv).'''
        self.libros.to_csv('libros.csv', index=False)
        print(self.libros.sort_values(by="TITULO", ascending=True).head(10))


    def eliminar_libro(self,pm_libro):
        print("Modo eliminar libro")
        self.libros.drop(pm_libro, inplace=True)
        self.libros.to_csv('libros.csv', index=False)
        print(self.libros)
        print(f"Eliminado numero {pm_libro}")




# ? Funciones extra
# * Funcion limpiar consola
def limpiar_consola():
    if os.name == "nt": 
        os.system("cls")
    else:
        os.system("clear")



#* Funcion evitar salir de rango
def fuera_rango(pm_limite, pm_variable, pm_base):
    while True:
        numero_rango = input(f"{pm_variable}: ")
        if numero_rango.lower().strip() == "exit":
            break
        else:
            try:
                numero_rango = int(numero_rango)
                if  numero_rango > pm_limite or numero_rango <= pm_base:
                    print(f"{pm_variable} fuera de límite")
                else:
                    limpiar_consola()
                    return numero_rango
            except:
                print("Digite un número, vuelva a intentarlo")



print("Bienvenido!")
obj_1 = Libro()
obj_1.preguntar_funcionalidad()

