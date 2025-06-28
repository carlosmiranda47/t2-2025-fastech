#18.
n = int (input("Quantos números você vai digitar?"))
numeros =[]
for i in range(n):
    num = float(input(f"Digite o {i + 1}° número:"))
    numeros.append(num)
print("Menor número:", min(numeros))
print("Maior número:", max(numeros))
print("Soma dos número:", sum(numeros))