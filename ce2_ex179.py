def raiz(n, chute):

#Definindo próximo caso da recursividade
    proximo = (chute + (n/chute))/2

#Checando a diferença de n e chute**2 nos dois casos

#Caso 1: onde n >= chute**2
    if n >= chute**2:
        if n - chute**2 <= 10**(-12):
            return chute
        else:
            return raiz(n, proximo)

#Caso 2: onde n < chute**2
    if n < chute**2:
        if chute**2 - n <= 10**(-12):
            return chute
        else:
            return raiz(n, proximo)

#Definindo a função main
def main():
    n = int(input("Indique um número inteiro: "))
    chute = 1
    resposta = raiz(n, chute)
    print("A raiz de {} é {:.2f} \n OBS: Resposta aproximada com 2 casas decimais.".format(n, resposta))

main()

