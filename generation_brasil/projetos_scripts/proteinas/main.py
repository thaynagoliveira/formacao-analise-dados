from funcoes import * 

while True:
    menu()
    opcao = int(input("Escolha a opção"))

    if opcao == 1:
        menu_objetivo() 
        objetivo = int(input("Qual o seu objetivo?"))
        peso = float(input("Qual o seu peso(Kg)?"))

        resultado_proteinas = calc_proteinas(peso,objetivo) 
        print("Você precisa de", round(resultado_proteinas,2))
        # o comando round arredonda um número
        # ex.: 3,1415 - round(numero,2) = 3,14
    elif opcao == 2:
        peso = float(input("Qual o seu peso(Kg)?"))
        altura = float(input("Qual a sua altura em metros?"))

        resultado_imc = calc_imc(peso,altura)
        print("Seu IMC é", resultado_imc)
    else:
        print("Tchau")
        break
