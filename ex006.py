t = input('Digite algo: ')

print("O tipo primitivo deste valor é: ",type(t))
print("Só tem espaços? ", t.isspace())
print("É um número? ", t.isnumeric())
print("É alfanumérico? ", t.isalnum())
print("Está em maiúsculas? ", t.isupper())
print("Está em minúsculas? ", t.islower())
print("Está capitalizada? ", t.istitle())
