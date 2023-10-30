#KUR NAUDOJOMA IF

#for raktas in seka
#print (raktas)
# for i in range(5):
#     print("skaicius", i)

#sarasas su "for"
# skaiciai = [1,2,3,4,5]
# for skaicius in skaiciai:
#     print("Mano saraso skaicius", skaicius)

#tekstas su "for"
# tekstas = "Python data science"
# for raide in tekstas:
#     print(raide)


#zodynas su "for"
# zodynas = {"a":1, "b":2, "c":3}
# for raktas in zodynas:
#     print(raktas, zodynas[raktas])

#sustabdo pasiekus skaiciu su break po if
# sarasas = [1,2,3,4,5]
# for skaicius in sarasas:
#     if skaicius == 3:
#         break
#     print(skaicius)

#continue tesia darba, bet praleidzia 3
# sarasas = [1,2,3,4,5]
# for skaicius in sarasas:
#     if skaicius == 3:
#         continue
#     print(skaicius)


# skaiciai = [15,20,35,82,44]
#
# suma = sum(skaiciai)
#
# vidurkis = suma /len(skaiciai)
# #print("Gautas vidurkis", vidurkis)
#
# for skaicius in skaiciai:
#     if skaicius > vidurkis:
#         print(skaicius)


#Atspausdinti vardus atskirose eilutese
# sarasas = ["Jonas", "Ona", "Petras", "Albinas"]
# for vardas in sarasas:
#     print(vardas)
#
# sarasas = ["Jonas", "Ona", "Petras", "Albinas"]
# for vardas in sarasas:
#     print(vardas+'\n')

# sarasas = ["Jonas", "Ona", "Petras", "Albinas"]
# print('\n'.join(sarasas))


#parasyti zodi atvirskciai su "for"
# title_1 = "python"
# title_2 = ""
# for letter in title_1:
#     title_2 = letter+title_2
#     print(title_2)


#Daugybos lenteles sudarymas
# daugybos_lentele = 10
# for i in range(1, daugybos_lentele +1):
#     for j in range(1,daugybos_lentele +1):
#         print(i*j, end="\t")                                   #(\t - reiskia tarpa)
#     print()

#Parasyti sakyni be kabuciu su for.
# sarasas = ["Labas", "rytas", "mieli", "mokiniai"]
# sarasas_2 = ""
# for zodis in sarasas:
#     sarasas_2 += zodis+" "
# sujungtas_tekstas = sarasas_2.rstrip()
# print(sujungtas_tekstas)

# sarasas = ["labas", "rytas", "suraitytas", "skanios", "kavytes"]
# for i in sarasas:
#     print(i, end=" ")
###################################################THE END OF "FOR"###################################################################

######################################################-WHILE-#########################################################################


# skaicius = 1
# while skaicius <= 20:
#     print(skaicius)
#     skaicius +=1

#ieskoma teigiamo skaiciaus
# ivestis = int(input("iveskite teigiama skaiciu:"))
# while ivestis < 0:
#     print("jusu skaicius neigiamas")
#     ivestis = int(input("bandykite dar karta:"))
# print("ivedete teigiama skaiciu")
#

#Zaidimas atspeti skaiciu
# atsakymas = 5
# spejimas = int(input("spekite skaiciu nuo 1 iki 10:"))
# while spejimas != atsakymas:
#     spejimas != int(input("Neteisingas atsakymas! Bandykite dar karta:"))
# print("Sveikiname, atspejote!")


#sukiriam programa kuri su while kuri atlieka veiksma paspaudus tam tikra skaiciu#
#     print("----Meniu----")
#     print("1. Atspausdiniti pasisveikinima")
#     print("2. Iveskite nauja varda")
#     print("3. Iseiti")
#
#     pasirinkimas = input("Iveskite savo pasirinkima (1/2/3):")
#     if pasirinkimas =="1":
#         print(f"Labas!")
#     elif pasirinkimas == "2":
#         vardas = input("iveskite nauja varda:")
#
#         print("Sekmingai ivedete nauja varda!")
#         print(f"Jusu vardas pakeistas i {vardas}")
#     elif pasirinkimas == "3":
#         print("Aciu, kad naudojates programa. IKI!")
#         break
#     else:
#         print("Neteisingas pasirinkimas! Bandykite dar karta")
#

####Tokia pati programa kaip virsuje tik uzbaigia uzduoti kaip ivedus teisinga skaiciu#######

# ar_veikia = True
# while True:
#     print("----Meniu----")
#     print("1. Atspausdiniti pasisveikinima")
#     print("2. Iveskite nauja varda")
#     print("3. Iseiti")
#
#     pasirinkimas = input("Iveskite savo pasirinkima (1/2/3):")
#     if pasirinkimas =="1":
#         print(f"Labas!")
#     elif pasirinkimas == "2":
#         vardas = input("iveskite nauja varda:")
#
#         print("Sekmingai ivedete nauja varda!")
#         print(f"Jusu vardas pakeistas i {vardas}")
#     elif pasirinkimas == "3":
#         print("Aciu, kad naudojates programa. IKI!")
#         ar_veikia = False
#     else:
#         print("Neteisingas pasirinkimas! Bandykite dar karta")


#Parasyti programa kurioje yra tam tikras zodis kol atspes ta zodi

# atsakymas = "Sniegas"
# spejimas = int(input("Spekite zodi is raides S:"))
#
# while spejimas != atsakymas:
#     spejimas != int(input("spekite paslaptingaji zodi"))
# print("Sveikinu atspejote!")


# atsakymas = 5
# spejimas = int(input("spekite skaiciu nuo 1 iki 10:"))
# while spejimas != atsakymas:
#     spejimas != int(input("Neteisingas atsakymas! Bandykite dar karta:"))
# print("Sveikiname, atspejote!")



###parasyti programa kurioje irasius skaiciu turi ismesti to skaiciaus daugybos lentele

# max_skaicius = 1
# pasirinkimas = int(input("pasirinkite skaiciu nuo 1 iki 10:"))
# while max_skaicius <= 10:
#     result = max_skaicius * pasirinkimas
#     print(f'{pasirinkimas} x {max_skaicius} = {result}')
#     max_skaicius += 1



##################################-FUNKCIJA-########################################
#sintakse finkcijose: def funkcijospavadinimas(argumentai)

# def pasisveikinti():
#     print("hello python")
#
# pasisveikinti()

# if __name__=="__bandymas__": #funkcijos iskvietimas is kitos programps
#     pasisveikinti()


#pasisveikinimas!
# def pasisveikinti(vardas):
#     print(f"Hello {vardas}")
#
# pasisveikinti("Zygimantas")

####skaiciavimas su funkcija

# def suma(a,b):
#     return a + b
#
# atsakymas = suma(5,3)
# print(atsakymas)

#tas pats sprendimas kaip virsuje
# def suma(a,b):
#     return a + b
#
# print(suma(5,3))


#Naujas projektas: knygu valdymo sistema, prideti, keisti ir t.t.
#
# def rodyti_meniu():
#     print("----Meniu----")
#     print("1. Prideti knyga")
#     print("2. perziureti visas knygas")
#     print("3. Ieskoti knygos pagal pavadinima")
#     print("4. Iseiti")
#
# def prideti_knyga(knygu_sarasas):
#     pavadinimas = input("Iveskite knygos pavadinima:")
#     autorius = input("Iveskite knygos autoriu")
#     knygu_sarasas.append({"pavadinimas": pavadinimas,"autorius":autorius})
#     print(f"Knyga '{pavadinimas}' prideta!")
#
# def perziureti_knygas(knygu_sarasas):
#     for knyga in knygu_sarasas:
#         print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#
# def ieskoti_knygos(knygu_sarasas):
#     ieskomas_pavadinimas = input("Iveskiti knygos pavadinima kurio ieskote:")
#     rasti_knygas = [knyga for knyga in knygu_sarasas if ieskomas_pavadinimas.lower() in knyga['pavadinimas'].lower()]
#
#     if rasti_knygas:
#         for knyga in rasti_knygas:
#             print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#     else:
#         print(f"Knyga su pavadinimu: '{ieskomas_pavadinimas}'nerasta")
#
# def main():
#     knygu_sarasas = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksma (1-4):")
#         if pasirinkimas == "1":
#             prideti_knyga(knygu_sarasas)
#         elif pasirinkimas == "2":
#             perziureti_knygas(knygu_sarasas)
#         elif pasirinkimas == "3":
#             ieskoti_knygos(knygu_sarasas)
#         elif pasirinkimas == "4":
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prasome nuo 1 iki 4")
#
# if __name__ == '__main__':
#     main()


#########_Bankine_sistema###############
#ideti pinigus, isimti pinigus, uzdaryti saskaita
#
# banko_saskaitos = {
#
#
# }
# def rodyti_meniu():
#     print("\n=== Mini Banko sistema ===")
#     print("1. Atidaryti naują saskaitą")
#     print("2. Įnešti pinigus")
#     print("3. Nusiimti pinigus")
#     print("4. Peržiūrėti sąskaitos likutį")
#     print("5. Uždaryti sąskaitą")
#     print("6. Išeiti")
#
# def prideti_saskaita():
#     saskaitos_turetojas = input("Iveskite vardą: ")
#     pradinis_likutis = int(input("Įveskite pradinį pinigų likutį: "))
#     saskaitos_nr = len(banko_saskaitos) + 1
#     banko_saskaitos[saskaitos_nr] = {"saskaitos_turetojas": saskaitos_turetojas, "pradinis_likutis": pradinis_likutis}
#     print(f"Nauja sąskaita '{saskaitos_nr}' sekmingai prideta!")
#
# def inesti_pinigus():
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.: "))
#     suma = int(input("Įveskite įnešamų pinigų sumą: "))
#     banko_saskaitos[saskaitos_nr]["pradinis_likutis"] += suma
#     print(f"Į sąskaitą nr.: '{saskaitos_nr}' sėkmingai įnešta '{suma}' eurai")
#
# def nusiimti_pinigus():
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.: "))
#     suma = int(input("Įveskite nusiimamų pinigų sumą: "))
#     if suma <= banko_saskaitos[saskaitos_nr]["pradinis_likutis"]:
#         banko_saskaitos[saskaitos_nr]["pradinis_likutis"] -= suma
#         print(f"Iš sąskaitos nr.: '{saskaitos_nr}' sėkmingai nusiimta '{suma}' eurai")
#     else:
#         print(f"Jūsų pradinis likutis yra per mazas. Jis yra: '{banko_saskaitos[saskaitos_nr]['pradinis_likutis']}' eurai")
#
# def perziureti_likuti():
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.:"))
#     likutis = banko_saskaitos[saskaitos_nr]["pradinis_likutis"]
#     print(f"Sąskaitos nr.: '{saskaitos_nr}' likutis yra '{likutis}' eurai")
#
# def istrinti_saskaita():
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.:"))
#     del banko_saskaitos[saskaitos_nr]
#     print(f"Banko sąskaita nr.: '{saskaitos_nr}' buvo ištrinta")
#
#
# def main():
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksmą(1-6): ")
#         if pasirinkimas == "1":
#             prideti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "2":
#             inesti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "3":
#             nusiimti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "4":
#             perziureti_likuti(banko_saskaitos)
#         elif pasirinkimas == "5":
#             istrinti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "6":
#             print("Iki greito!")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prasome pasirinkti nuo 1 iki 6")
#
# main()



#Sukurkite funkciją pvm_skaiciuokle(), kuri priimtų kainą be PVM ir grąžintų kainą su 21% PVM.

# def pvm_skaiciuokle (kaina):
#     pvm_tarifas = 0.21
#     kaina_su_pvm = kaina + kaina * pvm_tarifas
#     print(kaina_su_pvm, 'kaina su PVM.')
#
# kaina_be_pvm = float(input("Kaina be PVM:"))
# pvm_skaiciuokle(kaina_be_pvm)

# def pvm_skaiciuokle(kaina):
#     print(f"kaina su pvm yra {kaina *1.21} eurai")
#
# kaina_be_pvm = float(input("Kaina be PVM:"))
# pvm_skaiciuokle(kaina_be_pvm)

# def be_pvm(kaina):
#     return kaina * 1.21
#
# kaina_su_pvm = be_pvm(int(input("Iveskite kaina be PVM: ")))
# print("Kaina su PVM", + kaina_su_pvm)


