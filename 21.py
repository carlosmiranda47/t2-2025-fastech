#21.
num = int(input("Digite um número:"))
divisores = 0
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1
if divisores == 2:
   print(f"{num} é um numero primo.")
else:
    print(f"{num} NÃO é um numero primo.")