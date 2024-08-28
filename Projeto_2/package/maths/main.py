

def criar_forma_geometrica(self):
    if self.forma() == 'circulo':
        return int(input('Você escolheu criar um Círculo, forma geométrica disponível. Digite o raio e os dois pontos do seu círculo respectivamente'))
    elif self.forma() == 'quadrado':
        return 'Você escolheu criar um Quadrado, forma geométrica disponível.'
    elif self.forma() == 'retangulo':
        return 'Você escolheu criar um Retângulo, forma geométrica disponível.'
    else:
        return 'OPS! Esta forma geométrica não está disponível. Tente novamente.'

def Circle():

    def __init__(self, r, x, y):
        self.r = r 
        self.x = x
        self.y = y
    
    def area_circle(self):
        area_circle = 3.14 * pow(self.r, 2)

def Quadrado():

    def __init__(self, base, altura):
        self.base = base 
        self.altura = altura 

    def area_quadrado(self):
        area_quadrado = self.base * self.altura

def Retangulo():

    def __init__(self, base, altura):
        self.base = base 
        self.altura = altura 

    def area_retangulo(self):
        area_retangulo = self.base * self.altura 




