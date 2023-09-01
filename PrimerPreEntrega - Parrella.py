class UserDatabase:
    def __init__(self):
        self.DB = []

    def register(self):
        print("\nRegistrarse")
        user = input("Usuario: ")
        password = input("Contraseña: ")
        self.DB.append({'user': user, 'password': password})

    def login(self):
        print("\nIniciar Sesión")
        user = input("Usuario: ")
        password = input("Contraseña: ")
        
        for login in self.DB:
            if login['user'] == user and login['password'] == password:
                print("Inicio de sesión exitoso.")
                return
        
        print("Usuario o contraseña incorrectos o no estás registrado.")

    def show_data(self):
        print("\nUsuarios registrados:")
        for entry in self.DB:
            print(f"Usuario: {entry['user']}, Contraseña: {entry['password']}")

def main():
    user_db = UserDatabase()

    while True:
        print("\nOpciones:")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Ver usuarios y contraseñas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            user_db.register()
        elif opcion == "2":
            user_db.login()
        elif opcion == "3":
            user_db.show_data()
        elif opcion == "4":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
