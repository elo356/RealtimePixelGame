import firebase_admin
from firebase_admin import credentials, db

# Inicializar la conexión con Firebase
cred = credentials.Certificate("realtimepixelapp-firebase-adminsdk-1ir4n-f0dd95e25a.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://realtimepixelapp-default-rtdb.firebaseio.com/'
})

def escribir_datos():
    try:
        ref = db.reference("/test_connection") #Grupo main
        ref.set({  #sub grupos
            "mensaje": "Hola, Firebase!",
            "estado": "Conexión exitosa"
        })
        print("Datos escritos correctamente.")
    except Exception as e:
        print(f"Error al escribir datos: {e}")

def leer_datos():
    try:
        ref = db.reference("/test_connection")
        datos = ref.get()
        print("Datos leídos desde Firebase:", datos)
    except Exception as e:
        print(f"Error al leer datosss: {e}")

if __name__ == "__main__":
    escribir_datos()
    leer_datos()
