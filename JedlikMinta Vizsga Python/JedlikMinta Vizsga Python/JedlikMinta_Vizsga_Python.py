print("\nFeladat 1 : Kisebb-nagyobb meghatározása")
Beker1=input("\tKérem adjon meg egy számot: ")
Szam1=int(Beker1)
Beker2=input("\tKérem adjon meg egy második számot: ")
Szam2=int(Beker2)
if  Szam1>Szam2 :
    print("\tA nagyobb szám : " , Szam1," a kisebb szám :", Szam2)
elif  Szam2>Szam1  :
    print("\tA nagyobb szám : ", Szam2," a kisebb szám :", Szam1)
elif  Szam1==Szam2 :
    print("\tA két szám egyenlő")

print("\n---------------------------------------------------------------\n")
print("\nFeladat 2: Szökőévek ")
Bekeres1=input("Kérem adjon meg egy évszámot: ")
BeKertEv1=int(Bekeres1)
Bekeres2=input("Kérem adjon meg egy másik évszámot: ")
BeKertEv2=int(Bekeres2)
i=0
Evek_List=[]
n=abs(BeKertEv1-BeKertEv2)
if BeKertEv1>BeKertEv2:
    for i in range(n):
        i+=1
        Ev=BeKertEv2+i
        Evek_List.append(Ev)


elif BeKertEv2>BeKertEv1:
   for i in range(n):       
        i+=1
        Ev=BeKertEv1+i
        Evek_List.append(Ev)

for i in Evek_List:
    if i%4==0 and i%100!=0 or i%400==0: 
        print("\t",i )

print("\n---------------------------------------------------------------\n")

print("Feladat 3: Európa legmagasabb épületei")
EuropaiLegnagyobbEpuletei_List=[]
beolvasottDB=0
fajl=open("legmagasabb.txt", encoding="utf-8")
#név;város;ország;magasság;emelet;épült
for egySor in fajl:
    egySor=egySor.strip()
    dbok=egySor.split(";")
    EuropaLegmagasabb={
        "Nev":dbok[0],
        "Varos":dbok[1],
        "Orszag":dbok[2],
        "Magassag":float(dbok[3]),
        "Emelet":int(dbok[4]),
        "Epult":int(dbok[5])
        }
    EuropaiLegnagyobbEpuletei_List.append(EuropaLegmagasabb)
    beolvasottDB+=1
fajl.close()
if(beolvasottDB>0):
    print("Sikeres beolvasás, beolvasott sorok száma: ",beolvasottDB)
else:
   print("Sikertelen beolvasás")
print("\n---------------------------------------------------------------\n")
print("Határozza meg és írja ki a képernyőre, hogy hány épület található a forrásállományban!")
print("\tÉpületek száma az állományban: ", len(EuropaiLegnagyobbEpuletei_List))
print("\n---------------------------------------------------------------\n")
print("Határozza meg és írja ki a képernyőre az állományba található épületek emeleteinek az összegét!")
EmeletOsszeg=0
for Emelet in EuropaiLegnagyobbEpuletei_List:
    EmeletOsszeg+=Emelet["Emelet"]
print("Európai épűlet emeleteinek összege: ",EmeletOsszeg)
print("\n---------------------------------------------------------------\n")
print("Határozza meg és írja ki a képernyőre a minta szerint, a legmagasabb épület adatait! Feltételezheti, hogy nem alakult ki holtverseny!")
i=0
MaxNev="cica"
MaxVaros="cica"
MaxOrszag="cica"
MaxMagassag=0
MaxEmelet=0
MaxEpult=0
for Emelet in EuropaiLegnagyobbEpuletei_List:
    if Emelet["Magassag"]>MaxMagassag:
        MaxMagassag=Emelet["Magassag"]
        MaxEmelet=Emelet["Emelet"]
        MaxOrszag=Emelet["Orszag"]
        MaxVaros=Emelet["Varos"]
        MaxEpult=Emelet["Epult"]
        MaxNev=Emelet["Nev"]
print("\tNév: ", MaxNev)
print("\tMagasság: ",MaxMagassag)
print("\tEmelet: ", MaxEmelet)
print("\tOrszág: ", MaxOrszag)
print("\tVáros: ",MaxVaros)
print("\tÉpítés éve: ", MaxEpult)
print("\n---------------------------------------------------------------\n")
print("Döntse el, hogy az adatok között található-e olasz épület! A keresését ne folytassa, ha a választ meg tudja adni!")
Dontes=False
for d in EuropaiLegnagyobbEpuletei_List:
    if(d["Orszag"]=="Olaszország"):
        print("\tVan Olasz ország a listában")
        break