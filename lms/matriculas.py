from alunos import Aluno
from disciplinas import Disciplina
from turma import Turma

class Matricula:
    
    def __init__(self,ra_aluno,nome_disciplina, ano,semestre_ofertado,id_turma):
        self.ra_aluno = ra_aluno
        self.nome_disciplina = nome_disciplina
        self.ano_ofertado = ano
        self.semestre_ofertado = semestre_ofertado
        self.id_turma = id_turma
        self.data_matricula = None
        self.data_cancelamento = None
        self.data_confirmacao = None

    def altera_aluno(self, a):
        if type(a) == Aluno:
            self.aluno = a
            return True
        return False
    
    def altera_disciplina(self, disciplina):
        if type(disciplina) == Disciplina:
            self.disciplina = disciplina
            return True
        return False

    def retorna_disciplina(self):
        return self.disciplina

    def retorna_aluno(self):
        return self.aluno
