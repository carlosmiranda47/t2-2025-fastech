#8.um programa que leia 5 números e informe a media da soma dos números
soma = 0
for i in range(5):
    num = float(input(f"Digite 0{i+1}°número"))
    soma += num
media = soma / 5
print("soma:",soma)
print("Média", media)