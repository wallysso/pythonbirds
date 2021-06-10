class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list (filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos{cls}'

if __name__ == '__main__':
    wallysson = Wallysson(nome='Wallysson')
    jéssica = Pessoa(wallysson, nome='Jéssica')
    print(Pessoa.cumprimentar(jéssica))
    print(id(jéssica))
    print(jéssica.cumprimentar())
    print(jéssica.nome)
    print(jéssica.idade)
    for filho in jéssica.filhos:
        print(filho.nome)
    jéssica.sobrenome = 'Ferreira'
    del jéssica.filhos
    print(jéssica.__dict__)
    print(wallysson.__dict__)
    print(Pessoa.olhos)
    print(wallysson.olhos)
    print(jéssica.olhos)
    print(id(Pessoa.olhos), id(jéssica.olhos), id(wallysson.olhos))
    print(Pessoa.metodo_estatico(), jéssica.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), jéssica.nome_e_atributo_de_classe())
