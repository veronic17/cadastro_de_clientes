# Lista pra armazenar os cadastros
pessoas = []

while True:
    print("\nCadastro de pessoa")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade onde nasceu: ")

# Adicionando a pessoa como dicionário na lista
    pessoa = {"nome": nome, "Idade": idade, "Cidade": cidade}
    pessoas.append(pessoa)

# Perguntar se quer continuar
    continuar = input("Deseja cadastrar outra pessoa? (s/n):").strip().lower()
    if continuar != "s":
        break

# Exibindo os cadastros
print("\nPessoas cadastradas")
for i, pessoas in enumerate(pessoas, start=1):
    print(f"{i}. Nome: {pessoa['nome']}, Idade: {pessoa['Idade']}, Cidade: {pessoa['Cidade']}")
    