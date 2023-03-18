def fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return True
    else:
        return False


numero = int(input("Digite um número: "))
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
