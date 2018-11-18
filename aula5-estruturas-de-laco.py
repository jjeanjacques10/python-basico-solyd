nomes = []
for i in range(5):
    nomes.append(input("Digite o nome: "))

print("\n  Lista de convidados \n")

for i in range(5):
    print("Convidado número {}: {} ".format((i+1),nomes[i]))
