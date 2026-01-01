# as portas lógicas são divididas em 3 portas principais
# porta NOT - negar alguma informação (não)
# porta do OR - porta para condição (ou)
# porta do AND - porta de condição (e)

#exemplos

a = True
b = False

# seja a variável a ou b quaisquer a gente pode ter vários resultados
print("Not A:", not a)
# em alguns momentos eu posso usar o operardor != para falar que é diferente

# porta or
print("a ou b:", a or b)

# porta and
print("a e b", a and b)

# ------- exemplo de como usar AND ----------

idade = 16
carteira = False

# enquanto for menor de idade e não tiver carteira o sistema pergunta
# se eu fiz aniversário e se eu tirei a carteira
# quando eu tiver idade + carteira ele fala que eu posso dirigir

while idade < 18 or carteira == False:
    pergunta_aniversario = input("Você já fez aniversário?")
    if pergunta_aniversario.lower() == "sim":
        idade = idade + 1
        print("Parabéns, então você tem", idade)
    pergunta_carteira = input("Você tirou carta?")
    if pergunta_carteira.lower() == "sim":
        carteira = True

print("Pode dirigir")



