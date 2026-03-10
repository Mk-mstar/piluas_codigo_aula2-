import datetime
#entrada
data_compra = (input ('Digite a data da compra (dd/mm/aaaa): '))
garantia = int(input ('Prazo de garantia: '))

#processamento
data_compra = datetime.datetime.strptime(data_compra, '%d/%m/%Y')
garantia = data_compra + datetime.timedelta(days = garantia * 30)

#saída
print(f'Garantia válida até {garantia.strftime('%d/%m/%Y')}')
print(f'Dia da semana {garantia.strftime('%A')}')