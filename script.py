import sqlite3

conn = sqlite3.connect ("university.db")
cursor = conn.cursor ()

cursor.execute ("""
CREATE TABLE Inclusoes
(
    estado VARCHAR (30) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE Student
(
    name VARCHAR (30) NOT NULL,
    matricula VARCHAR (20) NOT NULL PRIMARY KEY,
    password VARCHAR (20) NOT NULL,
    codEscola VARCHAR (20) NOT NULL,
    periodo VARCHAR (10) NOT NULL,
    codCurso VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE Administrador
(
    name VARCHAR (30) NOT NULL,
    matricula VARCHAR (20) NOT NULL PRIMARY KEY,
    password VARCHAR (20) NOT NULL,
    codEscola VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE NotaPresenca
(
    codigoTurma VARCHAR (30) NOT NULL,
    codigoDisc VARCHAR (30) NOT NULL,
    matriculaStudent VARCHAR (20) NOT NULL,
    nota VARCHAR (20) NOT NULL,
    presenca VARCHAR (20) NOT NULL,
    periodo VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE Periodo
(
    codigo VARCHAR (30) NOT NULL,
    matriculaStudent VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE Professor
(
    name VARCHAR (30) NOT NULL,
    matricula VARCHAR (20) NOT NULL PRIMARY KEY,
    password VARCHAR (20) NOT NULL,
    codEscola VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE FuncAdm
(
    name VARCHAR (30) NOT NULL,
    matricula VARCHAR (20) NOT NULL PRIMARY KEY,
    password VARCHAR (20) NOT NULL,
    codEscola VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE FuncFinanceiro
(
    name VARCHAR (30) NOT NULL,
    matricula VARCHAR (20) NOT NULL PRIMARY KEY,
    password VARCHAR (20) NOT NULL,
    codEscola VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE Graduacao
(
    name VARCHAR (30) NOT NULL,
    codigo VARCHAR (30) NOT NULL,
    codEscola VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE PosGraduacao
(
    name VARCHAR (30) NOT NULL,
    codigo VARCHAR (30) NOT NULL,
    codEscola VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE StudentTurma
(
    matriculaStudent VARCHAR (20) NOT NULL,
    codigoTurma VARCHAR (20) NOT NULL,
    codigoDisc VARCHAR (20) NOT NULL,
    periodo VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE ProfessorTurma
(
    matriculaProfessor VARCHAR (20) NOT NULL,
    codigoTurma VARCHAR (20) NOT NULL,
    codigoDisc VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE Disciplina
(
    name VARCHAR (30) NOT NULL,
    codigo VARCHAR (20) NOT NULL PRIMARY KEY,
    cargaHoraria INTEGER NOT NULL,
    codEscola VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE Turma
(
    codigo VARCHAR (20) NOT NULL,
    codigoDisc VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE Escola
(
    name VARCHAR (30) NOT NULL,
    codigo VARCHAR (20) NOT NULL,
    codigoDisc VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE ContasParaPagar
(
    matricula VARCHAR (20),
    contaBancaria VARCHAR (20) NOT NULL,
    agenciaBancaria VARCHAR (20) NOT NULL,
    valor VARCHAR (10) NOT NULL
);
""")

cursor.execute ("""
CREATE TABLE Boleto
(
    matriculaStudent VARCHAR (20) NOT NULL,
    valor VARCHAR (20) NOT NULL,
    codigo VARCHAR (20) NOT NULL
);
""")

cursor.execute ("""
INSERT INTO Student (name, matricula, password, codEscola, periodo, codCurso)
VALUES (?,?,?,?,?,?)
""", ("aluno", "aluno", "aluno", "1", "0", "10"))
conn.commit ()

cursor.execute ("""
INSERT INTO Professor (name, matricula, password, codEscola)
VALUES (?,?,?,?)
""", ("Professor", "professor", "professor", "1"))
conn.commit ()

cursor.execute ("""
INSERT INTO Disciplina (name, codigo, cargaHoraria, codEscola)
VALUES (?,?,?,?)
""", ("Algoritmo", "1", "10", "1"))
conn.commit ()

cursor.execute ("""
INSERT INTO Turma (codigo, codigoDisc)
VALUES (?,?)
""", ("a02", "1"))
conn.commit ()

cursor.execute ("""
INSERT INTO Turma (codigo, codigoDisc)
VALUES (?,?)
""", ("a01", "1"))
conn.commit ()

cursor.execute ("""
INSERT INTO FuncAdm (name, matricula, password, codEscola)
VALUES (?,?,?,?)
""", ("Joao", "123", "123", "1"))
conn.commit ()

cursor.execute ("""
INSERT INTO FuncFinanceiro (name, matricula, password, codEscola)
VALUES (?,?,?,?)
""", ("Joao", "qwer", "qwer", "1"))

conn.commit ()

cursor.execute ("""
INSERT INTO Administrador (name, matricula, password, codEscola)
VALUES (?,?,?,?)
""", ("Ezekieldor", "zxcv", "zxcv", "1"))

conn.commit ()

cursor.execute ("""
INSERT INTO Inclusoes (estado)
VALUES (?)
""", ("0"))

conn.commit ()