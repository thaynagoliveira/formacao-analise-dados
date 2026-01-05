# comando de repetir
# while == enquanto

idade = 17

while idade <18: 
    print("Você é menor de idade")
    # tática do incremento
    idade = idade + 1
    

pergunta = input("Digite Sim para sair")
# o símbolo != quer dizer diferente ou negar
while pergunta != "Sim":
    pergunta = input("Você digitou errado, digite mais uma vez")
    break
# o comando break faz o sistema parar também

# converter tudo para minúsculo

palavra = input("Digite uma palavra tudo em maiúsculo")

print(palavra.lower())
# o comando lower() deixa todo o conteúdo da variável minúsculo

palavra2 = input("Para finalizar o sistema digite sair ou finalizar")

while palavra2.lower() == "sair" or palavra2.lower() == "finalizar":
    print("sistema finalizado")
    

print("Você digitou errado, mas acabou o exemplo")


