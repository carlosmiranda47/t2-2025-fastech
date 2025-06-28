#19.
n = int (input("Quantos números você vai digitar?"))
numeros = []
for i in range(n):
    while True:
        num = float(input(f"Digite o {i + 1}° número (entre 0 e 1000):"))
        if 0 <= num <= 1000:
            numeros.append(num)
            break
        else:
            print("Números fora do intervalo! tente de novo.")
print("Menor número:", min(numeros))
print("Menor número:", max(numeros))
print("Soma dos número:", sum(numeros))