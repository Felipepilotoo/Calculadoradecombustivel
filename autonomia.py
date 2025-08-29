km_inicial = 0
km_percorrido = int(input('Quantos km o seu carro andou após abastecer? '))
litros_abastecidos = int(input('Quantos litros você abasteceu? '))

consumo = km_percorrido / litros_abastecidos

print(f'{consumo}Km/L')