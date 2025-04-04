import { TextInput, Text, View, Pressable } from "react-native-gesture-handler";




export default function UserEditingView(){
    return(
        <View>
            <Text style={title}> Editar Perfil</Text>

            <Text style={styles.label}> Nombre</Text>
            <TextInput style={styles.input}/>

            <Text style={styles.label}> Correo</Text>
            <TextInput style={styles.input}/>

            <Text style={styles.label}> Contraseña</Text>
            <TextInput style={styles.input}/>

            <Pressable>
                <Text>Guardar cambios</Text>
            </Pressable>
        </View>
    )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding:10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title:{
    fontSize: 30,
    fontWeight: "bold"
  },
  label:{
    fontSize: 20,
    fontWeight: "bold"
  },
  input:{
    borderRadius: 10,
    borderWidth: 2,
    borderColor: "black",
    fontSize: 15,
    width:"auto",
  }
});
