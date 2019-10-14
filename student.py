import person

class Student (person.Person) :

    turm = list ()
    periodo = ""
    codCurso = ""

    def __init__ (self, name, matricula, password, codEscola, periodo, codCurso, turm) :
        self.name = name
        self.matricula = matricula
        self.password = password
        self.codEscola = codEscola
        self.periodo = periodo
        self.turm = turm
        self.codCurso = codCurso