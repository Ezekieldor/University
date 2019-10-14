import funcionario

class Professor (funcionario.Funcionario) :

    turm = list ()

    def __init__ (self, name, matricula, password, codEscola, turm) :
        self.name = name
        self.matricula = matricula
        self.password = password
        self.codEscola = codEscola
        self.turm = turm