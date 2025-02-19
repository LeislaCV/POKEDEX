#Ruteo
from flask import Blueprint, request, jsonify #Blueprint seccionar el servidor por carpetitas, Request maneja la peticion que haga el usuario, jsonify  response  
from app.schemas.user_schema import UserSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory #Traer la colección de usuarios
from bson import ObjectId #Formato que maneja mongo


bp = Blueprint("users", __name__, url_prefix="/users")  #Blueprint se instancea, secciona el servidor en carpetitas
user_schema = UserSchema() #Instanciar
user_model = ModelFactory.get_model("users") #Ir por el modelo de ususarios que ya declaramos

#LOGEAR AL USUARIO

@bp.route("/login", methods=["POST"]) #Los ruteos reciben dos parametros, la ruta y los metodos que va a recibir
def login():
    data = request.json
    email = data.get("email",None) #.get viene del json, traeme la clave que tenga email, si no trae nada va a ser none
    password = data.get("password", None)
    if not email or not password:
      return jsonify("Upss, es necesario enviar todas las credenciales", 400)
   
    user= user_model.get_by_email_password(email, password) #Va a traer el usuario si existe
    if not user:
        return jsonify("Upss, NO se encontro un usuario", 400)
    return jsonify(user, 200)

@bp.route("/register", methods=["POST"]) #
def register():
    try:
      data = user_schema.load(request.json) #Valida la informacion que se esta mandando, si algo anda mal va lanzar un error, error de validación "try, except"
      user_id = user_model.create(data)  #Retorna el id insertado tipo especifico ObjectId
      return jsonify({user_id:str(user_id)}), 200 #200 es un código de respuesta

    except ValidationError as err:
       return jsonify("Upss, Los parametros enviados son incorrectos"), 400 #Espera dos argumentos un mensaje y un código "err 400"  
    
    #ACTUALIZAR
    #Ruteo dinamico en la ruta 
@bp.route("/update/<strinng:user_id>", methods = ["PUT"]) #Va venir con parametro con la ruta
def update(user_id): #
    try:
        data = user_schema.load(request.json)
        user= user_model.update(ObjectId(user_id), data) #Esta recibiendo dos parametros, objectid y no recuerdo el otro jaja
        return jsonify({
           "data": user
        }), 200
    except ValidationError as err:
       return jsonify("Upss, Los parametros enviados son incorrectos"), 400 #Espera dos argumentos un mensaje y un código "err 400"  
    
    #ELIMINAR

@bp.route("/delete/<strinng:user_id>", methods = ["DELETE"]) #Va venir con parametro con la ruta
def delete(user_id):
    user_model.delete(ObjectId(user_id)) #Esta recibiendo dos parametros, objectid
    return jsonify("Usuario eliminado con exito"), 200

    #OBTENER

@bp.route("/get/<strinng:user_id>", methods = ["GET"])
def get_user(user_id):
   user = user_model.find_by_id(ObjectId(user_id))
   return jsonify(user, 200)


    
