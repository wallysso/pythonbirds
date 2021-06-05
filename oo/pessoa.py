class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list (filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':
    wallysson = Pessoa(nome='Wallysson')
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