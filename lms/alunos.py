from pessoas import Pessoa
from usuarios import Usuario
from curso import Curso

class Aluno(Pessoa, Usuario):

    def __init__(self,sigla):
        self.sigla_curso = sigla
        self.ra_aluno = ra_aluno

    def altera_sigla(self, sigla):
        if type(sigla) == str:
            self.sigla_curso = sigla
            return True
        return False

    def retorna_sigla(self):
        return self.sigla_curso

 
    def altera_celular(self, celular):
        print("Alterando Celular do aluno")
        self.celular = celular