import pandas as pd
import os

# Debe utilizar: colecciones (listas, tuplas, etc), 
# funciones y clases de Python.

class Libro():

    def __init__(self):
        self.libros = pd.read_csv('libros.csv')



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

