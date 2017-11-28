class Pessoa:

    def __init__(self):
        self.nome = nome
        self.celular = celular
        self.email = email

    def altera_celular(self, celular):
        if type(celular) == str:
            self.celular = celular
            return True
        return False

    def retorna_celular(self):
        return self.celular