from package.maths.terms import Dodecagono , Eneagono

def workspace():

    tamanho_lados_dodecagono = int(input('Digite o tam. dos lados do Dodecagono abaixo:'))
    cor_dodecagono = str(input('Digite a cor do Dodecagono e do Eneágono:'))
    tamanho_lados_eneagono = int(input('Digite o tam. dos lados do Eneágono abaixo:'))

    dodecagono = Dodecagono(tamanho_lados_dodecagono, cor_dodecagono)
    eneagono = Eneagono (tamanho_lados_eneagono, dodecagono)
    dodecagono.model()
    eneagono.model()

    print(f'O tamanho dos lados do dodecagono é de: {tamanho_lados_dodecagono}, o tamanho dos lados do eneágono é de: {tamanho_lados_eneagono} e a cor do decágono e do dodecágono é a cor: {eneagono.dodecagono.color}.')
    



if __name__ == "__main__":

    print("O arquivo 'testbenchassociacao.py' foi envocado como programa")
    print(f'_name_ =={__name__}')
    workspace()

else:

    print("o arquivo 'testbenchassociacao.py' foi envocado como modulo")
    print(f'__name__ =={__name__}')  
