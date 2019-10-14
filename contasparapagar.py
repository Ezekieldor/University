
class ContasParaPagar :
    matricula = ""
    contaBancaria = ""
    agenciaBancaria = ""
    valor = ""

    def __init__ (self, matricula, contaBancaria, agenciaBancaria, valor) :
        self.matricula = matricula
        self.contaBancaria = contaBancaria
        self.agenciaBancaria = agenciaBancaria
        self.valor = valor