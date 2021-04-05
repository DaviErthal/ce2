def romano(s):

#Caso base:
    if s == "":
        return 0

#Próximo termo da recursividade
    proximo = s[0: len(s)-1]

#Fazendo os testes com cada algorismo romano: I, V, X, L, C, D, M
    if s[-1] == "I":
        return 1 + romano(proximo)


    if s[-1] == "V":
        if s[len(s)-1] in "I":
            #Caso o número a esquerda seja menor que o da direita se subtrai o da direita.
            return 5 + romano(proximo) - 2*romano(s[-2])
        else:
            return 5 + romano(proximo)

    if s[-1] == "X":
        if s[len(s)-1] in "VI":
            return 10 + romano(proximo) - 2*romano(s[-2])
        else:
            return 10 + romano(proximo)

    if s[-1] == "L":
        if s[len(s) - 1] in "XVI":
            return 50 + romano(proximo) - 2*romano(s[-2])
        else:
            return 50 + romano(proximo)

    if s[-1] == "C":
        if s[len(s) - 1] in "LXVI":
            return 100 + romano(proximo) - 2*romano(s[-2])
        else:
            return 100 + romano(proximo)

    if s[-1] == "D":
        if s[len(s) - 1] in "CLXVI":
            return 500 + romano(proximo) - 2*romano(s[-2])
        else:
            return 500 + romano(proximo)
    if s[-1] == "M":
        return 1000 + romano(proximo)

#Definindo a função main
def main():
    r = input("Digite um número em algorismos romanos: ").upper()
    n = romano(r)
    print("Esse número romano corresponde ao número {}".format(n))


#Chamando a função main
main()
