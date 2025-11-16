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
- app_bb.py
    - Osztály:
        - app_bb
    - Függvények:
      - betoltes
      - mentes
      - listaz_minden
      - listaz_mentettek
      - keres
      - uj_recept
      - recept_frissitese
      - torles_recept
      - mentes_recept
      - torol_mentettbol
- gui_bb.py
  - Osztály:
    - bb_szakacskonyv
  - Függvények:
    - tartalom_torles
    - recept_lista_widgetek
    - feltolt_recept_lista
    - kivalasztott_recept
    - keresesesi_nezet
    - recept_keresese
    - osszes_recept
    - mentett_receptek
    - bb_uj_recept
    - reszletek
    - kedvenc_recept_mentes
    - recept_torles
    - recept_szerkesztes
    - mentettbol_torles
    - ablak_bezarasa
    - futtatas
- main.py
