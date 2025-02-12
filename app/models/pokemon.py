from app import mongo

class Pokemon:
    collection = mongo.db.pokemons #Llave

    #Crear metodos, estaticos el estatico no lo podemos modificar
    #Metodo statico se crea con un arroba @
    #decorador - le asigna un saco a una funcion  

    @staticmethod
    def find_all():
        pokemons = Pokemon.collection.find() #Devuelve un tipo cursor, no es arreglo "cursos" manejador de datos
        return list(pokemons) #Metodo para encontrar todos los pokemones

    @staticmethod
    def find_by_id(pokemon_id): #Metodo para encontrar el pokemon unicamente por el "ID"
        pokemon = Pokemon.collection.find_one({ #Para crear un filtro es similar al crear un objeto
            "_id": pokemon_id
        }) 
        return pokemon
    
    @staticmethod 
    def create(data): #Metodo para crear un pokemon
        pokemon = Pokemon.collection.insert_one(data)
        return pokemon.inserted_id #Nos retorna el "ID" del pokemon que creamos
    
    @staticmethod
    def update(pokemon_id, data): #Metodo para guardar el pokemonn
        pokemon = Pokemon.collection.update_one({
            "_id": pokemon_id
        },{
            "$set": data 
        })
        return pokemon
    
    @staticmethod
    def delete(pokemon_id): #Metodo para eliminar el pokemon
        return Pokemon.collection.delete_one({"_id": pokemon_id})

    

    #Dos colecciones una de usuarios y otra de pokemones, pokemones guardados
    