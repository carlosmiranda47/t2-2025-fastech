#11.o mesmo so que altera a soma para mostra no final
num1 = int(input("Digite o primero número:"))
num2 = int(input("Digite o segundo número:"))
menor, maior = sorted([num1, num2])
soma = 0
for i in range(menor + 1, maior):
    print(i)
    soma += 1
    print("Soma dos números no intervalo:", soma)