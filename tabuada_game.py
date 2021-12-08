from random import randint

class Tabuada:

    def mensagem_inicio(self):
        print('=====================================')
        print('= Bem vindo a tabuada school cAsper =')
        print('=====================================')

    def tabuada_nvl_1(self):
        n1 = (randint(1,10))
        n2 = (randint(1,10))
        print("Tabuada do 1 ao 10 ")
        print("{} x {} = ".format(n1, n2))
        resp = int(input())
        if resp == n1 * n2:
            print("Correto")
        else:
            print("Errado")

obj_tabuada = Tabuada()
obj_tabuada.mensagem_inicio()
nvl1 = 1
while nvl1 <= 10:
    obj_tabuada.tabuada_nvl_1()
    print(nvl1)
    nvl1 = nvl1 + 1
