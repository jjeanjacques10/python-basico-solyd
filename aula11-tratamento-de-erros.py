import time

def abre_arquivo():
    try:
        arquivo = open('arquivoido.txt')
        return True
    except Exception as erro:
        print("Aconteceu algum erro: ", erro)
        return False

while not abre_arquivo():
    print('Tentando abri o arquivo')
    time.sleep(5)
print("consegui abrir o arquivo")