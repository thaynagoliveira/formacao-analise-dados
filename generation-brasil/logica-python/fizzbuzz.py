# autora: Thayna G Oliveira
# projeto: FizzBuzz
# versão: v1
# descrição: o FizzBuzz é um exercício que imprime números de 1 a 100. Sempre que o número é múltiplo de 3, ele imprime "Fizz". Sempre que é múltiplo de 5, ele imprime "Buzz". E se for múltiplo de 3 e 5, ele imprime "FizzBuzz"

numero = 1
numero_fim = int(input("Até que número gostaria de ir?"))

# caso usando while
while numero <= 100:
    if numero % 3 == 0:
        if numero % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else: 
        print(numero)
    numero = numero + 1 
print("")
print("")
print("\n\n ----- Fim ----")


# ---- FizzBuzz usando FOR 

# Para cada elemento entre 1 e 100
for i in range(1,101):
    # se o resto da divisão de i por 3 for zero E o resto da divisão de i por 5 também for zero, faça
    if i % 3 == 0 and i % 5 == 0: 
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# ------ informe de um número ------

fizzbuzz = int(input("Informe um número"))

if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print("FizzBuzz")
elif fizzbuzz % 3 == 0:
    print("Fizz")
elif fizzbuzz % 5 == 0:
    print("Buzz")
else:
    print(fizzbuzz)
    






        


    
