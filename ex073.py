times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitéria', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'os cinco times em primeiros são {times[0:5]}')
print('----------------------------------------------------------------------------------')
print(f'os últimos quatros colocados são {times[-4:]}')
print('----------------------------------------------------------------------------------')
print(f'os times em ordem alfabética {sorted(times)}')
print('----------------------------------------------------------------------------------')
posicao = times.index('Chapecoense')
print(f'o Chapecoence esta em {posicao + 1}º')