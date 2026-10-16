print ("como se chama")
objetivo = input("nome:")
print("o meu nome é:", objetivo)

print ("diz me um numero")
objetivo = int(input("numero:"))
print ("escreve um numero no ecra:" , objetivo)

import random 
lmin,lmax = 1,100
numbertoguess = random.randint(lmin,lmax)

guess = ""
while (guess != numbertoguess and guess != 'end'):
    guess = input(f"adivinha o numero entre {lmin} e {lmax}:-->")

print(f'valor inserido: {guess}')
if (guess.isnumeric()):
  guess = int(guess)
  print(f"numero inserido: {guess}")
  if (guess> numbertoguess):
      print("mais baixo")
  elif (guess < numbertoguess):
      print("mais alto")
  else:
        print("acertou")
   
    
else:
    print(f"{guess} não é um numero inteiro")

print(f"acabou, o numero a adivinhar era {numbertoguess}")

