volta = int(input())
clima = input()
dificul = input()
tipo_pneu = input()
durabilidade = 0

if tipo_pneu == 'duro':
    durabilidade = 90
if tipo_pneu == 'médio':
    durabilidade = 70
if tipo_pneu == 'macio' or tipo_pneu == 'chuva':
    durabilidade = 50




if tipo_pneu == 'chuva' and clima == 'sol':
    mult_voltas = volta * 15
    durabilidade -= mult_voltas
elif tipo_pneu == 'duro' and clima == 'chuva':
    mult_voltas = volta * 15
    durabilidade -= mult_voltas
elif tipo_pneu == 'médio' and clima == 'chuva':
    mult_voltas = volta * 15
    durabilidade -= mult_voltas
elif tipo_pneu == 'macio' and clima == 'chuva':
    mult_voltas = volta * 15
    durabilidade -= mult_voltas

if clima == 'sol':
    if dificul == 'baixa' or dificul == 'média':
        if tipo_pneu == 'macio':
            mult_volta1 = volta * 2
            durabilidade -= mult_volta1
        elif tipo_pneu == 'médio':
            mult_volta1 = volta * 2
            durabilidade -= mult_volta1
    elif dificul == 'alta':
        if tipo_pneu == 'macio':
            mult_volta1 = volta * 3
            durabilidade -= mult_volta1
        elif tipo_pneu == 'duro':
            durabilidade -= volta
else: 
    if dificul == 'baixa' and tipo_pneu == 'chuva':
        durabilidade -= volta 
    elif dificul == 'média' and tipo_pneu == 'chuva':
        mult_volta2 = volta * 2
        durabilidade -= mult_volta2
    elif dificul == 'alta' and tipo_pneu == 'chuva':
        mult_volta2 = volta * 3 
        durabilidade -= mult_volta2
# add new version
if durabilidade < 0:
    print("ferrou")
if durabilidade >= 20:
    print(f'A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {durabilidade}.')
else:
    print(f'Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {durabilidade} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.')




