from package.maths.terms import Triangulos, Angulos

def workspace():
    trianguloequilatero = Triangulos('equilatero', 'azul')
    trianguloequilatero.quantos_angulos(3)

    trianguloisosceles = Triangulos('isosceles', 'verde')
    trianguloisosceles.quantos_angulos(3)

    trianguloretangulo = Triangulos('retangulo', 'rosa')
    trianguloretangulo.quantos_angulos(3)


    trianguloisosceles.quantos_angulos_all()
    trianguloequilatero.quantos_angulos_all()
    trianguloretangulo.quantos_angulos_all()



if __name__ == "__main__":

    print("O arquivo 'testbenchOctogono.py' foi envocado como programa")
    print(f'_name_ =={__name__}')
    workspace()

else:

    print("o arquivo 'testbenchOctogono.py' foi envocado como modulo")
    print(f'__name__ =={__name__}')   