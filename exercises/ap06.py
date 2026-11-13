




opçao = -1
while opçao != 0:
   
    print("1 admistração:")
    print("2  Companhia: ")
    print("3  Passageiros:")
    print("0  Sair:")

    opçao = (input("escolha uma opçao:"))
    if opçao.isnumeric():
       opçao = int(opçao)
    
    if opçao == 2:
        print("2  Companhia: ")
    elif opçao == 1:
        print("1 admistração:")
    elif opçao == 3:
        print("3  Passageiros:")
    
    if opçao==0:
        print(f'opçao {opçao} é valida')
    elif opçao==1:
        print(f'opçao {opçao} é valida')
    elif opçao==2:
        print(f'opçao {opçao} é valida')
    elif opçao==3:
        print(f'opçao {opçao} é valida')
    else:
        print(f'{opçao} não é valida')

