import random

def tas_kagit_makas_SELİN_ÇABUKEL():
    def baslangic_mesaji():
        #İlk başlangıç mesajı ekrana yazdırdık.
        print("Taş-Kağıt-Makas oyununa hoş geldiniz!")
        print("Yapmanız gerekenler sadece 'taş', 'kağıt', 'makas' veya oyun oynamaya devam etmek istemiyorsanız 'çık' yazmak.")
        print("Kurallar: 1. Taş makası ezer, 2. Kağıt taşı sarar, 3. Makas kağıdı keser, 4. İlk iki turu kazanan oyunun galibi olur.")
        print("Keyifli oyunlar dileriz :)")

    def bilgisayar_secim_fonks():
        #Bilgisayardan rastgele bir seçim aldık ve seçimi döndürdük.
        secimler = ["taş", "kağıt", "makas"]
        return random.choice(secimler)

    def kullanici_secim_fonks():
        #Kullanıcıdan seçim aldık.
        while True:
            kullanici_sec = input("Taş, kağıt veya makas seçin (oyundan çıkmak için 'çık' yazın): ").lower()
            if kullanici_sec in ["taş", "kağıt", "makas"]:
                return kullanici_sec
            elif kullanici_sec == "çık":
                return "çık"
            else:
                print("Geçersiz seçim, lütfen 'taş', 'kağıt' veya 'makas' yazın.")

    def kazanan(kullanici_secimi, bilgisayar_secimi):
        #kazananın sonucunu if else ile belirledik.
        if kullanici_secimi == bilgisayar_secimi:
            return "Beraberlik!"
        elif (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or \
             (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
             (kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt"):
            return "Kazandınız!"
        else:
            return "Kaybettiniz!"

    def oynanan_tur():
        #HTur sayısını gösterdik ve kazananı belirledik.
        kullanici_wins = 0
        bilgisayar_wins = 0
        tur_sayisi = 1
        
        while kullanici_wins < 2 and bilgisayar_wins < 2:
            print(f"\n--- Tur {tur_sayisi} ---")
            kullanici_secimi = kullanici_secim_fonks()
            if kullanici_secimi == "çık":
                return "çık"
            
            bilgisayar_secimi = bilgisayar_secim_fonks()
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
            
            sonuc = kazanan(kullanici_secimi, bilgisayar_secimi)
            print(sonuc)
            
            if sonuc == "Kazandınız!":
                kullanici_wins += 1
            elif sonuc == "Kaybettiniz!":
                bilgisayar_wins += 1
            
            print(f"Tur {tur_sayisi} Sonuçları: Kullanıcı {kullanici_wins} - Bilgisayar {bilgisayar_wins}")
            tur_sayisi += 1
        
        if kullanici_wins == 2:
            return "Kullanıcı"
        elif bilgisayar_wins == 2:
            return "Bilgisayar"

    baslangic_mesaji()

    toplam_oyun = 0
    while True:
        toplam_oyun += 1
        print(f"\n--- Oyun {toplam_oyun} ---")
        
        oyun_kazanani = oynanan_tur()
        if oyun_kazanani == "çık":
            print("Oyun sona erdi. Bir daha bu oyuna girme!")
            break
        else:
            print(f"Bu oyunun galibi: {oyun_kazanani}!")
        
        while True:
            tekrar_oyna = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").strip().lower()
            if tekrar_oyna == "evet":
                break
            elif tekrar_oyna == "hayır":
                print("Oynadığınız için teşekkürler.Görüşmek üzeree :)")
                return
            else:
                print("Geçersiz yanıt. Lütfen 'evet' veya 'hayır' yazın.")
        
        # Bilgisayarın devam etmek isteyip istemediğini rastgele belirledik.
        bilgisayar_devam = random.choice(["evet", "hayır"])
        if bilgisayar_devam == "hayır":
            print("Bilgisayar oyunu bitirdi.Oynadığınız için teşekkürler.Görüşmek üzeree :)")
            break
        else:
            print("Bilgisayar oyuna devam ediyor ")

#Fonksiyonu çalıştırdık.
tas_kagit_makas_SELİN_ÇABUKEL()
