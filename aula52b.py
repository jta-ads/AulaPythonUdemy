hora = input('Que Horas São? ')

try:
    hora = int(hora)
    bom_dia = hora >= 0 and hora <= 11
    boa_tarde = hora >= 12 and hora <= 17
    boa_noite = hora >= 18 and hora <= 23

    if bom_dia:
        print(f'Bom dia são {hora}h')
    if boa_tarde:
        print(f'Boa tarde são {hora}h')
    if boa_noite:
        print(f'Boa noite são {hora}h')
except:
    print('Digito Inválido!')