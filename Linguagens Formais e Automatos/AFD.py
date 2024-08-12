# Automatos Finitos Deterministicos

estados = []
while True:
    estado = input('Digite os estados: ').strip()
    if estado == '':
        break
    estados.append(estado)

alfabeto = []
while True:
    simbolo = input('Digite os alfabetos: ').strip()
    if simbolo == '':
        break
    alfabeto.append(simbolo)

transicoes = {}
for estado in estados:
    transicao_temporaria = {}
    for simbolo in alfabeto:
        transicao_atual = input(f'({estado}, {simbolo}) => ').strip()
        transicao_temporaria[simbolo] = transicao_atual
    transicoes[estado] = transicao_temporaria

estado_inicial = input('Digite o estado inicial: ').strip()

estados_finais = []
while True:
    estado_final = input('Digite os estados finais: ').strip()
    if estado_final == '':
        break
    estados_finais.append(estado_final)

while True:
    estado_atual = estado_inicial
    palavra = input('Digite a palavra: ').strip()

    if palavra == '':
        break

    for simbolo in palavra:
        estado_atual = transicoes[estado_atual][simbolo]
    
    if estado_atual in estados_finais:
        print('Palavra aceita')
    else:
        print('Palavra rejeitada')