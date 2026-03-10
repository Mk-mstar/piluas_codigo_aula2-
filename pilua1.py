import math
#entrada
assinantes = int(input('Digite a quantidade de assinantes atuais:'))
mensalidade = float(input('Digite o valor da mensalidade: '))
taxa = float(input('Digite a taxa de crescimento mensal %: '))/100
meses = int(input('Digite a quantidade de meses da projeção: '))

#processamento
assinantes_finais = assinantes * math.pow((1 + taxa), meses) 
receita_final = assinantes_finais * mensalidade
             
#saída 
print(f'Assinantes projetados: {assinantes_finais:.0f}') 
print(f'Receita estimada: R$ {receita_final:.2f}') 
