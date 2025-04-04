import { Pressable, TextInput, Text, View } from "react-native";

export default function  RegisterUsers  () {

    return(
        <View>
            <Text style={styles.title}> Registrate</Text>
            <Text style={styles.label}>Nombre</Text>
            <TextInput style={styles.input} placeholder="Nombre Completo" />
            <Text style={styles.label}>Correo Electronico</Text>
            <TextInput style={styles.input}  />
            <Text style={styles.label}>Contraseña</Text>
            <TextInput style={styles.input} />
            <Text style={styles.label}>Repite tu Contraseña</Text>
            <TextInput style={styles.input} placeholder="Confirmar Cotraseña"/>
            <Pressable>
                <Text>Registrar</Text>
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
