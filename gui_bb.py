import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Optional

from backend import Recept
from app_bb import bb_app


class bb_szakacskonyv(tk.Tk):
    def __init__(self, app: bb_app):
        super().__init__()
        self.title("Receptes projekt")
        self.geometry("800x600")

        self.app = app                           # <-- régen self.kezelo volt
        self.protocol("WM_DELETE_WINDOW", self.ablak_bezarasa)

        self.gomb_keret = tk.Frame(self)
        self.gomb_keret.pack(side=tk.TOP, fill=tk.X, pady=5)

        tk.Button(self.gomb_keret, text="Keresés", command=self.keresesesi_nezet).pack(side=tk.LEFT, padx=5)
        tk.Button(self.gomb_keret, text="Receptjeim", command=self.osszes_recept).pack(side=tk.LEFT, padx=5)
        tk.Button(self.gomb_keret, text="Mentett receptek", command=self.mentett_receptek).pack(side=tk.LEFT, padx=5)
        tk.Button(self.gomb_keret, text="Recept hozzáadása", command=self.bb_uj_recept).pack(side=tk.LEFT, padx=5)

        self.tartalom_keret = tk.Frame(self)
        self.tartalom_keret.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.aktualis_receptek_lista: List[Recept] = []

        self.keresesesi_nezet()

    def tartalom_torles(self):
        for widget in self.tartalom_keret.winfo_children():
            widget.destroy()

    def recept_lista_widgetek(self):
        lista_keret = tk.Frame(self.tartalom_keret)
        lista_keret.pack(fill=tk.BOTH, expand=True)

        self.recept_lista = tk.Listbox(lista_keret)
        self.recept_lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        gorgeto = tk.Scrollbar(lista_keret, orient=tk.VERTICAL, command=self.recept_lista.yview)
        gorgeto.pack(side=tk.RIGHT, fill=tk.Y)
        self.recept_lista.config(yscrollcommand=gorgeto.set)

        gomb_keret = tk.Frame(self.tartalom_keret)
        gomb_keret.pack(fill=tk.X, pady=5)

        tk.Button(gomb_keret, text="Részletek", command=self.reszletek).pack(side=tk.LEFT, padx=5)
        tk.Button(gomb_keret, text="Szerkesztés", command=self.recept_szerkesztes).pack(side=tk.LEFT, padx=5)
        tk.Button(gomb_keret, text="Kedvencekhez", command=self.kedvenc_recept_mentes).pack(side=tk.LEFT, padx=5)
        tk.Button(gomb_keret, text="Törlés", command=self.recept_torles).pack(side=tk.LEFT, padx=5)
        tk.Button(gomb_keret, text="Kedvencekből törlés", command=self.mentettbol_torles).pack(side=tk.LEFT, padx=5)

    def feltolt_recept_lista(self, receptek: List[Recept]):
        self.aktualis_receptek_lista = receptek
        self.recept_lista.delete(0, tk.END)
        for r in receptek:
            szoveg = f"{r.nev} ({r.tipus}, {r.elkeszitesi_ido} perc)"
            self.recept_lista.insert(tk.END, szoveg)

    def kivalasztott_recept(self) -> Optional[Recept]:
        kivalasztas = self.recept_lista.curselection()
        if not kivalasztas:
            return None
        index = kivalasztas[0]
        if index < 0 or index >= len(self.aktualis_receptek_lista):
            return None
        return self.aktualis_receptek_lista[index]

    def keresesesi_nezet(self):
        self.tartalom_torles()

        cimke = tk.Label(self.tartalom_keret, text="Keresés", font=("Arial", 16, "bold"))
        cimke.pack(pady=5)

        keret = tk.Frame(self.tartalom_keret)
        keret.pack(fill=tk.X, pady=5)

        tk.Label(keret, text="Név:").grid(row=0, column=0, sticky="w")
        nev_mezo = tk.Entry(keret, width=30)
        nev_mezo.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(keret, text="Hozzávaló:").grid(row=1, column=0, sticky="w")
        hozzavalo_mezo = tk.Entry(keret, width=30)
        hozzavalo_mezo.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(keret, text="Típus:").grid(row=2, column=0, sticky="w")
        tipus_valtozo = tk.StringVar()
        tipus_lenyilo = ttk.Combobox(
            keret,
            textvariable=tipus_valtozo,
            values=["", "reggeli", "ebéd", "vacsora"],
            state="readonly",
            width=27,
        )
        tipus_lenyilo.grid(row=2, column=1, padx=5, pady=2)
        tipus_lenyilo.current(0)

        def recept_keresese():
            nev = nev_mezo.get().strip() or None
            hozzavalo = hozzavalo_mezo.get().strip() or None
            tipus = tipus_valtozo.get().strip() or None

            talalatok = self.app.keres(nev=nev, hozzavalo=hozzavalo, tipus=tipus)
            self.feltolt_recept_lista(talalatok)

        keres_gomb = tk.Button(keret, text="Keresés", command=recept_keresese)
        keres_gomb.grid(row=3, column=0, columnspan=2, pady=5)

        self.recept_lista_widgetek()

    def osszes_recept(self):
        self.tartalom_torles()

        cimke = tk.Label(self.tartalom_keret, text="Összes recept", font=("Arial", 16, "bold"))
        cimke.pack(pady=5)

        self.recept_lista_widgetek()
        self.feltolt_recept_lista(self.app.listaz_minden())

    def mentett_receptek(self):
        self.tartalom_torles()

        cimke = tk.Label(self.tartalom_keret, text="Mentett receptek", font=("Arial", 16, "bold"))
        cimke.pack(pady=5)

        self.recept_lista_widgetek()
        self.feltolt_recept_lista(self.app.listaz_mentettek())

    def bb_uj_recept(self):
        self.tartalom_torles()

        cimke = tk.Label(self.tartalom_keret, text="Új recept hozzáadása", font=("Arial", 16, "bold"))
        cimke.pack(pady=5)

        uj_recept_keret = tk.Frame(self.tartalom_keret)
        uj_recept_keret.pack(fill=tk.X, pady=5)

        tk.Label(uj_recept_keret, text="Név:").grid(row=0, column=0, sticky="w", pady=2)
        nev_mezo = tk.Entry(uj_recept_keret, width=40)
        nev_mezo.grid(row=0, column=1, sticky="w", pady=2)

        tk.Label(uj_recept_keret, text="Hozzávalók (vesszővel elválasztva):").grid(row=1, column=0, sticky="w", pady=2)
        hozzavalok_mezo = tk.Entry(uj_recept_keret, width=40)
        hozzavalok_mezo.grid(row=1, column=1, sticky="w", pady=2)

        tk.Label(uj_recept_keret, text="Elkészítési idő (perc):").grid(row=2, column=0, sticky="w", pady=2)
        elkeszitesi_ido_mezo = tk.Entry(uj_recept_keret, width=15)
        elkeszitesi_ido_mezo.grid(row=2, column=1, sticky="w", pady=2)

        tk.Label(uj_recept_keret, text="Típus:").grid(row=3, column=0, sticky="w", pady=2)
        tipus_valtozo = tk.StringVar()
        tipus_lenyilo = ttk.Combobox(
            uj_recept_keret,
            textvariable=tipus_valtozo,
            values=["reggeli", "ebéd", "vacsora"],
            state="readonly",
            width=12,
        )
        tipus_lenyilo.grid(row=3, column=1, sticky="w", pady=2)
        tipus_lenyilo.current(0)

        tk.Label(uj_recept_keret, text="Leírás:").grid(row=4, column=0, sticky="nw", pady=2)
        leiras_szoveg = tk.Text(uj_recept_keret, width=40, height=6)
        leiras_szoveg.grid(row=4, column=1, pady=2)

        def recept_hozzaadasa():
            nev = nev_mezo.get().strip()
            hozzavalok_szoveg = hozzavalok_mezo.get().strip()
            elkeszitesi_ido_szoveg = elkeszitesi_ido_mezo.get().strip()
            tipus = tipus_valtozo.get().strip()
            leiras = leiras_szoveg.get("1.0", tk.END).strip()

            if not nev:
                messagebox.showerror("Hiba", "A név nem lehet üres.")
                return
            if not hozzavalok_szoveg:
                messagebox.showerror("Hiba", "Legalább egy hozzávaló kell.")
                return
            hozzavalok_lista = [h.strip() for h in hozzavalok_szoveg.split(",") if h.strip()]
            if not elkeszitesi_ido_szoveg.isdigit():
                messagebox.showerror("Hiba", "Az elkészítési időnek egész számnak kell lennie.")
                return
            elkeszitesi_ido = int(elkeszitesi_ido_szoveg)

            self.app.uj_recept(
                nev=nev,
                hozzavalok=hozzavalok_lista,
                elkeszitesi_ido=elkeszitesi_ido,
                leiras=leiras,
                tipus=tipus,
            )
            self.app.mentes("receptek.json")

            messagebox.showinfo("Siker", "Recept sikeresen hozzáadva!")

            nev_mezo.delete(0, tk.END)
            hozzavalok_mezo.delete(0, tk.END)
            elkeszitesi_ido_mezo.delete(0, tk.END)
            leiras_szoveg.delete("1.0", tk.END)

        hozzaadas_gomb = tk.Button(self.tartalom_keret, text="Recept hozzáadása", command=recept_hozzaadasa)
        hozzaadas_gomb.pack(pady=10)

    def reszletek(self):
        recept = self.kivalasztott_recept()
        if not recept:
            messagebox.showwarning("Figyelem", "Nincs kiválasztott recept.")
            return

        sorok = [
            f"Név: {recept.nev}",
            f"Típus: {recept.tipus}",
            f"Elkészítési idő: {recept.elkeszitesi_ido} perc",
            "Hozzávalók:",
        ]
        for h in recept.hozzavalok:
            sorok.append(f"  - {h}")
        sorok.append("Leírás:")
        sorok.append(recept.leiras)

        messagebox.showinfo("Recept részletei", "\n".join(sorok))

    def kedvenc_recept_mentes(self):
        recept = self.kivalasztott_recept()
        if not recept:
            messagebox.showwarning("Figyelem", "Nincs kiválasztott recept.")
            return

        if self.app.mentes_recept(recept.azonosito):
            self.app.mentes("receptek.json")
            messagebox.showinfo("Siker", "Recept elmentve a kedvencek közé.")
        else:
            messagebox.showwarning("Info", "Már a kedvencek között van, vagy nem sikerült menteni.")

    def recept_torles(self):
        recept = self.kivalasztott_recept()
        if not recept:
            messagebox.showwarning("Figyelem", "Nincs kiválasztott recept.")
            return

        if not messagebox.askyesno("Megerősítés", "Biztosan törlöd ezt a receptet?"):
            return

        if self.app.torles_recept(recept.azonosito):
            self.app.mentes("receptek.json")
            messagebox.showinfo("Siker", "Recept törölve.")
            self.feltolt_recept_lista(self.app.listaz_minden())
        else:
            messagebox.showerror("Hiba", "Nem sikerült törölni a receptet.")

    def recept_szerkesztes(self):
        recept = self.kivalasztott_recept()
        if not recept:
            messagebox.showwarning("Figyelem", "Nincs kiválasztott recept.")
            return

        ablak = tk.Toplevel(self)
        ablak.title("Recept szerkesztése")
        ablak.geometry("400x420")

        tk.Label(ablak, text="Név:").pack(anchor="w", padx=10, pady=(10, 0))
        nev_mezo = tk.Entry(ablak)
        nev_mezo.insert(0, recept.nev)
        nev_mezo.pack(fill=tk.X, padx=10)

        tk.Label(ablak, text="Hozzávalók (vesszővel):").pack(anchor="w", padx=10, pady=(10, 0))
        hozzavalok_mezo = tk.Entry(ablak)
        hozzavalok_mezo.insert(0, ", ".join(recept.hozzavalok))
        hozzavalok_mezo.pack(fill=tk.X, padx=10)

        tk.Label(ablak, text="Elkészítési idő (perc):").pack(anchor="w", padx=10, pady=(10, 0))
        elkeszitesi_ido_mezo = tk.Entry(ablak)
        elkeszitesi_ido_mezo.insert(0, str(recept.elkeszitesi_ido))
        elkeszitesi_ido_mezo.pack(fill=tk.X, padx=10)

        tk.Label(ablak, text="Típus:").pack(anchor="w", padx=10, pady=(10, 0))
        tipus_valtozo = tk.StringVar(value=recept.tipus)
        tipus_lenyilo = ttk.Combobox(
            ablak,
            textvariable=tipus_valtozo,
            values=["reggeli", "ebéd", "vacsora"],
            state="readonly",
        )
        tipus_lenyilo.pack(fill=tk.X, padx=10)

        tk.Label(ablak, text="Leírás:").pack(anchor="w", padx=10, pady=(10, 0))
        leiras_mezo = tk.Text(ablak, height=6)
        leiras_mezo.insert("1.0", recept.leiras)
        leiras_mezo.pack(fill=tk.BOTH, padx=10, pady=(0, 10), expand=True)

        def valtoztatasok_mentese():
            uj_nev = nev_mezo.get().strip()
            uj_hozzavalok_szoveg = hozzavalok_mezo.get().strip()
            uj_elkeszitesi_ido_szoveg = elkeszitesi_ido_mezo.get().strip()
            uj_tipus = tipus_valtozo.get()
            uj_leiras = leiras_mezo.get("1.0", tk.END).strip()

            if not uj_nev:
                messagebox.showerror("Hiba", "A név nem lehet üres.")
                return
            uj_hozzavalok = [h.strip() for h in uj_hozzavalok_szoveg.split(",") if h.strip()]
            if not uj_hozzavalok:
                messagebox.showerror("Hiba", "Legalább egy hozzávaló kell.")
                return
            if not uj_elkeszitesi_ido_szoveg.isdigit():
                messagebox.showerror("Hiba", "Az időnek számnak kell lennie.")
                return

            self.app.recept_frissitese(
                azonosito=recept.azonosito,
                nev=uj_nev,
                hozzavalok=uj_hozzavalok,
                elkeszitesi_ido=int(uj_elkeszitesi_ido_szoveg),
                leiras=uj_leiras,
                tipus=uj_tipus,
            )
            self.app.mentes("receptek.json")
            messagebox.showinfo("Siker", "Recept frissítve.")
            ablak.destroy()
            self.feltolt_recept_lista(self.app.listaz_minden())

        tk.Button(ablak, text="Változtatások mentése", command=valtoztatasok_mentese).pack(pady=10)

    def mentettbol_torles(self):
        recept = self.kivalasztott_recept()
        if not recept:
            messagebox.showwarning("Figyelem", "Nincs kiválasztott recept.")
            return

        if self.app.torol_mentettbol(recept.azonosito):
            self.app.mentes("receptek.json")
            messagebox.showinfo("Siker", "Kedvencekből törölve.")
            self.feltolt_recept_lista(self.app.listaz_mentettek())
        else:
            messagebox.showwarning("Figyelem", "Ez a recept nincs a kedvencek között.")

    def ablak_bezarasa(self):
        self.app.mentes("receptek.json")
        self.destroy()


def futtatas():
    alkalmazas = bb_app()
    alkalmazas.betoltes("receptek.json")
    app = bb_szakacskonyv(alkalmazas)
    app.mainloop()
    alkalmazas.mentes("receptek.json")
