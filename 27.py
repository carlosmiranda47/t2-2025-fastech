#27.
turmas = (int(input("Digite 2 o número de turmas:")))
total_alunos = 0
for i in range(turmas):
    while True:
        alunos = int(input(f"Digite a quantidade de alunos da turma{i + 1}:"))
        if alunos <=40:
            total_alunos += alunos
            break
        else:
            print("Uma turma não pode ter mais de 40 alunos!")
media = total_alunos /turmas
print("Media de alunos por turma:", media)