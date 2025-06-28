#5.um programa que o usuario deve digitar os valores dos paises A e B
while True:
    população_A = int(input("População do país A:"))
    população_B = int(input("População do país B:"))
    taxa_A = float(input("Digite a taxa de cresimento de A(em %):")) / 100
    taxa_b = float(input("Digite a taxa de cresimento de B (em %)")) / 100
    if população_A > 0 and população_B and taxa_A > 0 and  taxa_b > 0:
        break
    print("Todos esses valores deveram ser maior que zero.")
anos =0
while população_A <= população_B:
    população_A *= (1 + taxa_A)
    população_B *= (1 + taxa_b)
    anos += 1
print(f"vai levar {anos} anos para a população do país A utrapassara ou igualar com o país B.")