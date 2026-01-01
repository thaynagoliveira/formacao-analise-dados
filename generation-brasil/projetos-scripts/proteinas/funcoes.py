def menu():
    print("Bem-vindo ao protein-cal-gen")
    print("Escolha uma opção")
    print("1 - calcular proteínas")
    print("2 - calcular IMC")
    print("Qualquer outro número - sair")

# -- função para saber o objetivo do usuário 
def menu_objetivo():
    print("Qual sua meta?")
    print("1 - Perder peso")
    print("2 - Manter peso")
    print("3 - Ganhar peso")

def calc_proteinas(peso, objetivo):
    if objetivo == 1:
        return peso * 2
    elif objetivo == 2:
        return peso * 1.6
    elif objetivo == 3:
        return peso * 1.8
    else:
        return None
    # o comando None é para não fazer nada

def calc_imc(peso, altura):
    return peso / (altura**2)

def imc(valor_imc):
    if valor_imc < 18.5:
        return "Abaixo do peso"
    elif valor_imc < 24.9:
        return "Peso normal"
    elif valor_imc < 29.9:
        return "Sobrepeso"
    else: 
        return "Obesidade"
