#7.um programa que ve qual é dos numeros maior informando o numero.
maior = None
num = int(input("Digite um numero:"))
for i in range(5):
    num = float(input(f"Digite o{i+1}°número:"))
    if maior is None or num > maior:
        maior = num 
print("O maior número é:",maior)
   