from random import randint

resultados = {}

for c in range(100):
    resultados[c] = randint(1, 6)

r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0

for c in range(100):
    if resultados[c] == 1:
        r1 += 1
    if resultados[c] == 2:
        r2 += 1
    if resultados[c] == 3:
        r3 += 1
    if resultados[c] == 4:
        r4 += 1
    if resultados[c] == 5:
        r5 += 1
    if resultados[c] == 6:
        r6 += 1

print(f"1  = {r1} vezes")
print(f"2  = {r2} vezes")
print(f"3  = {r3} vezes")
print(f"4  = {r4} vezes")
print(f"5  = {r5} vezes")
print(f"6  = {r6} vezes")