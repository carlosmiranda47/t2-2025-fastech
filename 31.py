#31.
while True:
    print("\nLojas tabajara")
    total = 0
    contador = 1
    while True:
        preço = float(input(f"produto {contador}: R$"))
        if preço == 0:
            break
        total += preço
        contador += 1
    print(f"Total:.2f")
    dinheiro = float(input("Dinheiro recebido: R$"))
    troco = dinheiro - total
    print(f"Troco: R$ {troco:.2f}")
    continuar = input("Deseja registrar outra compra? (s/n):").lower()
    if continuar != 'S':
        break