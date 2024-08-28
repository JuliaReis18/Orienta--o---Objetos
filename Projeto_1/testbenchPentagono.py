from package.maths.terms import Pentagono

def workspace():
    tamanho_lado = int(input('Digite o tamanho do lado do pentagono:'))
    cor_pentagono = str(input('Digite a cor do pentagono:'))
    segmento_2 = Pentagono (tamanho_lado, cor_pentagono)
    segmento_2.model()
    print(f'area:{segmento_2.area()}')
    print(f'perímetro:{segmento_2.perimetro()}')
    print(f'cor:{segmento_2.cor()}')




if __name__ == "__main__":

    print("O arquivo 'testbenchPentagono.py' foi envocado como programa")
    print(f'_name_ =={__name__}')
    workspace()

else:

    print("o arquivo 'testbenchPentagono.py' foi envocado como modulo")
    print(f'__name__ =={__name__}')   


