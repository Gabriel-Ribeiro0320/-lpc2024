from validate_docbr import CPF

cpf = input("Digite seu CPF: ")

if CPF(cpf):
    print("O CPF informado é válido!")
else:
    print("O CPF informado é inválido")
