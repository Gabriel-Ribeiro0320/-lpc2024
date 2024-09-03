from num2words import num2words

numero = int(input("Informe um número: "))
extenso = num2words(numero, lang="pt")
print(extenso)