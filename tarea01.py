import pandas as pd
import os

# Debe utilizar: colecciones (listas, tuplas, etc), 
# funciones y clases de Python.

class Libro():

    def __init__(self):
        self.libros = pd.read_csv('libros.csv')
        self.opciones = ["Listar todos los libros", "Editar libro", "Eliminar libro", "Agregar libro", "Filtrar por ..."]
        self.filtrar = ["ID","TITULO","GENERO","ISBN","EDITORIAL","AUTORES"]
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
            pass
        elif opcion == 4:
            pass
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
        pass



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
                print(self.libros["TITULO"][int(x[0])])
                flag = True

        if not(flag):
            print(f"No existen libros con {num} autor(es)")



    def agregarLibro(self):
        pass



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



    def actualizarLibro(self):
        '''Editar o actualizar datos de un libro 
        (título, género, ISBN, editorial y autores).
        '''
        pass



    def guardaLibro(self):
        ''' Guardar libros en archivo de disco duro (.txt o csv).'''
        self.libros.to_csv('libros.csv', index=False)
        print(self.libros.sort_values(by="TITULO", ascending=True).head(10))



    def eliminarLibro(self):
        pass


print("Bienvenido!")
obj_1 = Libro()
obj_1.preguntar_funcionalidad()

