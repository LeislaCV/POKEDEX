#METODOS: CREATE, DELETE, GET
from flask import Blueprint, request, jsonify #Blueprint seccionar el servidor por carpetitas, Request maneja la peticion que haga el usuario, jsonify  response  
from marshmallow import ValidationError
from app.models.factory import ModelFactory #Traer la colección de usuarios
from bson import ObjectId #Formato que maneja mongo

bp = Blueprint("pokemon", __name__, url_prefix="/pokemons")  #Blueprint se instancea, secciona el servidor en carpetitas
pokemon_model = ModelFactory.get_model("pokemons") #Ir por el modelo de pokemones que ya declaramos

#CREAR

@bp.route("/create", methods=["POST"]) #
def create():
    try:
        data = request.json
        pokemon_id = pokemon_model.create(data)  #Retorna el id insertado tipo especifico ObjectId
        return jsonify({pokemon_id:str(pokemon_id)}), 200 #200 es un código de respuesta

    except ValidationError as err:
        return jsonify("Upss, Los parametros enviados son incorrectos"), 400

#ELIMINAR

@bp.route("/delete/<string:pokemon_id>", methods = ["DELETE"]) #Va venir con parametro con la ruta
def delete(pokemon_id):
    pokemon_model.delete(ObjectId(pokemon_id)) #Esta recibiendo dos parametros, objectid
    return jsonify("Yeiii, pokemon eliminado con éxito jiji"), 200

#OBTENER

@bp.route("/get/<string:pokemon_id>", methods = ["GET"])
def get_pokemon(pokemon_id):
    pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
    return jsonify(pokemon), 200

