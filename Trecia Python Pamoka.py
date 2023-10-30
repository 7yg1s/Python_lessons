#####################----Objektinis  programavimas!!!----###########################

########_Uzduotis-########
# class automobilis:
#     def __init__(self, marke, modelis, metai, variklio_turis, kuro_tipas):
#         self.marke = marke
#         self.modelis = modelis
#         self.metai = metai
#         self.varilio_turis = variklio_turis
#         self.kuro_tipas = kuro_tipas
#         self.rida = 0
#
#
#     def automobilio_pavadinimas(self):
#         return (f"Automobilis: {self.marke}\nAutomobilio Modelis:{self.modelis}\nAutomobilio pagaminimo metai:{self.metai}\n"
#                 f"Variklio turis:{self.varilio_turis}\nKuro tipas:{self.kuro_tipas}")
#
#     def vaziuoti(self, km):
#         self.rida += km
#         return f"Vaziuojama {km} km. Bendra rida{self.rida} km"
#
# auto1 = automobilis("Audi", "A8", 2021, 3.0, "Benzinas")
# auto2 = automobilis("Toyota", "Avensis", 2013, 2.0, "Benzinas")
#
#
# print(auto1.automobilio_pavadinimas())
# print(auto1.vaziuoti(150))
# print()
# print(auto2.automobilio_pavadinimas())
# print(auto2.vaziuoti(150))


##########-UZDUOTIS2-#############
# class gyvunas(object):
#     def __init__(self, rusis, svoris, amzius, vardas):
#         self.rusis = rusis
#         self.svoris = svoris
#         self.amzius = amzius
#         self.vardas = vardas
#
#     def gyvuno_aprasymas(self):
#         return f"Gyvunas:{self.rusis}\nVardas:{self.vardas}\nSvoris:{self.svoris}\nAmzius:{self.amzius}"
#     def valgyti(self):
#         return f'{self.vardas} eina valgyti'
#
#     def prisistatymas(self):
#         return f"As esu {self.rusis} ir mano vardas {self.vardas}"
#
# gyvunas1 = gyvunas("Liutas",200,5, "Karalius")
#
# print(gyvunas1.gyvuno_aprasymas())
# print()
# print (gyvunas1.valgyti())
# print()
# print(gyvunas1.prisistatymas())
#

########## Uzduotis: padaryti mano darbu sarasa. ################
# from colorama import init, Fore
# init()
# class Uzduotis:
#     def __init__(self, pavadinimas, aprasymas):
#         self.pavadinimas = pavadinimas
#         self.aprasymas = aprasymas
#         self.atlikta = False
#
#     def atlikimas(self):
#         self.atlikta = True
#         print(f"Uzduotis '{self.pavadinimas}' buvo atlikta")
#
#     def info(self):
#         return f"{Fore.GREEN}Pavadinimas {self.pavadinimas}\nAprasymas: {self.aprasymas}"
#
# class TodoSarasas:
#     def __init__(self):
#         self.uzduociu_sarasas = []
#
#     def prideti_uzduoti(self, pavadinimas, aprasymas):
#         uzduotis = Uzduotis(pavadinimas, aprasymas)
#         self.uzduociu_sarasas.append(uzduotis)
#
#     def visos_uzduotys(self):
#         if not self.uzduociu_sarasas:
#             print("Uzduociu sarasas yra tuscias!")
#         for uzduotis in self.uzduociu_sarasas:
#             print(uzduotis.info())
#
#     def pazymeti_kaip_atlikta(self, pavadinimas):
#         for uzduotis in self.uzduociu_sarasas:
#             if uzduotis.pavadinimas == pavadinimas:
#                 uzduotis.atlikimas()
#                 return
#         print(f"fUzduotis pavadinimu: '{pavadinimas}' nerasta")
#
# todo_sarasas = TodoSarasas()
#
# while True:
#     print("\nPasirinkite veiksma:")
#     print("1. Prideti uzduoti")
#     print("2. Perziureti uzduoti")
#     print("3. Pazymeti uzduoti kaip atlikta ")
#     print("4. Iseiti")
#     pasirinkimas = input("Prasome pasirinkti veiksma")
#
#     if pasirinkimas == "1":
#         pavadinimas = input("iveskite uzduoties pavadinima:")
#         aprasymas = input("Iveskite uzduoties aprasyma:")
#         todo_sarasas.prideti_uzduoti(pavadinimas, aprasymas)
#         print("uzduotis prideta sekmingai!")
#
#     elif pasirinkimas == "2":
#         todo_sarasas.visos_uzduotys()
#     elif pasirinkimas == "3":
#         pavadinimas = input("Iveskite uzduoties pavadinimas kuria norite pazymeti kaip atlikta:")
#         todo_sarasas.pazymeti_kaip_atlikta(pavadinimas)
#     elif pasirinkimas == "4":
#         print("Iseinama..")
#         break
#     else:
#         print("Neteisingas pasirinkimas! Prasome bandyti dar karta!")


#########---Naujas uzdavinys: sukurti banko saskaita i kuria galima ideti pinigu, isimti ir likutis-----################################
#
# class saskaita:
#     def __init__(self, vardas, pavarde, pradinis_likutis = 0):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pradinis_likutis = pradinis_likutis
#
#     def ideti_pinigu(self, suma):
#         if suma > 0:
#             self.pradinis_likutis += suma
#         else:
#             print("Klaida, negalima ideti neigiamos sumos")
#
#     def nusiimti_pinigu(self,suma):
#         if  suma >= 0:
#             if  self.pradinis_likutis > suma:
#                 self.pradinis_likutis -= suma
#                 print(f'Jus sekmingai nuimete pinigus {suma}')
#             else:
#                 print("klaida, jusu likutis nepakankamas")
#         else:
#             print("Klaida, negalima isimti neigiamos sumos")
#
#     def saskaitos_likutis(self, suma):
#         return f"Kliento: {self.vardas} {self.pavarde} saskaitos likutis yra: {self.pradinis_likutis}"
#
# numeris_vienas = saskaita("Jonas", "Jonas", 1200)
#
#
#
# numeris_vienas.ideti_pinigu(200)
#
# numeris_vienas.nusiimti_pinigu(50)
#
# print(numeris_vienas.pradinis_likutis)



#----Uzduotis:
# Sukurkite Studentas klase kuri reprezentuoja individualų studentą, turintį
# savo vardą, pavardę, amžių, studento numerį ir pažymių sąrašą.
# Antroje klasėje StudentuValdymoSistema - tai klasė, skirta valdyti studentų
# sąrašą. Ji leidžia pridėti naujus studentus, gauti informaciją apie konkretų
# studentą pagal jo numerį ir išvesti visų studentų informaciją.


class Studentas:
    def __init__(self, vardas, pavarde, amzius, studento_numeris, pazymiai = None):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        self.studento_numeris = studento_numeris
        self.pazymiai = pazymiai if pazymiai else []

    def studento_vidurkis(self):
        return sum(self.pazymiai) / len(self.pazymiai) if self.pazymiai else 0

    def prideti_pazymi(self, pazymys):
        self.pazymiai.append(pazymys)

    def studento_informacija(self):
        return (f"Studentas: {self.vardas} {self.pavarde}, amzius {self.amzius},"
                f" studento numeris: {self.studento_numeris}, pazymiai: {self.pazymiai}")

    def pasalinti_pazymi(self, pazymys):
        if 0 <= pazymys < len(self.pazymiai):

            del self.pazymiai[pazymys]
        else:
            print("toks pazymys nerastas")




class StudentuValdymoSistema:
    def __init__(self):
        self.studentu_sarasas = []

    def prideti_studenta(self, studentas):
        self.studentu_sarasas.append(Studentas)
        print("studentas sekmingai pridetas")

    def pasalinti_studenta(self, studento_numeris):
        naujas_studentu_sarasas = []
        for s in self.studentu_sarasas:
            if s.studento_numeris != studento_numeris:
                naujas_studentu_sarasas.append(s)
        self.studentu_sarasas = naujas_studentu_sarasas

    def visi_studentai(self):
        return self.studentu_sarasas

    def __str__(self):
        return "\n".join(str(studentas) for studentas in self.studentu_sarasas )





studentu_sistema = StudentuValdymoSistema()

studentas1 = Studentas("Jonas", "Jonaitis",22,132211)
studentas2 = Studentas("Jonas", "Petraitis",23,132212)

studentas1.prideti_pazymi(7)
studentas1.prideti_pazymi(5)
studentas1.prideti_pazymi(3)

studentu_sistema.prideti_studenta(studentas1)

studentas1.pasalinti_pazymi(1)

studentas1.studento_informacija()
studentas2.studento_informacija()

for studentas in studentu_sistema.visi_studentai():
    print(studentas)

print(StudentuValdymoSistema)