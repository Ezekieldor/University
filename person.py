
class Person :
    name = ""
    matricula = ""
    password = ""
    typed = 0
    codEscola = ""

    def __init__ (self, name, matricula, password, type, codEscola) :
        self.name = name
        self.matricula = matricula
        self.password = password
        self.type = type
        self.codEscola = codEscola