import sys
sys.stdout.reconfigure(encoding="utf-8")
# comentario
'''
comentario de varias linguas
'''

nome = "pedro abrunhosa"
print("olá " + nome)

print(f"ola {nome} , \nbemvindo !")

# receber dados de utilizador
atividade = input(f"ola {nome},escreve o nome de uma disciplina:")

print(f"ola {nome} , \nbemvindo a {atividade}!")

print("nome é do tipo: " + type(nome).__name__)

