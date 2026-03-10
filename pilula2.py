import random
#entrada
cotacao = float(input('Digite a cotação atual do dólar:  '))
variacao = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao * (1 + variacao)   

#saída 
print(f'Variação simulado: {variacao:.3%}')
print(f'Nova cotação: {nova_cotacao:.2f} ')



