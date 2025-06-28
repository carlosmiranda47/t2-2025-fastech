#23.
n = int(input("Digite um número:"))
total_divisoes = 0 
print(f"Números primos entre 1 e {n}:")
for num in  range(2, n + 1):
 numero_primo = True
 for i in range(2, num): 
  total_divisoes += 1
  if num % i == 0:
     numero_primo = False
     break
 if numero_primo:
   print(num, end="")
print("\nTotsl de divisões feitas:", total_divisoes)
  