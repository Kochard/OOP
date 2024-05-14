# from abc import ABC, abstractmethod
# from datetime import datetime

# class Szoba(ABC):
#     def __init__(self, szobaszam, ar):
#         self.szobaszam = szobaszam
#         self.ar = ar

#     @abstractmethod
#     def get_ar(self):
#         pass

# class EgyagyasSzoba(Szoba):
#     def get_ar(self):
#         return self.ar

# class KetagyasSzoba(Szoba):
#     def get_ar(self):
#         return self.ar * 1.5

# class Foglalas:
#     def __init__(self, szoba, datum):
#         self.szoba = szoba
#         self.datum = datum

# class Szalloda:
#     def __init__(self, nev):
#         self.nev = nev
#         self.szobak = []
#         self.foglalasok = []

#     def add_szoba(self, szoba):
#         self.szobak.append(szoba)

#     def foglal(self, szobaszam, datum):
#         for szoba in self.szobak:
#             if szoba.szobaszam == szobaszam:
#                 for foglalas in self.foglalasok:
#                     if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
#                         print("A szoba már foglalt erre a dátumra.")
#                         return
#                 foglalas = Foglalas(szoba, datum)
#                 self.foglalasok.append(foglalas)
#                 print("Sikeres foglalás!")
#                 return
#         print("Nem található ilyen szobaszám.")

#     def cancel_foglalas(self, szobaszam, datum):
#         for foglalas in self.foglalasok:
#             if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
#                 self.foglalasok.remove(foglalas)
#                 print("Foglalás sikeresen törölve.")
#                 return
#         print("Nem található ilyen foglalás.")

#     def list_foglalasok(self):
#         for foglalas in self.foglalasok:
#             print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

# def main():
#     szalloda = Szalloda("Példa Szálloda")
#     szalloda.add_szoba(EgyagyasSzoba("101", 100))
#     szalloda.add_szoba(EgyagyasSzoba("102", 120))
#     szalloda.add_szoba(KetagyasSzoba("201", 150))

#     for i in range(1, 6):
#         szalloda.foglal(f"{i}01", datetime.now())

#     while True:
#         print("1. Foglalás")
#         print("2. Lemondás")
#         print("3. Foglalások listázása")
#         print("4. Kilépés")
#         choice = input("Válasszon műveletet: ")

#         if choice == "1":
#             szobaszam = input("Adja meg a foglalandó szoba számát: ")
#             datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
#             try:
#                 datum = datetime.strptime(datum_str, "%Y-%m-%d")
#                 if datum < datetime.now():
#                     print("Hibás dátum! Kérjük adjon meg jövőbeli dátumot.")
#                     continue
#                 szalloda.foglal(szobaszam, datum)
#             except ValueError:
#                 print("Hibás dátumformátum!")

#         elif choice == "2":
#             szobaszam = input("Adja meg a lemondani kívánt foglalás szobaszámát: ")
#             datum_str = input("Adja meg a lemondani kívánt foglalás dátumát (YYYY-MM-DD formátumban): ")
#             try:
#                 datum = datetime.strptime(datum_str, "%Y-%m-%d")
#                 szalloda.cancel_foglalas(szobaszam, datum)
#             except ValueError:
#                 print("Hibás dátumformátum!")

#         elif choice == "3":
#             szalloda.list_foglalasok()

#         elif choice == "4":
#             break

# if __name__ == "__main__":
#     main()

# from abc import ABC, abstractmethod
# from datetime import datetime, timedelta

# # Szoba absztrakt osztály
# class Szoba(ABC):
#     def __init__(self, ar, szobaszam):
#         self.ar = ar
#         self.szobaszam = szobaszam

#     @abstractmethod
#     def foglal(self, datum):
#         pass

# # EgyágyasSzoba osztály
# class EgyagyasSzoba(Szoba):
#     def foglal(self, datum):
#         print(f"Egyágyas szoba foglalva {datum}-ra, ár: {self.ar} Ft")

# # KétágyasSzoba osztály
# class KetagyasSzoba(Szoba):
#     def foglal(self, datum):
#         print(f"Kétágyas szoba foglalva {datum}-ra, ár: {self.ar} Ft")

# # Szálloda osztály
# class Szalloda:
#     def __init__(self, nev):
#         self.nev = nev
#         self.szobak = []
#         self.foglalasok = {}

#     def szoba_hozzaad(self, szoba):
#         self.szobak.append(szoba)

#     def foglalas(self, szobaszam, datum):
#         if datum < datetime.today().date():
#             return "Hibás dátum!"
#         for foglalas in self.foglalasok.values():
#             if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
#                 return "A szoba ezen a napon már foglalt."
#         for szoba in self.szobak:
#             if szoba.szobaszam == szobaszam:
#                 self.foglalasok[datum] = {'szobaszam': szobaszam, 'datum': datum}
#                 szoba.foglal(datum)
#                 return szoba.ar
#         return "Nincs ilyen szobaszám."

#     def foglalas_lemondas(self, datum):
#         if datum in self.foglalasok:
#             del self.foglalasok[datum]
#             return "Foglalás lemondva."
#         return "Nincs foglalás ezen a napon."

#     def foglalasok_listazasa(self):
#         for datum, foglalas in self.foglalasok.items():
#             print(f"{datum}: Szoba {foglalas['szobaszam']}")

# # Foglalás osztály
# class Foglalas:
#     def __init__(self, szalloda, szobaszam, datum):
#         self.szalloda = szalloda
#         self.szobaszam = szobaszam
#         self.datum = datum
#         self.ar = self.szalloda.foglalas(szobaszam, datum)

# # Példa adatokkal
# szalloda = Szalloda("Budapest Hotel")
# szalloda.szoba_hozzaad(EgyagyasSzoba(10000, 101))
# szalloda.szoba_hozzaad(KetagyasSzoba(20000, 102))
# szalloda.szoba_hozzaad(EgyagyasSzoba(15000, 103))

# # Felhasználói interfész
# def main():
#     print("Üdvözöljük a Budapest Hotel foglalási rendszerében!")
#     while True:
#         print("\nVálasztható műveletek:")
#         print("1 - Foglalás")
#         print("2 - Lemondás")
#         print("3 - Foglalások listázása")
#         print("4 - Kilépés")
#         valasztas = input("Kérem válasszon egy opciót: ")
#         if valasztas == '1':
#             szobaszam = int(input("Adja meg a szobaszámot: "))
#             datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
#             datum = datetime.strptime(datum, "%Y-%m-%d").date()
#             print(szalloda.foglalas(szobaszam, datum))
#         elif valasztas == '2':
#             datum = input("Adja meg a lemondás dátumát (YYYY-MM-DD formátumban): ")
#             datum = datetime.strptime(datum, "%Y-%m-%d").date()
#             print(szalloda.foglalas_lemondas(datum))
#         elif valasztas == '3':
#             szalloda.foglalasok_listazasa()
#         elif valasztas == '4':
#             print("Köszönjük, hogy a Budapest Hotelt választotta. Viszlát!")
#             break

# if __name__ == "__main__":
#     main()

# import numpy as np
# from datetime import datetime, timedelta

# # Szoba absztrakt osztály
# class Szoba:
#     def __init__(self, ar, szobaszam):
#         self.ar = ar
#         self.szobaszam = szobaszam

#     def foglal(self, datum):
#         return f"Szoba {self.szobaszam} foglalva {datum} napra. Ár: {self.ar} Ft."

# # EgyágyasSzoba osztály
# class EgyagyasSzoba(Szoba):
#     def __init__(self, ar, szobaszam):
#         super().__init__(ar, szobaszam)

# # KétágyasSzoba osztály
# class KetagyasSzoba(Szoba):
#     def __init__(self, ar, szobaszam):
#         super().__init__(ar, szobaszam)

# # Szálloda osztály
# class Szalloda:
#     def __init__(self, nev):
#         self.nev = nev
#         self.szobak = []
#         self.foglalasok = {}

#     def szoba_hozzaad(self, szoba):
#         self.szobak.append(szoba)

#     def foglalas(self, szobaszam, datum):
#         if datum < datetime.today().date():
#             return "A dátum nem lehet a múltban."
#         if any(f for f in self.foglalasok if f['szobaszam'] == szobaszam and f['datum'] == datum):
#             return "Ez a szoba ezen a napon már foglalt."
#         self.foglalasok[(szobaszam, datum)] = {'szobaszam': szobaszam, 'datum': datum}
#         return next(szoba.foglal(datum) for szoba in self.szobak if szoba.szobaszam == szobaszam)

#     def foglalas_lemondas(self, szobaszam, datum):
#         if (szobaszam, datum) in self.foglalasok:
#             del self.foglalasok[(szobaszam, datum)]
#             return "Foglalás törölve."
#         return "Nincs ilyen foglalás."

#     def foglalasok_listazasa(self):
#         for key in self.foglalasok:
#             print(f"Szobaszám: {self.foglalasok[key]['szobaszam']}, Dátum: {self.foglalasok[key]['datum']}")

# # Példányosítás és előre feltöltés
# szalloda = Szalloda("Grande Hotel")
# szalloda.szoba_hozzaad(EgyagyasSzoba(15000, 101))
# szalloda.szoba_hozzaad(KetagyasSzoba(20000, 102))
# szalloda.szoba_hozzaad(EgyagyasSzoba(18000, 103))

# # Foglalások előre feltöltése
# datumok = [datetime.today().date() + timedelta(days=i) for i in range(1, 6)]
# for i, datum in enumerate(datumok):
#     szobaszam = 101 + i % 3
#     szalloda.foglalas(szobaszam, datum)

# # Felhasználói interfész
# def main():
#     print(f"Üdvözöljük a {szalloda.nev} foglalási rendszerében!")
#     while True:
#         print("\nVálasztható műveletek:")
#         print("1 - Foglalás")
#         print("2 - Lemondás")
#         print("3 - Foglalások listázása")
#         print("4 - Kilépés")
#         choice = input("Kérem válasszon egy opciót: ")
#         if choice == '1':
#             szobaszam = int(input("Adja meg a szobaszámot: "))
#             datum = datetime.strptime(input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): "), "%Y-%m-%d").date()
#             print(szalloda.foglalas(szobaszam, datum))
#         elif choice == '2':
#             szobaszam = int(input("Adja meg a szobaszámot, amelyikből a foglalást törölni szeretné: "))
#             datum = datetime.strptime(input("Adja meg a lemondás dátumát (YYYY-MM-DD formátumban): "), "%Y-%m-%d").date()
#             print(szalloda.foglalas_lemondas(szobaszam, datum))
#         elif choice == '3':
#             szalloda.foglalasok_listazasa()
#         elif choice == '4':
#             print("Köszönjük, hogy minket választott. Viszontlátásra!")
#             break

# if __name__ == "__main__":
#     main()

import numpy as np
from datetime import datetime, timedelta

# Szoba absztrakt osztály
class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    def foglal(self, datum):
        return f"Szoba {self.szobaszam} foglalva {datum} napra. Ár: {self.ar} Ft."

# EgyágyasSzoba osztály
class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

# KétágyasSzoba osztály
class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

# Szálloda osztály
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = {}

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        if datum < datetime.today().date():
            return "A dátum nem lehet a múltban."
        for key, foglalas in self.foglalasok.items():
            if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
                return "Ez a szoba ezen a napon már foglalt."
        self.foglalasok[(szobaszam, datum)] = {'szobaszam': szobaszam, 'datum': datum}
        return next((szoba.foglal(datum) for szoba in self.szobak if szoba.szobaszam == szobaszam), "Nincs ilyen szobaszám.")

    def foglalas_lemondas(self, szobaszam, datum):
        key = (szobaszam, datum)
        if key in self.foglalasok:
            del self.foglalasok[key]
            return "Foglalás törölve."
        return "Nincs ilyen foglalás."

    def foglalasok_listazasa(self):
        for key, foglalas in self.foglalasok.items():
            print(f"Szobaszám: {foglalas['szobaszam']}, Dátum: {foglalas['datum']}")

# Példányosítás és előre feltöltés
szalloda = Szalloda("Grande Hotel")
szalloda.szoba_hozzaad(EgyagyasSzoba(15000, 101))
szalloda.szoba_hozzaad(KetagyasSzoba(20000, 102))
szalloda.szoba_hozzaad(EgyagyasSzoba(18000, 103))

# Foglalások előre feltöltése
datumok = [datetime.today().date() + timedelta(days=i) for i in range(1, 6)]
for i, datum in enumerate(datumok):
    szobaszam = 101 + i % 3
    szalloda.foglalas(szobaszam, datum)

# Felhasználói interfész
def main():
    print(f"Üdvözöljük a {szalloda.nev} foglalási rendszerében!")
    while True:
        print("\nVálasztható műveletek:")
        print("1 - Foglalás")
        print("2 - Lemondás")
        print("3 - Foglalások listázása")
        print("4 - Kilépés")
        choice = input("Kérem válasszon egy opciót: ")
        if choice == '1':
            szobaszam = int(input("Adja meg a szobaszámot: "))
            datum = datetime.strptime(input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): "), "%Y-%m-%d").date()
            print(szalloda.foglalas(szobaszam, datum))
        elif choice == '2':
            szobaszam = int(input("Adja meg a szobaszámot, amelyikből a foglalást törölni szeretné: "))
            datum = datetime.strptime(input("Adja meg a lemondás dátumát (YYYY-MM-DD formátumban): "), "%Y-%m-%d").date()
            print(szalloda.foglalas_lemondas(szobaszam, datum))
        elif choice == '3':
            szalloda.foglalasok_listazasa()
        elif choice == '4':
            print("Köszönjük, hogy minket választott. Viszontlátásra!")
            break

if __name__ == "__main__":
    main()
