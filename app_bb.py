from typing import List, Optional
from backend import ReceptKezelo, Recept


class bb_app:

    def __init__(self):
        self.kezelo = ReceptKezelo()

    def betoltes(self, fajlnev: str = "receptek.json") -> bool:
        return self.kezelo.betoltes_fajlbol(fajlnev)

    def mentes(self, fajlnev: str = "receptek.json") -> None:
        self.kezelo.mentes_fajlba(fajlnev)

    def listaz_minden(self) -> List[Recept]:
        return self.kezelo.listaz_minden()

    def listaz_mentettek(self) -> List[Recept]:
        return self.kezelo.listaz_mentettek()

    def keres(
        self,
        nev: Optional[str] = None,
        hozzavalo: Optional[str] = None,
        tipus: Optional[str] = None,
    ) -> List[Recept]:
        return self.kezelo.keres(nev=nev, hozzavalo=hozzavalo, tipus=tipus)

    def uj_recept(
        self,
        nev: str,
        hozzavalok: list[str],
        elkeszitesi_ido: int,
        leiras: str,
        tipus: str,
    ) -> Recept:
        return self.kezelo.recept_hozzaadas(
            nev=nev,
            hozzavalok=hozzavalok,
            elkeszitesi_ido=elkeszitesi_ido,
            leiras=leiras,
            tipus=tipus,
        )

    def recept_frissitese(
        self,
        azonosito: int,
        nev: str,
        hozzavalok: list[str],
        elkeszitesi_ido: int,
        leiras: str,
        tipus: str,
    ) -> bool:
        return self.kezelo.recept_frissitese(
            azonosito=azonosito,
            nev=nev,
            hozzavalok=hozzavalok,
            elkeszitesi_ido=elkeszitesi_ido,
            leiras=leiras,
            tipus=tipus,
        )

    def torles_recept(self, azonosito: int) -> bool:
        return self.kezelo.toroles_recept(azonosito)

    def mentes_recept(self, azonosito: int) -> bool:
        return self.kezelo.mentes_recept(azonosito)

    def torol_mentettbol(self, azonosito: int) -> bool:
        return self.kezelo.torol_mentettbol(azonosito)
