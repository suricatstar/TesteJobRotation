import json

with open('dados.json') as f:
    faturamento = json.load(f)

# lista com os valores diários de faturamento
valores_diarios = [dia['valor'] for dia in faturamento]

# calcula o menor valor de faturamento
menor_valor = min(valores_diarios)

# calcula o maior valor de faturamento
maior_valor = max(valores_diarios)

# filtra os dias com faturamento para calcular a média
dias_com_faturamento = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# calcula o número de dias com faturamento superior à média mensal
dias_acima_da_media = len([dia for dia in faturamento if dia['valor'] > media_mensal])

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")
