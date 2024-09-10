
string = input("Digite uma string: ")


lowercase_string = string.lower()


quantidade = lowercase_string.count('a')


if quantidade > 0:
    print(f"A letra 'a' ocorre {quantidade} vezes na string.")
else:
    print("A letra 'a' não foi encontrada na string.")
