from app import mongo 

class PokemonSaved:
    collection = mongo.db.pokemons_saved

    @staticmethod
    def find_all():
        pokemons = PokemonSaved.collection.find()
        return list(pokemons)
    
    @staticmethod
    def find_by_id(pokemon_id):
        pokemon = PokemonSaved.collection.find_one({
            "_id": pokemon_id
        })
        return pokemon

    @staticmethod
    def create(data):
        pokemon = PokemonSaved.collection.insert_one(data)
        return pokemon.inserted_id

    @staticmethod
    def update(pokemon_id, data):
        pokemon = PokemonSaved.collection.update_one({
            "_id": pokemon_id
        }, {
            "$set": data
        })
        return pokemon

    @staticmethod
    def delete(pokemon_id):
        return  PokemonSaved.collection.delete_one({"_id": pokemon_id})
       