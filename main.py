import fnmatch # a wildcard keresés miatt kell inportálni
import keyboard # a billentyű lenyomásokat érzékeli
import os 
import time

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
   
   
    def displayContents(self,adatok):
        with open(adatok, "r", encoding="utf-8") as file:
            contents = file.read()
            print(contents)

    def AddName(self,phone_number,name,adatok):
        if phone_number  not in self.rekordok: #ha eddig nincs benne a telefonszám, akkor a tel szám és név felvétele a dictionary-be
            self.rekordok[phone_number]=name
            with open(adatok, "a", encoding="utf-8") as file:
                hozzaadott_sor = f"\n{phone_number} : {name}"
                file.write(hozzaadott_sor) # a rekord hozzáadása a txt végéhez
                print("Név sikeresen hozzáadva!")
        else:
            print("Ez a név és telefonszám kombináció már létezik") # ha a rekord már létezik egy üzenetet ad vissza

    def DelName(self,phone_number,name,adatok):
        torol = ''
        if phone_number in self.rekordok:
            del self.rekordok[phone_number]
            with open(adatok, "r+", encoding="utf-8") as file:
                l= file.readlines()
                for i in range(len(l)):
                    if f"{phone_number} : {name}" in l[i]:
                        l[i] =l[i].replace(f"{phone_number} : {name}",torol)
                file.seek(0)
                file.truncate(0)
                file.writelines(l)
                file.close()
                print("Sikeres törlés!")
        else:
            print("Ez a telefonszám nincs benne a telefonkönyvben")
    
    def SearchName(self, name_pattern):
        matched_numbers = []
        for phone_number, stored_name in self.rekordok.items():
             if fnmatch.fnmatch(stored_name, name_pattern):
                matched_numbers.append((stored_name, phone_number))
    
        if matched_numbers:
            return matched_numbers
        else:
            print("Nincs találat a keresett névre.")
            return None

konyv = Telefonkonyv("nevek.txt")

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and macOS
    else:
        os.system('clear')


print("Üdvözlöm a konzolos telefonkönyv alkalmazásban!\nKérem Válassza ki a kívánt műveletet!")
print("Kilépés a 0 billenytűvel!")
print("Nyomja meg bármelyik gombot a kezdéshez!")
    

while True:
    key = keyboard.read_event()
    # Display menu
    print("1. A teljes telefonkönyv megtekintése\n2. Név/telefonszám hozzáadása\n3. Telefonszám keresése\n4. Telefonszám törlése\n5. A képernyő törlése")
    
    try:
        option = int(input())
        
        if option == 1:
            konyv.displayContents("nevek.txt")
        
        elif option == 2:
            print("Kérem adja meg a hozzáadni kívánt telefonszámot:")
            tel_szam = input()
            print("Kérem adja meg a hozzáadni kívánt nevet:")
            nev = input()
            konyv.AddName(tel_szam, nev, "nevek.txt")
        
        elif option == 3:
            print("A kereső a * karaktert is elfogadja\n Pl.: *Miklós az összes Miklós nevű rekordot kikeresi, amennyiben az benne van a telefonkönyvben\nKérem írja be a keresni kívánt nevet:")
            keresett_nev = input()
            print(konyv.SearchName(keresett_nev))
        
        elif option == 4:
            print("Kérem írja be a törölni kívánt nevet:")
            torlendo_nev = input()
            print("Kérem írja be a törölni kívánt telefonszámot:")
            torlendo_szam = input()
            konyv.DelName(torlendo_szam, torlendo_nev, "nevek.txt")
        elif option ==5:
            clear_screen()
        elif option == 0:
            break
        else:
            print("Kérem a felsorolt lehetőségek közül válasszon (1-4)!")
    
    except ValueError:
        print("Hibás bemenet. Kérem, számot adjon meg (1-4)!")
    

    

