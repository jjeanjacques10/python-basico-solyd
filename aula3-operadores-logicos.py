idade = int(input("Digite sua idade: "))
peso = int(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

if(idade < 18):
    print("O candidato é menor de idade")
else:
    if(peso >= 60):
        if(altura > 1.70):
            print("Está apto a entrar no exercito")
        else:
            print("Tem que crescer mais!")
    else:
        print("Não tem peso o suficiente")