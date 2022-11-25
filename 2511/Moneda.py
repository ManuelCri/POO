class moneda:
    def __init__(self, IdMoney, nameMoney, Valor ) :
        self.IdMoney = IdMoney
        self.nameMoney = nameMoney
        self.Valor = Valor
        self


    def print(self) :
        i = 0
        while i <= 3:
            print("ingrese el nombre de la moneda: " )
            self.nameMoney = input(self.nameMoney)

            print("ingrese la Id de la moneda: " )
            self.IdMoney = input(self.IdMoney)

            print("ingrese el valor de la moneda: " )
            self.Valor = input(self.Valor)

            print("el nombre de la moneda es: ",self.nameMoney)
            print("el la Id de la moneda es: ",self.IdMoney)
            print("el valor de la moneda es: ",self.Valor)

