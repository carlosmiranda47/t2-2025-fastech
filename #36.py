#36.
numero = int(input("Montar a tabuada de:"))
inicio = int(input("Começar por:"))
fim = int(input("Terminar em:"))
if fim < inicio:
    print("Erro: o final não pode ser menor que o início.")
else:
    print(f"\nTabuada de {numero}, de {inicio} até {fim}:")
    for i in range(inicio, fim + 1):
        print(f"{numero} x {i} = {numero * i}")