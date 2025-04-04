import { Pressable, TextInput } from "react-native";
import {  Text, TextInput, View } from 'react-native';


export default function  RecoveryPassword  () {

    return(
        <View>
            <Text style={styles.title}> Restablecer Contraseña</Text>
            <Text style={styles.label}>Contraseña Nueva</Text>
            <TextInput style={styles.input} placeholder="Nueva Cotraseña"/>
            <Text style={styles.label}>Vuelve a escribir tu Contraseña</Text>
            <TextInput style={styles.input} placeholder="Confirmar Cotraseña"/>
            <Pressable>
                <Text>Restablecer</Text>
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
