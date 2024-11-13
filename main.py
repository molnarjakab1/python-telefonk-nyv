print("Telefonköynyv")


class Telefonkonyv:
    rekordok={}
    #telefonkönyv osztály létrehozása, az adatokat tartalmazó dictionary üresen definiálva
    def __init__(self,adatok):
        with open(adatok,"r", encoding="utf-8") as file: #megnyitjuk az adatokat tartalmazó txt-t, az utf-8-as kódolás azért kellett mert mindig hibát dobott
            
            for sor in file: #egy for loop-al végigmegyünk az összes soron
            
                tartalom = sor.split(":",1) 
            
                if len(tartalom) ==2:
                    telefonszam = tartalom[0].strip() #whitespace-k törlése strip-el
                    nev = tartalom[1].strip()
                    self.rekordok[telefonszam]=nev
   
   
    def displayContents(self):
        print(self.rekordok)

    def AddNAme(self,phone_number,name,adatok):
        if phone_number  not in self.rekordok: #ha eddig nincs benne a telefonszám, akkor a tel szám és név felvétele a dictionary-be
            self.rekordok[phone_number]=name
            with open(adatok, "a", encoding="utf-8") as file:
                hozzaadott_sor = f"{phone_number} : {name}"
                file.write(hozzaadott_sor) # a rekord hozzáadása a txt végéhez
        else:
            print("Ez a név és telefonszám kombináció már létezik") # ha a rekord már létezik egy üzenetet ad vissza



konyv = Telefonkonyv("nevek.txt")
konyv.displayContents()
konyv.AddNAme("+36701231234","Kiss Miklós","nevek.txt")
konyv.AddNAme("+36707791309","Gogolyák Péter István", "nevek.txt")
konyv.displayContents()



            


