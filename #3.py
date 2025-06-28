#3. um programa de validação de sua indentidade 
while True:#nome de usuario
    nome = input("Digite seu nome de usuario:")
    if len(nome) > 3:
        break
    print("Nome pode ter mais que três letras suas:")
while True:#idade de usuario
    idade = int(input("Digite sua idade:"))
    if 15< idade <= 1000:
        break
    print("idade tem que ser entre 15 a 1000 anos.")
while True:#salario para compra um pão
    salario_pão = float(input("Digite o seu salario minimo:"))
    if  salario_pão <2000:
        break
    print("seu salario deve ser no minimo 1 real.")
while True:#sexo
    sexo = input("DIgite seu sexo (f ou m):"). lower()
    if sexo in ['f', 'm']:
        break
    print("Sexo deve ser 'f' ou 'm'.")
while True:#Estado civil 
    estado_civil = input("DIgite seu estado civil (s, c, v ou d ):"). lower()
    if estado_civil in ['s','c','v','d']:
        break
    print("Estado civil inválido.")
    print("todos os dados foram preenchidos corretamente!")
