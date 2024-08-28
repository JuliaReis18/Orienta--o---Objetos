
import math

class Ponto():

    def __init__(self, coordenada = None):
        self.coordenada = coordenada

    def coord_dos_pontos(self):
        x = int(input("Digite a coordenada de x: "))
        y = int(input("Digite a coordenada de y: "))
        self.coordenada = (x, y)
        return self.coordenada

    def coordenadas_dos_pontos(self):
        return self.coordenada

    def coordenada_x(self):
        return self.coordenada[0] if self.coordenada else None

    def coordenada_y(self):
        return self.coordenada[1] if self.coordenada else None
    
    def model(self):
        print(f'Os parametros do meu modelo de ponto são: minha coordenada x ={self.coordenada_x()}, e minha coordenada y={self.coordenada_y()}')

    def identif(self):
        return 'Ponto'
    
    def calcular_distancia(ponto1, ponto2):
        return math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
    
    def ponto_proximo_segmento(ponto, segmento, tolerancia):
        x1, y1 = segmento[0]
        x2, y2 = segmento[1]
        px, py = ponto
        
        vx, vy = x2 - x1, y2 - y1
        wx, wy = px - x1, py - y1
        
        func = (wx * vx + wy * vy) / (vx * vx + vy * vy)
        
        if func < 0:
            dist = Ponto.calcular_distancia(ponto, (x1, y1))

        elif func > 1:
            dist = Ponto.calcular_distancia(ponto, (x2, y2))
            
        else:
            funcx = x1 + func * vx
            funcy = y1 + func * vy
            dist = Ponto.calcular_distancia(ponto, (funcx, funcy))

        return dist <= tolerancia
    

    


    
class Reta():
    def __init__(self,a,b): 

        self.a = a
        self.b = b


    def interpolar(self,x):

        y = self.a * x + self.b
        return y



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
    
    def identif(self):
        return 'Círculo'
    
    def model(self):
        print(f'Os parametros do meu modelo de cídrculo são: meu raio ={self.r}, e minhas duas coordenadas são são x={self.x} e y={self.y} . ')

    


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
        return cor
    

    



class Quadrado(Quadrilatero):
    pass

    def model(self):
        print(f'Os parametros do meu modelo de quadrado são: altura={self.altura}, base={self.base} e cor={self.color}.')

    def identif(self):
        return 'Quadrado'

class Retangulo(Quadrilatero):
    pass
    
    def model(self):
        print(f'Os parametros do meu modelo de retangulo são: altura={self.altura} , base={self.base} e cor={self.color}.')

    def identif(self):
        return 'Retangulo'
    


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

    def identif(self):
        return 'Hexágono' 


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

class Formas():
    def __init__(self):
        self.forma = {}
        self.contar = 0

    def adicionar(self, instancia):
        self.contar += 1
        self.forma[self.contar] = instancia

    def remover(self, numero):
        if numero in self.forma:
            del self.forma[numero]
            return True 
        else:
            return False 
        
    def lista(self):
        if not self.forma:
            print('Voce ainda não criou formas geométricas.')
        else:
             for numero, form in self.forma.items():
                 print(f'{numero}: {form.identif()}')

    def retornar(self,numero):
        return self.forma.get(numero, None)
                 
        

     

class Inferencia():
    def ponto_no_circulo(ponto_x,ponto_y,centro_y, centro_x, raio):
        distancia = math.sqrt((ponto_x - centro_x)**2 + (ponto_y - centro_y)**2)
        return distancia <= raio
    



    def ponto_no_retangulo(ponto_x_r, ponto_y_r ,  x_inferior_esquerdo, y_inferior_esquerdo, largura, altura):
    # Verifica se o ponto está dentro dos limites do retângulo
        return (x_inferior_esquerdo <= ponto_x_r <= x_inferior_esquerdo + largura) and (y_inferior_esquerdo <= ponto_y_r <= y_inferior_esquerdo + altura)
    
    def ponto_no_quadrado(ponto_x_q, ponto_y_q,  x_superior_esquerdo, y_superior_esquerdo, lado_quadrado):
        return x_superior_esquerdo <= ponto_x_q <= x_superior_esquerdo + lado_quadrado and y_superior_esquerdo <= ponto_y_q <= y_superior_esquerdo + lado_quadrado
           


    def calcular_distancia(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    
    
    

