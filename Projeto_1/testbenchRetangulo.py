from package.maths.terms import Retangulo

def workspace():
    tamanho_base = int(input('Digite o tamanho da base do retangulo:'))
    tamanho_altura = int(input('Digite o tamanho da altura do retangulo:'))
    cor_retangulo = str(input('Digite a cor do retangulo:'))
    segmento_2 = Retangulo (tamanho_base, tamanho_altura, cor_retangulo)
    segmento_2.model()     #nome da variável.metodo()  ------ a sua variavel esta chamando a funçao
    print(f'area: {segmento_2.area()}')
    print(f'perimetro: {segmento_2.perimetro()}')
    print(f'cor: {segmento_2.color}')
   
    

if __name__ == "__main__":

    print("O arquivo 'testbenchRetangulo.py' foi envocado como programa")
    print(f'_name_ =={__name__}')
    workspace()

else:

    print("o arquivo 'testbenchRetangulo.py' foi envocado como modulo")
    print(f'__name__ =={__name__}')