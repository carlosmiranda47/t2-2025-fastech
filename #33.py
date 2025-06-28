#33.
temperaturas = []
while True:
    temp = input("Digite uma temperatura (ou 'fim'para  encerrar):").strip().lower()
    if temp == "fim":
        break
    try:
       temperatura = (float(temp))
       temperaturas.append(temperatura)
    except ValueError:
     print("por favor, digite um número válido ou 'fim para sair.")
if temperaturas:
    print("\nMenor temperatura:", min (temperaturas))
    print("\nMaior temperatura:", max (temperaturas))
    print("\nMedia temperatura:", round(sum (temperaturas) / len(temperaturas), 2))
else:
    print("Nenhuma temperatura foi informada.")