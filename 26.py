#26.
votos1 = votos2 = votos3 = 0
eleitores = int(input("Digite o número total de eleitores:"))
for i in range(eleitores):
    voto = int(input(f"Eleitor {i+1}, vote no candidato 1, 2 ou 3:"))
    if voto == 1:
        votos += 1
    elif voto == 2:
        votos2 += 1
    elif voto == 3:
        votos3 += 1
    else:
        print("Voto inválido!")
print("Resultado da eleição")
print("candidato 1:", votos1, "votos")
print("candidato 2:", votos2, "votos")
print("candidato 3:", votos3, "votos")