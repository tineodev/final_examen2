import pandas as pd

# Debe utilizar: colecciones (listas, tuplas, etc), 
# funciones y clases de Python.

class Libro():

    def __init__(self):
        pass

    def leer(self):
        self.libros = pd.read_csv('libros.csv', sep=';')
        return self.libros

    def listarLibros(self):
        '''listar libros involucra: título, género, ISBN,
         editorial y autor(es).
         ordenar por titulo
         '''
        pass

    def buscarLibro(self):
        '''
        Buscar libros por autor, editorial o género. 
        Se deben sugerir las opciones y listar los resultados.
        '''
        pass

    def buscar_num_Autores(self):

        '''Buscar libros por número de autores. 
        Se debe ingresar un número por ejemplo 2 
        (hace referencia a dos autores) y se 
         deben listar todos los libros que 
         contengan 2 autores.'''
        pass

    def agregarLibro(self):
        pass

    def actualizarLibro(self):
        '''Editar o actualizar datos de un libro 
        (título, género, ISBN, editorial y autores).
        '''
        pass

    def guardaLibro(self):
        ''' Guardar libros en archivo de disco duro (.txt o csv).'''
        pass

    def eliminarLibro(self):
        pass