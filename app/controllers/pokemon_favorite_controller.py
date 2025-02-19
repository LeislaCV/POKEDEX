#SOLAMENTE SE CREA Y SE ELIMINA
#MODIFICAR EL MODELO Y EVITAR QUE LOS USUARIOS USEN METODOS INDEBIDOS
#METODOS: CREATE, DELETE
from flask import Blueprint, request, jsonify #Blueprint seccionar el servidor por carpetitas, Request maneja la peticion que haga el usuario, jsonify  response  
from app.schemas.pokemons_favorites_schema import PokemonFavoriteSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory #Traer la colección de usuarios
from bson import ObjectId #Formato que maneja mongo

bp = Blueprint("pokemon_favorite", __name__, url_prefix="/pokemon_favorite")
pokemon_favorite_schema = PokemonFavoriteSchema() #Instanciar
pokemon_favorite_model = ModelFactory.get_model("pokemon_favorites") #Ir por el modelo de POKEMONES FAVORITOS que ya declaramos

#CREAR
@bp.route("/create", methods=["POST"]) #
def create():
    try:
        data = pokemon_favorite_schema.load(request.json) #Valida la informacion que se esta mandando, si algo anda mal va lanzar un error, error de validación "try, except"
        pokemon_favorite_id = pokemon_favorite_model.create(data)  #Retorna el id insertado tipo especifico ObjectId
        return jsonify({pokemon_favorite_id:str(pokemon_favorite_id)}), 200 #200 es un código de respuesta

    except ValidationError as err:
        return jsonify("Upss, Los parametros enviados son incorrectos"), 400 #Espera dos argumentos un mensaje y un código "err 400"
    
#ELIMINAR

@bp.route("/delete/<strinng:pokemon_favorite_id>", methods = ["DELETE"]) #Va venir con parametro con la ruta
def delete(pokemon_favorite_id):
    pokemon_favorite_model.delete(ObjectId(pokemon_favorite_id)) #Esta recibiendo dos parametros, objectid
    return jsonify("Yeiii, pokemon eliminado con éxito jiji"), 200