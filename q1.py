
numero = int(input("Informe um número: "))


fibonacci = [0, 1]


while True:
    prox_numero = fibonacci[-1] + fibonacci[-2]
    if prox_numero > numero:
        break
    fibonacci.append(prox_numero)


if numero in fibonacci:
    print(f"O número {numero} pertence a sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence a sequência de Fibonacci.")
