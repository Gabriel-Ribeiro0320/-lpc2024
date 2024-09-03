fra = input("Escreve uma palavra ou frase: ")
fra = fra.lower()
fra = fra.replace(" ", "")
t = int(len(fra)) - 1
arf = ""

for c in range(t, -1, -1):
    arf += fra[c]

if fra == arf:
    print("A palavra/frase é um palíndromo")
else:
    print("A palavra/frase não é um palíndromo")