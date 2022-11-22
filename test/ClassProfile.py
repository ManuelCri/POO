class Profile:
    ##Atributos##
    #username = ""
    #email = ""
    #password = ""
    ##Fin Atributos
    def __init__(self, id, username, email, password, status = "online", level = 0):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.status = status
        self.level = level

    def print(self):
        print("ingrese su id: " )
        self.id = input(self.id)

        print("ingrese su username: " )
        self.username = input(self.username)

        print("ingrese su email: " )
        self.email = input(self.email)

        print("ingrese su password: " )
        self.password = input(self.password)

        print("ingrese su status: " )
        self.status = input(self.status)

        print("ingrese su level: " )
        self.level = input(self.level)

        print("el id es: ",self.id)
        print("el usauario es: ",self.username)
        print("el  email: ",self.email)
        print("el id password: ",self.password)
        print("el  status: ",self.status)
        print("el level: ",self.level)

    def cambiar_contraseña(self):
        print("su contraseña es: ",self.password)
        print("ingrese su password nuevo: " )
        self.password = input(self.password)


