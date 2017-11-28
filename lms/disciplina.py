from disciplina import Disciplina

class Disciplina:

    def __init__(self,nome):
        self.nome_disciplina = nome
        self.carga_horaria = carga_horaria
        self.teoria = teoria
        self.pratica = pratica
        self.ementa = ementa
        self.competencias = competencias
        self.habilidades = habilidades
        self.conteudo = conteudo
        self.bibliografia_basica = bibliografia_basica
        self.bibliografia_complementar = bibliografia_complementar

    def altera_nome(self, nome):
        if type(nome) == str:
            self.nome = nome
            return True
        return False

    def retorna_nome(self):
        return self.nome