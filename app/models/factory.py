from app.models.pokemon import Pokemon
from app.models.pokemon_favorite import PokemonFavorites
from app.models.users import Users

class ModelFactory: #Instancear
    @staticmethod
    def get_model(collection_name):
        models = {
            "users": Users,
            "pokemons": Pokemon,
            "pokemon:favorites": PokemonFavorites
        }
        if collection_name in models:
            return models[collection_name]() #Estamos instanceando la clase
        raise ValueError(f"Upss, la colección enviado: {collection_name} no existe") #f - concatenar los strings de manera dinamica