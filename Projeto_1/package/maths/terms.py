class Reta():


    def __init__(self,a,b): 

        self.a = a
        self.b = b


    def interpolar(self,x):

        y = self.a * x + self.b
        return y

    
    def model(self):

        print(f'Os parâmertros do meu modelo de reta são: a={self.a}, b={self.b}')


class Circle():

    def __init__(self, r, x, y):
        self.r = r 
        self.x = x
        self.y = y

    def circunferencia(self):
        circunferencia = 2 * 3.14  * self.r
        return circunferencia 
    
    def area(self):
        area = 3.14 * pow(self.r, 2)
        return area
    
    def diametro(self):
        diametro = self.r * 2
        return diametro
    
    def model(self):
        print(f'Os parametros do meu modelo de círculo são: meu raio ={self.r}, e meus dois pontos são x={self.x} e y={self.y} . ')


class Quadrilatero():
    def __init__(self, base, altura, color):
        self.base = base 
        self.altura = altura 
        self.color = color

    def area(self):
        area = self.base * self.altura
        return area
    
    def perimetro(self):
        perimetro = ((self.base) * 2)+((self.altura)*2)
        return perimetro
    
    def cor(self):
        cor = self.color
    



class Quadrado(Quadrilatero):
    pass

    def model(self):
        print(f'Os parametros do meu modelo de quadrado são: altura={self.altura}, base={self.base} e cor={self.color}.')


class Retangulo(Quadrilatero):
    pass
    
    def model(self):
        print(f'Os parametros do meu modelo de retangulo são: altura={self.altura} , base={self.base} e cor={self.color}.')



class Hexagono():
    
    def __init__(self, lado, color):
        self.lado = lado
        self.color = color

    def area(self):
        import math
        area = ((6 *(self.lado * self.lado * math.sqrt(3))) / 4)
        return area 
    
    def perimetro(self):
        perimetro = 6 * self.lado
        return perimetro    

    def cor(self):
        cor = self.color
        return cor
    
    def model(self):
        print(f'Os parametros do meu modelo de hexágono são: lado={self.lado} e cor={self.color}.')


class Pentagono():

    def __init__(self, lado, color):
        self.lado = lado
        self.color = color

    def area(self):
        import math
        area = ((5 *(self.lado * self.lado * math.sqrt(3))) / 4)
        return area 
    
    def perimetro(self):
        perimetro = 5 * self.lado
        return perimetro
    
    def cor(self):
        cor = self.color
        return cor
    
    def model(self):
        print(f'Os parametros do meu modelo de pentágono são: lado={self.lado} e cor={self.color}.')


class Octogono():

    def __init__(self, lado, color):
        self.lado = lado
        self.color = color

    def area(self):
        import math
        area = ((9 *(self.lado * self.lado * math.sqrt(3))) / 4)
        return area 
    
    def perimetro(self):
        perimetro = 8 * self.lado
        return perimetro
    
    def cor(self):
        cor = self.color
        return cor
    
    def model(self):
        print(f'Os parametros do meu modelo de octogono são: lado={self.lado} e cor={self.color}.')




    

class Dodecagono():
    def __init__(self, t_lado, color):
        self.t_lado = t_lado
        self.color = color 

    
    def model(self):
        print(f'Os parametros do meu modelo de Dodecágono são: lado={self.t_lado} e cor={self.color}. ')

class Eneagono():
    def __init__(self, lado , dodecagono):
        self.lado = lado
        self.dodecagono = dodecagono

        

    def model(self):
        print(f'Os parâmetros do meu modelo de Eneágono são: lado={self.lado} e cor do octógono={self.dodecagono.color}.')





class Triangulos():
    def __init__ (self, nome, cor):
        self.nome = nome 
        self.cor = cor 
        self.angulos = []

    def quantos_angulos(self, lados):
        self.angulos.append(Angulos(lados))

    def quantos_angulos_all(self):
        for angulos in self.angulos:
            print(f'Este triangulo possui {angulos.lados} angulos.')

class Angulos():
        def __init__(self, lados):
            self.lados = lados 









 






     

