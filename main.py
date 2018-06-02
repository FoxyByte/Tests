wyniki = open("el2.txt", "r")
lines = wyniki.readlines()
daty = []
liczby = []
wartosc = []
losowanie = []
for line in lines:
    losowanie = (line.split())
    daty.append(losowanie[1])
    liczby.append(losowanie[2].split(","))
wyniki.close()
for wynik in liczby:
    wynik = [int(i) for i in wynik]
    wartosc.append(wynik)
Mini = dict(zip(daty, wartosc))
print(Mini)


