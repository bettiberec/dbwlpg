Szakácskönyv

Ez a projekt egy egyszerű receptkezelő alkalmazás, amely Pythonban készült, Tkinter grafikus felülettel.
A program segítségével recepteket lehet hozzáadni, keresni, szerkeszteni, törölni és elmenteni.
Minden adat automatikusan mentésre kerül egy receptek.json fájlba, így a receptek újraindítás után is megmaradnak.

---Funkciók---
 
////Keresés////
  A keresőfelületen több feltétel alapján kereshetünk:
    -név alapján
    -hozzávaló alapján
    -ételtípus alapján (reggeli, ebéd, vacsora)
  A találatokat listában jeleníti meg.

////Összes recept////
  -Megjeleníti az összes eddig hozzáadott receptet.

////Mentett receptek////
  -Lehetőség van recepteket „kedvencként” elmenteni, majd külön megtekinteni őket.
  -A kedvenceket külön el is lehet távolítani.

////Új recept hozzáadása////
  Új recept létrehozásához az alábbi mezők szerepelnek:
    -Név
    -Hozzávalók (vesszővel elválasztva)
    -Elkészítési idő
    -Leírás
    -Típus (reggeli, ebéd, vacsora)

////Recept szerkesztése////
  Bármely meglévő recept adatai szerkeszthetők:
    -név
    -hozzávalók
    -elkészítési idő
    -leírás
    -típus
  Szerkesztés után a módosítások automatikusan mentődnek.

////Recept törlése////
  Teljes recept törölhető a listából.
  Ha korábban el volt mentve kedvencként, onnan is automatikusan eltávolítja.

////Adatmentés////
  A projekt minden receptet egy JSON fájlban tárol: receptek.json
  Induláskor a program beolvassa a fájl tartalmát, így az adatok nem vesznek el.
  Kilépéskor és minden változtatás után automatikusan menti a recepteket.

////Technológiák////
 -Python 3
 -Tkinter GUI
 -Dataclasses
 -JSON fájlkezelés

