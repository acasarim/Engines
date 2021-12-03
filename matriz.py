#-*- coding: utf-8
'''
    (int, int, valor) -> matriz (lista de listas)
    Cria e retorna uma matriz com n_linhas linha e n_colunas
    colunas em que cada elemento é igual ao valor dado.
'''
class Matriz:
    def __init__(self, n_colunas, n_linhas, valor):
        self.n_colunas = n_colunas
        self.n_linhas = n_linhas
        self.valor = valor
        print('MATRIZ')

    def criar_matriz(self):
        matriz = [] #Lista vazia
        for i in range (int(self.n_linhas)):
            #cria a linha \/ 'i'
            linha = [] #lista vazia
            for j in range (int(self.n_colunas)):
                print(self.valor, end=' ') #O valor é que vai receber os valores e armazenar na matriz
                #cria coluna -> 'j'
                linha.append(self.valor)
            print('')
            #coloque linha na matriz
            matriz.append(linha)
        return matriz

n_colunas = int(input('Quantas colunas deseja? '))
n_linhas = int(input('Quantas linhas deseja? '))
valor = int(input('Qual valo deseja atribuir? '))
aMatriz = Matriz(n_colunas, n_linhas, valor)
aMatriz.criar_matriz()
