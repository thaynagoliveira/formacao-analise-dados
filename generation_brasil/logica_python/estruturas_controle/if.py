# if é o comando "=SE do excel"
# ou seja, ele é o comando de condições

# verificar idade
idade = int(input("Qual a sua idade?"))

if idade >= 18:
    # indentação
    print("Você é maior de idade")
else:
    # o comando else quer dizer senão
    print("Você é menor de idade")


# prova de soft skills
# nota A - 9 ou 10
# nota B - 8 ou 7
# nota C - 6 ou 5
# nota D - 4 ou menor

nota1 = int(input("Qual a nota 1?"))
nota2 = int(input("Qual a nota 2?"))
nota3 = int(input("Qual a nota 3?"))

media = (nota1+nota2+nota3)/3

if media > 10: 
    print("Erro ao informar as notas")
elif media >= 9: 
    # o comando elif é utilizado quando temos mais do que duas respostas possíveis para um if
    print("Nota A")
elif media >= 7:
    print("Nota B") 
elif media >= 5: 
    print("Nota C")  
else: 
    print("Nota D") 
# cada símbolo de if representa pelo menos duas respostas

