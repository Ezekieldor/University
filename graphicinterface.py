from tkinter import *
import interface
import disciplina
import turma
from tkinter.font import Font
from random import *
from tkinter import messagebox

class GraphicInterface :
    objInterface = interface.Interface ()
    Inclusoes = False

    def __init__ (self) :

        if (self.objInterface.GetEstadoInclusoes ()[0] == '1') :
            self.Inclusoes = True
        else :
            self.Inclusoes = False
        self.Start ()

    def center (self, obj, w, h) :
        ws = obj.winfo_screenwidth()
        hs = obj.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        obj.resizable (0, 0)

        obj.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def Historico (self, obj) :
        scren = Tk ()

        scren.title("Histórico")

        frame = Frame (scren, width = 450, height = 550, bg = "#FF8C00")
        frame.pack ()

        self.center (scren, 450, 550)

        lb1 = Listbox (scren, width = 50, height = 30)
        lb1.place (relx = 0.05, rely = 0.05)

        prd = self.objInterface.ListarPeriodos (obj.matricula)

        for i in prd :
            lb1.insert (END, "Periodo: " + i.codigo)

            nf = self.objInterface.GetNotaPresenca (obj.matricula, i.codigo)
            for j in nf :
                lb1.insert (END, "Disciplina: " + self.objInterface.GetDiscByCodigo (j.codigoDisc).name + "   " + "Nota: " + j.nota + "  " + "Presenças: " + j.presenca)

            lb1.insert (END, "")

    def CompMatricula (self, obj) :
        scren = Tk()

        scren.title("Comprovante de Matrícula")

        frame = Frame(scren, width=700, height=400, bg="#FF8C00")
        frame.pack()

        self.center(scren, 700, 400)

        lb1 = Listbox(scren, width=79, height=20)
        lb1.place(relx=0.05, rely=0.05)

        aux = self.objInterface.GetTurmaStudent (obj)

        for i in aux:
            lb1.insert(END, "Turma: " + i.codigo + "  " + "Disciplina: " + self.objInterface.GetDiscByCodigo(i.codigoDisc).name)

    def Boletos (self, obj) :
        scren = Tk()

        scren.title("Boletos")

        frame = Frame(scren, width=700, height=400, bg="#FF8C00")
        frame.pack()

        self.center(scren, 700, 400)

        lb1 = Listbox(scren, width=79, height=20)
        lb1.place(relx=0.05, rely=0.05)

        aux = self.objInterface.GetBoletoEstudante (obj.matricula)

        for i in aux:
            lb1.insert (END, "Valor: " + i.valor)
            lb1.insert(END, "Código: " + i.codigo)
            lb1.insert(END, "")

    def NotaFreq (self, obj, prd) :
        scren = Tk ()

        scren.title("Notas e Frequências")

        frame = Frame (scren, width = 700, height = 400, bg = "#FF8C00")
        frame.pack ()

        self.center(scren, 700, 400)

        lb1 = Listbox (scren, width = 79, height = 20)
        lb1.place (relx = 0.05, rely = 0.05)

        aux = self.objInterface.GetNotaPresenca (obj.matricula, obj.periodo)

        for i in aux :
            lb1.insert (END, "Disciplina: " + self.objInterface.GetDiscByCodigo (i.codigoDisc).name + "  "\
                        + "Turma: " + self.objInterface.GetTurmaByCodigo (i.codigoTurma).codigo + "  " + "Nota: " + i.nota + "  " + "Presença: " + i.presenca)

    def InclDisc (self, obj) :
        scren = Tk ()

        scren.title("Incluir Disciplina")

        frame = Frame (scren, width = 700, height = 700, bg = "#FF8C00")
        frame.pack ()

        self.center (scren, 700, 700)

        lb1 = Listbox (scren, width = 40, height = 20)
        lb1.place (relx = 0.05, rely = 0.05)

        lb2 = Listbox (scren, width = 40, height = 10)
        lb2.place (relx = 0.05, rely = 0.65)

        disc = self.objInterface.GetDisc (obj.codEscola)

        for i in disc :
            lb1.insert (END, i.codigo + (20 * " ") + i.name)

        entry1 = Entry (scren, bd = 1)
        entry1.place (relx = 0.65, rely = 0.05)

        panel = Text (scren, height = '20', width = '30')
        panel.place (relx = '0.60', rely = '0.30')

        for i in range (0, len (obj.turm)) :
            panel.insert (END, obj.turm[i].codigo + "  " + self.objInterface.GetDiscByCodigo (obj.turm[i].codigoDisc).name + '\n')
        panel.configure (state = "disable")

        def buttomInclDisc () :
            panel.configure (state = "normal")
            aux = None
            aux2 = self.objInterface.GetTurmaByCodigo (entry1.get ())

            if (aux2 != None) : aux = self.objInterface.GetDiscByCodigo (aux2.codigoDisc)

            if (aux != None) :
                panel.insert (END, entry1.get () + "  " + aux.name + "\n")
                entry1.delete (first = 0, last = 10)
                messagebox.showinfo("Atenção", "Disciplina Incluída!")
                panel.configure (state = "disable")

            else : messagebox.showinfo ("Atenção", "Disciplina não existe!")

        buttom1 = Button (scren, text = "Incluir", command = buttomInclDisc, width = 5, height = 3)
        buttom1.place (relx = 0.65, rely = 0.10)

        def buttomSalvar () :
            str = panel.get ("1.0", END).split ('\n')
            obj.turm.clear ()

            if (len (str) > 0) :
                for i in str :
                    val = i.split ('  ')
                    if (len (i) > 2) : obj.turm.append (turma.Turma (val[0], self.objInterface.GetDiscByName (val[1]).codigo))

                self.objInterface.UpdateStudent (obj)
                scren.destroy ()

        buttom2 = Button (scren, text = "Salvar", command = buttomSalvar, width = 5, height = 3)
        buttom2.place(relx = 0.88, rely = 0.90)

        def buttomLimpar () :
            panel.configure (state = "normal")
            obj.turm.clear ()
            panel.delete ("1.0", END)
            panel.configure (state = "disable")

        buttom3 = Button (scren, text = "Limpar", command = buttomLimpar, width = 5, height = 3)
        buttom3.place (relx = 0.79, rely = 0.10)

        def buttomAcessarTurmas () :
            lb2.delete (0, END)
            aux = self.objInterface.GetTurmaDisc (entry1.get ())

            for i in aux :
                lb2.insert (END, i.codigo)

        buttom4 = Button (scren, text = "Acessar Turmas", command = buttomAcessarTurmas, width = 10, height = 3, wraplength = 100)
        buttom4.place (relx = 0.05, rely = 0.52)

        label1 = Label (scren, text = "Código", bg = "#FF8C00")
        label1.place (relx = 0.57, rely = 0.05)

    def ScrenStudent (self, obj) :
        scren = Tk ()

        scren.title("Estudante")

        frame = Frame (scren, width = 800, height = 600, bg = "#FF8C00")
        frame.pack ()

        self.center(scren, 800, 600)

        def FAux1 (): self.Historico (obj)

        buttom1 = Button (scren, text = "Histórico", command = FAux1, width = 12, height = 5)
        buttom1.place (relx = 0.10, rely = 0.10)

        def FAux2 (): self.CompMatricula (obj)

        buttom2 = Button (scren, text = "Comprovante de Matrícula", command = FAux2, width = 12, height = 5, wraplength = 100)
        buttom2.place (relx = 0.40, rely = 0.10)

        def FAux3 (): self.Boletos (obj)

        buttom3 = Button (scren, text = "Boletos", command = FAux3, width = 12, height = 5)
        buttom3.place (relx = 0.70, rely = 0.10)

        def FAux4 (): self.NotaFreq (obj, obj.periodo)

        buttom4 = Button (scren, text = "Notas e Frequências", command = FAux4, width = 12, height = 5, wraplength = 100)
        buttom4.place(relx = 0.10, rely = 0.30)

        def FAux5 ():
            if (self.Inclusoes) : self.InclDisc (obj)
            else : messagebox.showinfo("Atenção", "Fora do periodo de inclusão.")

        buttom5 = Button (scren, text = "Matrícula / Inclusão", command = FAux5, width = 12, height = 5, wraplength = 100)
        buttom5.place (relx = 0.40, rely = 0.30)

        def FAux7 ():
            scren.destroy ()
            self.Start ()

        buttom7 = Button (scren, text = "Sair", command = FAux7, width = 5, height = 3, wraplength = 100)
        buttom7.place (relx = 0.90, rely = 0.88)


    def FazerChamada (self, obj) :
        scren = Tk  ()
        frame = Frame (scren, width = 700, height = 700, bg = "#FF8C00")
        frame.pack ()

        self.center(scren, 700, 700)

        label1 = Label (scren, text = "Código da Turma", bg = "#FF8C00")
        label1.place (relx = 0.05, rely = 0.10)

        label1 = Label (scren, text = "Código da Disciplina", bg = "#FF8C00")
        label1.place (relx = 0.05, rely = 0.15)

        entry1 = Entry (scren, bd = 1)
        entry1.place (relx = 0.25, rely = 0.10)

        entry2 = Entry (scren, bd = 1)
        entry2.place (relx = 0.25, rely = 0.15)

        lb1 = Listbox (scren, width = 38, height = 20)
        lb1.place (relx = 0.05, rely = 0.30)

        def FAux1 () :
            stud = self.objInterface.GetStudentByTurma (entry1.get(), entry2.get())

            for i in stud :
                lb1.insert(END, "Nome: " + i.name + "    Matricula: " + i.matricula)

        buttom1 = Button (scren, text = "Acessar", command = FAux1, width = 5, height = 3)
        buttom1.place (relx = 0.39, rely = 0.20)

        label3 = Label(scren, text="Matricula", bg="#FF8C00")
        label3.place(relx=0.60, rely=0.10)

        entry3 = Entry(scren, bd=1)
        entry3.place(relx=0.70, rely=0.10)

        label5 = Label(scren, text="Presença", bg="#FF8C00")
        label5.place(relx=0.60, rely=0.15)

        entry5 = Entry(scren, bd=1)
        entry5.place(relx=0.70, rely=0.15)

        def FAux2 () :
            if (entry1.get() != "" and entry2.get() != "" and entry3.get() != "" and entry5.get() != "" and self.objInterface.GetStudentByMatricula(entry3.get ()) != None):
                self.objInterface.UpdateFreq (entry3.get (), entry1.get(), entry2.get(), entry5.get (), self.objInterface.GetStudentByMatricula (entry3.get ()).periodo)

        buttom2 = Button(scren, text = "Incluir", command = FAux2, width = 5, height = 3)
        buttom2.place(relx = 0.70, rely = 0.20)

    def InclNota (self, obj) :
        scren = Tk ()
        frame = Frame (scren, width = 700, height = 700, bg = "#FF8C00")
        frame.pack ()

        self.center(scren, 700, 700)

        label1 = Label(scren, text="Código da Turma", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.10)

        label2 = Label(scren, text="Código da Disciplina", bg="#FF8C00")
        label2.place(relx=0.05, rely=0.15)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.25, rely=0.10)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.25, rely=0.15)

        lb1 = Listbox(scren, width=38, height=20)
        lb1.place(relx=0.05, rely=0.30)

        def FAux1 ():
            stud = self.objInterface.GetStudentByTurma(entry1.get(), entry2.get())

            for i in stud:
                lb1.insert(END, "Nome: " + i.name + "    Matricula: " + i.matricula)

        buttom1 = Button (scren, text = "Acessar", command=FAux1, width=5, height=3)
        buttom1.place (relx=0.39, rely = 0.20)

        label3 = Label (scren, text = "Matricula", bg="#FF8C00")
        label3.place (relx = 0.60, rely = 0.10)

        entry3 = Entry (scren, bd = 1)
        entry3.place (relx=0.70, rely=0.10)

        label4 = Label(scren, text="Nota", bg="#FF8C00")
        label4.place(relx=0.60, rely=0.15)

        entry4 = Entry(scren, bd=1)
        entry4.place(relx=0.70, rely=0.15)

        def FAux2 () :
            if (entry1.get() != "" and entry2.get() != "" and entry3.get () != "" and entry4.get () != "" and self.objInterface.GetStudentByMatricula(entry3.get ()) != None) :
                self.objInterface.UpdateNota (entry3.get (), entry1.get(), entry2.get(), entry4.get (),  self.objInterface.GetStudentByMatricula (entry3.get ()).periodo)

        buttom2 = Button(scren, text = "Incluir", command = FAux2, width = 5, height = 3)
        buttom2.place(relx = 0.70, rely = 0.20)

    def ProfessorInclTurm (self, obj) :
        scren = Tk()

        scren.title ("Incluir Turma")

        frame = Frame(scren, width=700, height=700, bg="#FF8C00")
        frame.pack()

        self.center(scren, 700, 700)

        lb1 = Listbox(scren, width=40, height=20)
        lb1.place(relx=0.05, rely=0.05)

        lb2 = Listbox(scren, width=40, height=10)
        lb2.place(relx=0.05, rely=0.65)

        disc = self.objInterface.GetDisc(obj.codEscola)

        for i in disc:
            lb1.insert (END, i.codigo + (20 * " ") + i.name)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.65, rely=0.05)

        panel = Text(scren, height='20', width='30')
        panel.place(relx='0.60', rely='0.30')

        for i in range(0, len(obj.turm)):
            panel.insert(END, obj.turm[i].codigo + "  " + self.objInterface.GetDiscByCodigo(
                obj.turm[i].codigoDisc).name + '\n')
        panel.configure(state="disable")

        def buttomInclDisc():
            panel.configure(state="normal")
            aux = None
            aux2 = self.objInterface.GetTurmaByCodigo(entry1.get())

            if (aux2 != None): aux = self.objInterface.GetDiscByCodigo(aux2.codigoDisc)

            if (aux != None):
                panel.insert(END, entry1.get() + "  " + aux.name + "\n")
                entry1.delete(first=0, last=10)
                panel.configure(state="disable")
                messagebox.showinfo("Atenção", "Disciplina Incluída!")

            else: messagebox.showinfo("Atenção", "Disciplina não existe!")

        buttom1 = Button(scren, text="Incluir", command=buttomInclDisc, width=5, height=3)
        buttom1.place(relx=0.65, rely=0.10)

        def buttomSalvar ():
            str = panel.get("1.0", END).split('\n')
            obj.turm.clear()

            if (len(str) > 0):
                for i in str:
                    val = i.split('  ')
                    if (len(i) > 2): obj.turm.append(
                        turma.Turma(val[0], self.objInterface.GetDiscByName(val[1]).codigo))

                self.objInterface.UpdateProdessor (obj)
                scren.destroy()

        buttom2 = Button(scren, text="Salvar", command=buttomSalvar, width=5, height=3)
        buttom2.place(relx=0.88, rely=0.90)

        def buttomLimpar():
            panel.configure(state="normal")
            obj.turm.clear()
            panel.delete("1.0", END)
            panel.configure(state="disable")

        buttom3 = Button(scren, text="Limpar", command=buttomLimpar, width=5, height=3)
        buttom3.place(relx=0.79, rely=0.10)

        def buttomAcessarTurmas():
            lb2.delete(0, END)
            aux = self.objInterface.GetTurmaDisc(entry1.get())

            for i in aux:
                lb2.insert(END, i.codigo)

        buttom4 = Button(scren, text="Acessar Turmas", command=buttomAcessarTurmas, width=10, height=3, wraplength=100)
        buttom4.place(relx=0.05, rely=0.52)

        label1 = Label(scren, text="Código", bg="#FF8C00")
        label1.place(relx=0.57, rely=0.05)

    def ListarTurmaProfessor (self, obj) :
        scren = Tk()

        scren.title ("Turmas")

        frame = Frame(scren, width=400, height=500, bg="#FF8C00")
        frame.pack()

        self.center(scren, 400, 500)

        label1 = Label(scren, text="Turmas", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        lb1 = Listbox(scren, width=44, height=20)
        lb1.place(relx=0.05, rely=0.10)

        for i in obj.turm :
            lb1.insert(END, i.codigo + "  " + self.objInterface.GetDiscByCodigo (i.codigoDisc).name)

        def FAux10 ():
            scren.destroy ()

        buttom10 = Button (scren, text = "Sair", command = FAux10, width = 5, height = 3, wraplength = 100)
        buttom10.place(relx=0.80, rely=0.88)

    def ScrenProfessor (self, obj) :
        scren = Tk ()

        scren.title ("Professor")

        frame = Frame (scren, width = 800, height = 600, bg = "#FF8C00")
        frame.pack ()

        self.center(scren, 800, 600)

        def FAux1 (): self.FazerChamada (obj)

        buttom1 = Button (scren, text = "Fazer a Chamada", command = FAux1, width = 12, height = 5, wraplength = 100)
        buttom1.place (relx = 0.10, rely = 0.10)

        def FAux2 (): self.InclNota (obj)

        buttom2 = Button (scren, text = "Incluir Nota", command = FAux2, width = 12, height = 5, wraplength = 100)
        buttom2.place (relx = 0.40, rely = 0.10)

        def FAux3 ():
            if (self.Inclusoes): self.ProfessorInclTurm (obj)
            else: messagebox.showinfo("Atenção", "Fora do periodo de inclusão.")

        buttom3 = Button (scren, text = "Incluir Turma", command = FAux3, width = 12, height = 5, wraplength = 100)
        buttom3.place (relx = 0.70, rely = 0.10)

        def FAux4 (): self.ListarTurmaProfessor (obj)

        buttom4 = Button (scren, text = "Listar Turmas", command = FAux4, width = 12, height = 5, wraplength = 100)
        buttom4.place (relx = 0.10, rely = 0.32)

        def FAux10 ():
            scren.destroy ()
            self.Start ()

        buttom10 = Button (scren, text = "Sair", command = FAux10, width = 5, height = 3, wraplength = 100)
        buttom10.place(relx=0.90, rely=0.88)

    def CadastrarDisc (self, obj) :
        scren = Tk ()

        scren.title("Cadastrar Disciplina")

        frame = Frame (scren, width=350, height=300, bg="#FF8C00")
        frame.pack ()

        self.center(scren, 350, 300)

        label1 = Label(scren, text="Nome", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        label2 = Label(scren, text="Código", bg="#FF8C00")
        label2.place(relx=0.05, rely=0.15)

        label3 = Label(scren, text="Carga Horária", bg="#FF8C00")
        label3.place(relx=0.05, rely=0.25)

        label4 = Label(scren, text="Código da Escola", bg="#FF8C00")
        label4.place(relx=0.05, rely=0.35)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.37, rely=0.15)

        entry3 = Entry(scren, bd=1)
        entry3.place(relx=0.37, rely=0.25)

        entry4 = Entry(scren, bd=1)
        entry4.place(relx=0.37, rely=0.35)

        def FAux1 () :
            if (entry1.get () != "" and entry2.get () != "" and entry3.get () != "" and entry4. get () != "" and self.objInterface.GetDiscByCodigo (entry2.get ()) == None) :
                self.objInterface.CadastrarDisc (entry1.get (), entry2.get (), entry3.get (), entry4. get ())
                scren.destroy ()

        buttom1 = Button(scren, text="Cadastrar", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.65)

    def ListarDisc (self, obj) :
        scren = Tk ()

        scren.title("Listar Disciplina")

        frame = Frame(scren, width=400, height=500, bg="#FF8C00")
        frame.pack ()

        self.center(scren, 400, 500)

        label1 = Label(scren, text="Codigo da Escola", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        lb1 = Listbox(scren, width=38, height=20)
        lb1.place(relx=0.05, rely=0.30)

        def FAux1 ():
            aux = self.objInterface.ListarDisc (entry1.get())
            lb1.delete (0, END)

            for i in aux :
                lb1.insert (END, i.name + "  " + i.codigo)


        buttom1 = Button(scren, text="Listar", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.15)

    def CadastrarTurma (self, obj) :
        scren = Tk()

        scren.title("Cadastrar Turma")

        frame = Frame(scren, width=350, height=300, bg="#FF8C00")
        frame.pack()

        self.center(scren, 350, 300)

        label1 = Label(scren, text="Codigo da Turma", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        label2 = Label(scren, text="Código da Disciplina", bg="#FF8C00")
        label2.place(relx=0.05, rely=0.15)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.42, rely=0.05)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.42, rely=0.15)

        def FAux1 () :
            if (entry1.get () != "" and entry2.get () != "" and self.objInterface.GetTurmaByCodigo (entry1.get ()) == None) :
                if (self.objInterface.CadastrarTurma (entry1.get (), entry2.get ()) == True) :
                    scren.destroy ()

        buttom1 = Button(scren, text="Cadastrar", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.65)

    def ListarTurma (self, obj) :
        scren = Tk()

        scren.title("Listar Turma")

        frame = Frame(scren, width=400, height=500, bg="#FF8C00")
        frame.pack()

        self.center(scren, 400, 500)

        label1 = Label(scren, text="Codigo da Escola", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        lb1 = Listbox(scren, width=38, height=20)
        lb1.place(relx=0.05, rely=0.30)

        def FAux1 ():
            aux = self.objInterface.ListarTurma (entry1.get())
            lb1.delete(0, END)

            for i in aux:
                lb1.insert(END, i.codigo + "  " + self.objInterface.GetDiscByCodigo (i.codigoDisc).name)

        buttom1 = Button(scren, text="Listar", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.15)

    def MatricularStudent (self, obj) :
        scren = Tk()

        scren.title("Matricular Estudante")

        frame = Frame(scren, width=350, height=300, bg="#FF8C00")
        frame.pack()

        self.center(scren, 350, 300)

        label1 = Label(scren, text="Nome", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        label2 = Label(scren, text="Matricula", bg="#FF8C00")
        label2.place(relx=0.05, rely=0.15)

        label3 = Label(scren, text="Password", bg="#FF8C00")
        label3.place(relx=0.05, rely=0.25)

        label4 = Label(scren, text="Código da Escola", bg="#FF8C00")
        label4.place(relx=0.05, rely=0.35)

        label5 = Label(scren, text="Código do Curso", bg="#FF8C00")
        label5.place(relx=0.05, rely=0.45)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.37, rely=0.15)

        entry3 = Entry(scren, bd=1)
        entry3.place(relx=0.37, rely=0.25)

        entry4 = Entry(scren, bd=1)
        entry4.place(relx=0.37, rely=0.35)

        entry5 = Entry(scren, bd=1)
        entry5.place(relx=0.37, rely=0.45)

        def FAux1 ():
            if (entry1.get () != "" and entry2.get () != "" and entry3.get () != "" and entry4.get () != "" and entry5.get () != "" and self.objInterface.GetStudentByMatricula (entry2.get ()) == None) :
                self.objInterface.MatricularStudent (entry1.get (), entry2.get (), entry3.get (), entry4.get (), entry5.get ())
                scren.destroy()

        buttom1 = Button(scren, text="Matricular", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.65)

    def ListarStudents (self, obj) :
        scren = Tk()

        scren.title("Listar Estudantes")

        frame = Frame(scren, width=400, height=500, bg="#FF8C00")
        frame.pack()

        self.center(scren, 400, 500)

        label1 = Label(scren, text="Codigo da Escola", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        lb1 = Listbox(scren, width=38, height=20)
        lb1.place(relx=0.05, rely=0.30)

        def FAux1():
            aux = self.objInterface.ListarStudents (entry1.get())
            lb1.delete(0, END)

            for i in aux:
                lb1.insert (END, i.name + "  " + i.matricula)

        buttom1 = Button(scren, text="Listar", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.15)


    def ListarCursoGrad (self, obj) :
        scren = Tk()

        scren.title("Listar Curso de Graduação")

        frame = Frame(scren, width=400, height=500, bg="#FF8C00")
        frame.pack()

        self.center(scren, 400, 500)

        label1 = Label(scren, text="Codigo da Escola", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        lb1 = Listbox(scren, width=38, height=20)
        lb1.place(relx=0.05, rely=0.30)

        def FAux1 ():
            aux = self.objInterface.ListarCursoGrad (entry1.get ())
            lb1.delete(0, END)

            for i in aux:
                lb1.insert (END, i.name + "  " + i.codigo)

        buttom1 = Button (scren, text="Listar", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place (relx=0.05, rely=0.15)

    def ListarCursoPos (self, obj):
        scren = Tk()

        scren.title("Listar Curso de Pós-graduação")

        frame = Frame(scren, width=400, height=500, bg="#FF8C00")
        frame.pack()

        self.center(scren, 400, 500)

        label1 = Label(scren, text="Codigo da Escola", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        lb1 = Listbox(scren, width=38, height=20)
        lb1.place(relx=0.05, rely=0.30)

        def FAux1():
            aux = self.objInterface.ListarCursoPos(entry1.get())
            lb1.delete(0, END)

            for i in aux:
                lb1.insert(END, i.name + "  " + i.codigo)

        buttom1 = Button(scren, text="Listar", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.15)

    def CadastrarProfessor (self, obj) :
        scren = Tk()

        scren.title("Cadastrar Professor")

        frame = Frame(scren, width=350, height=300, bg="#FF8C00")
        frame.pack()

        self.center(scren, 350, 300)

        label1 = Label(scren, text="Nome", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        label2 = Label(scren, text="Matricula", bg="#FF8C00")
        label2.place(relx=0.05, rely=0.15)

        label3 = Label(scren, text="Password", bg="#FF8C00")
        label3.place(relx=0.05, rely=0.25)

        label4 = Label(scren, text="Código da Escola", bg="#FF8C00")
        label4.place(relx=0.05, rely=0.35)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.37, rely=0.15)

        entry3 = Entry(scren, bd=1)
        entry3.place(relx=0.37, rely=0.25)

        entry4 = Entry(scren, bd=1)
        entry4.place(relx=0.37, rely=0.35)

        def FAux1():
            if (entry1.get() != "" and entry2.get() != "" and entry3.get() != "" and entry4.get() != "" and self.objInterface.GetProfessorByMatricula (entry2.get ()) == None) :
                self.objInterface.CadastrarProfessor (entry1.get(), entry2.get(), entry3.get(), entry4.get())
                scren.destroy()

        buttom1 = Button(scren, text="Cadastrar", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.65)

    def ListarProfessores (self, obj) :
        scren = Tk()

        scren.title("Listar Professores")

        frame = Frame(scren, width=400, height=500, bg="#FF8C00")
        frame.pack()

        self.center(scren, 400, 500)

        label1 = Label(scren, text="Codigo da Escola", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        lb1 = Listbox(scren, width=38, height=20)
        lb1.place(relx=0.05, rely=0.30)

        def FAux1():
            aux = self.objInterface.ListarProfessores (entry1.get())
            lb1.delete(0, END)

            for i in aux:
                lb1.insert(END, i.name + "  " + i.matricula)

        buttom1 = Button(scren, text="Listar", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.15)

    def Semestre (self, obj) :
        scren = Tk()

        scren.title("Semestre")

        frame = Frame(scren, width=400, height=300, bg="#FF8C00")
        frame.pack()

        self.center (scren, 400, 300)

        label1 = Label(scren, text="Semestre", bg="#FF8C00")
        label1.place(relx=0.45, rely=0.05)

        def FAux1 () :
            aux = self.objInterface.ListarAllStudents ()

            for i in aux :
                i.periodo = str (int (i.periodo) + 1)
                i.turm.clear ()
                self.objInterface.UpdateStudent (i)
            self.objInterface.SetEstadoInclusoes ("1")
            self.Inclusoes = True
            messagebox.showinfo ("Atenção", "Inclusões Iniciadas!")
            scren.destroy()

        buttom1 = Button (scren, text = "Iniciar Inclusões", command = FAux1, width = 12, height = 5, wraplength = 100)
        buttom1.place (relx = 0.10, rely = 0.25)

        def FAux2 () :
            self.objInterface.SetEstadoInclusoes("0")
            self.Inclusoes = False
            messagebox.showinfo("Atenção", "Inclusões Terminadas!")
            scren.destroy ()

        buttom2 = Button (scren, text = "Finalizar Inclusões", command = FAux2, width = 12, height = 5, wraplength = 100)
        buttom2.place (relx = 0.60, rely = 0.25)

        def FAux15 ():
            scren.destroy ()

        buttom15 = Button (scren, text = "Sair", command = FAux15, width = 5, height = 3, wraplength = 100)
        buttom15.place(relx=0.74, rely=0.75)

    def CadastrarCursoGrad (self, obj) :
        scren = Tk ()

        scren.title("Cadastrar Curso de Graduação")

        frame = Frame(scren, width=350, height=300, bg="#FF8C00")
        frame.pack()

        self.center(scren, 350, 300)

        label1 = Label(scren, text="Nome", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        label2 = Label(scren, text="Código", bg="#FF8C00")
        label2.place(relx=0.05, rely=0.15)

        label3 = Label(scren, text="Código da Escola", bg="#FF8C00")
        label3.place(relx=0.05, rely=0.25)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.37, rely=0.15)

        entry3 = Entry(scren, bd=1)
        entry3.place(relx=0.37, rely=0.25)

        def FAux1():
            if (entry1.get() != "" and entry2.get() != "" and entry3.get() != "" and self.objInterface.GetCursoGraByCod (entry2.get ()) == None):
                self.objInterface.CadastrarCursoGrad (entry1.get(), entry2.get(), entry3.get())
                scren.destroy()

        buttom1 = Button (scren, text="Cadastrar", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.65)

    def CadastrarCursoPos (self, obj) :
        scren = Tk ()

        scren.title("Cadastrar Curso de Pós-graduação")

        frame = Frame(scren, width=350, height=300, bg="#FF8C00")
        frame.pack()

        self.center(scren, 350, 300)

        label1 = Label(scren, text="Nome", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        label2 = Label(scren, text="Código", bg="#FF8C00")
        label2.place(relx=0.05, rely=0.15)

        label3 = Label(scren, text="Código da Escola", bg="#FF8C00")
        label3.place(relx=0.05, rely=0.25)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.37, rely=0.15)

        entry3 = Entry(scren, bd=1)
        entry3.place(relx=0.37, rely=0.25)

        def FAux1 ():
            if (entry1.get() != "" and entry2.get() != "" and entry3.get() != "" and self.objInterface.GetCursoPosByCod (entry2.get ()) == None):
                self.objInterface.CadastrarCursoPos (entry1.get(), entry2.get(), entry3.get())
                scren.destroy()

        buttom1 = Button (scren, text="Cadastrar", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.65)

    def CadastrarCurso (self, obj) :
        scren = Tk()

        scren.title("Cadastrar Curso")

        frame = Frame(scren, width=400, height=300, bg="#FF8C00")
        frame.pack()

        self.center(scren, 400, 300)

        def FAux1():
            self.CadastrarCursoGrad(obj)

        buttom1 = Button(scren, text="Graduação", command=FAux1, width=12, height=5, wraplength=100)
        buttom1.place(relx=0.10, rely=0.25)

        def FAux2():
            self.CadastrarCursoPos (obj)

        buttom2 = Button(scren, text="Pós-graduação", command=FAux2, width=12, height=5, wraplength=100)
        buttom2.place(relx=0.60, rely=0.25)

        def FAux15():
            scren.destroy()

        buttom15 = Button(scren, text="Sair", command=FAux15, width=5, height=3, wraplength=100)
        buttom15.place(relx=0.74, rely=0.75)

    def ScrenListar (self, obj) :
        scren = Tk ()

        scren.title ("Funcionário Administrativo")

        frame = Frame (scren, width = 800, height = 600, bg = "#FF8C00")
        frame.pack ()

        self.center(scren, 800, 600)

        def FAux1 (): self.ListarDisc (obj)

        buttom1 = Button(scren, text="Listar Disciplina", command=FAux1, width=12, height=5, wraplength=100)
        buttom1.place(relx=0.10, rely=0.10)

        def FAux2 (): self.ListarTurma (obj)

        buttom2 = Button(scren, text="Listar Turmas", command=FAux2, width=12, height=5, wraplength=100)
        buttom2.place(relx=0.40, rely=0.10)

        def FAux3 (): self.ListarStudents (obj)

        buttom3 = Button(scren, text="Listar Alunos", command=FAux3, width=12, height=5, wraplength=100)
        buttom3.place(relx=0.70, rely=0.10)

        def FAux4 (): self.ListarCursoGrad (obj)

        buttom4 = Button(scren, text="Listar Cursos de Graduação", command=FAux4, width=12, height=5, wraplength=100)
        buttom4.place(relx=0.10, rely=0.32)

        def FAux5 (): self.ListarProfessores (obj)

        buttom5 = Button(scren, text="Listar Professores", command=FAux5, width=12, height=5, wraplength=100)
        buttom5.place(relx=0.40, rely=0.32)

        def FAux6 (): self.ListarCursoPos (obj)

        buttom6 = Button(scren, text="Listar Cursos de Pós-graduação", command=FAux6, width=12, height=5, wraplength=100)
        buttom6.place(relx=0.70, rely=0.32)

        def FAux15 ():
            scren.destroy ()

        buttom15 = Button (scren, text = "Sair", command = FAux15, width = 5, height = 3, wraplength = 100)
        buttom15.place(relx=0.90, rely=0.88)

    def ScrenFuncAdm (self, obj) :
        scren = Tk ()

        scren.title ("Funcionário Administrativo")

        frame = Frame (scren, width = 800, height = 600, bg = "#FF8C00")
        frame.pack ()

        self.center(scren, 800, 600)

        def FAux1 (): self.CadastrarDisc (obj)

        buttom1 = Button (scren, text = "Cadastrar Disciplina", command = FAux1, width = 12, height = 5, wraplength = 100)
        buttom1.place (relx = 0.10, rely = 0.10)

        def FAux2 (): self.ScrenListar (obj)

        buttom2 = Button(scren, text="Listar", command=FAux2, width=12, height=5, wraplength=100)
        buttom2.place(relx=0.40, rely=0.10)

        def FAux3 (): self.CadastrarTurma (obj)

        buttom3 = Button(scren, text="Cadastrar Turma", command=FAux3, width=12, height=5, wraplength=100)
        buttom3.place(relx=0.70, rely=0.10)

        def FAux4 (): self.MatricularStudent (obj)

        buttom4 = Button(scren, text="Matricular Aluno", command=FAux4, width=12, height=5, wraplength=100)
        buttom4.place(relx=0.10, rely=0.32)

        def FAux5 (): self.CadastrarCurso (obj)

        buttom5 = Button(scren, text="Cadastrar Curso", command=FAux5, width=12, height=5, wraplength=100)
        buttom5.place(relx=0.40, rely=0.32)

        def FAux6 (): self.CadastrarProfessor (obj)

        buttom6 = Button(scren, text="Cadastrar Professor", command=FAux6, width=12, height=5, wraplength=100)
        buttom6.place(relx=0.70, rely=0.32)

        def FAux7 (): self.Semestre (obj)

        buttom7 = Button(scren, text="Semestre", command=FAux7, width=12, height=5, wraplength=100)
        buttom7.place(relx=0.10, rely=0.54)

        def FAux15 ():
            scren.destroy ()
            self.Start ()

        buttom15 = Button (scren, text = "Sair", command = FAux15, width = 5, height = 3, wraplength = 100)
        buttom15.place(relx=0.90, rely=0.88)

    def SoliciPagFuncionario (self, obj) :
        scren = Tk ()

        scren.title("Pagamento Funcionário")

        frame = Frame (scren, width = 500, height = 300, bg = "#FF8C00")
        frame.pack ()

        self.center(scren, 500, 300)

        label1 = Label(scren, text="Matrícula do Funcionário", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        label2 = Label(scren, text="Número da Conta", bg="#FF8C00")
        label2.place(relx=0.05, rely=0.15)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.37, rely=0.15)

        label3 = Label(scren, text="Agência Bancária", bg="#FF8C00")
        label3.place(relx=0.05, rely=0.25)

        entry3 = Entry(scren, bd=1)
        entry3.place(relx=0.37, rely=0.25)

        label4 = Label(scren, text="Valor", bg="#FF8C00")
        label4.place(relx=0.05, rely=0.35)

        entry4 = Entry(scren, bd=1)
        entry4.place(relx=0.37, rely=0.35)

        def FAux10 () :
            if (entry1.get() != "" and entry2.get() != "" and entry3.get() != "" and entry4.get() != "") :
                self.objInterface.SoliciPag (entry1.get (), entry2.get (), entry3.get (), entry4.get ())
                scren.destroy ()

        buttom10 = Button(scren, text="Solicitar", command=FAux10, width=5, height=3, wraplength=100)
        buttom10.place(relx = 0.82, rely=0.75)


    def SoliciPagDespesas (self, obj) :
        scren = Tk ()

        scren.title("Pagar Despesas")

        frame = Frame (scren, width=500, height=300, bg="#FF8C00")
        frame.pack ()

        self.center (scren, 500, 300)

        label2 = Label (scren, text="Número da Conta", bg="#FF8C00")
        label2.place (relx=0.05, rely=0.05)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.37, rely=0.05)

        label3 = Label(scren, text="Agência Bancária", bg="#FF8C00")
        label3.place(relx=0.05, rely=0.15)

        entry3 = Entry(scren, bd=1)
        entry3.place(relx=0.37, rely=0.15)

        label4 = Label(scren, text="Valor", bg="#FF8C00")
        label4.place(relx=0.05, rely=0.25)

        entry4 = Entry(scren, bd=1)
        entry4.place(relx=0.37, rely=0.25)

        def FAux10():
            if (entry2.get() != "" and entry3.get() != "" and entry4.get() != "") :
                self.objInterface.SoliciPag ("", entry2.get (), entry3.get (), entry4.get ())
                scren.destroy ()

        buttom10 = Button (scren, text="Solicitar", command=FAux10, width=5, height=3, wraplength=100)
        buttom10.place (relx=0.82, rely=0.75)


    def ContasParaPagar (self, obj) :
        scren = Tk ()

        scren.title("Contas Para Pagar")

        frame = Frame (scren, width=500, height=500, bg="#FF8C00")
        frame.pack ()

        self.center (scren, 500, 500)

        lb1 = Listbox (scren, width = 38, height = 30)
        lb1.place (relx=0.05, rely=0.05)

        aux = self.objInterface.ListarContas ()

        k = 1

        for i in aux :
            if (i.matricula != "") : lb1.insert (k, i.matricula)
            k += 1
            lb1.insert (k, i.contaBancaria)
            k += 1
            lb1.insert (k, i.agenciaBancaria)
            k += 1
            lb1.insert (k, i.valor)
            k += 1
            lb1.insert (k, "-----------------------------------------------------------------------------")
            k += 1

    def GerarCodigoBoleto (self, valor) :
        aux = ""
        for i in range (40) :
            aux += str (randint (0, 9))

        return aux

    def EnviarBoletoEstudante (self, obj) :
        scren = Tk()

        scren.title("Enviar Boleto Para Estudante")

        frame = Frame(scren, width=500, height=300, bg="#FF8C00")
        frame.pack()

        self.center(scren, 500, 300)

        label2 = Label(scren, text="Matricula", bg="#FF8C00")
        label2.place(relx=0.05, rely=0.05)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.37, rely=0.05)

        label3 = Label(scren, text="Valor", bg="#FF8C00")
        label3.place(relx=0.05, rely=0.15)

        entry3 = Entry(scren, bd=1)
        entry3.place(relx=0.37, rely=0.15)

        def FAux10 ():
            if (entry2.get() != "" and entry3.get()) :
                self.objInterface.SetBoletoEstudante (entry2.get (), entry3.get (), self.GerarCodigoBoleto (entry3.get ()))
                scren.destroy ()

        buttom10 = Button (scren, text="Enviar", command=FAux10, width=5, height=3, wraplength=100)
        buttom10.place (relx=0.82, rely=0.75)


    def ScrenFuncFinanceiro (self, obj) :
        scren = Tk ()

        scren.title ("Financeiro")

        frame = Frame(scren, width=800, height=600, bg="#FF8C00")
        frame.pack ()

        self.center (scren, 800, 600)

        def FAux1 (): self.SoliciPagFuncionario (obj)

        buttom1 = Button (scren, text = "Solicitar Pagamento de Funcionário", command = FAux1, width = 12, height = 5, wraplength = 100)
        buttom1.place (relx = 0.10, rely = 0.10)

        def FAux2 (): self.SoliciPagDespesas (obj)

        buttom2 = Button (scren, text = "Solicitar Pagamento de Despesas", command = FAux2, width = 12, height = 5, wraplength = 100)
        buttom2.place (relx = 0.40, rely = 0.10)

        def FAux3 (): self.ContasParaPagar (obj)

        buttom3 = Button (scren, text = "Contas Para Pagar", command = FAux3, width = 12, height = 5, wraplength = 100)
        buttom3.place (relx = 0.70, rely = 0.10)

        def FAux4 (): self.EnviarBoletoEstudante (obj)

        buttom1 = Button (scren, text = "Enviar Boleto Para Estudante", command = FAux4, width = 12, height = 5, wraplength = 100)
        buttom1.place (relx = 0.10, rely = 0.30)

        def FAux10():
            scren.destroy()
            self.Start()

        buttom3 = Button(scren, text="Sair", command=FAux10, width=5, height=3, wraplength=100)
        buttom3.place(relx=0.90, rely=0.88)

    def CadastrarFuncAdm (self, obj) :
        scren = Tk()

        scren.title("Cadastrar Funcionário Administrativo")

        frame = Frame(scren, width=350, height=300, bg="#FF8C00")
        frame.pack()

        self.center(scren, 350, 300)

        label1 = Label(scren, text="Nome", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        label2 = Label(scren, text="Matricula", bg="#FF8C00")
        label2.place(relx=0.05, rely=0.15)

        label3 = Label(scren, text="Password", bg="#FF8C00")
        label3.place(relx=0.05, rely=0.25)

        label4 = Label(scren, text="Código da Escola", bg="#FF8C00")
        label4.place(relx=0.05, rely=0.35)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.37, rely=0.15)

        entry3 = Entry(scren, bd=1)
        entry3.place(relx=0.37, rely=0.25)

        entry4 = Entry(scren, bd=1)
        entry4.place(relx=0.37, rely=0.35)

        def FAux1():
            if (entry1.get() != "" and entry2.get() != "" and entry3.get() != "" and entry4.get() != ""):
                self.objInterface.CadastrarFuncAdm (entry1.get(), entry2.get(), entry3.get(), entry4.get())
                scren.destroy()

        buttom1 = Button(scren, text="Matricular", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.65)

    def CadastrarFuncFinanceiro (self, obj) :
        scren = Tk()

        scren.title("Cadastrar Funcionário Financeiro")

        frame = Frame(scren, width=350, height=300, bg="#FF8C00")
        frame.pack()

        self.center(scren, 350, 300)

        label1 = Label(scren, text="Nome", bg="#FF8C00")
        label1.place(relx=0.05, rely=0.05)

        label2 = Label(scren, text="Matricula", bg="#FF8C00")
        label2.place(relx=0.05, rely=0.15)

        label3 = Label(scren, text="Password", bg="#FF8C00")
        label3.place(relx=0.05, rely=0.25)

        label4 = Label(scren, text="Código da Escola", bg="#FF8C00")
        label4.place(relx=0.05, rely=0.35)

        entry1 = Entry(scren, bd=1)
        entry1.place(relx=0.37, rely=0.05)

        entry2 = Entry(scren, bd=1)
        entry2.place(relx=0.37, rely=0.15)

        entry3 = Entry(scren, bd=1)
        entry3.place(relx=0.37, rely=0.25)

        entry4 = Entry(scren, bd=1)
        entry4.place(relx=0.37, rely=0.35)

        def FAux1():
            if (entry1.get() != "" and entry2.get() != "" and entry3.get() != "" and entry4.get() != ""):
                self.objInterface.CadastrarFuncFinanceiro (entry1.get(), entry2.get(), entry3.get(), entry4.get())
                scren.destroy()

        buttom1 = Button(scren, text="Matricular", command=FAux1, width=5, height=3, wraplength=100)
        buttom1.place(relx=0.05, rely=0.65)

    def ScrenAdministrador (self, obj) :
        scren = Tk()

        scren.title ("Administrador")

        frame = Frame(scren, width=800, height=600, bg="#FF8C00")
        frame.pack()

        self.center(scren, 800, 600)

        def FAux1 (): self.CadastrarFuncAdm (obj)

        buttom1 = Button(scren, text="Cadastrar Funcionario Administrativo", command = FAux1, width=12, height=5, wraplength=100)
        buttom1.place(relx=0.10, rely=0.10)

        def FAux2 (): self.CadastrarFuncFinanceiro (obj)

        buttom1 = Button(scren, text="Cadastrar Funcionario do Financeiro", command = FAux2, width=12, height=5, wraplength=100)
        buttom1.place(relx=0.40, rely=0.10)

        def FAux10():
            scren.destroy()
            self.Start()

        buttom3 = Button(scren, text="Sair", command=FAux10, width=5, height=3, wraplength=100)
        buttom3.place(relx=0.90, rely=0.88)

    def Buttom1Start (self, entry1, entry2, scren1) :
        user = entry1.get ()
        passWord = entry2.get ()

        objStudent = self.objInterface.GetStudent (user, passWord)
        objProfessor = self.objInterface.GetProfessor (user, passWord)
        objFuncAdm = self.objInterface.GetFuncAdm (user, passWord)
        objFuncFinanceiro = self.objInterface.GetFuncFinanceiro (user, passWord)
        objAdministrador = self.objInterface.GetAdministrador (user, passWord)

        if (objStudent != None) :
            scren1.destroy ()
            self.ScrenStudent (objStudent)

        elif (objProfessor != None) :
            scren1.destroy ()
            self.ScrenProfessor (objProfessor)

        elif (objFuncAdm != None) :
            scren1.destroy ()
            self.ScrenFuncAdm (objFuncAdm)

        elif (objFuncFinanceiro != None) :
            scren1.destroy ()
            self.ScrenFuncFinanceiro (objFuncFinanceiro)

        elif (objAdministrador != None) :
            scren1.destroy()
            self.ScrenAdministrador (objAdministrador)

        else : messagebox.showinfo("Atenção", "Usuário Não Encontrado!")

    def Start (self) :
        scren1 = Tk ()

        scren1.title ("Login")

        frame1 = LabelFrame (scren1, width = 800, height = 600, bg = "#FF8C00")
        frame1.pack (fill="both", expand="yes")

        self.center (scren1, 800, 600)

        C = Canvas (scren1, bg="#FFA500", height = 470, width=635)
        C.place (relx = 0.10, rely = 0.10)

        myFont = Font(family="Arial", size=12)

        label1 = Label (text = "Matrícula", bg = "#FFA500")
        label1.place (relx = 0.30, rely = 0.30)


        label1.configure(font=myFont)

        label2 = Label (text = "Senha", bg = "#FFA500")
        label2.place (relx = 0.30, rely = 0.35)

        label2.configure (font=myFont)

        entry1 = Entry (scren1, bd = 1)
        entry1.place (relx = 0.45, rely = 0.30)

        entry2 = Entry (scren1, bd = 1, show = "*")
        entry2.place (relx = 0.45, rely = 0.35)

        def FAux (): self.Buttom1Start (entry1, entry2, scren1)

        buttom1 = Button (scren1, text = "Entrar", command = FAux)
        buttom1.place (relx = 0.45, rely = 0.45)

        buttom1.configure(font=myFont)

        scren1.mainloop ()
