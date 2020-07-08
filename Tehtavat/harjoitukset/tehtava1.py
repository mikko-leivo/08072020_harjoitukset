def tehtava1():
    import statistics
    numerot = input('Syötä pötkö numeroita: ')
    lista = []
    for num in numerot:
        numa = int(num)
        lista.append(numa)
    pienin = min(lista)
    suurin = max(lista)
    moodi = statistics.mode(lista)
    keskiarvo = statistics.mean(lista)
    mediaani = statistics.median(lista)

    print(f'Listan pienin numero on {pienin}.\nListan suurin numero on {suurin}.\nListan moodi on {moodi}.\nListan keskiarvo on {keskiarvo}.\nListan mediaani on {mediaani}.')

    # statistics.mode(set)
tehtava1()