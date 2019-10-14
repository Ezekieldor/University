import person
import disciplina
import student
import professor
import funcadm
import sqlite3
import turma
import funcfinanceiro
import administrador
import notapresenca
import periodo
import graduacao
import posgraduacao
import contasparapagar
import boleto

class Data :

    def GetStudent (self, username, password) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM Student
        WHERE matricula = ? AND password = ?
        """, (username, password))

        res = cursor.fetchall ()

        cursor.execute ("""
        SELECT * FROM StudentTurma
        WHERE matriculaStudent = ?
        """, (username,))

        aux = list ()

        for i in cursor.fetchall () :
            aux.append (turma.Turma (i[1], i[2]))

        conn.close ()

        if (len (res) != 0) : return student.Student (res[0][0], res[0][1], res[0][2], res[0][3], res[0][4], res[0][5], aux)
        return None

    def UpdateStudent (self, user) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM Periodo
        WHERE codigo = ? AND matriculaStudent = ?
        """, (user.periodo, user.matricula))

        if (len (cursor.fetchall ()) == 0 and user.periodo != '0') :
            cursor.execute("""
            INSERT INTO Periodo (codigo, matriculaStudent)
            VALUES (?,?)
            """, (user.periodo, user.matricula))
            conn.commit ()

        cursor.execute ("""
        UPDATE Student
        SET name = ?, password = ?, codEscola = ?, periodo = ?
        WHERE matricula = ?
        """, (user.name, user.password, user.codEscola, user.periodo, user.matricula))

        conn.commit()

        cursor.execute ("""
        DELETE FROM StudentTurma
        WHERE matriculaStudent = ?
        """, (user.matricula,))

        conn.commit()

        for i in user.turm :
            cursor.execute ("""
            INSERT INTO StudentTurma (matriculaStudent, codigoTurma, codigoDisc, periodo)
            VALUES (?,?,?,?)
            """, (user.matricula, i.codigo, i.codigoDisc, user.periodo))

        conn.commit ()
        conn.close ()

    def UpdateProdessor(self, user) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE Professor
        SET name = ?, password = ?, codEscola = ?
        WHERE matricula = ?
        """, (user.name, user.password, user.matricula, user.codEscola))

        cursor.execute("""
        DELETE FROM ProfessorTurma
        WHERE matriculaProfessor = ?
        """, (user.matricula,))

        for i in user.turm :
            cursor.execute("""
            INSERT INTO ProfessorTurma (matriculaProfessor, codigoTurma, codigoDisc)
            VALUES (?,?,?)
            """, (user.matricula, i.codigo, i.codigoDisc))

        conn.commit()

        conn.close()

    def GetTurmaStudent (self, user) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM StudentTurma
        WHERE matriculaStudent = ? AND periodo = ?
        """, (user.matricula, user.periodo))

        aux = list ()

        for i in cursor.fetchall () :
            aux.append (turma.Turma (i[1], i[2]))

        conn.close()

        return aux

    def GetDisc (self, escola) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM Disciplina
        WHERE codEscola = ?
        """, (escola,))

        aux = list ()

        for i in cursor.fetchall () :
            aux.append (disciplina.Disciplina (i[0], i[1], i[2], i[3]))

        conn.close ()

        return aux

    def GetTurmaDisc (self, disc) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM Turma
        WHERE codigoDisc = ?
        """, (disc,))

        aux = list ()

        for i in cursor.fetchall () :
            aux.append (turma.Turma (i[0], i[1]))

        conn.close ()

        return aux

    def GetDiscByCodigo (self, codigo) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM Disciplina
        WHERE codigo = ?
        """, (codigo,))

        aux = cursor.fetchall ()

        conn.close ()

        if (len (aux) != 0) : return disciplina.Disciplina (aux[0][0], aux[0][1], aux[0][2], aux[0][3])
        return None

    def GetTurmaByCodigo (self, codigo) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM Turma
        WHERE codigo = ?
        """, (codigo,))

        aux = cursor.fetchall ()

        conn.close()

        if (len (aux) != 0): return turma.Turma (aux[0][0], aux[0][1])
        return None

    def GetProfessorByMatricula (self, codigo) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Professor
        WHERE matricula = ?
        """, (codigo,))

        aux = cursor.fetchall()

        conn.close()

        if (len(aux) != 0): return professor.Professor (aux[0][0], aux[0][1], aux[0][2], aux[0][3])
        return None

    def GetCursoPosByCod(self, codigo) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM PosGraduacao
        WHERE codigo = ?
        """, (codigo,))

        aux = cursor.fetchall()

        conn.close()

        if (len(aux) != 0): return turma.Turma(aux[0][0], aux[0][1])
        return None

    def GetCursoGraByCod (self, codigo) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Graduacao
        WHERE codigo = ?
        """, (codigo,))

        aux = cursor.fetchall()

        conn.close()

        if (len(aux) != 0): return turma.Turma(aux[0][0], aux[0][1])
        return None

    def GetDiscByName (self, name) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute ("""
        SELECT * FROM Disciplina
        WHERE name = ?
        """, (name,))

        aux = cursor.fetchall()

        conn.close()

        if (len (aux) != 0): return disciplina.Disciplina (aux[0][0], aux[0][1], aux[0][2], aux[0][3])
        return None

    def GetProfessor (self, username, password) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Professor
        WHERE matricula = ? AND password = ?
        """, (username, password))

        res = cursor.fetchall()

        cursor.execute("""
        SELECT * FROM ProfessorTurma
        WHERE matriculaProfessor = ?
        """, (username,))

        aux = list()

        for i in cursor.fetchall():
            aux.append (turma.Turma(i[1], i[2]))

        conn.close()

        if (len(res) != 0): return professor.Professor (res[0][0], res[0][1], res[0][2], res[0][3], aux)
        return None

    def GetAdministrador (self, username, password) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM Administrador
        WHERE matricula = ? AND password = ?
        """, (username, password))

        aux = cursor.fetchall ()
        conn.close ()

        if (len(aux) != 0) : return administrador.Administrador (aux[0][0], aux[0][1], aux[0][2])
        return None

    def GetFuncFinanceiro (self, username, password) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute ("""
        SELECT * FROM FuncFinanceiro
        WHERE matricula = ? AND password = ?
        """, (username, password))

        aux = cursor.fetchall()
        conn.close()

        if (len(aux) != 0) : return funcfinanceiro.FuncFinanceiro (aux[0][0], aux[0][1], aux[0][2])
        return None

    def GetFuncAdm (self, usarname, password):
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM FuncAdm
        WHERE matricula = ? AND password = ?
        """, (usarname, password))

        aux = cursor.fetchall()
        conn.close()

        if (len(aux) != 0): return funcadm.FuncAdm (aux[0][0], aux[0][1], aux[0][2])
        return None

    def GetStudentByTurma (self, codigo, codigoDisc) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT name, matricula, password, codEscola, Student.periodo, codCurso
        FROM Student, StudentTurma
        WHERE matriculaStudent = matricula AND codigoTurma = ? AND codigoDisc = ?
        """, (codigo, codigoDisc))

        aux = list ()

        res = cursor.fetchall ()

        for i in res :
            cursor.execute("""
            SELECT * FROM StudentTurma
            WHERE matriculaStudent = ?
            """, (i[1],))

            aux2 = list ()

            for j in cursor.fetchall () :
                aux2.append (turma.Turma (j[0], j[1]))

            aux.append (student.Student (i[0], i[1], i[2], i[3], i[4], i[5], aux2))

        conn.close()
        return aux

    def GetNotaPresenca (self, matriculaStudent, prd) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM NotaPresenca
        WHERE matriculaStudent = ? AND periodo = ?
        """, (matriculaStudent, prd))

        aux = list ()

        for i in cursor.fetchall () :
            aux.append (notapresenca.NotaPresenca (i[0], i[1], i[2], i[3], i[4], i[5]))

        return aux

    def UpdateNota (self, matriculaStudent, codigoTurma, codigoDisc, nota, prd) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM NotaPresenca
        WHERE matriculaStudent = ? AND codigoTurma = ? AND codigoDisc = ? AND periodo = ?
        """, (matriculaStudent, codigoTurma, codigoDisc, prd))

        aux = cursor.fetchall ()

        aux2 = 0
        if (len(aux) > 0) :
            cursor.execute("""
            DELETE FROM NotaPresenca
            WHERE matriculaStudent = ? AND codigoTurma = ? AND codigoDisc = ? AND periodo = ?
            """, (matriculaStudent, codigoTurma, codigoDisc, prd))

            aux2 = aux[0][4]
            conn.commit()

        cursor.execute ("""
        INSERT INTO NotaPresenca (codigoTurma, codigoDisc, matriculaStudent, nota, presenca, periodo)
        VALUES (?,?,?,?,?,?)
        """, (codigoTurma, codigoDisc, matriculaStudent, nota, str (aux2), prd))

        conn.commit ()
        conn.close ()

    def UpdateFreq (self, matriculaStudent, codigoTurma, codigoDisc, presenca, prd) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM NotaPresenca
        WHERE matriculaStudent = ? AND codigoTurma = ? AND codigoDisc = ? AND periodo = ?
        """, (matriculaStudent, codigoTurma, codigoDisc, prd))

        aux = cursor.fetchall ()

        aux2 = 0
        aux3 = 0
        if (len (aux) > 0) :
            cursor.execute("""
            DELETE FROM NotaPresenca
            WHERE matriculaStudent = ? AND codigoTurma = ? AND codigoDisc = ? AND periodo = ?
            """, (matriculaStudent, codigoTurma, codigoDisc, prd))
            conn.commit()

            aux2 = aux[0][3]
            aux3 = aux[0][4]

        cursor.execute ("""
        INSERT INTO NotaPresenca (codigoTurma, codigoDisc, matriculaStudent, nota, presenca, periodo)
        VALUES (?,?,?,?,?,?)
        """, (codigoTurma, codigoDisc, matriculaStudent, str (aux2), str (int (presenca) + int (aux3)), prd))

        conn.commit ()
        conn.close ()

    def GetStudentByMatricula (self, matricula) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Student
        WHERE matricula = ?
        """, (matricula,))

        res = cursor.fetchall()

        cursor.execute("""
        SELECT * FROM StudentTurma
        WHERE matriculaStudent = ?
        """, (matricula,))

        aux = list()

        for i in cursor.fetchall():
            aux.append(turma.Turma(i[1], i[2]))

        conn.close ()

        if (len(res) != 0): return student.Student(res[0][0], res[0][1], res[0][2], res[0][3], res[0][4], res[0][5], aux)
        return None


    def CadastrarDisc (self, name, codigo, cargaHoraria, codigoEscola) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Disciplina
        WHERE codigo = ?
        """, (codigo,))

        aux = len (cursor.fetchall ())

        conn.close()

        if (aux == 0) :
            conn = sqlite3.connect('university.db')
            cursor = conn.cursor()

            cursor.execute ("""
            INSERT INTO Disciplina (name, codigo, cargaHoraria, codEscola)
            VALUES (?,?,?,?)
            """, (name, codigo, cargaHoraria, codigoEscola))

            conn.commit()
            conn.close()

    def ListarDisc (self, codigoEscola) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute ("""
        SELECT * FROM Disciplina
        WHERE codEscola = ?
        """, (codigoEscola,))

        aux = list ()

        for i in cursor.fetchall () :
            aux.append (disciplina.Disciplina (i[0], i[1], i[2], i[3]))

        conn.close ()

        return aux

    def CadastrarTurma (self, codigo, codigoDisc) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute ("""
        SELECT * FROM Disciplina
        WHERE codigo = ?
        """, (codigoDisc,))

        if (len (cursor.fetchall ()) != 0) :
            cursor.execute("""
            INSERT INTO Turma (codigo, codigoDisc)
            VALUES (?,?)
            """, (codigo, codigoDisc))

            conn.commit()
            conn.close()
            return True

        conn.close()

        return False

    def ListarTurma (self, codigoEscola) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute ("""
        SELECT Turma.codigo, codigoDisc FROM Turma, Disciplina
        WHERE Turma.codigoDisc = Disciplina.codigo AND Disciplina.codEscola = ?
        """, (codigoEscola,))

        aux = list ()

        for i in cursor.fetchall () :
            aux.append (turma.Turma (i[0], i[1]))

        conn.close ()

        return aux

    def MatricularStudent (self, name, matricula, password, codigoEscola, codCurso) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        INSERT INTO Student (name, matricula, password, codEscola, periodo, codCurso)
        VALUES (?,?,?,?,?,?)
        """, (name, matricula, password, codigoEscola, '0', codCurso))

        conn.commit ()
        conn.close ()

    def CadastrarProfessor (self, name, matricula, password, codigoEscola) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
                INSERT INTO Professor (name, matricula, password, codEscola)
                VALUES (?,?,?,?)
                """, (name, matricula, password, codigoEscola))

        conn.commit()
        conn.close()

    def ListarStudents (self, codigoEscola) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Student
        WHERE codEscola = ?
        """, (codigoEscola,))

        aux = list()
        res = cursor.fetchall ()

        for i in res:
            cursor.execute("""
            SELECT * FROM StudentTurma
            WHERE matriculaStudent = ?
            """, (i[1],))

            aux2 = list()

            for j in cursor.fetchall ():
                aux2.append(turma.Turma (j[0], j[1]))

            aux.append (student.Student(i[0], i[1], i[2], i[3], i[4], i[5], aux2))

        conn.close()

        return aux

    def ListarProfessores(self, codigoEscola):
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Professor
        WHERE codEscola = ?
        """, (codigoEscola,))

        aux = list()
        res = cursor.fetchall()

        for i in res:
            cursor.execute("""
            SELECT * FROM ProfessorTurma
            WHERE matriculaProfessor = ?
            """, (i[1],))

            aux2 = list()

            for j in cursor.fetchall():
                aux2.append (turma.Turma(j[0], j[1]))

            aux.append (professor.Professor (i[0], i[1], i[2], i[3], aux2))

        conn.close()

        return aux

    def CadastrarFuncAdm (self, name, matricula, password, codigoEscola) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO FuncAdm (name, matricula, password, codEscola)
        VALUES (?,?,?,?)
        """, (name, matricula, password, codigoEscola))

        conn.commit()
        conn.close()

    def CadastrarFuncFinanceiro (self, name, matricula, password, codigoEscola) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO FuncFinanceiro (name, matricula, password, codEscola)
        VALUES (?,?,?,?)
        """, (name, matricula, password, codigoEscola))

        conn.commit()
        conn.close()

    def SetBoletoEstudante (self, matricula, valor, codigo) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        INSERT INTO Boleto (matriculaStudent, valor, codigo)
        VALUES (?, ?, ?)
        """, (matricula, valor, codigo))

        conn.commit ()
        conn.close ()

    def GetBoletoEstudante (self, matricula) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute ("""
        SELECT * FROM Boleto
        WHERE matriculaStudent = ?
        """, (matricula,))

        aux = list ()

        for i in cursor.fetchall () :
            aux.append (boleto.Boleto (i[0], i[1], i[2]))

        return aux

    def ListarAllStudents(self) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Student
        """)

        aux = list()
        res = cursor.fetchall()

        for i in res:
            cursor.execute("""
            SELECT * FROM StudentTurma
            WHERE matriculaStudent = ?
            """, (i[1],))

            aux2 = list()

            for j in cursor.fetchall():
                aux2.append(turma.Turma(j[0], j[1]))

            aux.append(student.Student(i[0], i[1], i[2], i[3], i[4], i[5], aux2))

        conn.close ()

        return aux

    def ListarPeriodos (self, matriculaStudent) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute ("""
        SELECT * FROM Periodo
        WHERE matriculaStudent = ?
        """, (matriculaStudent,))

        aux = list ()

        for i in cursor.fetchall () :
            aux.append (periodo.Periodo (i[0], i[1]))

        conn.close ()

        return aux

    def CadastrarCursoGrad (self, nome, codigo, codEscola) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        INSERT INTO Graduacao (name, codigo, codEscola)
        VALUES (?, ?, ?)
        """, (nome, codigo, codEscola))

        conn.commit ()
        conn.close ()

    def CadastrarCursoPos(self, nome, codigo, codEscola) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO PosGraduacao (name, codigo, codEscola)
        VALUES (?, ?, ?)
        """, (nome, codigo, codEscola))

        conn.commit()
        conn.close()

    def ListarCursoGrad (self, codigoEscola) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM Graduacao
        WHERE codEscola = ?
        """, (codigoEscola,))

        aux = list ()

        for i in cursor.fetchall () :
            aux.append (graduacao.Graduacao (i[0], i[1], i[2]))

        conn.close ()

        return aux

    def ListarCursoPos(self, codigoEscola) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM PosGraduacao
        WHERE codEscola = ?
        """, (codigoEscola,))

        aux = list()

        for i in cursor.fetchall():
            aux.append(posgraduacao.PosGraduacao(i[0], i[1], i[2]))

        conn.close()

        return aux

    def SoliciPag (self, matricula, contaBancaria, agenciaBancaria, valor) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        INSERT INTO ContasParaPagar (matricula, contaBancaria, agenciaBancaria, valor)
        VALUES (?,?,?,?)
        """, (matricula, contaBancaria, agenciaBancaria, valor))

        conn.commit ()
        conn.close ()

    def ListarContas (self) :
        conn = sqlite3.connect ('university.db')
        cursor = conn.cursor ()

        cursor.execute ("""
        SELECT * FROM ContasParaPagar
        """)

        aux = list ()

        for i in cursor.fetchall () :
            aux.append (contasparapagar.ContasParaPagar (i[0], i[1], i[2], i[3]))

        return aux

    def GetEstadoInclusoes (self) :
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Inclusoes
        """)

        aux = cursor.fetchall ()[0]

        conn.close ()

        return aux

    def SetEstadoInclusoes(self, val):
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE Inclusoes
        SET estado = ?
        """, (val,))

        conn.commit()
        conn.close()
