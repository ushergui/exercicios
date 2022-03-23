#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por
# dia e R$0,15 por Km rodado.

kms = float(input('Quantos kilômetros o carro percorreu durante o aluguel? '))
dias = float(input('Quantos dias o carro ficou alugado? '))
km = kms * 0.15
dia = dias * 60
tot=km+dia
print('O carro ficou alugado por {} dias, percorreu {} km, o valor das diárias será de R${} e dos km percorridos de R${}. '
      'Total a pagar: R${}'.format(dias,kms,dia,km,tot))