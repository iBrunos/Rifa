
from statistics import mode 
from random import randint
#Gerando numeros aleatórios

numerosp0 = [(randint(1, 100)) for i in range(10)]
numerosp1 = [(randint(1, 100)) for i in range(10)]
numerosp2 = [(randint(1, 100)) for i in range(10)]
numerosp3 = [(randint(1, 100)) for i in range(10)]
numerosp4 = [(randint(1, 100)) for i in range(10)]
numerosp5 = [(randint(1, 100)) for i in range(10)]
numerosp6 = [(randint(1, 100)) for i in range(10)]
numerosp7 = [(randint(1, 100)) for i in range(10)]
numerosp8 = [(randint(1, 100)) for i in range(10)]
numerosp9 = [(randint(1, 100)) for i in range(10)]

verificador = numerosp0 + numerosp1 + numerosp2 + numerosp3 + numerosp4 + numerosp5 + numerosp6 + numerosp7 + numerosp8 + numerosp9

#Dicionario que informa os participantes da rifa
participantes = {
        'pessoa0': ['bruno', 'bruno@outlook.com'], #Definindo pessoa 0
        'pessoa1': ['vanessa', 'vanessa@outlook.com'], #Definindo pessoa 1
        'pessoa2': ['bruna', 'bruna@outlook.com'], #Definindo pessoa 2
        'pessoa3': ['debora', 'debora@outlook.com'], #Definindo pessoa 3
        'pessoa4': ['felipe', 'felipe@outlook.com'], #Definindo pessoa 4
        'pessoa5': ['gustavo', 'gustavo@outlook.com'], #Definindo pessoa 5
        'pessoa6': ['jose', 'jose@outlook.com'], #Definindo pessoa 6
        'pessoa7': ['amanda', 'amanda@outlook.com'], #Definindo pessoa 7
        'pessoa8': ['breno', 'breno@outlook.com'], #Definindo pessoa 8
        'pessoa9': ['carlos', 'carlos@outlook.com'] #Definindo pessoa 9
                }
#Função que imprime os vencedores da rifa
def imprimiVencedor(n_sorteado):
    #Verificando se o numero que o participante tem, foi o ganhador
    if n_sorteado in numerosp0:
        print("Vencedor: ")
        print(participantes['pessoa0']) #Verificando pessoa 0 e imprimindo se ela é um vencedor
   
    if n_sorteado in numerosp1:
        print("Vencedor: ")
        print(participantes['pessoa1']) #Verificando pessoa 1 e imprimindo se ela é um vencedor
    
    if n_sorteado in numerosp2:
        print("Vencedor: ")
        print(participantes['pessoa2'])#Verificando pessoa 2 e imprimindo se ela é um vencedor
    
    if n_sorteado in numerosp3:
        print("Vencedor: ")
        print(participantes['pessoa3']) #Verificando pessoa 3 e imprimindo se ela é um vencedor
    
    if n_sorteado in numerosp4:
        print("Vencedor: ")
        print(participantes['pessoa4']) #Verificando pessoa 4 e imprimindo se ela é um vencedor

    if n_sorteado in numerosp5:
        print("Vencedor: ")
        print(participantes['pessoa5']) #Verificando pessoa 5 e imprimindo se ela é um vencedor

    if n_sorteado in numerosp6:
        print("Vencedor: ")
        print(participantes['pessoa6']) #Verificando pessoa 6 e imprimindo se ela é um vencedor

    if n_sorteado in numerosp7:
        print("Vencedor: ")
        print(participantes['pessoa7']) #Verificando pessoa 7 e imprimindo se ela é um vencedor

    if n_sorteado in numerosp8:
        print("Vencedor: ")
        print(participantes['pessoa8']) #Verificando pessoa 8 e imprimindo se ela é um vencedor
    
    if n_sorteado in numerosp9:
        print("Vencedor: ")
        print(participantes['pessoa9']) #Verificando pessoa 9 e imprimindo se ela é um vencedor

    #Logica para verificar qual é numero mais escolhido da rifa
  
def frequencia(verificador): 
    return(mode(verificador))  
  
    #Main com o menu da rifa
def main():
    print("Bem vindo ao sorteio da rifa do BRUNÃO")
    n_sorteado = int(input("Qual foi o numero sorteado?> "))
    imprimiVencedor(n_sorteado)
    print("Numero mais comprado pelos participantes:") 
    print(frequencia(verificador))
main()
