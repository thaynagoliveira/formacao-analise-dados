# quais são os operadores matemáticos da informática?
# soma +
# subtração - 
# multiplicação *
# divisão / 
# para mostrar o resto da divisão %

# criar o jogo do par ou ímpar usando if
# REGRAS
# PERGUNTAR AO USUÁRIO DOIS NÚMEROS
# SOMAR ESSES DOIS NÚMEROS
# APLICAR OPERAÇÃO % PARA DESCOBRIR O RESTO
# SE O RESTO FOR 0 É PAR
# SENÃO, É ÍMPAR

numero1 = int(input("Qual o número 1?"))
numero2 = int(input("Qual o número 2?"))

soma = numero1 + numero2

resto = soma % 2

if resto == 0:
    print("Número par")
else: 
    print("Número ímpar")
    


