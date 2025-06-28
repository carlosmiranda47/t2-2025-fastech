#22.
num = int(input("Digite um  número:"))
divisor = []
for i in range(1, num + 1):
    if num % i == 0:
        divisor. append(i)
if len(divisor) == 2:
    print(f"{num} é primo.")
else:
    print(f"{num} NÂO é primo.")
    print("Divisor:", divisor)