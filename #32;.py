#32.
num = int(input("Fatorial de:"))
fatorial = 1
conta = ""
for i in range(num, 0, -1):
    fatorial *= i
    conta += f"{i}."if i != 1 else f"{i}"
print(f"{num}! = {conta} = {fatorial}")