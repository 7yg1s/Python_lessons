#importuojamos bibliotekos visuomet rasomos pirmose eilutese!!!!!!
import os
import shutil



# vardas = "Jonas"
# amzius = "30"
# ar_jonas_moka_programuoti = False
# jono_pirkiniu_krepselio_suma = 34.5
# print(type(ar_jonas_moka_programuoti))
# print("Mano draugo vardas yra " + vardas + " jo amzius", amzius, ar_jonas_moka_programuoti, jono_pirkiniu_krepselio_suma);


#listas(array) masyvas = []
# vaisiai = ["Obuolys", "Arbuzas", "Bananas", "Kriause"]
# print(type(vaisiai))

# vaisiai = ["Obuolys", "Arbuzas", "Bananas", "Kriause"]
# ilgis = len(vaisiai)
# print(ilgis)

#slicing
# vaisiai = ["Obuolys", "Arbuzas", "Bananas", "Kriause"]
# print(vaisiai[:-1])

#append - prideti reiksme
# vaisiai = ["Obuolys", "Arbuzas", "Bananas", "Kriause"]
# pridedame_vaisiu = vaisiai.append("Melionas")
# print(vaisiai)

#append - prideti reiksme i tam tikra vieta
# vaisiai = ["Obuolys", "Arbuzas", "Bananas", "Kriause"]
# vaisiai.insert(0,"Melionas")
# print(vaisiai)

#Keiciam indexa
# vaisiai = ["Obuolys", "Arbuzas", "Bananas", "Kriause"]
# keiciam_reiksme = vaisiai[1] = "Kivis"  arba vaisiai[1] = "Kivis"
# print(vaisiai)

# Suzinoti indexa
# vaisiai = ["Obuolys", "Arbuzas", "Bananas", "Kriause"]
# indeksas = vaisiai.index("Arbuzas")
# print(indeksas)

# # Istrinti
# vaisiai = ["Obuolys", "Arbuzas", "Bananas", "Kriause"]
# vaisiai.remove("Bananas")
# print(vaisiai)

# Istrinti pagal indexa
# vaisiai = ["Obuolys", "Arbuzas", "Bananas", "Kriause"]
# vaisiai.pop(2)
# print(vaisiai)

# dictionary - structure = my_dict = {key1:value1, key2:value2}
# zodynas = {
#     "Vardas": "Jonas",
#     "Amzius": 30,
#     "Miestas": "Vilnius"
# }
# print(zodynas["Miestas"])
#
# #prideti nauja rakta
# zodynas = {
#     "Vardas": "Jonas",
#     "Amzius": 30,
#     "Miestas": "Vilnius"
# }
# zodynas["ar_studentas"] = True
# print(zodynas)

#pasalinti
# zodynas = {
#     "Vardas": "Jonas",
#     "Amzius": 30,
#     "Miestas": "Vilnius"
# }
# del zodynas ["Miestas"]
# print(zodynas)

##Didesnis zodynas dictionary
# studentai = {
#     "Jonas": {
#         "Amzius":32,
#         "Miestas": "Kaunas",
#         "Profesija": "Inzinierius"
#         },
#     "Ona": {
#         "Amzius":25,
#         "Miestas": "Klaipeda",
#         "Profesija": "Gydytoja"
#         },
#     "Antanas": {
#         "Amzius": 46,
#         "Miestas": "Vilnius",
#         "Profesija": "Mokytojas"
#         }
# }
# print(studentai["Jonas"])

# studentai = [
#         {
#         "Vardas": "Jonas",
#         "Amzius":32,
#         "Miestas": "Kaunas",
#         "Profesija": "Inzinierius"
#         },
#         {
#         "Vardas": "Ona",
#         "Amzius":25,
#         "Miestas": "Klaipeda",
#         "Profesija": "Gydytoja"
#         },
#         {
#         "Vardas": "Antanas",
#         "Amzius": 46,
#         "Miestas": "Vilnius",
#         "Profesija": "Mokytojas"
#         }
# ]
# print(studentai[0])

#Pridedamas naujas studentas
# studentai = [
#         {
#         "Vardas": "Jonas",
#         "Amzius":32,
#         "Miestas": "Kaunas",
#         "Profesija": "Inzinierius"
#         },
#         {
#         "Vardas": "Ona",
#         "Amzius":25,
#         "Miestas": "Klaipeda",
#         "Profesija": "Gydytoja"
#         },
#         {
#         "Vardas": "Antanas",
#         "Amzius": 46,
#         "Miestas": "Vilnius",
#         "Profesija": "Mokytojas"
#         }
# ]
# naujas_studentas = {
#         "Vardas": "Petras",
#         "Amzius": 46,
#         "Miestas": "Kaunas",
#         "Profesija": "Siuvejas"
# }
# studentai.append(naujas_studentas)
# print(studentai)
# if salyga - if salyga: jusu veiksmai:
# amzius = 20
# if amzius >= 18:
#     print("Asmuo yra pilnametis")

#if salyga su negiama funkcija
# amzius = 15
# if amzius >= 18:
#     print("Asmuo yra pilnametis")
# else:
#     print("Asmuo nera pilnametis")

#if salyga elif galima naudoti kiek nori kartu didinama ar mazinama reiksme
# amzius = 5
# if amzius >= 18:
#     print("Asmuo yra pilnametis")
# elif amzius > 13:
#     print("Asmuo yra pauglys")
# else:
#     print("Asmuo nera pilnametis")

#papildomos reiksmes gali buti naudojamos kaip: and, if not, or

# vaisiai = ["bananas", "kivis", "obuolys"]
# if "kivis" in vaisiai:
#     print("Vaisius kivis")
# elif not "kivis" in vaisiai:
#     print("Asmuo yra pauglys")
# else:
#     print("Vaisiu sarasas tuscias")

# vaisiai = ["bananas"]
# if not vaisiai:         ##if not - tikrina ar yra kazkas sarase
#     print("Vaisiu sarasas tuscias")
# elif "kivis" in vaisiai:
#     print("Vaisius kivis")
# else:
#     print("Vaisius nerastas, taciau sarase yra elementu")


#dar vienas if pavizdys su papildomu if kitame if;
# age = 18
# has_id = False
#
# if age >=18:
#     if has_id:
#         print("Gali balsuoti")
#     else:
#         print("jumes reikia asmens tapatybes korteles")
#
# else:
#     print("Jums dar negalima balsuoti")

###########################VISKA SUJUNGSIM KAS YRA VIRSUJE############################################# #Norime rasti prekes kategorija "Mesa" ir prekes "Vistiena";
# prekiu_kategorijos = ['Vaisiai', 'Mesa', 'Darzoves']
#
# prekes = {
#     'Vaisiai': ['Obuoliai','Bananai'],
#     'Mesa': ['Kiauliena','Vistiena'],
#     'Darzoves': ['Bulves','Pomidorai']
# }

# norima_kategorija = 'Darzoves'
# norima_preke = 'Bulves'
#
# if norima_kategorija in prekiu_kategorijos:
#     if norima_preke in prekes[norima_kategorija]:
#         print(f"Parduotuveje yra {norima_preke}")
#     else:
#         print(f"parduotuveje nera {norima_preke}")
# else:
#     print(f"Parduotuveje nera prekiu kategorijos: {norima_kategorija}")


# 1 užduotis:
# 1 dalis. Sukurkite sąrašą su žmonių vardais ir amžiumi:


# 2 dalis. Jūsų užduotis - parašyti kodą, kuris išvestų kiekvieno žmogaus vardą su amžiumi: "nepilnametis", "suaugęs" arba "vaikas" (jei amžius yra 18).

# Zmones = [
#         {
#         "Vardas": "Algirdas",
#         "Amzius":15,
#         },
#         {
#         "Vardas": "Audrius",
#         "Amzius":18,
#         },
#         {
#         "Vardas": "Aurimas",
#         "Amzius": 24,
#         }
# ]
# print(type(Zmones))
# zmogus = Zmones[0]
#
# if zmogus['Amzius'] >= 18:
#     print(f'{zmogus["Vardas"]} yra pilnametis')
# if zmogus['Amzius'] < 18:
#     print(f'{zmogus["Vardas"]} yra pauglys')  #####taip prodedama reiksme is lenteles tarp {} skliaustu
#

# darbuotojas = {
#         "Vardas": "Tomas",
#         "Atlyginimas": 2200,
#         "Pareigos": "Inzinierius"
# },
#
# if darbuotojas["Pareigos"] == "Inzinierius"
#
#


# 3 užduotis:
# 1 dalis: Sukurkite sąrašą su knygų informacija(Pavadinimas, išleidimo metai);
# 2 dalis: Suraskite norimos knygos metus pagal vartotojo įvesti;

# knygos = [
#         {"pavadinimas": "Haris Poteris", "isleidimo metai": 1997},
#         {"pavadinimas": "Moby Dick", "isleidimo metai": 1851},
#         {"pavadinimas": "Metai", "isleidimo metai": 2002},
# ]
# print(type(knygos))

# knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus kuriu ieskote_> "))

# if knygos[0] ["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#         print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['pavadinimas']}")
# if knygos[0] ["isleidimo metai"] != knyga_pagal_ieskomus_metus:
#         print("Tokia knyga nerasta")

# if knygos[0] ["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#         print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['pavadinimas']}")
# else:
#         print("Tokia knyga nerasta")

# try:
#         knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus kuriu ieskote_> "))
#
#         if knygos[0]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#                 print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['pavadinimas']}")
#         elif knygos[1]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#                 print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[1]['pavadinimas']}.")
#         elif knygos[2]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#                 print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[2]['pavadinimas']}.")
#         else:
#                 print(f"Deja, knygų išleistų {knyga_pagal_ieskomus_metus} metais nėra.")
# except ValueError:
#         print(f"Deja, knygu isleistu {knyga_pagal_ieskomus_metus} metais nera.")
##########################################################################################################################################


#importuojamos bibliotekos VISUOMET rasomos pirmose eilutese!!!


# dabartinis_katalogas = os.getcwd()
#
# naujas_katalogas = input("Prasome nurodyti naujo katalogo lokacija:")
#
# try:
#     naujas_katalogas = os.chdir(naujas_katalogas)
#     if os.getcwd() == naujas_katalogas:
#         print(f"Darbinis katalogas sekmingai pakeistas i {naujas_katalogas}")
#     turinys = os.listdir(naujas_katalogas)
#     print(", ".join(turinys))
# except FileNotFoundError:
#     print(f"Deja aplanlas '{naujas_katalogas}' nerastas")

# EXTENSION_MAP ={
#     '.jpg': "Images",
#     '.jpeg': "images",
#     '.png': "Images",
#     '.gif': "Images",
#     '.pdf': "Documents",
#     '.txt': "Documents"
# }
# print(type(EXTENSION_MAP))
# filename = input("Please write the name of the file you want to organize:")
#
# file_extension = os.path.splitext(filename)[1]
#
# try:
#     if os.path.exists(filename) and file_extension in EXTENSION_MAP:
#         directory_name = EXTENSION_MAP[file_extension]
#
#         #create the directory if it doesn't exist
#         if not os.path.exists(directory_name):
#             os.makedirs(directory_name)
#
#         #move the file
#         shutil.move(filename, os.path.join(directory_name, filename))
#         print(f"{filename} has been moved to {directory_name}")
#     else:
#         print("The file does not exist or its extension is not recognized")
# except PermissionError:
#     print(f"Error: You don't have permissions to move '{filename}'")





# if salyga: jusu veiksmai; jeigu norim priesingos reiksmes, tai tada rasom else lygiai taip pat, kaip ir if;
#
# darbuotojas = {
#     "Vardas": "Tomas",
#     "Atlyginimas": 2200,
#     "Pareigos": "inzinierius"
# }
#
# if darbuotojas["Pareigos"] == "inzinierius":
#     #padidinti 10 proc. atlyginima
#     #ilgesnis uzrasymas
#     # darbuotojas["Atlyginimas"] = darbuotojas["Atlyginimas"] * 1.10
#     #trumpesnis uzrasymas
#     # darbuotojas["Atlyginimas"] *= 1.10
#
# # du lygu == lyginimas, o = yra priskyrimas
#
# print(darbuotojas)
