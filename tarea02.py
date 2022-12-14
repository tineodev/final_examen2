import requests
import time
import os


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

    # * Funcion - obtener los datos de generacion & forma & habilidad 
    def funcion_universal(self, pm_url:str, pm_tipo_dato:str):
        lista_opciones_1 = ["generación", "hábitat", "forma"]
        data = self.__conectaAPI(pm_url)
        lista_datos:list = [variable["name"] for variable in data["results"]]


        # * Imprime en pantalla - opciones de pm_tipo_dato
        print(f"Digite la opción de {pm_tipo_dato} del que desea ver")
        contador = 0
        for i in lista_datos:
            print(f"[{contador+1}]: {i}")
            contador+=1
        # numero = int(input("Opción: "))
        # numero -= 1
        numero = fuera_rango(len(lista_datos)) -1 #type: ignore


        # * Url especiess + link
        url = data["results"][numero]["url"]
        data_2 = self.__conectaAPI(url)


        # * Variable & direccion de tipo de dato
        if pm_tipo_dato in lista_opciones_1:
            lista_pokemon:list = [variable["name"] for variable in data_2["pokemon_species"]]
        else:
            lista_pokemon = [variable["pokemon"]["name"] for variable in data_2["pokemon"]]
        lista_pokemon_link:list = [f"https://pokeapi.co/api/v2/pokemon/{link}/" for link in lista_pokemon]

        titulo = f" {pm_tipo_dato.capitalize()} - Pokemons "
        print(titulo.center(60, "="))
        print()

        # * Sacar stats de cada pokemon:
        for i in lista_pokemon_link:
            data_3 = self.__conectaAPI(i)
            print(f"Nombre: {data_3['name']}")
            print(f"URL Imagen: {data_3['sprites']['front_default']}")
            lista_abilities = [skill["ability"]["name"] for skill in data_3["abilities"]]
            print("Habilidades:")
            for i in lista_abilities:
                print(f"\t{i}")
            print()


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



#* Funcion limpiar consola
def limpiar_consola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



#* Funcion evitar salir de rango
def fuera_rango(pm_limite):
    while True:
        numero_rango = input("Opción: / EXIT para salir. ")
        if numero_rango == "exit":
            break
        else:
            try:
                numero_rango = int(numero_rango)
                if  numero_rango > pm_limite or numero_rango <= 0:
                    print("Opción fuera de límite")
                else:
                    limpiar_consola()
                    return numero_rango
            except:
                print("Digite un número, vuelva a intentarlo")



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
