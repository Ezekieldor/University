import person

class Administrador (person.Person) :

    def __init__ (self, name, matricula, password):
        self.name = name
        self.matricula = matricula
        self.password = password