import time

print("""
Kütüphane Programına Hoşgeldiniz...

Kitap alındığında '1' e basınız..

Kitap iade edildiğinde '2' ye basınız..

Çıkış için 'q' ye basınız..
""")

class Kitap():
    def __init__(self,kitap_adı,kitap_türü,yazarı):
        self.kitap_adı = kitap_adı
        self.kitap_türü = kitap_türü
        self.yazarı = yazarı
    def bilgiler(self):
        print("""
        
        Kitap Bilgisi
        
        Kitap Adı: {}
        Kitap Türü: {}
        Yazarı: {}
        """.format(self.kitap_adı,self.kitap_türü,self.yazarı))

tutunamayanlar = Kitap(kitap_adı= "Tutunamayanlar",kitap_türü="Roman",yazarı="Oğuz Atay")
tutunamayanlar.bilgiler()

class Kitap2(Kitap):
    pass

tehlikeli_oyunlar = Kitap(kitap_adı="Tehlikeli Oyunlar",kitap_türü="Roman",yazarı="Oğuz Atay")
tehlikeli_oyunlar.bilgiler()

class Kitap3(Kitap):
    pass

kuyucaklı_yusuf = Kitap(kitap_adı="Kuyucaklı Yusuf",kitap_türü="Roman",yazarı="Sabahattin Ali")
kuyucaklı_yusuf.bilgiler()

class Kitap4(Kitap):
    pass

karşı = Kitap(kitap_adı="Karşı",kitap_türü="Şiir",yazarı="Orhan Veli Kanık")
karşı.bilgiler()

class Kitap5(Kitap):
    pass

göğebakmadurağı = Kitap(kitap_adı="Göğe Bakma Durağı",kitap_türü="Şiir",yazarı="Turgut Uyar")
göğebakmadurağı.bilgiler()

kütüphane = [tutunamayanlar,tehlikeli_oyunlar,karşı,kuyucaklı_yusuf,göğebakmadurağı]

while True:
    işlem = input("Lütfen işlem seçiniz:")

    if işlem == 'q':
        print("İşleminiz yapılıyor..")
        time.sleep(1)
        print("Yine bekleriz..")
        break

    elif işlem == '1':

        seçim = input("Alacağınız kitabı seçiniz:")

        if seçim == 'Tutunamayanlar':
            print("Kontrol ediliyor..")
            time.sleep(1)

            if tutunamayanlar in kütüphane:
                print("Kitap kütüphanede mevcuttur..")
                karar = input("Kitabı alıyor musunuz:")
                if karar == 'Evet':
                    print("Lütfen bekleyiniz..")
                    time.sleep(1)
                    print("Talebiniz alındı. Keyifli okumalar..")
                    kütüphane.remove(tutunamayanlar)

                elif karar == 'Hayır':
                    print("Lütfen bekleyiniz..")
                    time.sleep(1)
                    print("Talebiniz alındı..")

            else:
                print("Kitap kütüphanede mevcut değildir..")

        elif seçim == 'Tehlikeli Oyunlar':
            print("Kontrol ediliyor..")
            time.sleep(1)

            if tehlikeli_oyunlar in kütüphane:
                print("Kitap kütüphanede mevcuttur..")
                karar = input("Kitabı alıyor musunuz:")
                if karar == 'Evet':
                    print("Lütfen bekleyiniz..")
                    time.sleep(1)
                    print("Talebiniz alındı. Keyifli okumalar..")
                    kütüphane.remove(tehlikeli_oyunlar)

                elif karar == 'Hayır':
                    print("Lütfen bekleyiniz..")
                    time.sleep(1)
                    print("Talebiniz alındı..")

            else:
                print("Kitap kütüphanede mevcut değildir..")

        elif seçim == 'Karşı':
            print("Kontrol ediliyor..")
            time.sleep(1)

            if karşı in kütüphane:
                print("Kitap kütüphanede mevcuttur..")
                karar = input("Kitabı alıyor musunuz:")
                if karar == 'Evet':
                    print("Lütfen bekleyiniz..")
                    time.sleep(1)
                    print("Talebiniz alındı. Keyifli okumalar..")
                    kütüphane.remove(karşı)

                elif karar == 'Hayır':
                    print("Lütfen bekleyiniz..")
                    time.sleep(1)
                    print("Talebiniz alındı..")

            else:
                print("Kitap kütüphanede mevcut değildir..")

        elif seçim == 'Kuyucaklı Yusuf':
            print("Kontrol ediliyor..")
            time.sleep(1)

            if kuyucaklı_yusuf in kütüphane:
                print("Kitap kütüphanede mevcuttur..")
                karar = input("Kitabı alıyor musunuz:")
                if karar == 'Evet':
                    print("Lütfen bekleyiniz..")
                    time.sleep(1)
                    print("Talebiniz alındı. Keyifli okumalar..")
                    kütüphane.remove(kuyucaklı_yusuf)

                elif karar == 'Hayır':
                    print("Lütfen bekleyiniz..")
                    time.sleep(1)
                    print("Talebiniz alındı..")

            else:
                print("Kitap kütüphanede mevcut değildir..")

        elif seçim == 'Göğe Bakma Durağı':
            print("Kontrol ediliyor..")
            time.sleep(1)

            if göğebakmadurağı in kütüphane:
                print("Kitap kütüphanede mevcuttur..")
                karar = input("Kitabı alıyor musunuz:")
                if karar == 'Evet':
                    print("Lütfen bekleyiniz..")
                    time.sleep(1)
                    print("Talebiniz alındı. Keyifli okumalar..")
                    kütüphane.remove(göğebakmadurağı)

                elif karar == 'Hayır':
                    print("Lütfen bekleyiniz..")
                    time.sleep(1)
                    print("Talebiniz alındı..")

            else:
                print("Kitap kütüphanede mevcut değildir..")

        else:
            if seçim in kütüphane:
                print("Kitap kütüphanede mevcuttur..")
            else:
                print("Lütfen bekleyiniz..")
                time.sleep(1)
                print("Bu kitap kütüphanemizde bulunmamaktadır..")

    elif işlem == '2':
        iade = input("İade edeceğiniz kitabı yazınız:")

        if iade == 'Tutunamayanlar':
            print("İşleminiz yapılıyor..")
            time.sleep(1)
            kütüphane.append(tutunamayanlar)
            print("İade işlemi gerçekleşti..")

        elif iade == 'Tehlikeli Oyunlar':
            print("İşleminiz yapılıyor..")
            time.sleep(1)
            kütüphane.append(tehlikeli_oyunlar)
            print("İade işlemi gerçekleşti..")

        elif iade == 'Karşı':
            print("İşleminiz yapılıyor..")
            time.sleep(1)
            kütüphane.append(karşı)
            print("İade işlemi gerçekleşti..")

        elif iade == 'Kuyucaklı Yusuf':
            print("İşleminiz yapılıyor..")
            time.sleep(1)
            kütüphane.append(kuyucaklı_yusuf)
            print("İade işlemi gerçekleşti..")

        elif iade == 'Göğe Bakma Durağı':
            print("İşleminiz yapılıyor..")
            time.sleep(1)
            kütüphane.append(göğebakmadurağı)
            print("İade işlemi gerçekleşti..")

