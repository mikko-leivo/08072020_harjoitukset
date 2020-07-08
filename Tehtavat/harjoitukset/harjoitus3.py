def filereaderapp(text, text1):
    import os
    try:
        #jos tiedosto on tyhjä, palauta "File is empty"
        if os.stat(text).st_size == 0:
            return 'File is empty'
        else:
        #avaa tiedosto ja listaa rivit
            f = open(text, "r")
            sana_lista = f.readlines()
            f.close()
        #avaa uusi tiedosto
        uusi_tiedosto = open(text1, 'w+')
        #sorttaa rivit
        uusi_lista = sorted(sana_lista, key=lambda x: (len(x), x))
        for sana in uusi_lista:
        #kirjoita jokainen rivi yksitellen uuteen tiedostoon
            uusi_tiedosto.write(sana)
            uusi_tiedosto.write("\n")
    except FileNotFoundError:
        return "No such file!"

#funktion käynnistys
if __name__ == '__main__':
    filereaderapp("jotain.txt")