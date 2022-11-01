from csv import excel_tab
from glob import iglob
import pandas as pd

# Debe utilizar: colecciones (listas, tuplas, etc), 
# funciones y clases de Python.

class Libro():

    def __init__(self):
        self.libros = pd.read_csv('libros.csv')
        

    def leer(self):
        
        #return self.libros
        pass

    def listarLibros(self): #//!ALVARO
        
        #self.res = self.leer()
        print(self.libros.sort_values(by="TITULO", ascending=True).head(3))


    def buscarLibro(self):
        '''
        Buscar libros por autor, editorial o género. 
        Se deben sugerir las opciones y listar los resultados.
        '''
        pass

    def buscar_num_Autores(self): #//!ALVARO
        '''Buscar libros por número de autores. 
        Se debe ingresar un número por ejemplo 2 
        (hace referencia a dos autores) y se 
         deben listar todos los libros que 
         contengan 2 autores.'''

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

        
    
    def agregarLibro(self):#//!ALVARO
        
        self.ultimoDig = int(self.libros['ID'].tail(1))
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
        
    def actualizarLibro(self): #//!MAMUT
        '''Editar o actualizar datos de un libro 
        (título, género, ISBN, editorial y autores).
        '''
        pass

    def guardaLibro(self): #//!ALVARO
        ''' Guardar libros en archivo de disco duro (.txt o csv).'''
        self.libros.to_csv('libros.csv', index=False)
        print(self.libros.sort_values(by="TITULO", ascending=True).head(10))
        

    def eliminarLibro(self): #//!MAMUT
        pass

#Libro().listarLibros()
#Libro().buscar_num_Autores()
Libro().agregarLibro()
