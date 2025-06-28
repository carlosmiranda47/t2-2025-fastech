#4.progama de calculo da população A utrapase outra população b.
população_A = 80000
população_B = 200000
anos = 0
while população_A <= população_B:
    população_A *= 1.03 # crecera para 3%
    população_B *= 1.015 # crecera para 1,5%
    anos += 1
print(f"vai levar {anos} anos para a população do país A utrapassara ou igualar com o país B.")