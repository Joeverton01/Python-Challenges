
print('GERADOR DE PA')
print('-=' * 10)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos_mostrados = 0
total_termos = 0

# Mostra os 10 primeiros termos
while termos_mostrados < 10:
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao
    termos_mostrados += 1
    total_termos += 1

print('PAUSA')

# Loop para termos adicionais
while True:
    opcao = int(input('Quantos termos você quer mostrar a mais? (0 para sair) '))

    if opcao == 0:
        break

    termos_mostrados = 0
    while termos_mostrados < opcao:
        print(primeiro_termo, end=' -> ')
        primeiro_termo += razao
        termos_mostrados += 1
        total_termos += 1

    print('PAUSA')

print('FIM')
print(f'Progressão finalizada com {total_termos} termos mostrados.')


'''def gerador_pa():
    print('GERADOR DE PA')
    print('-=' * 10)
    
    # Validação de entrada
    try:
        primeiro_termo = int(input('Primeiro termo: '))
        razao = int(input('Razão: '))
    except ValueError:
        print('Por favor, digite valores numéricos válidos.')
        return
    
    termos_mostrados = 0
    total_termos = 0
    termos_por_vez = 10  # Quantidade inicial de termos a mostrar
    
    while True:
        # Mostra os termos
        for _ in range(termos_por_vez):
            print(primeiro_termo, end=' -> ')
            primeiro_termo += razao
            termos_mostrados += 1
            total_termos += 1
        
        print('PAUSA')
        
        # Pergunta por mais termos
        try:
            termos_por_vez = int(input('Quantos termos você quer mostrar a mais? (0 para sair) '))
        except ValueError:
            print('Por favor, digite um número válido.')
            termos_por_vez = 0
        
        if termos_por_vez == 0:
            break
    
    print('FIM')
    print(f'Progressão finalizada com {total_termos} termos mostrados.')

if __name__ == '__main__':
    gerador_pa()
'''
