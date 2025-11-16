# Szakácskönyv

Hallgató: Berec Bettina

## Feladat leírás
Ez a projekt egy egyszerű receptkezelő alkalmazás, amely Pythonban készült, Tkinter grafikus felülettel.
A program segítségével recepteket lehet hozzáadni, keresni, szerkeszteni, törölni és elmenteni.
Minden adat automatikusan mentésre kerül egy receptek.json fájlba, így a receptek újraindítás után is megmaradnak.

## Modulok és tartalmuk

- backend.py
  - Osztályok:
    - Recept
    - ReceptKezelo
  - Függvények:
    - recept_hozzaadas
    - listaz_minden
    - listaz_mentettek
    - mentes_recept
    - keres
    - toroles_recept
    - recept_frissitese
    - torol_mentettbol
    - mentes_fajlba
    - betoltes_fajlbol
- gui_bb.py
  - Osztály:
    - bb_szakacskonyv
  - Függvények:
    - tartalom_torles
    - keresesesi_nezet
    - recept_keresese
    - feltolt_recept_lista
    - osszes_recept
    - mentett_receptek
    - bb_uj_recept
    - recept_hozzaadasa
    - recept_lista_widgetek
    - kivalasztott_recept
    - reszletek
    - kedvenc_recept_mentes
    - recept_torles
    - recept_szerkesztes
    - valtoztatasok_mentese
    - mentettbol_torles
    - ablak_bezarasa
    - futtatas
- main.py
