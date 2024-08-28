from package.maths.terms import Hexagono

def workspace():
    tamanho_lado = int(input('Digite o tamanho do lado do Hexagono:'))
    cor_hexagono = str(input('Digite a cor do Hexagono:'))
    segmento_2 = Hexagono (tamanho_lado, cor_hexagono)
    segmento_2.model()     
    print(f'area: {segmento_2.area()}')
    print(f'perimetro: {segmento_2.perimetro()}')
    print(f'cor: {segmento_2.cor()}')
   
    

if __name__ == "__main__":

    print("O arquivo 'testbenchHexagono.py' foi envocado como programa")
    print(f'_name_ =={__name__}')
    workspace()

else:

    print("o arquivo 'testbenchHexagono.py' foi envocado como modulo")
    print(f'__name__ =={__name__}')