# class Calculadora:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2

#     def adicao(self):
#       return self.num1+self.num2
    
#     def subtrair(self):
#       return self.num1-self.num2

      
#     def multiplicar(self):
#       return self.num1.self.num2

    
#     def divisao(self):
#       return self.num1/self.num2

# try:
#     num1=int(input('informe um numero'))
    
#     num2=int(input('informe um numero'))

#     result=Calculadora(num1,num2)
    
#     print(result.divisao())
# except (ValueError, IndexError):
#     print("Erro: Entrada inválida ou índice fora dos limites.")
    
# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida.")

# except Exception as e: # esse "as e" serve para capturar o erro e jogar na variavel e
#     print("Erro desconhecido:", str(e))
    



try:
    
    import random
    x = random.randint(1,52)
    print(x)

    num1=int(input('Advinhe o numero'))
    while num1!=x:
        num1=int(input('Advinhe o numero'))

        if num1<x:
            print('O numero é maior que',num1)
        elif num1>x:
            print('O numero é menor que',num1)
        elif num1==x:
            print('Parabens!!O numero é ',num1)   

except (ValueError, IndexError):
    print("Erro: Entrada inválida ou índice fora dos limites.")
    
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

except Exception as e: # esse "as e" serve para capturar o erro e jogar na variavel e
    print("Erro desconhecido:", str(e))
    

