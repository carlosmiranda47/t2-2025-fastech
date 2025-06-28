#10.um programa que gera numeros inteiros aparti de dois numeros inteiros
num1 = int(input("Digite o primero número:"))
num2 = int(input("Digite o segundo número:"))
#Garante que começa do menor o maior
if num1 < num2:
    inicio =num1 + 1
    fim = num2
else:
    inicio = num2 + 1
    fim = num1
for i in range(inicio, fim):
    print(i)