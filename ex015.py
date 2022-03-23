#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual o valor do produto? R$'))
comdesconto = (preco* 5/100)
final = preco-comdesconto

print('O valor do desconto de 5% é R${:.2f}'.format(comdesconto))
print('O valor do produto com desconto de 5% é R${:.2f}'.format(final))
