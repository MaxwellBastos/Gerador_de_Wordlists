import itertools

insr = input('Insira a string para gerar a wordlist: ')

resultado = itertools.permutations(insr, len(insr))

for i in resultado:
    print(''.join(i))