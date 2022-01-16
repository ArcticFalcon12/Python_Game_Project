import time #Importáljuk az időt ezzel tudunk késleltetni
#Rájönni hogyan válaszolhat a felhasználó a különböző esetekben
valasz_A = ["A", "a"]
valasz_B = ["B", "b"]
#A felhasználó csak a megadott választásokkal válaszolhasson
szukseges = ("\nCsak A vagy B-t használj!\n")
#Bemutatkozás
def intro():
 print("Üdvözöllek",'\033[1m' + 'Jack The Ripper: Resurection; The Game' + '\033[0m'
"Van számodra egy történetem! Szeretnél részt venni benne?")
 time.sleep(0.5)
 print ("""A. Igen szeretnék!
B. Kösz inkább kihagyom! """)
#Első választási lehetősége a játékosnak
 choice = input(">>> ")
 if choice in valasz_A:
     valasztas_kezdes()
 elif choice in valasz_B:
    print("\n Hát ezt sajnálattal hallom!..")
 else:
    print (szukseges)
def valasztas_kezdes():
 print("Legyen hát! Kezdődjön a show!")
 time.sleep(2)
 print ("Felkelsz egy ismeretlen házban, egy szobában. Körülnézel és azt látod, hogy ki van kötve az egyik kezed."
 "Pánikba esel. Egy baldachinos ágyon vagy kikötve."
 "A közelben látsz egy rozsdás kést, amivel megpróbálhatod elvágni a kötelet. Mit teszel? ")
 time.sleep(1)
 print ("""A. Megpróbálod a másik kezeddel kikötözni magadat!
B. Megpróbálsz elmenni a késért!""")
 choice = input(">>> ")
 if choice in valasz_A:
     valasztas_kez()
 elif choice in valasz_B:
     valasztas_kes()
 else:
    print (szukseges)
def valasztas_kes(): 
 print ("Miközben lelépsz az ágyról, megreccsen az öreg padlódeszka a lábad alatt. Megijedsz a hangjától."
         "Szépen lassan megpróbálsz odamenni a késért, de leversz egy képet az egyik szekrényről, és meglátod, hogy téged ábrázol."
         "Az arcod hirtelen látványától felsikoltasz. Lépteket hallasz. Nincs sok időd! Mit teszel?")
 time.sleep(1)
 print("""A. A kést elrejted a párna alá és visszafekszel az ágyra. 
B. Gyorsan elvágod a kötelet és elbújsz egy közeli szekrényben.""")
 choice = input(">>> ")
 if choice in valasz_A:
      print("A kést elrejted a párna alá és visszafekszel az ágyra")
      print("Az ismeretlen idegen bejön a szobába. Mivel az ágyon fekszel, nem gyanakszik semmire. Ezért továbbáll. Ezek után felkelsz az ágyból és kiutat kezdesz keresni. Kilépsz a szobából.")
      folyoso()
 elif choice in valasz_B:
      print("Miután elbújtál meglátod az szekrényajtó rése körül, hogy egy ismeretlen idegen belépett a szobába."
          "Lélegzet visszafojtva várod az eseményeket. Az idegen közelebb lép a szekrényhez majd hirtelen megáll." 
          "Ekkor észreveszed, hogy egy üvegszilánk megvágta a csuklódat és vércseppek jelzik hollétedet. Amint erre ráeszméltél, kinyílik a szekrényajtó és az idegen egy machete-t szúr a mellkasodba.")
 else:
     print (szukseges)
     valasztas_kes()
def valasztas_kez():
 print("Sikerül magad kikötöznöd magad, és ezért odamész a késhez. Lépteket hallasz.")
 time.sleep(1)
 print("A kést elrejted a párna alá és visszafekszel az ágyra. ")
 time.sleep(1)
 print("Az ismeretlen idegen bejön a szobába. Mivel az ágyon fekszel nem gyanakszik semmire."
"Ezért továbbáll. Ezekután felkelsz az ágyból, magadhoz veszed a kést és kiutat kezdesz keresni. Kilépsz a szobából.")
def folyoso():
 print("Kilépve a szobából egy folyosón találod magad, amely két irányba nyúlik el hosszan.")
 time.sleep(1)
 print("""A. Úgy döntesz, hogy balra fordulsz 
 B. Úgy döntesz, hogy jobbra fordulsz.""")
 choice = input(">>> ")
 if choice in valasz_A:
     valasztas_balra()
 elif choice in valasz_B:
    valasztas_jobbra()
 else: 
    print(szukseges)
    folyoso()
def valasztas_balra():
 print("Kilépsz a szobából. A folyosó bal része felé haladsz és meglátsz egy szobát, amiből fény szűrődik ki.")
 time.sleep(1)
 print(""" A. Bemész a szobába
B. Tovább haladsz a folyosón""")
 choice = input(">>> ")
 if choice in valasz_A:
   valasztas_szoba()
 elif choice in valasz_B:
    valasztas_tovabb()
 else:
    print(szukseges)
    valasztas_balra()
def valasztas_szoba():
    print("A szobába belépve megtalálod, hogy a fény forrása a telefonod. Közeleb lépve látod, hogy egy videó megy. A videón a te az újévi fogadalmadról beszélsz, miközben a háttérben neked kiabálnak és füttyögnek. A videó azzal zárul, hogy stoppolsz és egy fekete furgont látsz meg. Elszörnyülködsz azon, hogy mennyire ostoba voltál, majd elrakod a telefonod. Ezután visszaindulsz a folyosóra.  ")
    time.sleep(5)
    valasztas_tovabb()
def valasztas_tovabb():
 print("A folyosó végén egy szobát találsz tárva nyitva. A szoba nincs megvilágítva, de a félhomályban észreveszel egy lógó valamit, ami mintha lebegne. Rossz előérzeted van, ugyanakkor kíváncsi vagy mi van bent.")
 time.sleep(1)
 print("""A. Bemész a szobába
B. Nem mész be a szobába""")
 choice = input(">>> ")
 if choice in valasz_A:
  valasztas_bemesz_kinzo()
 elif choice in valasz_B:
  valasztas_halal()
 else:
    print(szukseges)
    valasztas_tovabb()
def valasztas_bemesz_kinzo():
    print("Kiváncsi vagy, hogy mi van a szobában, azonban az elviselhetetlen bűzön és a tócsákon kívűl nem érzel mást. Fényre van szükséged, ezért felkapcsolód a lámpát.")
    print("Hirtelen sokkot kapsz. Rájössz, hogy a szag, amit éreztél (valami durván kiiratni) hullaszag volt, a test, amit láttál lógni, egy felkoncolt fiatal lány volt és a tócsa, amit éreztél a lányból folyó vér volt.  A szoba közepén egy megviselt fogorvosi szék fogad, mellette pedig egy asztal, amin különböző kínzó eszközöket találtál. A fogorvosi széktől balra még egy asztalt találtál, amin csontdarabok és bőrcafatokat találhatóak. Könyvek csillantak fel a szemed sarkában, aminek a címei Légy az eleségem, vagy Egyem a húsodat, Pizzafutár és egyéb gyorsételek. Miután körülnéztél a szobába a férfi benyit, és leüt egy balta markolatával. ")
    valasztas_finale()
def valasztas_halal():
    print("Úgy döntesz, hogy nem mész be. Jobbra tekintve egy másik helyiséget találsz. Hangokat hallasz magad mögött, hátra tekintve árnyakat látsz ezért félelmedben benyitsz a szobába. Az ajtóban egy nyitott medve csapda várta áldozatát és te sietségedben nem vetted észre, így az levágta a lábadat és elvéreztél.")
time.sleep(3)
print("Meghaltál.")

intro()