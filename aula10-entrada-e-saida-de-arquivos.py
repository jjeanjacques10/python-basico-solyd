#abertura do arquivo w = write r = read a = add

arquivo = open('arquivo.txt','a')

for i in range(1,2000):
    arquivo.write("{}Eai pessoal, aqui e o Jean\n".format(i))
