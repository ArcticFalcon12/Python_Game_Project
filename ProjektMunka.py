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
 print("..")
intro()