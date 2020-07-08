vastaus = int(input("Valitse numero: "))

def sieve(numero):
    alkuluku = [2]
    x = 3
    if numero < 2:
        return 0
    while x <= numero:
        for y in alkuluku:
            if x%y == 0:
                x += 2
                break
        else:
            alkuluku.append(x)
            x += 2
    print(alkuluku)
    for luku in alkuluku:
        print(luku)
sieve(vastaus)