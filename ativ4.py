tam = 50
lista = []

menu = {
    1:'Adicionar um número',
    2:'Remover um número',
    3:'Exibir o vetor completo',
    4:'Encontrar e exibir o maior e o menor número',
    5:'Calcular e exibir a soma de todos os números',
    6:'Sair',
}

while True:
    print(f"+{'-'*tam}+")
    print(f"|{'MENU':^{tam}}|")
    print(f"+{'-'*tam}+")
    for n, op in menu.items():
        print(f"|{f'{n} - {op}':{tam}}|")
    print(f"+{'-'*tam}+")

    try:
        dig = int(input('Escolha uma opção: '))
    except ValueError:
        print('ERRO! Digite uma opção válida!')
        continue

    match dig:
        case 1:
            try: 
                adic = int(input('Digite o número para adicionar: '))
                lista.append(adic)
                print(f'Numero {adic} adicionado com sucesso!')
            except ValueError:
                print('ERRO! Digite um numero válido!')

        case 2:
            if not lista:
                print('Lista vazia. Não há numeros para remover.')
                continue
            try:
                rem = int(input('Digite o número para remover: '))
                if rem in lista:
                    lista.remove(rem)
                    print(f'Numero {rem} removido com sucesso!')
                else:
                    print(f'O numero {rem} não está na lista.')
            except ValueError:
                print('ERRO! Digite um numero válido!')
                
        case 3:
            if not lista:
                print('Lista vazia.')
                continue
            print(f'O vetor completo é: {lista}')

        case 4:
            if not lista:
                print('Lista vazia.')
                continue
            print(f'O maior numero do vetor é: {max(lista)}')
            print(f'O menor numero do vetor é: {min(lista)}')
                
        case 5:
            if not lista:
                print('Lista vazia.')
                continue
            print(f'A soma do vetor é: {sum(lista)}')

        case 6:
            print('Encerrado')
            break

        case _:
            print('Opção inválida. Digite um número de 1 a 6.')
