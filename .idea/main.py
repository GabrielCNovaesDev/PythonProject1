

txt = input("Digite uma mensagem para ser codificada:")
desloc = int(input("Digite o deslocamento:"))
textinholegal = txt.lower()
listaDeLetras = "abcdefghijklmnopqrstuvwxyz"
#listaDeLetras = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")


def cifrar_mensagem(mensagem,deslocamento):
    mensagem_cifrada = []

    for letra in mensagem:
        indexCorrespondente = int(listaDeLetras.index(letra)) + deslocamento
        if indexCorrespondente >= 26:
            resto = indexCorrespondente % len(listaDeLetras)
            #print(listaDeLetras[resto], end="")
            mensagem_cifrada.append(listaDeLetras[resto])
        else:
            #print(listaDeLetras[indexCorrespondente], end="")
            mensagem_cifrada.append(listaDeLetras[indexCorrespondente])

    for letra in mensagem_cifrada:
        texto = "".join(mensagem_cifrada)

    return texto


def decifrar_mensagem(mensagem, deslocamento):

    for letra in mensagem:
        indexCorrespondente = int(listaDeLetras.index(letra)) - deslocamento
        if indexCorrespondente >= 26:
            resto = indexCorrespondente % len(listaDeLetras)
            print(listaDeLetras[resto], end="")
        else:
            print(listaDeLetras[indexCorrespondente], end="")



decifrar_mensagem(mensagemCifrada, desloc)







