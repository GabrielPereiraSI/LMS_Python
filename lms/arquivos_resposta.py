from resposta import Resposta

class arquivos_resposta():
    
    def __init__(self,nome_disciplina,ano_ofertado,semestre_ofertado,id_turma,numero_questao,ra_aluno):
        self.nome_disciplina = nome_disciplina
        self.ano_ofertado = ano_ofertado
        self.semestre_ofertado = semestre_ofertado
        self.id_turma = id_turma
        self.numero_questao = numero_questao
        self.ra_aluno = ra_aluno
              
        self.arquivo = '' #ultima aula VERIFICAR COMO FUNCIONA FILHO DA PUTA