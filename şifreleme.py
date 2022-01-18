import time
def sifrele(mesaj):
    sifre=str.maketrans("AaBbCcÇçDdEeFfGgĞğHhIıİiJjKkLlMmNnOoÖöPpRrSsŞşTtUuÜüVvYyZz","1Ю2q3ю4w5Ы6QWEe7ы8r9Щ0t*щ-yЖuжıДoдKpГJğгHüÇGişlkFjSAhgfdsa")
    sifrelenmis=mesaj.translate(sifre)
    print(sifrelenmis)

    
def cozumle(Smesaj):
     cozum=str.maketrans("1Ю2q3ю4w5Ы6QWEe7ы8r9Щ0t*щ-yЖuжıДoдKpГJğгHüÇGişlkFjSAhgfdsa", "AaBbCcÇçDdEeFfGgĞğHhIıİiJjKkLlMmNnOoÖöPpRrSsŞşTtUuÜüVvYyZz")
     cozulmus=Smesaj.translate(cozum)
     print(cozulmus)
while True:
     time.sleep(1)
     girdi=str(input("\nMesajınızı şifrelemek için 1'e basınız\nMesajınızın şifresini çözmek için 2'ye\nÇıkmak için Q'ya basınız:\n"))
     if girdi== "1":
         mesaj=input("mesajınızı yazın:\n")
         sifrele(mesaj)
     elif girdi=="2":
        Smesaj=input("şifrelenmiş mesajınızı yazın:\n")
        cozumle(Smesaj)
     elif girdi== "q":
        print("3 saniye içinde kapatılıyor")
        time.sleep(1)
        x=3
        while True:
            x=x-1
            print(x)
            time.sleep(1)
            if x==0:
                break
        break
     else:
         print("lütfen sadece yukarıdaki değerleri giriniz")