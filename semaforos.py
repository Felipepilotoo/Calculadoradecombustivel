import sys
semaforonum = None
houve_infracao = None
nivel_infracao = None
quanti_infracao = 0

semaforo = input('\nQual a cor do semáforo quando o veículo passou? ').lower()
velocidade = float(input('\nQual a velocidade do veículo? '))

if semaforo == 'vermelho': 
    houve_infracao = True
    print(f"\nHouve infração, por avançar o sinal")
    quanti_infracao += 1

elif semaforo == 'amarelo':
    houve_infracao = False

elif semaforo == 'verde':
    houve_infracao = False
else:
    print('\nEsta não é uma cor do semáforo, tente novamente com as 3 opções: vermelho, amarelo ou verde.')

if 66 < velocidade < 81:
    print('Infração grave por excesso de velocidade')
    quanti_infracao += 1
    print(f'{quanti_infracao} no total')
elif velocidade >= 81: 
    print('Infração gravíssima por excesso de velocidade')
    quanti_infracao += 2
    print(f'{quanti_infracao} no total')
else:
    print('OK')
    print(f'{quanti_infracao} Infrações')