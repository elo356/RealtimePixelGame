import os
import uuid
import firebase_admin
from firebase_admin import credentials, db

# Inicializar Firebase
cred = credentials.Certificate("realtimepixelapp-firebase-adminsdk-1ir4n-f0dd95e25a.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://realtimechattest-ff218-default-rtdb.firebaseio.com/'
})

logged_in_user_id = None
logged_in_user_name = None

def main():
    global logged_in_user_id, logged_in_user_name

    while True:
        mostrar_menu_principal()
        opcion = input()

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Saliendo del sistema... ¡Hasta luego!")
            return
        else:
            print("Opción no válida, por favor intenta de nuevo.")

def mostrar_menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===== Bienvenido a ELONET =====")
    print("1. Crear nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    print("Elige una opción: ")

def crear_usuario():
    global logged_in_user_id
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Ingresa tu nombre de usuario: ")
    username = input()

    print("Ingresa una contraseña: ")
    password = input()

    user_id = str(uuid.uuid4())
    nuevo_usuario = {'Id': user_id, 'Name': username, 'Password': password, 'IsOnline': False}

    print("Creando usuario...")
    db.reference("users").child(user_id).set(nuevo_usuario)

    print("¡Usuario creado exitosamente!")
    print(f"Tu ID único es: {user_id}")
    input("Presiona cualquier tecla para volver al menú...")

def iniciar_sesion():
    global logged_in_user_id, logged_in_user_name
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Ingresa tu nombre de usuario: ")
    username = input()

    print("Ingresa tu contraseña: ")
    password = input()

    print("Verificando credenciales...")
    usuarios = db.reference("users").get()

    usuario = next((u for u in usuarios.values() if u['Name'] == username and u['Password'] == password), None)

    if usuario:
        logged_in_user_id = usuario['Id']
        logged_in_user_name = usuario['Name']

        # Actualiza el estado a conectado
        db.reference("users").child(logged_in_user_id).update({"IsOnline": True})

        print("Inicio de sesión exitoso!")
        print(f"¡Bienvenido, {logged_in_user_name}!")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

    input("Presiona cualquier tecla para continuar...")

if __name__ == "__main__":
    main()
