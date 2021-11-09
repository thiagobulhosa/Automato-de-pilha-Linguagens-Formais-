def estadoAtual(regras):
    return regras[0]

def simboloAtual(regras):
    return regras[1]

def pilhaAtual(regras):
    return regras[2]

def estadoProx(regras):
    return regras[3]

def pilhaProx(regras):
    return regras[4]


cadeia = []
pilha = ['I']
regras = []
flag = 0
op = 0
existeRegra = 0

while (op != 3):
    print("1) Nova cadeia\n2) Nova regra\n3)Sair")
    op = int(input("Escolha uma opção:"))

    if (op == 1):
        if existeRegra == 1:
            entradaCadeia = input("Digite a cadeia:")
            for i in range(len(entradaCadeia)):
                cadeia.append(entradaCadeia[i])
            cadeia.append("_")

            print(pilha)
            for simbolo in cadeia:
                for i in range(nRegras):
                    if estado == estadoAtual(regras[i]):
                        if simbolo == simboloAtual(regras[i]) and simbolo != "_":
                            if pilha[-1] == pilhaAtual(regras[i]):

                                if pilhaProx(regras[i]) == "_":
                                    estado = estadoProx(regras[i])
                                    pilha.pop(-1)
                                    flag = 1
                                    break

                                else:
                                    if len(pilhaProx(regras[i])) == 1:
                                        estado = estadoProx(regras[i])
                                        pilha.pop(-1)
                                        pilha.append(pilhaProx(regras[i]))
                                        flag = 1
                                        break
                                    else:
                                        estado = estadoProx(regras[i])
                                        pilha.pop(-1)
                                        aux = list(reversed(pilhaProx(regras[i])))
                                        for j in range(len(aux)):
                                            pilha.append(aux[j])
                                        flag = 1
                                        break

                        elif simbolo == "_":
                            if pilha == []:
                                estado = estadoFinal
                                flag = 1
                                break
                            elif pilha[-1] == "I":
                                estado = estadoFinal
                                flag = 1
                                pilha.pop(-1)
                                break

                if (flag == 0):
                    print("A cadeia", entradaCadeia, "não é válida")
                    op = 0
                    pilha = ['I']
                    estado = estadoInicial
                    cadeia = []
                    break

                flag = 0
                print(pilha)

            if pilha == [] and estado == estadoFinal:
                pilha = ['I']
                estado = estadoInicial
                cadeia = []
                print("A cadeia", entradaCadeia, "é válida")

            op = 0

        else:
            print("Só é possível digitar uma cadeia após digitar as regras")
            op = 0

    elif (op == 2):
        regras = []
        estadoInicial= int(input("Digite o estado inicial:"))
        estadoFinal = int(input("Digite o estado final:"))
        estado= estadoInicial
        nRegras = int(input("Digite quantas regras serão usadas:"))
        for i in range(nRegras):
            print("Regra", i + 1, ":")
            regra = input()
            regra = regra.split(' ')
            regra[0] = int(regra[0])
            regra[3] = int(regra[3])
            regras.append(regra)

        existeRegra = 1
        print("As regras foram definidas com sucesso")
        op = 0