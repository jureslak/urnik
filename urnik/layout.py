def nastavi_barve(srecanja, barve):
    for srecanje in srecanja:
        srecanje.barve = set()
        if barve:
            for i, barva in enumerate(barve):
                if barva in (set(srecanje.ucitelji.all()) | {srecanje.ucilnica, srecanje.predmet} | (set(srecanje.predmet.letniki.all()) if srecanje.predmet else set()) | (set(srecanje.predmet.slusatelji.all()) if srecanje.predmet else set())):
                    srecanje.barve.add(i)

def razdeli_srecanja_po_dneh(srecanja):
    dnevi = {}
    for srecanje in srecanja:
        dnevi.setdefault(srecanje.dan, []).append(srecanje)
    return dnevi.values()


def razdeli_dan_na_bloke(srecanja):
    blok, konec_zadnjega_srecanja = [], None

    for srecanje in srecanja:
        # Če se naslednje srečanje začne za koncem vseh prejšnjih, zaključimo blok.
        if konec_zadnjega_srecanja is not None and srecanje.ura >= konec_zadnjega_srecanja:
            yield blok
            blok, konec_zadnjega_srecanja = [], None

        # Vstavimo v prvi stolpec, kjer je prostor. Če ga ni, dodamo novega.
        for stolpec in blok:
            if stolpec[-1].ura + stolpec[-1].trajanje <= srecanje.ura:
                stolpec.append(srecanje)
                break
        else:
            blok.append([srecanje])

        # Popravimo konec zadnjega srečanja.
        konec = srecanje.ura + srecanje.trajanje
        if konec_zadnjega_srecanja is None or konec > konec_zadnjega_srecanja:
            konec_zadnjega_srecanja = konec

    if blok:
        yield blok


def nastavi_sirine_srecanj(srecanja):
    for srecanja_dneva in razdeli_srecanja_po_dneh(srecanja):
        for blok in razdeli_dan_na_bloke(srecanja_dneva):
            for i, stolpec in enumerate(blok):
                for srecanje in stolpec:
                    srecanje.sirina = 1 / len(blok)
                    srecanje.zamik = i / len(blok)
                    srecanje.leftmost = (i == 0)
                    srecanje.rightmost = (i == len(blok) - 1)
    return srecanja
