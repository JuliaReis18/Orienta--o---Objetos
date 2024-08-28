from package.maths.terms import *

def workspace():
    formas = Formas()

    while(True):
        print('\nOlá! Aqui voce poderá obter informações personalizadas de diversas figuras geométricas. Siga os passos abaixo:')
        print('\nAs opções de formas geométricas disponíveis estão enumeradas a seguir.\n')
        print('1 - Círculo ') 
        print('2 - Quadrado')
        print('3 - Retangulo')
        print('4 - Hexagono')
        print('5 - Listar as figuras geométricas já criadas')
        print('6 - Remover forma geométrica criada da lista.')
        print('7 - Verificar se um ponto pertence ao domínio restrito de uma forma geométrica')
        print('8 - Obter a distancia entre 2 ou mais pontos')
        print('9 - Verificação se um ponto está nas proximidades de uma reta dada uma tolerancia')
        print('10 - SAIR DO PROGRAMA')
    

        selecione = int(input('Digite a opção escolhida:'))

            
        if selecione == 1: #Circulo
            x = int(input('Digite o valor da coordenada x:'))
            y = int(input('Digite o valor da coordenada y:'))
            raio = int(input('Digite o valor do raio:'))
            resultado = Circle(raio, x, y)
            resultado.model()     
            print('Aqui estão as informações da sua forma geométrica escolhida.')
            print(f'circunferencia: {resultado.circunferencia()}')
            print(f'area: {resultado.area()}')
            print(f'diametro: {resultado.diametro()}')
            print('\n[SEU CÍRCULO FOI CRIADO COM SUCESSO E ARMAZENADO NA LISTA.]')
            formas.adicionar(resultado)
            

        elif selecione == 2: #Quadrado
            base = int(input('Digite o valor da base do quadrado:'))
            altura = int(input('Digite o valor da altura do quadrado:'))
            cor = str(input('Digite a cor do quadrado:'))
            resultado = Quadrado(base, altura, cor)
            print('Aqui estão as informações da sua forma geométrica escolhida.')
            resultado.model() 
            print(f'área: {resultado.area()}')
            print(f'perímetro: {resultado.perimetro()}')
            print(f'cor: {resultado.cor()}')
            formas.adicionar(resultado)
            

        elif selecione == 3: #Retangulo
            base = int(input('Digite o valor da base do retangulo:'))
            altura = int(input('Digite o valor da altura do retangulo:'))
            cor = str(input('Digite a cor do retangulo:'))
            resultado = Retangulo(base, altura, cor)
            resultado.model() 
            print('Aqui estão as informações da sua forma geométrica escolhida.')
            print(f'área: {resultado.area()}')
            print(f'perímetro: {resultado.perimetro()}')
            print(f'cor: {resultado.cor()}')
            formas.adicionar(resultado)
             

        elif selecione == 4: #Hexagono
            lado = int(input('Digite o valor do lado do seu hexágono:'))
            cor = str(input('Digite a cor do seu hexágono:'))
            resultado = Hexagono(lado, cor)
            resultado.model()
            print('Aqui estão as informações da sua forma geométrica escolhida.')
            print(f'área: {resultado.area()}')
            print(f'perímetro: {resultado.perimetro()}')
            print(f'cor: {resultado.cor()}')
            formas.adicionar(resultado)
            

        elif selecione == 5: #Lista 
            formas.lista()
            print('\n')
            
            
        elif selecione == 6: #Remover figura da lista 
            formas.lista()
            numero = int(input("Insira o numero da forma geométrica que você queira apagar: "))
            if formas.remover(numero):
                print(f'\nForma {numero} removida!!! \n')
            else:
                print(f'\nA forma geométrica com o numero {numero} não existe, ou ainda não foi criada.\n')
            

        elif selecione == 7: #Verificar se pertence a um dom
            print('\nOlá! Aqui voce poderá verificar se um ponto pertence ao domínio restrito de uma forma geométrica.')
            print('\nAs opções de formas geométricas disponíveis para esta função estão enumeradas a seguir.\n')
            print('1 - Círculo ') 
            print('2 - Quadrado')
            print('3 - Retangulo')
            print('4 - Voltar ao menu inicial.')

            opcao = int(input('\nDigite a opção escolhida:'))


            if opcao == 1:
                ponto_x = int(input('Digite a cordenada do ponto x: '))
                ponto_y = int(input('Digite a coordenada do ponto y: '))
                centro_y = int(input('Digite o centro y do círculo: '))
                centro_x = int(input('Digite o centro x do círculo: '))
                raio = int(input('Digite o raio do círculo: '))
                if Inferencia.ponto_no_circulo(ponto_x, ponto_y, centro_y, centro_x, raio):
                    print(f"O ponto ({ponto_x}, {ponto_y}) está dentro do círculo.")
                else:
                    print(f"O ponto ({ponto_x}, {ponto_y}) está fora do círculo.")


            elif opcao == 2:
                ponto_x_q = int(input("Digite a coordenada x do ponto: "))
                ponto_y_q = int(input("Digite a coordenada y do ponto: "))
                x_superior_esquerdo = int(input("Digite a coordenada x do canto superior esquerdo do quadrado: "))
                y_superior_esquerdo = int(input("Digite a coordenada y do canto superior esquerdo do quadrado: "))
                lado_quadrado = int(input("Digite o tamanho do lado do quadrado: "))
                
                if Inferencia.ponto_no_quadrado(ponto_x_q, ponto_y_q,  x_superior_esquerdo, y_superior_esquerdo, lado_quadrado):
                    print(f"O ponto ({ponto_x_q}, {ponto_y_q}) está dentro do quadrado.")
                else:
                    print(f"O ponto ({ponto_x_q}, {ponto_y_q}) não está dentro do quadrado.")
                
            
            elif opcao == 3:
                ponto_x_r = int(input('Digite a coordenada x do ponto: '))
                ponto_y_r = int(input('Digite a coordenada y do ponto : '))
                x_inferior_esquerdo = int(input('Digite o ponto x do canto inferior esquerdo do retangulo: '))
                y_inferior_esquerdo = int(input('Digite o ponto y do canto inferior esquerdo do retangulo:  '))
                largura = int(input("Digite a largura do retângulo: "))
                altura = int(input("Digite a altura do retângulo: "))
                if Inferencia.ponto_no_retangulo(ponto_x_r, ponto_y_r ,  x_inferior_esquerdo, y_inferior_esquerdo , largura, altura):
                    print(f"O ponto ({ponto_x_r}, {ponto_y_r}) está dentro do retângulo.")
                else:
                    print(f"O ponto ({ponto_x_r}, {ponto_y_r}) está fora do retângulo.")


            elif opcao == 4:
                print('Voltando para o menu inicial...')
                

            else:
                print("Opção inválida. Tente novamente.")


        elif selecione == 8: #Dist entre pontos 
            print("Nesta opção, calcularemos a distância entre pontos")
            num_pontos = int(input("Digite o número de pontos (mín 2): "))
            
            if num_pontos < 2:
                print("O número de pontos não pode ser menor que 2.")
                return
            
            pontos = []
            for i in range(num_pontos):
                x = int(input(f"Digite a coordenada x do ponto {i+1}: "))
                y = int(input(f"Digite a coordenada y do ponto {i+1}: "))
                pontos.append((x, y))
                
                
            for i in range(num_pontos):
                for j in range(i + 1, num_pontos):
                    distancia = Ponto.calcular_distancia(pontos[i], pontos[j])
                    print(f"Distância entre o ponto {i+1} e o ponto {j+1} é de: {distancia:.2f}")


        elif selecione == 9: #Verificar se o ponto está nas prox. da reta 
            x1 = int(input("Digite a coordenada x do ponto inicial da reta: "))
            y1 = int(input("Digite a coordenada y do ponto inicial da reta: "))
            x2 = int(input("Digite a coordenada x do ponto final da reta: "))
            y2 = int(input("Digite a coordenada y do ponto final da reta: "))
            
            segmento = [(x1, y1), (x2, y2)]
        
            px = int(input("Digite a coordenada x do ponto: "))
            py = int(input("Digite a coordenada y do ponto: "))
            ponto = (px, py)
            
            tolerancia = int(input("Digite a tolerância para considerar o ponto próximo ao segmento: "))
            if Ponto.ponto_proximo_segmento(ponto, segmento, tolerancia):
                print(f"O ponto {px,py} está dentro das proximidades da reta.")
            else:
                print(f"O ponto {px,py} está fora das proximidades da reta.")


        elif selecione == 10: #SAIR 
            print('Puxa! Já está de saída? Volte logo, até mais.')
            break

        

        else:
            print('Esta opção não existe. Volte ao menu inicial e tente novamente!')
            










if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')




    





