import random

lado = int(input("Quantos lados tem o dado?"))
ladosN = []
numeros = []

for i in range(lado):
    ladosN.append(i+1)

quant = int(input("Quantos dados você vai jogar?"))

for i in range(quant):
    numeros.append(random.choice(ladosN))

print(f'Os numeros sorteados foram ' , end='')
for i in range(quant):
    print(f'{numeros[i-1]} ', end='')

    