class Cuenta:
    def __init__(self):
         self.accountList = []
         self.idAccount = 0

    def registerNewAccount(self, owner):
        self.idAccount += 1
        monto = 0
        accountId = self.idAccount
        accountDict = {"id": accountId, "owner": owner, "amount": 0}
        self.accountList.append(accountDict)
        print("\nLa transacción se ha realizado con éxito.\n Su número de cuenta es: "+str(accountId))

    def getTotalAmount(self, idAccount):
        pass

class Ingreso:
        def __init__(self):
            pass

class Egreso:
    def __init__(self):
        pass
