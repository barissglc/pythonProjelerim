# GUI ile tasarımdan önce küçük bir çalışmam.

aday1 = 0
aday2 = 0

while True:
    print("Aday1 Sayi: ", aday1)
    print("Aday2 Sayi: ", aday2)

    secim = input("Hangi adaya oy kullanmak istiyorsunuz? (1/2)")

    if secim == "1":
        print("aday 1 oyu 1 arttirilmistir")
        aday1 = aday1 + 1
    elif secim == "2":
        print("aday 2 oyu 1 arttirilmistir")
        aday2 = aday2 + 1
    elif secim == "cikis":
        print("cikis yapildi")
        print("Son durum:")
        print("Aday1 Sayi: ", aday1)
        print("Aday2 Sayi: ", aday2)
        break
    else:
        print("Yanlis bir secim yaptin. Tekrar goz at")
