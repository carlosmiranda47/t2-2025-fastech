#35.
n = int(input("Mostrar primos até:"))
print("Numeros primos:")
for num in range(2, n + 1):
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num, end="")