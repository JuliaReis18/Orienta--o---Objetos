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

    def _init_(self, r, x, y):
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


class Ponto():
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x
    
    def gety(self):
        return self.y
        

    def distancia(self):
        a = (self.x*2 + self.y*2)
        import math
        distancia = math.sqrt(a)
        return distancia
    
    def model(self):
        print(f'Os parametros do meu ponto são as coordenadas x={self.x} e y={self.y}.')







     

