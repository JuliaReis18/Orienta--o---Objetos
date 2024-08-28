from package.maths.terms import Octogono

def workspace():
    tamanho_lado = int(input('Digite o tamanho do lado do octógono:'))
    cor_octogono = str(input('Digite a cor do octógono:'))
    segmento_2 = Octogono (tamanho_lado, cor_octogono)
    segmento_2.model()
    print(f'area:{segmento_2.area()}')
    print(f'perímetro:{segmento_2.perimetro()}')
    print(f'cor:{segmento_2.cor()}')



if __name__ == "__main__":

    print("O arquivo 'testbenchOctogono.py' foi envocado como programa")
    print(f'_name_ =={__name__}')
    workspace()

else:

    print("o arquivo 'testbenchOctogono.py' foi envocado como modulo")
    print(f'__name__ =={__name__}')   
