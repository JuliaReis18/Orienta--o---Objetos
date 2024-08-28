
from package.maths.main import criar_forma_geometrica


def workspace():
   
   input_usuario = str(input("Digite a forma geométrica que você deseja criar: "))
   resultado = criar_forma_geometrica(input_usuario)
   print(resultado)





if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'_name_ =={__name__}')
    workspace()
else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ =={__name__}')