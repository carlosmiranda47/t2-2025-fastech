#20.
while True:
    num = int(input("Digite um número de 0 a 15 para ver o fatorial ( ou número negativo para sair)"))
    if num < 0:
        print("Programa encerrado.")
        break
    elif num > 15:
        print("numero muito grande! tente um menor meu chapa.")
        continue
    fatorial = 1  
    for i in range(1, num + 1):
        fatorial *= i
    print(f"{num}! = { fatorial}")