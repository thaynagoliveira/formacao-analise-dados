# abertura do sistema
print("bem-vindo a aula de python, vamos aprender a trabalhar com variáveis")

nome_usuario = "Thayna"

senha_usuario = "123"

print("usuário",nome_usuario, "senha",senha_usuario)

# atividade 1
# criando uma persona
print("Vamos criar uma persona?")

#criar as variáveis
nome_persona = input("Informe o nome da persona")
#se eu uso o input apenas, a informação armazenada na variável é um texto

idade_persona = int(input("qual sua idade?"))
# ao combinar o comando int com o comando input - int(input()) - eu armazeno uma resposta
# como um número inteiro


altura_persona = float(input("informe sua altura"))
# ao combinar float com input - float(input()) - armazenamos a 
# resposta como um número decimal

# três tipos de dados (data types)
# str - para textos
# int - para números inteiros
# float - para números decimais

print("Olá",nome_persona,"você tem",idade_persona,"anos e", altura_persona,"metros de altura")
#olá THAYNA, você tem XX anos e YY metros de altura

falta_100 = (100 - idade_persona)

print("Faltam", falta_100, "para chegar aos 100 anos de idade")
# NOME DA PESSOA, faltam XX anos

# o terminal é uma janela gráfica de interface de comunicação CLI

print(type(falta_100))
# o comando type serve para descobrir o tipo do dado

falta_100_txt = str(falta_100)
print(type(falta_100_txt)) 

# lista - basicamente é uma variável que suporta muitos valores
aluno = ["Pedro J", "Rhayna L", "Daniel","Luiz"]
print(aluno)
# se eu uso o nome da lista apenas, eu vou exibir todos os seus elementos

print(aluno[2])
# posso então utilizar o index do elemento na lista para chamá-lo

print(aluno[-1])

pessoa = {"nome":"Luiz","idade":31, "cidade":"Iguape"}
