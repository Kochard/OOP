from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def get_ar(self):
        pass

class EgyagyasSzoba(Szoba):
    def get_ar(self):
        return self.ar

class KetagyasSzoba(Szoba):
    def get_ar(self):
        return self.ar

class HaromagyasSzoba(Szoba):
    def get_ar(self):
        return self.ar

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datetime.strptime(datum, "%Y-%m-%d")

    def get_ar(self):
        return self.szoba.get_ar()

class FoglalasKezelo:
    def __init__(self):
        self.szalloda = Szalloda(nev="Példa Szálloda")
        self.foglalasok = []

    def foglalas(self, szoba, datum):
        if datetime.now() > datetime.strptime(datum, "%Y-%m-%d"):
            return "Érvénytelen dátum. Csak jövőbeni foglalás lehetséges."
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datetime.strptime(datum, "%Y-%m-%d"):
                return "A szoba már foglalt ezen a napon."
        self.foglalasok.append(Foglalas(szoba, datum))
        return f"Foglalás ára: {szoba.get_ar()}"

    def lemondas(self, szoba, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datetime.strptime(datum, "%Y-%m-%d"):
                self.foglalasok.remove(foglalas)
                return "Foglalás sikeresen lemondva."
        return "Nincs ilyen foglalás."

    def listaz_foglalasok(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    kezelo = FoglalasKezelo()

    egyagyas = EgyagyasSzoba(ar=100, szobaszam=101)
    ketagyas = KetagyasSzoba(ar=150, szobaszam=102)
    haromagyas = HaromagyasSzoba(ar=200, szobaszam=103)

    kezelo.szalloda.add_szoba(egyagyas)
    kezelo.szalloda.add_szoba(ketagyas)
    kezelo.szalloda.add_szoba(haromagyas)

    # Töltsd fel a rendszert 1 szállodával, 3 szobával és 5 foglalással a felhasználói adatbekérés előtt.
    for _ in range(5):
        kezelo.foglalas(egyagyas, "2024-06-15")
        kezelo.foglalas(egyagyas, "2024-06-25")
        kezelo.foglalas(haromagyas, "2024-07-01")
        kezelo.foglalas(ketagyas, "2024-06-18")
        kezelo.foglalas(egyagyas, "2024-06-06")


    while True:
        print("\nVálassz műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Választás (1/2/3/4): ")

        if valasztas == "1":
            szobaszam = int(input("Szobaszám: "))
            datum = input("Dátum (YYYY-MM-DD): ")
            print(kezelo.foglalas(egyagyas if szobaszam == 101 else ketagyas, datum))
        elif valasztas == "2":
            szobaszam = int(input("Szobaszám: "))
            datum = input("Dátum (YYYY-MM-DD): ")
            print(kezelo.lemondas(egyagyas if szobaszam == 101 else ketagyas, datum))
        elif valasztas == "3":
            kezelo.listaz_foglalasok()
        elif valasztas == "4":
            print("Viszontlátás!")
            break
        else:
            print("Érvénytelen választás. Kérlek, válassz újra.")