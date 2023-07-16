def reverte(palavra):
    novaPalavra = ""
    for i in range(len(palavra) - 1, -1, -1):
        novaPalavra += palavra[i]
    return novaPalavra


palavra = str(input("Digite uma palavra: "))
arvalap = reverte(palavra)
print(f"A string original é: {palavra}")
print(f"A string invertida fica: {arvalap}")
