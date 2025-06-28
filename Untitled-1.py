#1.um programa que pede para digitar entre 0 e 10.
while True: #Quando a nota pedir um numero entre 0 e 10, sera verdadeiro.
   try:
       nota = int(input( "Digite um numero entre 0 e 10:"))
       if 0 <= nota <= 10:
           print(f" nota correto:{nota}")
           break #sai do lop se for verdadeiro
       else:
           print("Erro!!!!! tente novamente.")
   except ValueError: 
        print("Erro!!!!!!.")