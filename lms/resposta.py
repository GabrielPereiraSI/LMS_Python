from alunos import Aluno
from questao import Questao
class Resposta():
    def __init__(self,ra, nome_disciplina,ano_ofertado,semestre_ofertado,id_turma,numero):
        self.nome_disciplina = nome_disciplina
        self.ano_ofertado = ano_ofertado
        self.semestre_ofertado = semestre_ofertado
        self.id_turma = id_turma
        self.numero_questao = numero
        self.ra_aluno = ra
        self.data_avaliacao = data_avaliacao
        self.nota = nota
        self.avaliacao = avaliacao
        self.descricao = descricao
        self.data_de_envio = data_de_envio
    