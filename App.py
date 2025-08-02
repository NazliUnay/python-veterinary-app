# serife nazli ünay
# 23100011009
#VETERINER OTOMASYONU
#YÖNETİCİ VE VETERINERLERIN KULLANIMINA YONELIK

import time
veteriner={} #bos_liste
hastalar={}  #bos_liste
first_id=0   #ideler sürekli artırılacak
girilen_bilgiler_hasta=['VET_ADI','ISIM','TUR','CINSIYET','RENK','YAS','AGIRLIK','KISIRLIK','AMELIYAT','ASI','KONTROL','ALCI','TESHIS']
girilen_bilgiler_veteriner=['AD','SOYAD','VET_SIFRE','UZMANLIK','NOBET']


yonetici_isim = "Nazli"
yonetici_soyisim = "Ünay"
yonetici_sifre = "Nazli123"

YONETICI_DOSYA = "data/yoneticiler.txt"
VETERINER_DOSYA = "data/veterinerler.txt"
HASTA_DOSYA = "data/hastalar.txt"
TABURCU_DOSYA = "data/taburcu.txt"
TATIL_DOSYA = "data/resmi_tatiller.txt"


def sifre_olustur():
   print("""
   Sifre olusturma kurallari
1.En az sekiz en fazla 12 karakterden olusmalidir
2.Sayi ile baslayip sayi ile bitemez
3.En az 1 büyük harf ve en az 1 küçük harf karakteri içermelidir.
4.Boşluk karakteri içeremez.
5.Şifre içinde tekrarlayan karakter bulunmamalıdır.
   """)
   while True:#yonetici icin sifre olusturma(önemli oldugu icin belirli kurallara göre)
       buyuk_harf = 0
       kucuk_harf = 0
       kontrol = 1
       turkce_karakterler = 'çışğüöI'
       sifre = input("\nLUTFEN OLUSTURMAK ISTEDIGINIZ SIFREYI GIRINIZ:")
       sifre_uzunlugu = len(sifre)
       if 8 <= sifre_uzunlugu <= 12:
           if sifre[0].isdigit() and sifre[-1].isdigit():
               print("!Sifre sayi ile baslayip sayi ile bitemez")
               kontrol = 0
           for i in range(len(sifre)):
                for j in range(i + 1, len(sifre)):
                    if sifre[i] == sifre[j]:
                       print("!Sifre tekrar eden karakterler iceremez")
                       print(f"Tekrarlayan karakter: {sifre[j]}")
                       kontrol=0
                       break
                if kontrol==0:
                    break
               
           for i in sifre:
               for k in turkce_karakterler:
                   if k == i:
                       print("!Sifre turkce karakter iceremez:", k)
                       kontrol = 0
                       break
               if 90 >= ord(i) >= 65:
                   buyuk_harf += 1
               elif 122 >= ord(i) >= 97:
                   kucuk_harf += 1
               if i == "":
                   print("!Boşluk karakteri iceremez")
                   kontrol = 0
           if buyuk_harf < 1 or kucuk_harf < 0:
               print("!Sifrede en az birer buyuk ve kucuk harf bulunmalidir.")
               kontrol = 0

           if kontrol == 0:
               print("\n!!!Gecerli bir sifre girmediniz")
               time.sleep(0.3)
               print("Lutfen tekrar sifre giriniz")
           else:
               print(":) Tebrikler gecerli bir sifre girdiniz")
               time.sleep(0.3)
               print("\n....>Sifreniz basarili bir sekilde kayit edilmistir")
               break
       else:
           print("!GECERLİ BİR SİFRE GİRMEDİNİZ")
           time.sleep(0.3)
           print("!!!!En az 8 en fazla 12 karakterden olusmalidir")

   return sifre#olusturulan sifre döndürülür

def yoneticikayit():
    global yonetici_isim, yonetici_soyisim, yonetici_sifre
    def kontrol_harf(ad): #harflerden mi olusuyor
        if ad.isalpha() == False:
            raise Exception("""
            ! Sadece alfabetik karakterlerden olusmalidir
            Lutfen tekrar giriniz :(
                                """)
        
    while True:
        try:
            yonetici_isim= input("-> Lutfen adinizi giriniz:")
            kontrol_harf(yonetici_isim)
        except Exception as hataad:
            print(hataad)
            time.sleep(0.3)
        else:
            break
    while True:
        try:
            yonetici_soyisim=input("-> Lutfen yonetici soyismini giriniz:")
            kontrol_harf(yonetici_soyisim)
        except Exception as hataad:
            print(hataad)
            time.sleep(0.3)
        else:
            break
    print("\n-> LUTFEN SIFRENIZI OLUSTURUNUZ")
    time.sleep(0.3)
    yonetici_sifre=sifre_olustur()
    print("\nŞİFRENİZ:",yonetici_sifre)

def yoneticigiris():
    #Default yönetici giriş

    while True:
        isim = input("-> lutfen isminizi giriniz:")
        if isim == yonetici_isim:
            kontrol = 1
            break
        else:
            print("!İsim yanlis girildi")
            kontrol=0
    while True:
        soyisim=input("-> Lutfen soyisminizi giriniz:")
        if soyisim==yonetici_soyisim:
            kontrol = 1
            break
        else:
            print("!Soyisim yanlıs girildi")
            kontrol=0
    print("\n!SIFRENIZI UC GIRIS HAKKINIZ VARDIR")
    for i in range(3):
        kalanhak=3-(i+1)
        sifre=input("-> Lutfen sifrenizi giriniz:")
        if sifre==yonetici_sifre:
            kontrol=1
            break
        else:
            print("!Şifre yanlis girildi")
            time.sleep(0.3)
            print("\nKALAN SIFRE GIRME HAKKINIZ:",kalanhak)
            kontrol=0
    if kontrol==0:
        return False
    else:
        return True

def ANAMENU():
    tarih=time.strftime("%d:%m:%Y")
    zaman=time.strftime("%H:%M")
    print(".......................")
    print("   TERİH:",tarih)
    print("   SAAT: ",zaman)
    print(".......................")
    print(""" 
              *************************************************
              *   VETERİNER KLİNİGİ OTOMASYONUNA HOS GELDINIZ *
              *************************************************
              0.PROGRAMI KAPAT
              1.YÖNETİCİ GİRİŞ
              2.VETERİNER GİRİS 
    """)
def Yoneticimenu():#yoneticinin önüne çıkacak menu
    print(""""
          *************************************************
          *   BU ISLEMLERI SADECE YÖNETİCİLER YAPABILIR   *
          *                                               *
          *   0 Ana Menuye Dön                            *
          *   1 Veteriner Kayıt                           *
          *   2 Veteriner Bilgi Ara                       *
          *   3 Veteriner Listele(YAZDIR)                 *
          *   4 Veteriner Güncelle                        *
          *   5 Veteriner Sil                             *
          *   6 Veteriner Nobet Olustur                   *
          *                                               *
          *************************************************
          """)

def veterinermenu():#veterinerin onune çıkacak menu
    print(""""
          **************************************************
          *   BU ISLEMLERI SADECE VETERINERLER YAPABILIR   *
          *                                                *
          *   0 Ana Menuye Dön                             *
          *   1 Hasta Kayıt                                *
          *   2 Hasta Listele(YAZDIR)                      *
          *   3 Hasta Taburcu Et                           *
          *   4 Hasta Tedavi                               *
          *   5 Hasta Bılgı Ara                            * 
          *                                                *
          **************************************************
        """)

def hastaKayit():
    def kontrol_harf(ad):#harflerden mi oluşuyor
        if ad.isalpha() == False:
            raise Exception("""
            ! Sadece alfabetik karakterlerden olusmalidir
            Lutfen tekrar giriniz :(
                                """)
    def kontrol_sayi(sayi):#rakamlardan mı oluşuyor
        if sayi.isdigit() == False:
            raise Exception("""
            ! Sadece rakamlardan olusmalidir
            Lutfen tekrar giriniz :(
            """)
    def kontrol_tur(tur):
        kontrol=0
        turler=['kedi','köpek','tavşan','kus','balık']
        for i in turler:
            if tur == i:
                kontrol=1
                break
        if kontrol==0:
            raise Exception("""
            ! Yukardakı hayvan turlerınden birini giriniz
            Lutfen tekrar giriniz :(
             """)
    def kontrol_cinsiyet(cinsiyet):
        kontrol=0
        cinsiyetler=['dişi','erkek']
        for i in cinsiyetler:
            if cinsiyet == i:
                kontrol=1
                break
        if kontrol==0:
            raise Exception("""
            ! Gecerli bir cinsiyet girmediniz
            Lutfen tekrar giriniz :(
             """)
    def kontrol_vet(vetler,veteriner):
        kontrol=0
        for i in vetler:
            if veteriner == i:
                kontrol = 1
                break
        if kontrol == 0:
            raise Exception("""
            ! Yukardakı veteriner isimlerinden birini girmediniz
            Lutfen tekrar giriniz :(
             """)
    while True:
        try:
            hasta_say= int(input("HASTA SAYISI GIRINIZ:"))
            break
        except ValueError:
            print("!LÜTFEN SAYILARDAN OLUŞAN BİR KARAKTER GİRİNİZ")

    try:
        with open(HASTA_DOSYA, "r", encoding="utf-8") as dosya_oku:
            son = dosya_oku.readlines()[-1].split()
            first_id = int(son[0])
    except ValueError:
        first_id=0
    except IndexError:
        first_id=0
    for i in range(1, hasta_say + 1):
        bilgi = dict()
        print(f"""
            *****************************************************
                {first_id + i} IDELI HASTANIN BILGILERINI GIRINIZ
            *****************************************************
        """)
        tutucu=i
        while True:
            try:
                vetler = []
                try:
                    with open(VETERINER_DOSYA, "r", encoding='utf-8') as dosya_oku:#oku
                        liste = dosya_oku.readlines()
                        print("VETERINERLER")
                        for i in range(3, len(liste)):
                            veterinerler = liste[i].split()
                            vetler.append(veterinerler[1])
                            print("*",veterinerler[1])
                except IOError:
                    print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")

                veteriner=input("-> Hangi veteriner muayene edecek:")
                kontrol_harf(veteriner)
                kontrol_vet(vetler,veteriner)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        bilgi["VET_ADI"] = veteriner
        hastalar={}
        while True:
            try:
                ad = input("-> Hastanin adi:")
                kontrol_harf(ad)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        bilgi["ISIM"] = ad
        print("\nHAYVAN TURLERI\n*kedi\n*köpek\n*tavşan\n*kus\n*balık\n")
        while True:
            try:
                tur= input("-> Hastanin turu:")
                kontrol_harf(tur)
                kontrol_tur(tur)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        bilgi["TUR"]=tur

        while True:
            try:
                print("\nCINSIYETLER\n*dişi\n*erkek")
                cinsiyet= input("-> Hastanin cinsiyeti:")
                kontrol_harf(cinsiyet)
                kontrol_cinsiyet(cinsiyet)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        bilgi["CINSIYET"]=cinsiyet
        while True:
            try:
                renk= input("-> Hastanin rengi:")
                kontrol_harf(renk)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        bilgi["RENK"]=renk

        while True:
            try:
                yas = input("-> Hastanin yasi:")
                kontrol_sayi(yas)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        bilgi["YAS"] =yas
        while True:
            try:
                agırlık = input("-> Hastanin ağırlığı:")
                kontrol_sayi(agırlık)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        bilgi["AGIRLIK"] = agırlık
        hastalar[first_id + tutucu] = bilgi#sözlük içi sözlük
    try:
        sayac = 1
        with open(HASTA_DOSYA, "a", encoding="utf-8") as dosya:#ekle
            for ide in hastalar:
                uzunluk = len(str(ide))
                dosya.write("{}".format(first_id + sayac))
                dosya.write(" " * (10 - uzunluk))#boşluklu için on
                for value in hastalar[ide].values():
                    uzunluk = len(value)
                    dosya.write("{}".format(value))
                    dosya.write(" " * (10- uzunluk))
                dosya.write("\n")
                sayac += 1
    except IOError:
        print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")

def vetideler():#tekrar tekrar kullandığım için fonk yaptim
    try:
        with open(VETERINER_DOSYA, "r", encoding="utf-8") as dosya:
            ide_listesi = []
            liste = dosya.readlines()
            for i in range(0, len(liste)):
                ide_listesi.append(liste[i].split(" ")[0])
        return ide_listesi, liste
    except IOError:
        print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")

def hastaideler():#tekara tekrar kullandığım için fonk yaptım
    try:
        with open(HASTA_DOSYA, "r", encoding="utf-8") as dosya:
            ide_listesi = []
            liste = dosya.readlines()
            for i in range(0, len(liste)):
                ide_listesi.append(liste[i].split(" ")[0])
        return ide_listesi, liste
    except IOError:
        print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")

def hastalistele():
    def kontrol_tercih(tercih):
        kontrol = 0
        tercihler = [1,2]
        for i in tercihler:
            if tercih == i:
                kontrol = 1
                break
        if kontrol == 0:
            raise Exception("""
            !YANLIS TERCIH YAPTINIZ
            1 veya 2 giriniz
            Lutfen tekrar giriniz :(
             """)
    kontrol = 0
    print("""
************************************************
*                HASTALARI GOR                 *
*  1.TUM HASTALARI GOR                         *
*  2.ISTENEN IDEYE GORE HASTAYI GOR            *
*                                              *
************************************************
       """)
    while True:
        try:
            tercih=int(input("YAPMAK ISTEDIGINIZ ISLEMI TUSLAYINIZ:"))
            kontrol_tercih(tercih)

            if tercih == 1:#dosya tumden oku
                print("-> Tum hasta bilgileri yazdiriliyor...............")
                time.sleep(0.5)
                dosya = open(HASTA_DOSYA, "r", encoding="utf-8")
                veri = dosya.read()
                print("\n" + veri)
                dosya.close()
            elif tercih == 2:#tek ideyi oku
                ide = input("\nLISTLEME YAPMAK ISTEDIGINIZ HASTANIN İDESINI GIRINIZ:")
                ide_listesi = hastaideler()[0]
                liste = hastaideler()[1]

                print(f"\n{ide} ideli hasta bilgileri yazdiriliyor..............\n")
                print('ide' + ' ' * (9 - len('ide')), end='')
                sayac = 0
                for i in ide_listesi:
                    if i == ide:
                        print("\n" + liste[sayac])
                        kontrol = 1
                    sayac += 1
                if kontrol == 0:
                    print(f"!{ide}ideli hasta yoktur")
        except ValueError:
            print("""
            !Rakam girilmeli
             Lutfen tekrar giriniz :(""")
        except Exception as hataad:
            print(hataad)
            time.sleep(1)
        else:
            break

def hasta_taburcu_et():
    ide =input("\nTABURCU EDILECEK HASTANIN İDESINI GIRINIZ:")
    kontrol=0
    liste=hastaideler()[1]
    ide_listesi=hastaideler()[0]
    for i in ide_listesi:
        if i==ide:
            taburcu=liste[ide_listesi.index(ide)]

            if len(liste[ide_listesi.index(ide)].split())>8:#taburcu olması için tedavi olması gerekir ve bu uzunluk sekizden büyüktür
                del liste[ide_listesi.index(ide)]
                with open("hastalar.txt", "w+", encoding="utf-8") as yeni_dosya:
                    for i in liste:
                        yeni_dosya.write(i)

                print("\nHASTA BILGILERI TABURCU OLANLARIN ICINE EKLENIYOR")
                with open(TABURCU_DOSYA, "a", encoding="utf-8") as dosya:
                    dosya.write(taburcu)
                time.sleep(1)
                print("HASTA TABURCU OLMUSTUR..............")
                kontrol = 1
                break
            else:
                print("\n!!!   BU HASTA TEDAVI GORMEDI TABURCU EDILEMEZ   !!!")
                return 0
    if kontrol==0:
        print(f"!{ide}ideli hasta yoktur")

def veterinerKayit():
    veteriner={} #önceki değerler olmasın
    def kontrol_harf(ad):
        if ad.isalpha()==False:
            raise Exception("""
            ! Sadece alfabetik karakterlerden olusmalidir
            Lutfen tekrar giriniz :(
                                """)

    vet_say = int(input("\nKAYIT ETMEK ISTEDIGINIZ VETERINER SAYISINI GIRINIZ:"))
    try:
        with open(VETERINER_DOSYA, "r", encoding="utf-8") as dosya_oku:#okuma
            first_id = int(dosya_oku.readlines()[-1].split(" ")[0])
    except ValueError:
        first_id=0
    except IndexError:
        first_id=0
    for i in range(1, vet_say + 1):
        bilgi = dict()
        print(f"""
           *******************************************************
                {first_id + i} IDELI VETERINER BILGILERINI GIRINIZ
           *******************************************************
        """)
        while True:
            try:
                ad = input("-> {} ideli veterinerin adi:".format(first_id + i))
                kontrol_harf(ad)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        bilgi["AD"] = ad

        while True:
            try:
                soyad = input("-> {} ideli veterinerin soyadi:".format(first_id + i))
                kontrol_harf(soyad)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        bilgi["SOYAD"]=soyad

        vetsifre = input("-> {} ideli veterinerin sifresi:".format(first_id + i))
        bilgi["VET_SIFRE"] = vetsifre

        uzmanlik = input("-> {} ideli veterinerin uzmanlik alani:".format(first_id + i))
        bilgi["UZMANLIK"] = uzmanlik

        veteriner[first_id + i] = bilgi
    sayac=1
    try:
        with open(VETERINER_DOSYA, "a", encoding="utf-8") as dosya:#ekleme
            for ide in veteriner:
                uzunluk = len(str(ide))
                dosya.write("{}".format(first_id + sayac))
                dosya.write(" " * (30 - uzunluk))
                for value in veteriner[ide].values():
                    uzunluk = len(value)
                    dosya.write("{}".format(value))
                    dosya.write(" " * (30 - uzunluk))
                dosya.write("\n")
                sayac += 1
    except IOError:
        print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")


def veteriner_listele():
    def listele():#dosyayı tumden oku
        try:
            print("Tum veterinerler listeleniyor...........")
            time.sleep(0.5)
            dosya = open(VETERINER_DOSYA, "r", encoding="utf-8")
            veri = dosya.read()
            print(veri)
            dosya.close()
        except IOError:
            print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")

    def veteriner_bul():#belirli bir idedeki veterineri yazdirir
        kontrol=0
        ide = input("\nLISTLEME YAPMAK ISTEDIGINIZ VETERINERIN İDESINI GIRINIZ:")
        ide_listesi = vetideler()[0]#fonkun dondurdugu degerin ilki
        liste = vetideler()[1]#fonkun dondurdugu degerin ikincisi

        sayac = 0
        for i in ide_listesi:
            if i == ide:
                print(f"\n{ide} ideli hasta bilgileri yazdiriliyor.........")
                print('IDE' + ' ' * (29 - len('ide')), end='')
                for i in girilen_bilgiler_veteriner:
                    print(i, ' ' * (29 - len(i)), end='')
                for i in range(150):
                    print('-', end='')
                for i in ide_listesi:
                    if i == ide:
                        print("\n" + liste[sayac])
                        kontrol = 1
                    sayac += 1
        if kontrol == 0:
            print(f"!{ide} ideli veteriner yoktur")


    print("""
****************************************
*            LISTELEME                 *
*  1.TUM VETERINERLERI LİSTELE         *
*  2.ISTENEN IDEYE GORE LİSTELE        *
*                                      *
****************************************
                """)
    while True:
        try:
            tercih = int(input("\nYapmak istediginiz islemi tuslayiniz:"))
            break
        except ValueError:
            print("!Lutfen rakam giriniz")
    kontrol=1
    while kontrol==1:
        if tercih == 1:
            listele()
            kontrol=0
        elif tercih == 2:
            veteriner_bul()
            kontrol=0
        else:
            print("!YANLIS TERCIH YAPTINIZ")

def veteriner_bilgi_ara():#spesifik bir bilgi için
    try:
        aranan_ide = input("\nHangi veterinerin bilgisini aramak istiyorsunuz(idesini giriniz):")
        kontrol = 0
        kontrol2 = 0
        liste = vetideler()[1]
        ide_listesi = vetideler()[0]
        sayac = 0
        for i in ide_listesi:
            if i == aranan_ide:
                print("\nBILGILER")
                for i in girilen_bilgiler_veteriner:
                    print("*", i)
                aranan_bilgi = input("-> Veterinerin hangi bilgisini aramak istiyorsunuz:")
                sayac2 = 1
                for bilgi in girilen_bilgiler_veteriner:
                    if bilgi == aranan_bilgi:
                        print(f"\n\n{aranan_ide} ideli veterinerin {aranan_bilgi} bilgisi--------->",
                              liste[sayac].split()[sayac2])
                        kontrol2 = 1
                    sayac2 += 1

                kontrol = 1
            sayac += 1
        if kontrol == 0:
            print(f"\n!{aranan_ide} ideli veteriner yok")
        elif kontrol2 == 0:
            print(f"\n!{aranan_ide} ideli veterinerin istediginiz bilgisine ulaşılamıyor")
    except IndexError:
        print("HENUZ BU BİLGİ GİRİLMEDİ")


def veterinersil():
    ide =input("\nSILMEK ISTEDIGINIZ VETERINERIN İDESINI GIRINIZ:")
    kontrol=0
    liste=vetideler()[1]
    ide_listesi=vetideler()[0]
    for i in ide_listesi:
        if i==ide:
            del liste[ide_listesi.index(ide)]
            with open(VETERINER_DOSYA, "w+", encoding="utf-8") as yeni_dosya:
                for i in liste:
                    yeni_dosya.write(i)
            print("Kayit siliniyor..........")
            time.sleep(1)
            print("Kayit basariyla silinmistir :)")
            kontrol=1
            break
    if kontrol==0:
        print(f"!{ide} ideli veteriner yoktur")

def veterinerguncelle():#belirli bir idedeki belirli bir bilgisini güncelle
    toplam=''
    ide=input("\nGUNCELLEME YAPMAK ISTEDIGINIZ VETERINERIN İDESINI GIRINIZ:")
    kontrol = 0
    liste = vetideler()[1]
    ide_listesi = vetideler()[0]
    sayac = 0
    for i in ide_listesi:
        if i == ide:
            print("\nDegıstırebılecegınız bılgıler")
            for i in girilen_bilgiler_veteriner:
                print("*",i)
            degisiklik=input("-> Hangi bilgiyi degistirmek istiyorsunuz:")
            sayac2=1
            for bilgi in girilen_bilgiler_veteriner:
                if bilgi==degisiklik:
                    bilgi = input(f"\n{bilgi}:")
                    yeni_liste=liste[sayac].split()
                    yeni_liste[sayac2]=bilgi
                    for i in yeni_liste:
                        toplam+=i+" " * (30 - len(i))
                    toplam+="\n"
                    liste[sayac]=toplam
                    kontrol=1
                sayac2 += 1
        sayac += 1

    if kontrol == 0:
        print("Güncelleme yapılamıyor")
        return 0
    try:
        with open(VETERINER_DOSYA, "w+", encoding="utf-8") as yeni_dosya:
            print("Istediginiz bilgi guncelleniyor..............")
            for i in liste:
                yeni_dosya.write(i)
    except IOError:
        print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")

def veterinergiris():
    print("\nVETERİNER GİRİS")
    IDE=input("-> Lütfen idenizi giriniz:")
    isim=input("-> Lutfen isminizi giriniz:")
    sifre=input("-> Lutfen sifrenizi giriniz:")

    liste = vetideler()[1]
    ide_listesi = vetideler()[0]
    kontrol=0
    sayac=0
    for i in ide_listesi:
        if i == IDE:
            vet_bilgileri=liste[sayac].split()
            if vet_bilgileri[3] ==sifre  and vet_bilgileri[1] ==isim:
                print("Tebrikler dogru giris yaptiniz :)")
                print("\n------------->Hos geldiniz sayın Veteriner: {}".format(vet_bilgileri[1]))
                kontrol=1
                return isim
        sayac+=1
    if kontrol==0:
        print("!Veteriner girisi yapilamadi")
        return False
    
def veteriner_nobet_olustur():
    print("""
                    *TATİL GUNLERİ HARİÇ HER GÜN BUTUN VETERINERLER CALISMAKTADIR
                    *TATİL GUNLERİ İCİN VETERİNERLERE NOBET YAZMANIZ GEREKMEKTEDIR    
            """)
    while True:
        try:
            with open(TATIL_DOSYA, "r", encoding="utf-8") as dosya:#oku
                veri = dosya.read()
                print(veri)
                dosya.tell()
                with open(VETERINER_DOSYA,"r",encoding="utf-8") as vet_dosya:
                    with open(TATIL_DOSYA, "r", encoding="utf-8") as dosya:
                        günler = dosya.readlines()
                        veterinerler = vet_dosya.readlines()
                        ide = input("->Hangi resmi tatil(ide gir):")
                        tutucu=0
                        for i in range(3, len(günler)):
                            if(günler[i].split()[0]==ide):
                               tutucu=1
                               break
                        if(tutucu==0):
                            print(f"{ide} ait resmi tatil yok")  
                            return     


                        print("VETERINERLER")
                        for i in range(3, len(veterinerler)):
                            print("*", veterinerler[i].split()[1])
                        vet = input("-> Hangi veterinere nobet yazmak istiyorsunuz:")
                        toplam = ""
                        sayac=2
                        kontrol=0
                        for i in range(3, len(günler)):
                            if günler[i].split()[0] == ide:
                                for i in range(3,len(veterinerler)):
                                    if veterinerler[i].split()[1] == vet:
                                        vet=veterinerler[i].split()
                                        vet.append(günler[i].split()[1])
                                        print(vet)
                                        for i in vet:
                                            toplam += i + " " * (30 - len(i))
                                        toplam += "\n"
                                        kontrol=1
                                    sayac+=1
                            if kontrol==1:
                                veterinerler[sayac] = toplam
            if kontrol==1:
                try:
                    with open(VETERINER_DOSYA, "w", encoding="utf-8") as yeni_dosya:  # tümden degiştirerek yaz
                        for i in veterinerler:
                            yeni_dosya.write(i)
                except IOError:
                    print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")
            else:
                print(f"{vet} isimli vet yok")

        except IOError:
            print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")
        else:
            break

def hasta_bilgi_ara():#belirli bi özellikteki hastalari yazdır
    def vetlere_göre():
        while True:
            try:
                hangi_vet = input("\nHangi veterinerin hastalari aransın:")
                print('IDE' + ' ' * (9 - len('ide')), end='')
                for i in girilen_bilgiler_hasta:
                    print(i, ' ' * (9 - len(i)), end='')
                for i in range(140):
                    print('-', end='')
                print("\n")
                with open(HASTA_DOSYA, "r", encoding="utf-8") as dosya:
                    hastalar = dosya.readlines()
                    for i in range(3, len(hastalar)):
                        if hastalar[i].split()[1] == hangi_vet:
                            print(hastalar[i], end='')
            except IOError:
                print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")
            else:
                break

    def ture_göre():
        def kontrol_tur(tur):
            kontrol = 0
            turler = ['kedi', 'köpek', 'tavşan', 'kus', 'balık']
            for i in turler:
                if tur == i:
                    kontrol = 1
                    break
            if kontrol == 0:
                raise Exception("""
                ! Yukardakı hayvan turlerınden birini giriniz
                Lutfen tekrar giriniz :(
                 """)

        while True:
            try:
                print("\nHAYVAN TURLERI\n*kedi\n*köpek\n*tavşan\n*kus\n*balık\n")
                hangi_tur = input("\nHangi turdekı hastalar aransın:")
                kontrol_tur(hangi_tur)
                print('IDE' + ' ' * (9 - len('ide')), end='')
                for i in girilen_bilgiler_hasta:
                    print(i, ' ' * (9 - len(i)), end='')
                for i in range(140):
                    print('-', end='')
                print("\n")
                with open(HASTA_DOSYA, "r", encoding="utf-8") as dosya:
                    hastalar = dosya.readlines()
                    for i in range(3, len(hastalar)):
                        if hastalar[i].split()[3] == hangi_tur:
                            print(hastalar[i],end='')
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            except IOError:
                print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")
            else:
                break

    def cinsiyete_göre():
        def kontrol_cinsiyet(cinsiyet):
            kontrol = 0
            cinsiyetler = ['dişi', 'erkek']
            for i in cinsiyetler:
                if cinsiyet == i:
                    kontrol = 1
                    break
            if kontrol == 0:
                raise Exception("""
                ! Gecerli bir cinsiyet girmediniz
                Lutfen tekrar giriniz :(
                 """)
        while True:
            try:
                print("CINSIYETLER\n*dişi\n*erkek")
                hangi_cinsiyet = input("\nHangi cinsiyetteki hastalar aransın:")
                kontrol_cinsiyet(hangi_cinsiyet)
                print('IDE' + ' ' * (9 - len('ide')), end='')
                for i in girilen_bilgiler_hasta:
                    print(i, ' ' * (9 - len(i)), end='')
                for i in range(140):
                    print('-', end='')
                print("\n")
                with open(HASTA_DOSYA, "r", encoding="utf-8") as dosya:
                    hastalar = dosya.readlines()
                    for i in range(3, len(hastalar)):
                        if hastalar[i].split()[4] == hangi_cinsiyet:
                            print(hastalar[i], end='')
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            except IOError:
                print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")
            else:
                break

    def tedavi_edilenler():
        liste = hastaideler()[1]
        print("TEDAVI OLAN HASTALAR")
        for i in range(3, len(liste)):
            if len(liste[i].split()) >8:
                print(f"*{liste[i].split()[0]} ideli {liste[i].split()[2]}")

    def tedavi_edilmeyenler():
        liste = hastaideler()[1]
        print("TEDAVI OLMAYAN HASTALAR")
        for i in range(3, len(liste)):
            if len(liste[i].split()) == 8:
                print(f"*{liste[i].split()[0]} ideli {liste[i].split()[2]}")
    def bilgi():
        try:
            aranan_ide = input("\nHangi hastanın bilgisini aramak istiyorsunuz(idesini giriniz):")
            kontrol = 0
            kontrol2 = 0
            liste = hastaideler()[1]
            ide_listesi = hastaideler()[0]
            sayac = 0
            for i in ide_listesi:
                if i == aranan_ide:
                    print("\nBILGILER")
                    for i in girilen_bilgiler_hasta:
                        print("*", i)
                    aranan_bilgi = input("-> Veterinerin hangi bilgisini aramak istiyorsunuz:")
                    sayac2 = 1
                    for bilgi in girilen_bilgiler_hasta:
                        if bilgi == aranan_bilgi:
                            print(f"\n\n{aranan_ide} ideli hastanin {aranan_bilgi} bilgisi--------->",
                                  liste[sayac].split()[sayac2])
                            kontrol2 = 1
                        sayac2 += 1
                    kontrol = 1
                sayac += 1
            if kontrol == 0:
                print(f"\n!{aranan_ide} ideli hasta yok")
            elif kontrol2 == 0:
                print(f"\n!{aranan_ide} ideli hastanin istediginiz bilgisine ulaşılamıyor")
        except IndexError:
            time.sleep(0.3)
            print("\nHASTA HENUZ TEDAVI OLMADI")

    def taburcu():
        try:
            print("-> Taburcu edilen hasta bilgileri yazdiriliyor...............")
            time.sleep(0.5)
            dosya = open(TABURCU_DOSYA, "r", encoding="utf-8")
            veri = dosya.read()
            print("\n" + veri)
            dosya.close()

        except IOError:
            print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")

    while True:
        try:
            print("""
**********************************************
*              BILGI ARAMA                   *  
*                                            *       
*   1.Veterinerlere göre                     *
*   2.Ture göre                              *
*   3.Cinsiyete göre                         *
*   4.Tedavı gorenler                        *
*   5.Tedavı gormeyenler                     *
*   6.Hastanın bilgisini                     *
*   7.Taburcu olan hastalar                  *
*                                            *
*********************************************
                """)
            tercih = int(input("\nYapmak istediginiz islemi tuslayiniz:"))
            break
        except ValueError:
            print("!Lutfen rakam giriniz")
    kontrol=1
    while kontrol==1:
        if tercih == 1:
            vetlere_göre()
            kontrol=0
        elif tercih == 2:
            ture_göre()
            kontrol=0
        elif tercih == 3:
            cinsiyete_göre()
            kontrol=0
        elif tercih == 4:
            tedavi_edilenler()
            kontrol=0
        elif tercih == 5:
            tedavi_edilmeyenler()
            kontrol=0
        elif tercih == 6:
            bilgi()
            kontrol=0
        elif tercih == 7:
            taburcu()
            kontrol=0
        else:
            print("!YANLIS TERCIH YAPTINIZ")

def hasta_tedavi(isim):#tedavi edilirken yapılan işlemelere evet yazılır en son tedavi ücreti hesaplanır
    def tedavi_edilmeyenler():
        liste = hastaideler()[1]
        print("TEDAVI OLMAYAN HASTALAR")
        for i in range(3, len(liste)):
            if len(liste[i].split()) == 8:
                print(f"*{liste[i].split()[0]} ideli {liste[i].split()[2]}")
    def kontrol_cevap(cvp):
        if cvp=='evet':
            pass
        elif cvp=='hayir':
            pass
        else:
            raise Exception("""
            !YANLIS TERCIH YAPTINIZ
            evet veya hayir giriniz
            Lutfen tekrar giriniz :(
            """)

    def hasta_muayene():
        print("!!LUTFEN \'evet\' veya \'hayir\' ŞEKLİNDE TUSLAYINIZ\n")
        while True:
            try:
                kısırlık = input("-> HASTA KISIRLAŞTIRILACAK MI:")
                kontrol_cevap(kısırlık)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        while True:
            try:
                ameliyat = input("-> HASTA AMELİYAT OLACAK MI:")
                kontrol_cevap(ameliyat)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        while True:
            try:
                asi = input("-> HASTANIN ASILARI TAM MI:")
                kontrol_cevap(asi)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        while True:
            try:
                kontroller = input("-> HASTA KONTROLLERE GİRECEK MI:")
                kontrol_cevap(kontroller)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        while True:
            try:
                alci = input("-> HASTA ALCI TEDAVISI GORECEK MI:")
                kontrol_cevap(alci)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break

        teshis=input("\n-> HASTANIN HASTALIGI NEDIR:")
        return kısırlık,ameliyat,asi,kontroller,alci,teshis
    def muayene_ucretlendir(ide):
        print("""
        ********************************************************
        *                 MUAYENE UCRETLERI                    *
        *  1 Kısırlaştırma                      :3000 TL       *
        *  2 Ameliyat                           :3000 TL       *
        *  3 Asi                                :2000 TL       *
        *  4 Kontroller(Röntgen/MR/Ultrason)    :1000 TL       * 
        *  5 Alci                               :1000 TL       *
        *  6 Genel Bakim                        :1000 RL       *
        *                                                      *
        ********************************************************""")

        liste = hastaideler()[1]
        ide_listesi = hastaideler()[0]
        fiyatler={'kısırlık':3000,
                  'ameliyat':3000,
                  'asi':2000,
                  'kontroller':1000,
                  'alci':1000,
                  'genel_bakım':1000,
                  }

        toplam_fiyat=1000
        for i in ide_listesi:
            if i == ide:
                print("UCRETLENDIRME YAPILIYOR")
                print("*Genel bakim zorunludur")
                muayene_edilecek_hasta = liste[ide_listesi.index(ide)].split()
                for i in range(8,len(muayene_edilecek_hasta)):
                    if muayene_edilecek_hasta[i]=='evet':
                        for key,value  in fiyatler.items():
                            if key==liste[1].split()[i]:
                                print(f"+{key} ucreti ekleniyor")
                                toplam_fiyat += value

        print(f"\n*FIYAT:{toplam_fiyat} TL")


    tedavi_edilmeyenler()
    ide = input("\nHANGI HASTAYI MUAYENE ETMEK ISTIYORSUNUZ(ide giriniz)")

    kontrol = 0
    toplam=''
    liste = hastaideler()[1]
    ide_listesi = hastaideler()[0]
    sayac=0
    for i in ide_listesi:
        if i == ide:
            muayene_edilecek_hasta= liste[ide_listesi.index(ide)].split()
            if muayene_edilecek_hasta[1]==isim:
                if len(muayene_edilecek_hasta) == 8:
                    for i in hasta_muayene():
                        muayene_edilecek_hasta.append(i)
                    for i in muayene_edilecek_hasta:
                        toplam += i + " " * (10 - len(i))
                    toplam += "\n"
                    liste[sayac] = toplam
                    kontrol = 1
                else:
                    print("!BU HASTA ONCEDEN MUAYENE EDILMISTIR")
            else:
                print("!BU HASTA SİZİN HASTANİZ DEGİL MUAYENE EDEMEZSINIZ")
                return 0
        sayac+=1
    try:
        with open(HASTA_DOSYA, "w+", encoding="utf-8") as yeni_dosya:
            for i in liste:
                yeni_dosya.write(i)
    except IOError:
        print("!!!!!!!PROGRAMIN VERI TABANINA ERISILEMIYOR!!!!!!!")

    if kontrol==0:
        print(f"!{ide} ideli hasta yoktur")
        return 0
    muayene_ucretlendir(ide)

tercih=1


while tercih != 0:
    ANAMENU()
    
    while True:
        try:
            tercih1 = int(input("\nLUTFEN YAPMAK ISTEDIGINIZ ISLEMI SECINIZ:"))
            break
        except ValueError:
            print("!lutfen rakam tuslayiniz")
    if tercih1==0:
        print("!!!!!!!!!!!!!!!         PROGRAMDAN CIKIS YAPILIYOR         !!!!!!!!!!!!!!!")
        break
    if tercih1==1:#yöneticinin yapabildiği işlemler
        print("""
        -> 1 : Yönetici Değiştir:
        -> 2 : Yönetici Giriş:
              """)
        sonuc=False
        tercih = int(input("\nLUTFEN YAPMAK ISTEDIGINIZ ISLEMI SECINIZ:"))
        if(tercih==1):
            print("\n\n\t\t\t\t.......................")
            print("\t\t\t\t YÖNETİCİ KAYIT EKRANI ")
            print("\t\t\t\t.......................")
            yoneticikayit()
        else:
            sonuc=yoneticigiris()
         
        
        if sonuc==True:
            print(f"\nHOS GELDİNİZ: {yonetici_isim} {yonetici_soyisim}")
            while True:
                Yoneticimenu()
                while True:
                    try:
                        tercih2 = int(input("\nLUTFEN YAPMAK ISTEDIGINIZ ISLEMI SECINIZ:"))
                        break
                    except ValueError:
                        print("!lutfen rakam tuslayiniz")
                if tercih2 == 0:
                    break
                elif tercih2 == 1:
                    veterinerKayit()
                elif tercih2 == 2:
                    veteriner_bilgi_ara()
                elif tercih2 == 3:
                    veteriner_listele()
                elif tercih2 == 4:
                    veterinerguncelle()
                elif tercih2 == 5:
                    veterinersil()
                elif tercih2 == 6:
                    veteriner_nobet_olustur()
                else:
                    print("\n!Yanlıs tusladiniz")
        else:
            print("!!!!! MAALESEF YONETİCİ GİRİSİ YAPILAMIYOR !!!!!")
    elif tercih1==2:#veterinerin yapabildiği işlemler
        isim=veterinergiris()
        if isim!=False:
            while True:
                veterinermenu()
                while True:
                    try:
                        tercih2 = int(input("\nLUTFEN YAPMAK ISTEDIGINIZ ISLEMI SECINIZ:"))
                        break
                    except ValueError:
                        print("!lutfen rakam tuslayiniz")
                if tercih2 == 0:
                    break
                elif tercih2 == 1:
                    hastaKayit()
                elif tercih2 == 2:
                    hastalistele()
                elif tercih2 == 3:
                    hasta_taburcu_et()
                elif tercih2 == 4:
                    hasta_tedavi(isim)
                elif tercih2==5:
                    hasta_bilgi_ara()
                else:
                    print("\n!Yanlıs tusladiniz")
    else:
        print("\n!Yanlıs tusladınız")



