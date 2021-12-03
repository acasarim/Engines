'''
Engine de sequência ASCII
FOR na pratica
'''
class Pattern:
    '''
    class com intuito de organizar OOP na pratica
    '''
    
    def __init__(self, n):
    '''
    método construtor recebe quantas "n" linhas vai imprimir
    a partir do número 65 da tabela ASCII
    '''
        self.n = n
    
    def sequency(self):
    '''
    engine funcional da operação
    primeiro for recebe a variavel n de linhas
    segundo for faz a captura do número estabelecido da tabela ASCII
    e imprimi a partir dela a sequência fornecida + 1 a cada linha
    '''
            num = 65
            for i in range(0, self.n):
                print("\r")
                for j in range(0, i+1):
                    ch = chr(num)
                    print(ch, end=" ")
                num = num + 1
                
    def mensagem_inicio(self):
    '''
    mensagem de entrada
    '''
        print("Bem vindo a apresentação de ASCII")

operacao1 = Pattern(0)
resposta = int(0)
num_sequency = 0
operacao1.mensagem_inicio()
num_sequency = int(input("\rQuantas sequências deseja inserir de ASCII? "))

while resposta == int(0):
    operacao1 = Pattern(num_sequency)
    operacao1.sequency()
    resposta = input("\rEscreva quit para encerrar: ")
    num_sequency = int(input("\rQuantas sequências deseja inserir de ASCII? "))
    if resposta == "quit":
        break
    else:
        resposta = int(0)
