import { Pressable, StyleSheet, Text, TextInput, View, Image } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <View>
        <Image source={{uri:"https://th.bing.com/th/id/R.b76c223ff813906920302b0551c19b96?rik=fjIqO368MjpW1w&riu=http%3a%2f%2forig15.deviantart.net%2ff4e0%2ff%2f2015%2f135%2f1%2f9%2f19711c44184e3f45e2e5403350ece0cc-d8tgzqd.jpg&ehk=ZUWoHkOp3R4Z515l%2fo2RRU8agnkrM5p6ca6ZZuB6GNM%3d&risl=&pid=ImgRaw&r=0" }} 
       width={200}
       height={200}
        />
    </View>
      <View>{/* container-form*/}
        <Text style={styles.title}>Inicia Sesión</Text> {/* title */}
        <Text style={styles.label}>Correo: </Text> {/* label */}
        <TextInput style={styles.input}/>
        <Text style={styles.label}>Contraseña: </Text> {/* label*/}
        <TextInput style={styles.input}/>
        <Pressable>
          <Text>Enviar</Text>
        </Pressable>
    </View>
    <View> {/* container-footer */}
      <Text>¿Olvidaste tu contraseña SONSOTE?</Text> 
      <Text>Registrate</Text>
    </View>

      </View>
   
  );
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
