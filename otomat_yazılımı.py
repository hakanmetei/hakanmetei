
## alkol ve yiyecek otamatı için yazılım 

b=int(input("lütfen doğum tarihinizi giriniz:"))
yaş = 2025-b


if yaş < 18:
    print("ALKOL ALAMAZSINIZ !!! ")

    while True:
        print("*"*50)
        a = int(input("""başka istediğin bir şey var mı ?\n1-çikolata\n2-kola\n3-cips  \nçıkmak için "0"'a basabilirsiniz\ncevabınız nedir:"""))
        print("*" * 50)
        if a == 1:
            print("çikolata veriliyor...VERİLDİ")

        elif a == 2:
            print("kola hazırlanıyor...VERİLDİ")

        elif a == 3:
            print("cips veriliyor...VERİLDİ")

        elif a== 0:
            print("çıkış yapılıyor...YAPILDI")
            print("*" * 50)
            break
        else:
            print("geçersiz tuşlama yaptınız lütfen tekrar deneyiniz...")





elif  yaş >= 18:
    print("yaşınız uygun")
    while True:
        print("*" * 50)
        a = int(input(
            """başka istediğin bir şey var mı ?\n1-çikolata\n2-kola\n3-cips  \nçıkmak için "0"'a basabilirsiniz\ncevabınız nedir:"""))
        print("*" * 50)
        if a == 1:
            print("çikolata veriliyor...VERİLDİ")

        elif a == 2:
            print("kola hazırlanıyor...VERİLDİ")

        elif a == 3:
            print("cips veriliyor...VERİLDİ")

        elif a == 0:
            print("çıkış yapılıyor...YAPILDI")
            print("*" * 50)
            break
        else:
            print("geçersiz tuşlama yaptınız lütfen tekrar deneyiniz...")

else :
    print("hatalı giriş yaptınız")
    while True:
        print("*" * 50)
        a = int(input(
            """başka istediğin bir şey var mı ?\n1-çikolata\n2-kola\n3-cips  \nçıkmak için "0"'a basabilirsiniz\ncevabınız nedir:"""))
        print("*" * 50)
        if a == 1:
            print("çikolata veriliyor...VERİLDİ")

        elif a == 2:
            print("kola hazırlanıyor...VERİLDİ")

        elif a == 3:
            print("cips veriliyor...VERİLDİ")

        elif a == 0:
            print("çıkış yapılıyor...YAPILDI")
            print("*" * 50)
            break
        else:
            print("geçersiz tuşlama yaptınız lütfen tekrar deneyiniz...")



