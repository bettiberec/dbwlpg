from dataclasses import dataclass, field
from typing import List, Optional
import json
import os

@dataclass
class Recept:
    azonosito: int
    nev: str
    hozzavalok: List[str]
    elkeszitesi_ido: int
    leiras: str
    tipus: str

@dataclass
class ReceptKezelo:
    receptek: List[Recept] = field(default_factory=list)
    mentett_recept_azonositok: List[int] = field(default_factory=list)
    kovetkezo_azonosito: int = 1

    def recept_hozzaadas(
        self,
        nev: str,
        hozzavalok: List[str],
        elkeszitesi_ido: int,
        leiras: str,
        tipus: str,
    ) -> Recept:
        recept = Recept(
            azonosito=self.kovetkezo_azonosito,
            nev=nev,
            hozzavalok=hozzavalok,
            elkeszitesi_ido=elkeszitesi_ido,
            leiras=leiras,
            tipus=tipus.lower(),
        )
        self.receptek.append(recept)
        self.kovetkezo_azonosito += 1
        return recept

    def listaz_minden(self) -> List[Recept]:
        return self.receptek

    def listaz_mentettek(self) -> List[Recept]:
        return [r for r in self.receptek if r.azonosito in self.mentett_recept_azonositok]

    def mentes_recept(self, azonosito: int) -> bool:
        if azonosito in self.mentett_recept_azonositok:
            return False
        if any(r.azonosito == azonosito for r in self.receptek):
            self.mentett_recept_azonositok.append(azonosito)
            return True
        return False

    def keres(
        self,
        nev: Optional[str] = None,
        hozzavalo: Optional[str] = None,
        tipus: Optional[str] = None,
    ) -> List[Recept]:
        eredmeny = self.receptek
        if nev:
            nev_kis = nev.lower()
            eredmeny = [r for r in eredmeny if nev_kis in r.nev.lower()]
        if hozzavalo:
            hozzavalo_kis = hozzavalo.lower()
            eredmeny = [
                r
                for r in eredmeny
                if any(hozzavalo_kis in h.lower() for h in r.hozzavalok)
            ]
        if tipus:
            tipus_kis = tipus.lower()
            eredmeny = [r for r in eredmeny if r.tipus == tipus_kis]
        return eredmeny

    def toroles_recept(self, azonosito: int) -> bool:
        for r in self.receptek:
            if r.azonosito == azonosito:
                self.receptek.remove(r)
                if azonosito in self.mentett_recept_azonositok:
                    self.mentett_recept_azonositok.remove(azonosito)
                return True
        return False

    def recept_frissitese(
        self,
        azonosito: int,
        nev: str,
        hozzavalok: List[str],
        elkeszitesi_ido: int,
        leiras: str,
        tipus: str,
    ) -> bool:
        for r in self.receptek:
            if r.azonosito == azonosito:
                r.nev = nev
                r.hozzavalok = hozzavalok
                r.elkeszitesi_ido = elkeszitesi_ido
                r.leiras = leiras
                r.tipus = tipus.lower()
                return True
        return False

    def torol_mentettbol(self, azonosito: int) -> bool:
        if azonosito in self.mentett_recept_azonositok:
            self.mentett_recept_azonositok.remove(azonosito)
            return True
        return False

    def mentes_fajlba(self, fajlnev: str = "receptek.json"):
        adat = {
            "kovetkezo_azonosito": self.kovetkezo_azonosito,
            "mentett_recept_azonositok": self.mentett_recept_azonositok,
            "receptek": [
                {
                    "azonosito": r.azonosito,
                    "nev": r.nev,
                    "hozzavalok": r.hozzavalok,
                    "elkeszitesi_ido": r.elkeszitesi_ido,
                    "leiras": r.leiras,
                    "tipus": r.tipus,
                }
                for r in self.receptek
            ],
        }
        with open(fajlnev, "w", encoding="utf-8") as f:
            json.dump(adat, f, ensure_ascii=False, indent=2)

    def betoltes_fajlbol(self, fajlnev: str = "receptek.json") -> bool:
        if not os.path.exists(fajlnev):
            return False

        with open(fajlnev, "r", encoding="utf-8") as f:
            adat = json.load(f)

        self.kovetkezo_azonosito = adat.get("kovetkezo_azonosito", 1)
        self.mentett_recept_azonositok = adat.get("mentett_recept_azonositok", [])

        self.receptek = []
        for elem in adat.get("receptek", []):
            recept = Recept(
                azonosito=elem["azonosito"],
                nev=elem["nev"],
                hozzavalok=elem["hozzavalok"],
                elkeszitesi_ido=elem["elkeszitesi_ido"],
                leiras=elem["leiras"],
                tipus=elem["tipus"],
            )
            self.receptek.append(recept)

        return True