#trabalho de PCEA

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 15, 19, 55, 66, 67, 69, 70, 80, 90, 200, 300, 350, 460, 500, 501, 700,]
    alvo = int (input ("digite o valor do numero para busca "))
    resultado = busca_binaria(lista, alvo)

    if resultado != -1:
        print(f"Elemento encontrado no índice {resultado}.")
    else:
        print("Elemento não encontrado.")
