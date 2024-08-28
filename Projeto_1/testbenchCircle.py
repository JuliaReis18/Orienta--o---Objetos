from package.maths.terms import Circle

def workspace():

    segmento_2 = Circle(3, 7, 5)
    segmento_2.model()     #nome da variável.metodo()  ------ a sua variavel esta chamando a funçao
    print(f'circunferencia: {segmento_2.circunferencia()}')
    print(f'area: {segmento_2.area()}')
    print(f'diametro: {segmento_2.diametro()}')



if __name__ == "__main__":

    print("O arquivo 'testbenchCircle.py' foi envocado como programa")
    print(f'_name_ =={__name__}')
    workspace()

else:

    print("o arquivo 'testbenchCircle.py' foi envocado como modulo")
    print(f'__name__ =={__name__}')
