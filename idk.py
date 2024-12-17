from abc import ABC, abstractmethod



class Letiště:
    def __init__(self, kód, jméno):
        self.kód = kód
        self.jméno = jméno
        self.letadelka = []

    def zobrazit_letiště(self):
        return f"Letiště: {self.jméno}"

    def přidej_letadlo(self, letadlo):
        self.letadelka.append(letadlo)

    def odeber_letadlo(self, letadlo):
        self.letadelka.remove(letadlo)

    def vypis_all_letadla(self):
        if not self.letadelka:
            return "Žádná letadla nejsou na letišti."
        return "\n".join([letadlo.zobrazit_letadlo() for letadlo in self.letadelka])



class Clovek(ABC):
    def __init__(self, jmeno, prijmeni, datum_narozeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.datum_narozeni = datum_narozeni

    def vypis_celou_jmeno(self):
        return f"{self.jmeno} {self.prijmeni}"



class Pilot(Clovek):
    def __init__(self, jmeno, prijmeni, datum_narozeni, typ_letadla, kapitan=False):
        super().__init__(jmeno, prijmeni, datum_narozeni)
        self.typ_letadla = typ_letadla
        self.kapitan = kapitan

    def popis(self):
        return f"Pilot: {self.vypis_celou_jmeno()}, Typ letadla: {self.typ_letadla}, Kapitán: {'Ano' if self.kapitan else 'Ne'}"

    def je_kapitan(self):
        return self.kapitan



class Pasazer(Clovek):
    def __init__(self, jmeno, prijmeni, datum_narozeni):
        super().__init__(jmeno, prijmeni, datum_narozeni)

    def popis(self):
        return f"Pasážer: {self.vypis_celou_jmeno()}"



class Letadlo:
    def __init__(self, typ, společnost, unikátní_kód, kapitan=None, pasazeri=None):
        self.typ = typ
        self.společnost = společnost
        self.unikátní_kód = unikátní_kód
        self.kapitan = kapitan if kapitan else None
        self.pasazeri = pasazeri if pasazeri else []

    def zobrazit_letadlo(self):
        return f"Letadlo: {self.typ} - Společnost: {self.společnost}, Kód: {self.unikátní_kód}"

    def zobrazit_kapitana_a_pasazery(self):
        pasazeri_names = ", ".join([pasazer.vypis_celou_jmeno() for pasazer in self.pasazeri])
        return f"Kapitán: {self.kapitan.vypis_celou_jmeno()}, Pasážéři: {pasazeri_names}"



class FlightManager:
    def fly(self, odkud, kam, letadlo):

        odkud.odeber_letadlo(letadlo)


        kam.přidej_letadlo(letadlo)


        flight_info = f"Letadlo {letadlo.zobrazit_letadlo()} letí z {odkud.jméno} do {kam.jméno}.\n"
        flight_info += f"Informace o letu: {letadlo.zobrazit_kapitana_a_pasazery()}"
        return flight_info



letiště1 = Letiště("PRG", "Letiště Václava Havla")
letiště2 = Letiště("PRD", "prdihrad")
letiště3 = Letiště("SMD", "smradihrad")


letadlo1 = Letadlo("Boeing 737", "ČSA", "737-001")
letadlo2 = Letadlo("Airbus A320", "SmartWings", "A320-002")
letadlo3 = Letadlo("Boeing 777", "Emirates", "777-003")
letadlo4 = Letadlo("bombardak","prdimates", "786-8643" )


pilot1 = Pilot("Jan", "Novak", "1985-03-15", "Hulihlad", True)
pilot2 = Pilot("Petr", "Svoboda", "1990-06-25", "vitekkvitek", False)


pasazer1 = Pasazer("Lucie", "Dvořáková", "1995-11-12")
pasazer2 = Pasazer("Jakub", "Kučera", "1988-02-28")


letadlo1.pasazeri.append(pasazer1)
letadlo1.pasazeri.append(pasazer2)


letadlo1.kapitan = pilot1
letadlo2.kapitan = pilot2


letiště1.přidej_letadlo(letadlo1)
letiště1.přidej_letadlo(letadlo3)
letiště2.přidej_letadlo(letadlo2)
letiště3.přidej_letadlo(letadlo4)


flight_manager = FlightManager()


print(flight_manager.fly(letiště1, letiště2, letadlo1))
print(flight_manager.fly(letiště2, letiště1, letadlo2))


print("\nLetadla na letišti Václava Havla:")
print(letiště1.vypis_all_letadla())

print("\nLetadla na letišti prdihrad:")
print(letiště2.vypis_all_letadla())


print("\nLetadla na letišti smradihrad:")
print(letiště3.vypis_all_letadla())
