import numpy as np


jogada = np.array([['   ','   ','   '],['   ','   ','   '], ['   ','   ','   ']])
jogador= int(1)
vencedor = None
jogadaP = ['', '']
posição = ['linha', 'coluna']

simbolo = None

print("Quem começa é o X")

while True:

    print('\n\n\n')



    print(f' 1   2   3')
    print(f'1{jogada[0,0]}|{jogada[0,1]}|{jogada[0,2]}')
    print(f' -----------')
    print(f'2{jogada[1,0]}|{jogada[1,1]}|{jogada[1,2]}')
    print(f' -----------')
    print(f'3{jogada[2,0]}|{jogada[2,1]}|{jogada[2,2]}')

    i = int(input(f'Me informe a {posição[0]}:'))
    j = int(input(f'Me informe a {posição[1]}:'))

            
    if jogada[i-1, j-1] == '   ':
        if jogador == 1:
            jogada[i-1, j-1] = ' X '
            simbolo = ' X '
        else:
            jogada[i-1, j-1] = ' O ' 
            simbolo = ' O '
    else:
        print("Essa jogada é inválida")
        continue



    for i in range(3):
            if all(jogada[i,j] == simbolo for j in range(3)):
                vencedor = simbolo.strip()


    for j in range(3):
            if all(jogada[i,j] == simbolo for i in range(3)):
              vencedor = simbolo.strip()


    if all(jogada[i,i] == simbolo for i in range(3)):
            vencedor = simbolo.strip()


    if all(jogada[i, 2 - i] == simbolo for i in range(3)):
            vencedor = simbolo.strip()

    
    if '   ' not in jogada:
        print('Empate')
        break
    
    if vencedor:
        print(f"O vencedor foi {vencedor}")
        break

    if jogador == 1:
        jogador = 2
    else:
        jogador = 1

        
















