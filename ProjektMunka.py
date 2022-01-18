import time  # Importáljuk az időt ezzel tudunk késleltetni

#Rájönni hogyan válaszolhat a felhasználó a különböző esetekben
valasz_A = ["A", "a"]
valasz_B = ["B", "b"]
#A felhasználó csak a megadott választásokkal válaszolhasson
szukseges = ("\nCsak A vagy B-t használj!\n")
#Bemutatkozás
def intro():
 print("Üdvözöllek",'\033[1m' + 'Jack The Ripper: Resurection; The Game' + '\033[0m'
" Van számodra egy történetem! Szeretnél részt venni benne?")
 time.sleep(0.5)
 print ("""A. Igen szeretnék!
B. Kösz inkább kihagyom! """)
#1. választási lehetősége a játékosnak
 choice = input(">>> ")
 if choice in valasz_A:
     valasztas_kezdes()
 elif choice in valasz_B:
    print("\n  Biztos vagyok benne, hogy érdekelni fog téged. Veszíteni valód nincsen, nem igaz? Na ugye! Szerintem el is kezdhetjük! Showtime!")
    valasztas_kezdes()
 else:
    print (szukseges)
def valasztas_kezdes():
 print("Kezdődjön a show!")
 time.sleep(2)
 print (" Egy számodra idegen helyen, egy idegen szobában ébredsz fel. A bal kezed egy baldachinos ágy egyik lábához van kikötözve. Nem emlékszel, hogy mi történt tegnap, ahogyan arra sem, hogy mit kereshetsz itt. Csak egy dologra tudsz gondolni: neked most nem kéne itt lenned. "
 "A földön megpillantasz egy rozsdás kést, amivel talán el tudnád vágni a kötelet.")
 time.sleep(1)
 #2. választási lehetőség a játékosnak
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
 print ("Úgy döntesz, a késsel próbálkozol. A lehető legóvatosabban lelépsz az ágyról és megpróbálod elérni a kezeddel a kést. Az öreg, megviselt padló nagyot reccsen a lábad alatt, amitől egy kicsit megijedsz.")
 print("Miközben próbálod kezeddel a kés markolatát megfogni, leversz egy képet az egyik szekrényről. Az a földre esik, és az üvegkeret szilánkokra esik. De mégsem ez a legrémisztőbb, hanem hogy a szilánkok alól saját arcképed néz rád vissza.")
 time.sleep(5)
 print(" Miután kellemesen sokkolódtál, arra leszel figyelmes, hogy léptek zajától visszhangzanak a ház falai. Az egyre közeledő léptek hallatán elfog a félelem. Eléred a kést, immáron kezedben a lehetőség. Mit teszel? ")
 time.sleep(1)
 #3. választási lehetőség a játékosnak
 print("""A. A kést elrejted a párna alá és visszafekszel az ágyra. 
B. Gyorsan elvágod a kötelet és elbújsz egy közeli szekrényben.""")
 choice = input(">>> ")
 if choice in valasz_A:
      print("A kést elrejted a párna alá és visszafekszel az ágyra")
      print("A léptek egyre hangosabbak, és hangosabbak, míg nem elérnek a szobaajtóig. Lélegzeted visszafolytva próbálod színlelni az alvást, és várod, hogy mi történik.")
      time.sleep(3)
      print("Egyszer csak ismételten lépteket hallasz, ezek azonban már halkulnak. Az illető elhagyta a szobát. Mikor már meggyőződtél arról, hogy kellőképpen távol van az a valaki, felkelsz az ágyból és elvágod a kötelet. Ideje menekülőre fogni és kiutat keresni. A kést eldobod és kilépsz a szobából.")
      folyoso()
 elif choice in valasz_B:
      print("A kötelet kioldod, majd rohamos tempóban bemenekülsz a szekrénybe. Az ajtó rései közül figyeled, ki lehet a zaj forrása. A léptek felhangosodnak, közelednek, majd hirtelen csend.")
      time.sleep(5)
      print("Egy emberi alak jelenik meg az ajtóban. A sötétben csak azt tudod kivenni, hogy egy magas és igencsak izmos ember, a fején valami dísszel.")
      time.sleep(5)
      print("Ekkor pillantod csak meg, hogy a kezedet elvágta a képkeret egy szilánkja, te pedig szép kis csíkot húztál magad után.")
      time.sleep(3)
      print("Az ajtó váratlanul kinyílik, és az idegen egy kést szúr a tüdődbe, majd a fejedbe. ")
      time.sleep(2)
      print("Meghaltál.")
      halal()
 else:
     print (szukseges)
     valasztas_kes()
def valasztas_kez():
 print("A kést elrejted a párna alá és visszafekszel az ágyra")
 print("A léptek egyre hangosabbak, és hangosabbak, míg nem elérnek a szobaajtóig. Lélegzeted visszafolytva próbálod színlelni az alvást, és várod, hogy mi történik.")
 time.sleep(3)
 print("Egyszer csak ismételten lépteket hallasz, ezek azonban már halkulnak. Az illető elhagyta a szobát. Mikor már meggyőződtél arról, hogy kellőképpen távol van az a valaki, felkelsz az ágyból és elvágod a kötelet. Ideje menekülőre fogni és kiutat keresni. A kést eldobod és kilépsz a szobából.")
 folyoso()
def folyoso():
 print("Kilépve a szobábó eléd tárul egy folyosó, amely hosszan elnyúlik balra és jobbra is.")
 time.sleep(1)
 #4. választási lehetőség a játékosnak
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
 print("Tehát balra indulsz. A tekinteted azonnal megragadja egy szoba, amelyből fény szűrődik ki. Veszélyes is lehet oda bemenni, ugyanakkor lehet, hogy még hasznodra válik bekukkantani oda.")
 time.sleep(1)
 #5. választási lehetőség a játékosnak
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
    print(" Eluralkodik rajtad a kíváncsiság, és úgy döntesz, belépsz. A szobába betoppanva meglátod, hogy a fény forrása egy telefon kijelzője, a telefon épp egy videót játszik le.  ")
    time.sleep(5)
    print(" A videó szereplője te vagy, ahogy éppen az újévi fogadalmadról beszélsz, miközben a háttérben neked kiabálnak és füttyögnek. A videó azzal zárul, hogy stoppolsz, és megáll melletted egy fekete furgon. Elszörnyülködsz azon, hogy mennyire ostoba voltál, s valószínűleg a fuvar miatt vagy itt. Elrakod a telefonod, majd tovább indulsz kiutat keresni.  ")
    time.sleep(5)
    valasztas_tovabb()
def valasztas_tovabb():
 print(" Továbbra is balra haladsz. A folyosón haladva egy kisasztalt találsz, fölötte pedig egy festményt vélsz felfedezni. Telefonodat hívod segítségül, hogy megcsodálhasd a képet.")
 time.sleep(5)
 print("Ám ezen döntésed hamar megbánod. A kép, amelyet felfedeztél, Csontváry Kosztka Tivadar Öreg Halász nevű fesménye, csak éppen a jobb oldali része van áttükrözve a másik oldalra is. A komor arcú, sátánt idéző halász portréja nem éppen segített a lelki állapotodon. Gyorsan elrakod a telefont és tovább halasz. ")
 print(" A folyosó végén egy szoba várt, tárva nyitva. A szoba nincs megvilágítva, ugyanúgy, mint a ház többi része, de a félhomályban észreveszel egy lógó valamit, ami mintha lebegne. Rossz előérzeted van, ugyanakkor el tudod képzelni, hogy erre lehet a kijárat.")
 time.sleep(1)
 #5. választási lehetőség a játékos
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
    print(" Óvatosan lépsz be a terembe. Kiváncsi vagy, hogy mi van itt azonban az elviselhetetlen bűzön és a tócsákon kívűl nem érzel mást. Fényre van szükséged, ide már a telefonod fénye sem lesz elég, ezért a falon tapogatózva megkeresed a kapcsolót, és felkapcsolód a lámpát.")
    time.sleep(7)
    print("Hirtelen sokkot kapsz. Rájössz, hogy a szag, amit éreztél hullaszag volt, a test, amit láttál lógni, egy felkoncolt fiatal lány és a tócsa, amit éreztél a lányból folyó vér volt.  A szoba közepén egy megviselt fogorvosi szék fogad, mellette pedig egy asztal, amin különböző kínzó eszközöket találtál. A fogorvosi széktől balra még egy asztalt, amin csontdarabok és bőrcafatokat találhatóak. Az asztal alatt egy stócbankönyveket véltél felfedezni. Kíváncsiságtól hajtva odalépsz és leemelsz pár könyvet a kupac tetejéről. A három könyv, amely kezed ügyébe akadt a Légy az eleségem, az Egyem a húsodat és a Pizzafutár és egyéb gyorsételek. Gyorsan levágod, merről fúj a szél: ezek kannibál receptkönyvek. Miután körülnéztél a szobába a férfi benyit, és leüt egy balta markolatával. ")
    time.sleep(10)
    valasztas_finale()
def valasztas_halal():
    print("Úgy döntesz, hogy nem mész be. Az ösztöneidre hallgatsz, és visszalépsz párat, ugyanis elhaladtál egy szoba mellett. Ránézésre ez is egy nagyobb szobának tűnik, ki tudja, hátha erre van a haza.")
    time.sleep(5)
    print("Magad mögött ismételten lépteket kezdesz hallani, feléd közeledő lépteket. Hátra tekintve árnyakat is látsz ezért félelmedben benyitsz a szobába. Az ajtóban egy nyitott medve csapda várta áldozatát és te sietségedben nem vetted észre, az bekapta a lábdat és perceken belül elvéreztél.")
    print(" Meghaltál.")
    time.sleep(2)
    halal()
time.sleep(3)
def valasztas_jobbra():
 print("A jobb mindig jobb, most is jó lesz a jobb irány. Céltudatosan halasz előre, finoman és óvatosan, ám egyszer csak rálépsz valamire. Felemelve a lábad tudomásul veszed, hogy bármi is volt a borítékban, azt sikeresen szétlapítottad. Érzésre valami gumis masszának, kocsonyás dolognak tűnik. Észreveszed, hogy további borítékok hevernek a földön, amik egyfajta iránymutatóként egy szobába vezetnek. ")
 time.sleep(2)
 #6. választási lehetőség a játékosnak
 print("""A. Bemész a szobába
B. Tovább haladsz a folyosón""")
 choice = input(">>>")
 if choice in valasz_A:
     valasztas_bemesz_szoba_jobb()
 elif choice in valasz_B:
     valasztas_tovabb_jobb()
 else:
    print(szukseges)
    valasztas_jobbra()
def valasztas_bemesz_szoba_jobb():
    print(" Követed a borítékokat és belépsz a szobába. Egészen megdöbbentő a látvány, ami téged fogad. A szoba, amibe beléptél a te fényképeiddel van kitapétázva. Képek, amin a barátaiddal szerepelsz, régi több évvel ezelőtti családiképek, fényképek iskolából, régi bulikból és: babafényképek. Azonban a legrémisztőbb az, hogy olyan fényképek is szerepelnek a falakon, amelyeket nem te készítettél magadról vagy többed magadról, hanem valaki más rólad. A veled szemben lévő fal előtt egy óriási íróasztal helyezkedik el, közepén egy gyertyával mellette egy kis üveggel. Közelebb lépsz, és meglátod, hogy a kis üvegcse valójában egy kis tintás üveg, amiben vörös tinta van. A gyertya előtt egy papírlap szerepel, amelyen az írás még friss. Arra leszel figyelmes, hogy a levél címzettje te vagy. ")
    level()
    time.sleep(10)
    print("Sokkolt állapotba kerülsz, felgyorsul a szívverésed. Aggódsz és félsz, és ahogy azt a levél is írja, legszívesebben menekülnél. Bele sem mersz gondolni, hogy miért vannak vörössel írva a sorok, vagy, hogy miért van a papír mellett heverő íróeszköznek emberi ujjcsont váza. Azonban azt már nem tudod figyelmen kívül hagyni, hogy az írás láthatóan friss, az írás még nem száradt meg. Ijedve rohansz vissza a folyosóra. ")
    valasztas_tovabb_jobb()
def level():
    print("Drága Mary,")
    print("Valószínűleg nem tudod, hogy miért vagy itt, össze vagy zavarodva és legszívesebben menekülnél innen. Menekülnél, vissza a régi, megszokott életedbe. Vissza oda, ahol a magadfajták nem nyerik el méltó büntetésüket. Pedig valójában hálásnak kéne lenned nekem, hogy eddig életben hagytalak.")
    time.sleep(5)
    print("Tudod, régóta vadásztam rád. Eleinte nagyon frusztrált, hogy nehéz préda vagy, és szinte sosem vagy egyedül, amikor is beléd márthatnám a pengémet, azonban idővel ráébredtem, hogy te tanítani akarsz nekem valamit. Valami nagyon fontosat. A nagy trófea nagy erőfeszítéseket kíván. Én pedig minden követ megmozgattam azért, hogy te most itt legyél a ketrecedben, kicsi kanárim!")
    time.sleep(5)
    print(" Már sok olyan áldozatom volt, mint te. Számomra élvezet titeket vadászni, szeretek veletek játszani. Bizony, eljátszom veletek, majd elvágom a torkotokat, kivágom a beleiteket, lenyúzom a bőrötöket, kitépem a csontjaitokat, lecsapolom a véreteket, és olykor megesik, hogy meg is eszem belőletek párat. Ilyenkor úgy érzem, felfalom a gonoszt, ezáltal megtisztítom a világot tőletek.")
    time.sleep(5)
    print(" Könnyedén teszem mindezt. És most itt van előttem még egy. De ez más, mint a többi, te más vagy. Kiemelkedő. Különleges. De sajnos, még úgy sincs esélyed ellenem, hogy jelenleg az én házamban járkálsz és lehetőséget biztosítottam neked elmenekülni. Mégis alul maradsz majd. Én vagyok a vadász, aki céloz a puskával, és te vagy a préda, akinek ott virít a célkereszt a homlokán. Én vagyok a hóhér és te vagy a halálra ítélt, akinek a fejére mérem épp a bárdot. Én ítéltelek halálra, ugyanúgy, mint a fajtársaidat. Hagyom, hogy egy kicsit még életben légy. Fuss, fuss kicsi lány, fuss, amíg még van lábad, és sikíts, amíg még épek a hangszálaid. Zihálj, amíg még nincs tőr a tüdödben, és könnyezz, amíg még nem téptem ki a szemgolyóid.")
    time.sleep(11)
    print("Játéra hívtalak téged, te pedig elfogadtad azzal, hogy kikeltél az ágyból.Hamarosan találkozunk.")
    time.sleep(4)
    print("Izgatottan vár új játszótársad:")
    time.sleep(4)
    print("A végzet")
def valasztas_tovabb_jobb():
    print("A folyosó végén látsz egy kétajtós szobát, aminek ajtajai résnyire vannak nyitva. Viszont ahogy közelítesz a szoba felé, orbitális bűz csapja meg az orrod. ")
    time.sleep(2)
    #7. választási lehetőség a játékosnak
    print("""A. Bemész a szobába
B. Nem mész be a szobába""")
    choice = input(">>>")
    if choice in valasz_A:
        valasztas_szoba_bemesz_jobb()
    elif choice in valasz_B:
        valasztas_nem_mesz_be_jobb()
    else:
        print(szukseges)
        valasztas_tovabb_jobb()
def valasztas_szoba_bemesz_jobb():
    print("Úgy döntesz, bemész a szobába. A résnyire nyitott ajtót beljebb lököd finoman, majd belépsz. Hirtelen felkapcsolódik a lámpa, anélkül, hogy te bármit is megnyomtál volna. De úgy érzed, bárcsak ne kapcsolódott volna fel semmi.Veled szemben két sorban a falnak döntve halott emberi testek hevernek. Arcuk össze van vagdosva, némelyikük hasa fel volt vágva, és belek lógtak ki belőlük, másoknak le volt vágva a kezük, a lábuk, és volt egy ember a szoba másik végén, pont veled szemben, akiből ki voltak harapva darabok.Ijedtedben az ajtó felé fordulsz, és már tennéd ki a lábad, ám egy halk, fájdalmaktól nyögő hang szólal meg a hátad mögül:")
    print("-Mivel… mivel érdemeltem… ezt ki?")
    print("Ekkor belép az ajtón egy férfi, zsákból készült maszkkal az arcán, és leüt.")
    time.sleep(5)
    valasztas_finale()
def valasztas_nem_mesz_be_jobb():
    print("Úgy döntesz, nem mész be a szobába. Visszafordulsz, és elindulsz a folyosó másik oldala felé. Visszaérsz abba a szobába, ahonnan indultál. De a szoba teljesen máshogy néz ki, mint azelőtt. Nincs ágy, nincs szekrény, se törött kép, vagy vérfoltok a földön. Csak egy vörös fényforrás, ami a koromsötétben még baljósabb hatást kelt. Közelebb mész a fényforráshoz, azonban nem veszed észre, hogy a földön szögesdrót fekszik, amiben megbotlasz, és ráesel. Borzalmas fájdalmak között vérzel el.")
    print("Meghaltál.")
    time.sleep(3)
    halal()
def valasztas_finale():
    #8. választási lehetőség a játékosnak
 print("Mikor magadhoz térsz, egy kivilágított, orvosi szoba szerűségben találod magad, egy orvosi székben. Melletted bőrmaszkok hevernek, mind-mind emberi bőrből. A kezed pántokkal a székhez van rögzítve, a lábaddal egyetemben. A jobb kezed mellett egy kis tartóban különböző nagyságú vágóeszközök vannak, a szikétől a séfkésen át, a machete-ig minden megtalálható benne.")
 time.sleep(5)
 print("A terem falain rajzok találhatóak, melyeket vélhetően vérrel festettek fel. Tőled balra egy ember látható, kalapban és öltönykabátban, ahogy vigyorogva néz előre. Tőled jobbra írások találhatóak. Kedves Főnök, Thomas Bond téved, Legyen igazad, Melville és még pár apróbb írás, melyet ilyen távolságból nem lehet elolvasni. Észreveszed, hogy számos tárgyon szerepel az ötös szám. Két maszkon, a veled szemben lévő ajtón is háromszor, de elforgatva, egy könyvön, amely a padlón hever, a falakon is kisebb-nagyobb méretben, és még a bal kezedet szorító pánton is. Hasonló rendetlenség jellemzi ezt a szobát, mint a többit, ennek ellenére a helyiségnek van egy egyedi, hátborzongató hangulata, máshogy rémisztő, mint a többi. Ez ijesztő, de érdekes is.")
 time.sleep(7)
 print("Az ajtó váratlanul kinyílik, és egy magas, izmos, idősödő, maszkos fazon lép be rajta. Mielőtt bármit is szólhattál volna, vagy csak megmozdulhattál volna, határozott, mély hangon elkezdi:")
 time.sleep(5)
 print("-Én, ki a pokolból jöttem, Whitechapel fia, üdvözöllek!")
 time.sleep(3)
 print("Maszkján két lyuk van vágva két szemének, ami jelen helyzetben kikerekedve néz rád.")
 print(" -Kissé rémültnek tűnsz. Talán megrémítettelek? Vagy a ház az oka? Nem tetszett, ahogy berendeztem neked? Pedig direkt neked dekoráltam ki ennyire. ")
 print("Közelebb lép hozzád és elvesz egy kést a melletted lévő tartóból.")
 print(" -A hálátlanságod nagyon nem tetszik. Tekintettel kéne lenned azokra az emberekre, akiket felhasználtam a dekorálás során.")
 time.sleep(5)
 print(" Elkezdesz feszengeni a székben, próbálod lefeszíteni a karpántokat a székről, hogy kiszabadulhass. De a pánt nem adja meg magát, te pedig idegesen rángatózol, amíg el nem fáradsz. A fickó megvárja, míg befejezed, majd neked szegezi a kérdést:")
 print("-Tudod, hogy miért van tele ez a szoba ötösökkel? Nos, számomra ez általános.")
 time.sleep(3)
 print("Idegességedben nekifeszülsz még egyszer és minden erődet beleadva próbálod letépni a bőrpántokat a székről. A maszkos ipse közeledik feléd.")
 print("- Ne ficánkolj annyit, míg a végén nélkülem esik bajod!")
 print("Eléd lép, és a torkodra helyezi a kést.Farkasszemet nézel a fogvatartóddal, aki a maszkja mögött vérszomjasan néz vissza rád.Megérzed, hogy a jobbkezednél meglazult a pánt. Nem vagy benne biztos, hogy egy mozdulattal le tudnád tépni, az azonban biztos, hogy ez ki fog oldani.")
 print("""A. Feszegeted még egy kicsit és kivársz.
B. Megpróbálod feltépni és megütni az idegent""")
 choice = input(">>>")
 if choice in valasz_A:
    valasztas_finale_jo()
 elif choice in valasz_B:
    valasztas_finale_halal()
 else:
    print(szukseges)
    valasztas_finale()
def valasztas_finale_halal():
    print("Megpróbálod egy hirtelen mozdulattal letépni a kezedről a pántot, az azonban nem tépődik el.A barátod viszont észreveszi a tervedet.-Én leírtam neked egy levélben, hogy innen nem menekülsz el, de ezek szerint nem találtad meg. Attól a perctől fogva, hogy beszálltál a furgonomba, megástad a sírodat, kis kanárim. Én élveztem a játékot, remélem te is!  Azzal elvágja a torkodat, majd a kést a fejedbe helyezi.")
    time.sleep(5)
    print(" Meghaltál. ")
    time.sleep(5)
    halal()
def valasztas_finale_jo():
 print("Feszegetned kell még a kötelet, ehhez viszont szükséged van időre. Szóval kell tartanod a fickót, és le kell nyugodnod, hogy koncentrálni tudj, ami a jelenlegi helyzetben piszok nehéz.")
 print("-Miért hoztál engem… ide?-kérdezed.")
 print("-Hát nem is emlékszel? te magad szálltál be a furgonomba tegnap éjjel! Csak magadra vess! Aki beszáll idegenek kocsijába...")
 time.sleep(5)
 print("A pánt egyre lazább, de a hallottakba belegondolva ismét kezdesz pánikba esni.")
 print("-Hálásnak kéne lenned nekem, amiért ennyi mindent tettem, pusztán csak hogy lenyűgözzelek. De, megmondom őszintén, úgy érzem, te nem értékeled a teljesítményem. Nem érdekel mit csináltam, mennyit szenvedtem ezért. És ez nagyon dühítő!")
 print("Úgy érzed a pánt már elég laza. Megrántod a karod, a pánt szétszakad, és egy óriási ütést mérsz a tag fejére. Ő kertiszékként csuklik össze. Megragadsz egy kést mellőled és elvágod a többi pántot, majd feltéped az ajtót és viharzol kifelé.")
 time.sleep(5)
 print("Az ajtót kinyitva felrohansz egy lépcsőn, majd meglepődve tapasztalod, hogy egy normálisan berendezett családi házban találod magad, mikor felérsz a lépcső tetejére. Eddig egy házban voltam, ami egy ház alatt volt?-gondolod magadban. Könnyen kiszúrod a kanapé mögött elhelyezkedő bejárati ajtót, és fellélegezve rohansz a szabadságot jelentő ajtó felé.")
 time.sleep(5)
 print("Ám hirtelen égető fájdalom nyilall a combodba. A barátod kést dobott bele. Elesel és kúszva igyekszel megközelíteni a célt. A maszkos lassú léptekkel halad feléd.  Megpillantasz két pisztolyt a kanapé lábánál, de nem tudod, melyik van töltve, ha egyáltalán töltve van valamelyik.")
 time.sleep(5)
 #9. választási lehetőség a játékosnak
 print("""A. Jobb oldali pisztoly
B. Bal oldali pisztoly""")
 choice = input(">>>")
 if choice in valasz_A:
     rossz_pisztoly()
 elif choice in valasz_B:
    jo_pisztoly()
    time.sleep(5)
    vege()
 else:
    print(szukseges)
    valasztas_finale_jo()
def rossz_pisztoly():
    print("A jobb oldali pisztoly után nyúlsz, és egy gyors mozdulattal ellenfeledre szegezed azt. De te is csak akkor döbbensz rá, hogy a kezedben tartott pisztoly piros színű műanyaggal van borítva, hátulján egy kis sárga tartóval, amin egy cetli szerepel ebbe töltse a vizet felirattal.Vizipisztoly van a kezedben.Mielőtt megbánhatnád döntésedet, egy bicska repül a fejedbe.")
    time.sleep(5)
    halal()
def jo_pisztoly():
    print("A bal oldali pisztoly után nyúlsz, és egy gyors mozdulattal ellenfeledre szegezed azt. Meghúzod a ravaszt, a pisztoly nagyot dörren. Fején találtad a szöget. Az immáron három lyukkal rendelkező maszk lassan átázik, majd a maszkos gyilkos nagyot koppan, s elhallgat. Eldobod a fegyvert, majd gyorsan kibicegsz az ajtón. Nem tudod, hol vagy, azt sem merre mész. De nem is számít. Bárhol jobb, mint itt. Elbicegsz a felkelő nap fényébe, és megfogadod, hogy soha, de soha nem fogsz erről beszélni senkinek.")
time.sleep(10)
def halal():
    print(" Sajna rossz döntést hoztál! Legközelebb legyél okosabb és akkor hátha sikerrel jársz! Addig is további minden jót!")
def vege():
    print(" Nos, ennyi volt az én kis mesém neked! Remélem elnyerte a tetszésedet!  ")
    time.sleep(3)
    print(" Nekem most haladnom kell tovább az utamon, megyek további történeteket írni, de szerintem hamarosan újra látjuk egymást!")
    time.sleep(3)
    print(" Addig is további minden jót! És csak óvatosan a fekete furgonokkal!")
intro()
