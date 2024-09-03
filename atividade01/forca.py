import random

caminho = input("Digite o caminho do arquivo: ")

with open(caminho, "r") as file:
    conteudo = file.read()

palavras = conteudo.splitlines()
palavra_aleatoria = random.choice(palavras)

chances = 6
palavra_oculta = ["_" for _ in palavra_aleatoria]
print(f'A palavra é {palavra_aleatoria}')
while "_" in palavra_oculta and chances > 0:
    print(f"Você tem {chances} chances")
    print("A palavra é:", " ".join(palavra_oculta))
    letra = input("Digite uma letra: ")

    if letra in palavra_aleatoria:
        for i, char in enumerate(palavra_aleatoria):
            if char == letra:
                palavra_oculta[i] = letra
    else:
        print(f"A letra {letra} não está na palavra.")
        chances -= 1

palavra_aleatoria = ''.join(palavra_aleatoria)
if "_" in palavra_oculta:
    print("Você não acertou :(")
    print(f"A palavra era {palavra_aleatoria}")
else:
    print(f"Parabéns! Você adivinhou a palavra: {palavra_aleatoria}")