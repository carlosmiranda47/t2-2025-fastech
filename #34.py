#34.
num = int(input("Digite um número:"))
numero_primo = True
if num <= 1:
    numero_primo = False
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            numero_primo = False
            break
print(f"{num} e´primo." if numero_primo else f"{num} NÂO é primo.")