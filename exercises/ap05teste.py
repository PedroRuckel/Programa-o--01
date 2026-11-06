import random , math
lmin,lmax = 1,1000
numbertoguess = random.randint(lmin,lmax)  

# guess = input(f"adivinha o numero entre {lmin} e {lmax}: -->")

# print(f'valor inserido: {guess}, do tipo ({type(guess).__name__})')
# print(f'{guess.isnumeric()} ;{guess.isdecimal()}')
guess = ""
attempt = 0
tentativas = []

while (guess != numbertoguess and guess != 'end'):
    guess = input(f"adivinha o numero entre {lmin} e {lmax}: -->")
    guess = guess.strip()

    print(f'valor inserido: {guess}')
    try:
        guess = int(guess)
        if (guess > numbertoguess):
             print("mais baixo")
        elif (guess < numbertoguess):
             print("mais alto")
        else:
             print("acertou")   
        attempt += 1
        tentativas.append(guess) #adiciona a ultima tentativaao fim da linha
        
    except Exception as ex:
        print(f'O valor "{guess}" não é um número válido: {type(ex).__name__}: {ex}')
    finally:
        print("erro desconhecido")
# fim do while


    
        
if (guess == 'end'):
        print(f'desitiu ao fim de {attempt} tentativas')
else:
    print(f'acertou no numero {numbertoguess} em {attempt} tentativas')
    print(tentativas)
for tentativa in tentativas:
        print(tentativa)

