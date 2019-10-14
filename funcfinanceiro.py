import funcionario

class FuncFinanceiro (funcionario.Funcionario) :

    def __init__ (self, name, matricula, password):
        self.name = name
        self.matricula = matricula
        self.password = password