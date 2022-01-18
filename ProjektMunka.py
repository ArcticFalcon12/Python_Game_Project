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
    print("\n Hát ezt sajnálattal hallom!..")
    valasztas_kezdes()
 else:
    print (szukseges)
def valasztas_kezdes():
 print("Kezdődjön a show!")
 time.sleep(2)
 print ("Felkelsz egy ismeretlen házban, egy szobában. Körülnézel és azt látod, hogy ki van kötve az egyik kezed."
 "Pánikba esel. Egy baldachinos ágyon vagy kikötve."
 "A közelben látsz egy rozsdás kést, amivel megpróbálhatod elvágni a kötelet. Mit teszel? ")
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
 print ("Miközben lelépsz az ágyról, megreccsen az öreg padlódeszka a lábad alatt. Megijedsz a hangjától."
         "Szépen lassan megpróbálsz odamenni a késért, de leversz egy képet az egyik szekrényről, és meglátod, hogy téged ábrázol."
         "Az arcod hirtelen látványától felsikoltasz. Lépteket hallasz. Nincs sok időd! Mit teszel?")
 time.sleep(1)
 #3. választási lehetőség a játékosnak
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
      halal()
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
 folyoso()
def folyoso():
 print("Kilépve a szobából egy folyosón találod magad, amely két irányba nyúlik el hosszan.")
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
 print("Kilépsz a szobából. A folyosó bal része felé haladsz és meglátsz egy szobát, amiből fény szűrődik ki.")
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
    print("A szobába belépve megtalálod, hogy a fény forrása a telefonod. Közeleb lépve látod, hogy egy videó megy. A videón a te az újévi fogadalmadról beszélsz, miközben a háttérben neked kiabálnak és füttyögnek. A videó azzal zárul, hogy stoppolsz és egy fekete furgont látsz meg. Elszörnyülködsz azon, hogy mennyire ostoba voltál, majd elrakod a telefonod. Ezután visszaindulsz a folyosóra.  ")
    time.sleep(5)
    valasztas_tovabb()
def valasztas_tovabb():
 print("A folyosó végén egy szobát találsz tárva nyitva. A szoba nincs megvilágítva, de a félhomályban észreveszel egy lógó valamit, ami mintha lebegne. Rossz előérzeted van, ugyanakkor kíváncsi vagy mi van bent.")
 time.sleep(1)
 #5. választási lehetőség a játékosnak
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
    time.sleep(10)
    valasztas_finale()
def valasztas_halal():
    print("Úgy döntesz, hogy nem mész be. Jobbra tekintve egy másik helyiséget találsz. Hangokat hallasz magad mögött, hátra tekintve árnyakat látsz ezért félelmedben benyitsz a szobába. Az ajtóban egy nyitott medve csapda várta áldozatát és te sietségedben nem vetted észre, így az levágta a lábadat és elvéreztél.")
    time.sleep(2)
    halal()
time.sleep(3)
def valasztas_jobbra():
 print("Kilépsz a szobából! A folyosó jobb része felé haladva. Ahogy haladsz, a folyosón rálépsz egy borítékra. A boríték tartalmát kilapítottad azzal, hogy ráléptél. Érzésre valami gumis masszának, kocsonyás dolognak tűnik. Észreveszed, hogy további borítékok hevernek a földön, amik egyfajta iránymutatóként egy szobába vezetnek ")
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
    print("Követed a borítékokat és belépsz a szobába. Egészen megdöbbentő, amit látsz. A szoba, amibe beléptél a te fényképeiddel van kitapétázva. Képek, amin a barátaiddal szerepelsz, régi több évvel ezelőtti családiképek, fényképek iskolából, régi bulikból és: babafényképek. Azonban a legrémisztőbb az, hogy olyan fényképek is szerepelnek a falakon, amelyeket nem te készítettél magadról vagy többed magadról, hanem valaki más rólad. A veled szemben lévő fal előtt egy óriási íróasztal helyezkedik el, közepén egy gyertyával mellette egy kis üveggel. Közelebb lépsz, és meglátod, hogy a kis üvegcse valójában egy kis tintás üveg, amiben vörös tinta van. A gyertya előtt egy papírlap szerepel, amelyen az írás még friss. Arra leszel figyelmes, hogy a levél címzettje te vagy")
    level()
    time.sleep(10)
    print("Sokkolt állapotba kerülsz, felgyorsul a szívverésed. Aggódsz és félsz, és ahogy azt a levél is írja, legszívesebben menekülnél. Bele sem mersz gondolni, hogy miért vannak vörössel írva a sorok, vagy, hogy miért van a papír mellett heverő íróeszköznek emberi ujjcsont váza. Azonban azt már nem tudod figyelmen kívül hagyni, hogy az írás láthatóan friss, az írás még nem száradt meg. Ijedve rohansz vissza a folyosóra.")
    valasztas_tovabb_jobb()
def level():
    print("Drága Mary Valószínűleg nem tudod, hogy miért vagy itt, össze vagy zavarodva és legszívesebben menekülnél innen. Menekülnél, vissza a régi normális életedbe. Tudod, régóta vadásztam rád. Eleinte nagyon frusztrált, hogy nehéz préda vagy, és szinte sosem vagy egyedül, amikor is beléd márthatnám a pengémet, azonban idővel ráébredtem, hogy te tanítani akarsz nekem valamit. Valami nagyon fontosat. A nagy trófea nagy erőfeszítéseket kíván. Itt léted a munkám gyümölcse. A jól megérdemelt jutalmam.Mióta volt egy kellemetlen incidensem egy hozzád hasonlóval, azóta vadászom a magadfajtára. Eljátszom velük, majd elvágom a torkukat, kivágom a beleiket, lenyúzom a bőrüket, kitépem a csontjaikat, lecsapolom a vérüket, és olykor megesik, hogy megeszem őket. Ilyenkor úgy érzem, felfalom a gonoszt, ezáltal megtisztítom a világot tőletek. Ismered Jack-et? A mesteremet? Bizonyára nem sejted, kiről beszélek, pedig ismered őt, ebben biztos vagyok. Talán, talán ha úgy beszélek róla, mint az az ember, aki hasakat metszett fel? Na, ugye, így már ismerős. Élvezem a mi kis játékunkat. Én vagyok a vadász, aki céloz a puskával, és te vagy a préda, akinek ott virít a célkereszt a homlokán. Én vagyok a hóhér és te vagy a halálra ítélt, akinek a fejére mérem épp a bárdot. Én ítéltelek halálra, ugyanúgy, mint a fajtársaidat. Hagyom, hogy egy kicsit még életben légy. Fuss, fuss kicsi lány, fuss, amíg még van lábad, és sikíts, amíg még épek a hangszálaid. Zihálj, amíg még nincs tőr a tüdödben, és könnyezz, amíg még nem téptem ki a szemgolyóid. Játéra hívtalak téged, te pedig elfogadtad azzal, hogy kikeltél az ágyból.Hamarosan találkozunk.  Izgatottan vár régi játszótársad: Jacks son")
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
    print("Úgy döntesz, bemész a szobába. A résnyire nyitott ajtót beljebb lököd finoman, majd belépsz. Hirtelen felkapcsolódik a lámpa, anélkül, hogy te bármit is megnyomtál volna. De úgy érzed, bárcsak ne kapcsolódott volna fel semmi.Veled szemben két sorban a falnak döntve halott emberi testek hevernek. Arcuk össze van vagdosva, némelyikük hasa fel volt vágva, és belek lógtak ki belőlük, másoknak le volt vágva a kezük, a lábuk, és volt egy ember a szoba másik végén, pont veled szemben, akiből ki voltak harapva darabok.Ijedtedben az ajtó felé fordulsz, és már tennéd ki a lábad, ám egy halk, fájdalmaktól nyögő hang szólal meg a hátad mögül: -Mivel… mivel érdemeltem… ezt ki? Én nem akartam prosti lenni, de… A testén lévő, friss harapásnyomokból folyik ki a vér. A nő könnyek közt nyögi ki: -Jack… visszatért!Ekkor belép az ajtón egy férfi, zsákból készült maszkkal az arcán, és leüt.")
    time.sleep(5)
    valasztas_finale()
def valasztas_nem_mesz_be_jobb():
    print("Úgy döntesz, nem mész be a szobába. Visszafordulsz, és elindulsz a folyosó másik oldala felé. Visszaérsz abba a szobába, ahonnan indultál. De a szoba teljesen máshogy néz ki, mint azelőtt. Nincs ágy, nincs szekrény, se törött kép, vagy vérfoltok a földön. Csak valami vörös fényforrás, ami a koromsötétben még baljósabb hatást kelt. Közelebb mész a fényforráshoz, azonban nem veszed észre, hogy a földön szögesdrót fekszik, amiben megbotlasz, és ráesel. Borzalmas fájdalmak között vérzel el.")
    time.sleep(3)
    halal()
def valasztas_finale():
    #8. választási lehetőség a játékosnak
 print("Mikor magadhoz térsz, egy kivilágított, orvosi szoba szerűségben találod magad, egy orvosi székben. Melletted bőrmaszkok hevernek, mind-mind emberi bőrből. A kezed pántokkal a székhez van rögzítve, a lábaddal egyetemben. A jobb kezed mellett egy kis tartóban különböző nagyságú vágóeszközök vannak, a szikétől a séfkésen át, a machete-ig minden megtalálható benne. A terem falain rajzok találhatóak, melyeket vélhetően vérrel festettek fel. Tőled balra egy ember látható, kalapban és öltönykabátban, ahogy vigyorogva néz előre. Tőled jobbra írások találhatóak. Kedves Főnök, Thomas Bond téved, Legyen igazad, Melville és még pár apróbb írás, melyet ilyen távolságból nem lehet elolvasni. Észreveszed, hogy számos tárgyon szerepel az ötös szám. Két maszkon, a veled szemben lévő ajtón is háromszor, de elforgatva, egy könyvön, amely a padlón hever, a falakon is kisebb-nagyobb méretben, és még a bal kezedet szorító pánton is. Az ajtó váratlanul kinyílik, és egy magas, izmos, idősödő, maszkos fazon lép be rajta. Kezében egy táska van.Mielőtt bármit is szólhattál volna, vagy csak megmozdulhattál volna, határozott, mély hangon elkezdi:-Én, ki a pokolból jöttem, Whitechapel fia, üdvözöllek! Maszkján két lyuk van vágva két szemének, ami jelen helyzetben kikerekedve néz rád.-Kissé rémültnek tűnsz. Azt hittem, te, mint a borbélyház alkalmazottja már hozzá vagy szokva a magamfajta emberekhez.-Miről beszél, én nem vagyok prostituált!! És mégis mit akar tőlem?!Ő a válaszodon meglepődik. -Nos, ez mit sem változtat a dolgokon. Közelebb lép hozzád és elvesz egy kést a melletted lévő tartóból. -Akkor most játszunk egy kicsit!Elkezdesz feszengeni a székben, próbálod lefeszíteni a karpántokat a székről, hogy kiszabadulhass. De a pánt nem adja meg magát, te pedig idegesen rángatózol, amíg el nem fáradsz. A fickó megvárja, míg befejezed, majd neked szegezi a kérdést:-Tudod, hogy miért van tele ez a szoba ötösökkel? Nos, számomra ez általános.Idegességedben nekifeszülsz még egyszer és minden erődet beleadva próbálod letépni a bőrpántokat a székről. A maszkos ipse közeledik feléd.- Ne ficánkolj annyit, míg a végén nélkülem esik bajod!Eléd lép, és a torkodra helyezi a kést.Farkasszemet nézel a fogvatartóddal, aki a maszkja mögött vérszomjasan néz vissza rád.Megérzed, hogy a jobbkezednél meglazult a pánt. Nem vagy benne biztos, hogy egy mozdulattal le tudnád tépni, az azonban biztos, hogy ez ki fog oldani.")
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
    halal()
def valasztas_finale_jo():
 print("Feszegetned kell még a kötelet, ehhez viszont szükséged van időre. Szóval kell tartanod a fickót, és le kell nyugodnod, hogy koncentrálni tudj, ami a jelenlegi helyzetben piszok nehéz.-Miért hoztál engem… ide?-kérdezed.Ő dühösen néz rád, de a kérdésedtől nevetni kezd, és elveszi a pengét a torkodtól.-Hát nem is emlékszel? Te magad szálltál be a furgonomba, mikor egy buli után a borbélyház előtt stoppoltál. Szegénykém, nem is tudod, hogy te kissé részegen magadtól fogadtad el a játékomat!A pánt egyre lazább, de a hallottakba belegondolva ismét kezdesz pánikba esni. -Vicces, hogy egy buli után hozott, rossz döntésed fog a sírba vinni. Ez most nekem is fáj, mondjuk nyilván nem annyira, mint amennyire neked fog. De így már nem is tűnsz olyan remek prédának.Úgy éred a pánt már elég laza. Már csak a közeledbe kell vonzani az áldozatod.Mi sem egyszerűbb.-Te azzal a zsákkal a fejeden járkálsz állandóan? Ilyen ronda csak nem lehetsz! És nálad kevésbé kreatív embert még nem láttam. Látszik rajtad, hogy csak egy béna Hasfelmetsző Jack koppintás vagy!A célod elérted. Ő tombolva lép oda hozzád, és ismét penge szorul a nyakadhoz.Te pedig megrántod a karod, a pánt szétszakad, és egy óriási ütést mérsz a tag fejére. Ő kertiszékként csuklik össze. Megragadsz egy kést mellőled és elvágod a többi pántot, majd feltéped az ajtót és viharzol kifelé. Az ajtót kinyitva felrohansz egy lépcsőn, majd meglepődve tapasztalod, hogy egy normálisan berendezett családi házban találod magad, mikor felérsz a lépcső tetejére. Eddig egy házban voltam, ami egy ház alatt volt?-gondolod magadban. Könnyen kiszúrod a kanapé mögött elhelyezkedő bejárati ajtót, és fellélegezve rohansz a szabadságot jelentő ajtó felé. Ám hirtelen égető fájdalom nyilall a combodba. A barátod kést dobott bele. Elesel és kúszva igyekszel megközelíteni a célt. A maszkos lassú léptekkel halad feléd.  Megpillantasz két pisztolyt a kanapé lábánál, de nem tudod, melyik van töltve, ha egyáltalán töltve van valamelyik.")
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
    print("Marci ide irjál valamit")
def vege():
    print("Ide is ")
intro()
