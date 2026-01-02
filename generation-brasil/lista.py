# uma lista é uma "variável" que suporta muitos dados

frutas = []
# quando eu coloco a lista apenas com [], eu estou dizendo que ela é vazia

print(frutas)

# o usuário pode add valor a lista
# pode excluir a lista
# ver a lista
# sair da lista

print('----- Bem-vindo(a) ao Varejão Gen -----')
print('Suas opções são:')
print('1 - add fruta')
print('2 - excluir fruta')
print('3 - ver lista')
print ('4 - sair')

escolha = int(input('Qual a opção desejada?'))
if escolha < 1 or escolha > 4:
    print('Escolha não reconhecida, finalizando o sistema')
else: 
    while escolha >= 1 or escolha <= 4:
        # caso 1 - add
        if escolha == 1:
            nova_fruta = input('Qual fruta deseja adicionar?')
            # para adicionar um elemento na lista, eu devo chamar a lista e dar o atributo append, anexando assim, o novo valor
            frutas.append(nova_fruta)
            print('Fruta', frutas[-1],'adicionada')
            escolha = int(input('Qual a opção desejada?'))
        # caso 2 - excluir 
        elif escolha == 2:
            for posicao, cada_fruta in enumerate(frutas, start=1):
                print(posicao, " - ",cada_fruta)
            print('Agora você pode excluir um produto')
            posicao_fruta = int(input('Digite a posição da fruta'))
            frutas.pop(posicao_fruta - 1)
            # o comando pop é para excluir um item da lista baseado em sua posição
            print('Fruta excluída com sucesso')
            escolha = int(input('Qual a opção desejada?'))
        
        # caso 3 - ver lista
        elif escolha == 3:
            for nome_frutas in frutas:
                print(nome_frutas) 
            escolha = int(input('Qual a opção desejada?'))
        # caso 4 - sair
        elif escolha == 4:
            print('Finalizado')
            break




