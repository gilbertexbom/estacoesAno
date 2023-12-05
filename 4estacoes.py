# Sistema de informação para retornar a estação do ano

# Apresentação
print('\n\t\t\t -- Estações do Ano --\n')

# Entradas
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))

# Processamento e saída
if mes in(1, 2, 3):
    if(mes == 3 and dia >= 20):
        print('Outono')
    else:
        print('Verão')
elif mes in(4, 5, 6):
    if(mes == 6 and dia >= 21):
        print('Inverno')
    else:
        print('Outono')
elif mes in(7, 8, 9):
    if(mes == 9 and dia >= 23):
        print('Primavera')
    else:
        print('Inverno')
elif mes in(10, 11, 12):
    if(mes == 12 and dia >= 22):
        print('Verão')
    else:
        print('Primavera')
else:
    print(f'Mês {mes} incorreto!')
