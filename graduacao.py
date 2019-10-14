import curso

class Graduacao (curso.Curso) :

    def __init__ (self, name, codigo, codEscola) :
        self.name = name
        self.codigo = codigo
        self.codEscola = codEscola