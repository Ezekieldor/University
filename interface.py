import data

class Interface :
    objData = None

    def __init__ (self) :
        self.objData = data.Data ()

    def GetStudent (self, username, password) :
        return self.objData.GetStudent (username, password)

    def GetStudentByMatricula (self, matricula) :
        return self.objData.GetStudentByMatricula (matricula)

    def GetStudentByTurma (self, codigo, codigoDisc) :
        return self.objData.GetStudentByTurma (codigo, codigoDisc)

    def GetProfessor (self, username, password) :
        return self.objData.GetProfessor (username, password)

    def GetFuncAdm (self, username, password) :
        return self.objData.GetFuncAdm (username, password)

    def GetFuncFinanceiro (self, username, password) :
        return self.objData.GetFuncFinanceiro (username, password)

    def GetAdministrador (self, username, password) :
        return self.objData.GetAdministrador (username, password)

    def GetTurmaStudent (self, user) :
        return self.objData.GetTurmaStudent (user)

    def UpdateStudent (self, obj) :
        self.objData.UpdateStudent (obj)

    def UpdateProdessor (self, obj) :
        self.objData.UpdateProdessor (obj)

    def GetDisc (self, escola) :
        return self.objData.GetDisc (escola)

    def GetTurmaDisc (self, disc) :
        return self.objData.GetTurmaDisc (disc)

    def GetDiscByCodigo (self, codigo) :
        return self.objData.GetDiscByCodigo (codigo)

    def GetTurmaByCodigo (self, codigo) :
        return self.objData.GetTurmaByCodigo (codigo)

    def GetProfessorByMatricula (self, codigo) :
        return self.objData.GetProfessorByMatricula (codigo)

    def GetDiscByName (self, name) :
        return self.objData.GetDiscByName (name)

    def GetNotaPresenca (self, matriculaStudent, prd) :
        return self.objData.GetNotaPresenca (matriculaStudent, prd)

    def SetBoletoEstudante (self, matricula, valor, codigo) :
        return self.objData.SetBoletoEstudante (matricula, valor, codigo)

    def GetBoletoEstudante (self, matricula) :
        return self.objData.GetBoletoEstudante (matricula)

    def UpdateNota (self, matriculaStudent, codigoTurma, codigoDisc, nota, prd) :
        return self.objData.UpdateNota (matriculaStudent, codigoTurma, codigoDisc, nota, prd)

    def UpdateFreq (self, matriculaStudent, codigoTurma, codigoDisc, presenca, prd) :
        return self.objData.UpdateFreq (matriculaStudent, codigoTurma, codigoDisc, presenca, prd)

    def CadastrarDisc (self, name, codigo, cargaHoraria, codigoEscola) :
        return self.objData.CadastrarDisc (name, codigo, cargaHoraria, codigoEscola)

    def ListarDisc (self, codigoEscola) :
        return self.objData.ListarDisc (codigoEscola)

    def CadastrarTurma (self, codigo, codigoDisc) :
        return self.objData.CadastrarTurma (codigo, codigoDisc)

    def ListarTurma (self, codigoEscola):
        return self.objData.ListarTurma (codigoEscola)

    def MatricularStudent (self, name, matricula, password, codigoEscola, codCurso) :
        return self.objData.MatricularStudent (name, matricula, password, codigoEscola, codCurso)

    def ListarStudents (self, codigoEscola):
        return self.objData.ListarStudents (codigoEscola)

    def ListarAllStudents (self):
        return self.objData.ListarAllStudents ()

    def CadastrarFuncAdm (self, name, matricula, password, codigoEscola) :
        return self.objData.CadastrarFuncAdm (name, matricula, password, codigoEscola)

    def CadastrarFuncFinanceiro (self, name, matricula, password, codigoEscola) :
        return self.objData.CadastrarFuncFinanceiro (name, matricula, password, codigoEscola)

    def ListarPeriodos (self, matriculaStudent) :
        return self.objData.ListarPeriodos (matriculaStudent)

    def CadastrarCursoGrad (self, nome, codigo, codEscola) :
        self.objData.CadastrarCursoGrad (nome, codigo, codEscola)

    def CadastrarCursoPos (self, nome, codigo, codEscola) :
        self.objData.CadastrarCursoPos (nome, codigo, codEscola)

    def GetCursoGraByCod (self, codigo) :
        return self.objData.GetCursoGraByCod (codigo)

    def GetCursoPosByCod (self, codigo) :
        return self.objData.GetCursoPosByCod (codigo)

    def ListarCursoGrad (self, codigoEscola) :
        return self.objData.ListarCursoGrad (codigoEscola)

    def ListarCursoPos (self, codigoEscola) :
        return self.objData.ListarCursoPos (codigoEscola)

    def CadastrarProfessor (self, name, matricula, password, codigoEscola) :
        self.objData.CadastrarProfessor (name, matricula, password, codigoEscola)

    def ListarProfessores (self, codigoEscola) :
        return self.objData.ListarProfessores (codigoEscola)

    def SoliciPag (self, matricula, contaBancaria, agenciaBancaria, valor) :
        self.objData.SoliciPag (matricula, contaBancaria, agenciaBancaria, valor)

    def ListarContas (self) :
        return self.objData.ListarContas ()

    def GetEstadoInclusoes (self) :
        return self.objData.GetEstadoInclusoes ()

    def SetEstadoInclusoes(self, val) :
        self.objData.SetEstadoInclusoes (val)