#28.
cds = int(input("Quantos CDs você tem?"))
total = 0
for i in range(cds):
    valor = float(input(f"Digite o valor do CD {i+1}"))
    total += valor
media = total / cds
print("Valor total investido: R$", round(total, 2))
print("Valor médio por CD: R$",round(media, 2))