from funcoes import * 
# * = all = tudo 

def menu():
    print('Gen - Calc')
    print('1 - somar')
    print('2 - subtrair')
    print('3 - multiplicar')
    print('4 - dividir')
    print('5 - potência')
    print('6 - raiz')
    print('Qualquer outro digito - sair')

# vou criar a função principal de TODO sistema
if __name__ == "__main__":
# O if__name__ == "__main__": garante que o código só rode quando você executar o main.py
    menu()
    opcao = input("Escolha uma opção")

    num1 = float(input("Digite o número 1"))
    num2 = float(input("Digite o número 2"))

    if opcao == "1":
        print(soma(num1,num2))
    elif opcao == "2":
        print(subtracao(num1,num2))
    elif opcao == "3":
        print(multiplicacao(num1,num2))
    elif opcao == "4":
        print(divisao(num1,num2))
    elif opcao == "5":
        print(potencia(num1,num2))
    elif opcao == "6":
        print(raiz(num1, num2))
    else:
        print('Tchau')
