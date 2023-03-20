faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

valor_total = sum(faturamento_mensal.values())

percentual_estados = {}
for estado, valor in faturamento_mensal.items():
    percentual_estados[estado] = (valor / valor_total) * 100

for estado, percentual in percentual_estados.items():
    print(f'{estado}: {percentual:.2f}%')
