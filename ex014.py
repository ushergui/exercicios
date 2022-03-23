#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = int(input('Digite a largura da parede em metros: '))
comprimento = int(input('Digite o comprimento da parede em metros: '))
area = largura * comprimento
pintura = area/2
print('Sua parede tem a dimensão de {} metros X {} metros e área total de {} metros quadrados'.format(largura, comprimento, area))
print('Para pintar a parede você vai precisar de {:.2f} litros de tinta.'.format(pintura))
