from marshmallow import Schema, fields,ValidationError

class PokemonFavoriteSchema(Schema): 
    pokemon_id = fields.Str(
        required = True, #lamda, funcion flecha de python
        validate = lambda x: len(x) > 0,
        error_messages={
            "required": "Upsi, el id del pokemo es requerido"
        }
    )

    user_id = fields.Str(
        required = True, #lamda, funcion flecha de python
        validate = lambda x: len(x) > 0,
        error_messages={
            "required": "Upsi, el id del usuario es requerido"
        }
    )