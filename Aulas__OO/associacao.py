class Endereco:
    def __init__(self,rua,numero,cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade 

    
class Pessoa:
    def __init__(self,nome,endereco):
        self.nome = nome
        self.endereco = endereco


endereco = Endereco('rua A', 123, "cidade A")
pessoa = Pessoa ('joao',endereco)

print(pessoa.nome)

print(pessoa.endereco.numero)
