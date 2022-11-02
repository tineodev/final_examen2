import requests
import time

#listar pokemons involucra: nombre, habilidad y URL de la imagen
class Pokemon:
    def __init__(self,sel):
        
        # self.pk = self.__conectaAPI()
        self.sel = sel
        self.urlPokemon = 'https://pokeapi.co/api/v2/pokemon/'
        self.urlGeneracion = "https://pokeapi.co/api/v2/generation/"
        self.urlForma = "https://pokeapi.co/api/v2/pokemon-shape/"
        self.urlHabilidad = "https://pokeapi.co/api/v2/ability/"
        self.urlHabitat = "https://pokeapi.co/api/v2/pokemon-habitat/"
        self.urlTipo = "https://pokeapi.co/api/v2/type/"

        self.__pokeRes = "" #Almacena el json de todas las opciones

        self.__pokeSeleccion()

    def __pokeSeleccion(self):
        if self.sel == 1:
            self.funcion_universal(self.urlGeneracion, "generación")
        if self.sel == 2:
            self.funcion_universal(self.urlForma, "forma")
        if self.sel == 3:
            self.funcion_universal(self.urlHabilidad, "habilidad")
        if self.sel == 4:
            self.__pokeRes = self.__conectaAPI(self.urlHabitat)
            self.pokeHabitat()
        if self.sel == 5:
            self.__pokeRes = self.__conectaAPI(self.urlTipo)
            self.pokeTipo()

    
    def __conectaAPI(self,url):
        res = requests.get(url)

        if res.status_code != 200:
            print("Pokemon no encontrado")
            exit()
        else:
            return res.json()
        

    def __str__(self) -> None:
        pass

    def pokeGeneracion(self):
        '''Listar pokemons por generación. 
        Se ingresa alguna generación (1, 2, 3, ..)
        y se listan todos los pokemon respectivos.'''
        pass

    def pokeForma(self):
        '''Listar pokemons por forma. Se ingresa 
        alguna forma (deben sugerir valores) y se 
        listan todos los pokemons respectivos.'''
        pass

    def pokeHabilidad(self):
        '''Listar pokemons por habilidad. Se deben 
        sugerir opciones a ingresar para interactuar.'''
    
    def pokeHabitat(self):
        lista = []
        for i in range(int(self.__pokeRes["count"])):  # type: ignore
            lista.append(self.__pokeRes["results"][i]["name"]) # type: ignore

        print("\nSelecciona el HABITAT por su número:")
        for i,x in enumerate(lista, start=1):
            print(f"\t[{i}]: {x.capitalize()}")
        
        res = ""
        while res not in range(1,len(lista)+1):
            try:
                res = int(input("OPCIÓN: "))
            except ValueError:
                continue

        listaPokemon = self.__conectaAPI(self.urlHabitat+(str(res)))
        
        for i in range(len(listaPokemon["pokemon_species"])):
            self.nomPokemon = listaPokemon["pokemon_species"][int(i)]["name"]
            
            self.pokeDetalles(self.nomPokemon)


    def pokeDetalles(self, nombre):

        self.infoPokemon = self.__conectaAPI(self.urlPokemon + nombre)

        print(f"\t{nombre.upper()}")
        print("\tImagen: ", self.infoPokemon['sprites']['front_default'])
        print("\tHabilidades:")

        for j in self.infoPokemon["abilities"]:
            print("\t\t*",j["ability"]["name"].capitalize())
    
    
    def pokeTipo(self):
        '''Listar pokemons por tipo. Se deben sugerir
        opciones a ingresar para interactuar.'''
        lista = []
        for i in range(int(self.__pokeRes["count"])): # type: ignore
            lista.append(self.__pokeRes["results"][i]["name"]) # type: ignore

        print("\nSelecciona el TIPO por su número:")
        for i,x in enumerate(lista, start=1):
            print(f"\t[{i}]: {x.capitalize()}")
        
        res = ""
        while res not in range(1,len(lista)+1):
            try:
                res = int(input("OPCIÓN: "))
            except ValueError:
                continue

        if res == 19:
            res = 10001
            print("No hay ningún Pokemón agregado a esta lista.")
        elif res == 20:
            res = 10002
            print("No hay ningún Pokemón agregado a esta lista.")

        listaPokemon = self.__conectaAPI(self.urlTipo+(str(res)))

        for i in range(len(listaPokemon["pokemon"])):
            self.nomPokemon = listaPokemon["pokemon"][int(i)]["pokemon"]["name"]
            self.pokeDetalles(self.nomPokemon)

while True:
    print("OPCIONES A SELECCIONAR:")
    print("\t[1]: Listar por generación.")
    print("\t[2]: Listar por forma.")
    print("\t[3]: Listar por habilidad.")
    print("\t[4]: listar por habitat.")
    print("\t[5]: Listar por tipo.")

    try:
        sel = int(input("Ingresar número de la opción a listar: ").strip()) 
    except ValueError:
        print("Debe ingresar un número entre el 1 al 5.")
    except Exception:
        print("ERROR, vuelve a intentarlo")
    else:
        if sel not in range(1,6):
            print("\tDebe ser un número entre 1 al 5.\n")
            continue
        else:
            break

Pokemon(sel)
