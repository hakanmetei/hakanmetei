print("""hesap makinesine hoşgeldiniz
     1. toplama 
     2. çıkarma 
     3. çarpma 
     4. bölme 
     5. üs alma 
     q. çıkış
     """)
     
işlem = input("lütfen işlemi seç:")


 
if işlem =="1":
    sayı1=float(input("lütfen ilk sayıyı giriniz"))
    sayı2=float(input("lütfen ikinci sayıyı giriniz"))
    print("toplama işleminizin somnucu {}'dir".format(sayı1+sayı2))
 #tekrar aynılarını yazmaya gerek yok kopyalayıp yapıştırmak yeterlidir   
    
elif işlem=="2":
    sayı1=float(input("lütfen ilk sayıyı giriniz:"))
    sayı2=float(input("lütfen ikinci sayıyı giriniz:"))
    print("çıkarma işleminizin somnucu {}'dir".format(sayı1-sayı2))
    
elif işlem=="3":
    sayı1=float(input("lütfen ilk sayıyı giriniz:"))
    sayı2=float(input("lütfen ikinci sayıyı giriniz:"))
    print("çarpma işleminizin somnucu {}'dir".format(sayı1*sayı2))
    
elif işlem=="4":
    sayı1=float(input("lütfen ilk sayıyı giriniz:"))
    sayı2=float(input("lütfen ikinci sayıyı giriniz:"))
    print("bölme işleminizin somnucu {}'dir".format(sayı1/sayı2))
    
elif işlem=="5":
    sayı1=float(input("lütfen ilk sayıyı giriniz:"))
    sayı2=float(input("lütfen kaçıncı üs alınacak onu giriniz:"))
    print("üs alma işleminizin somnucu {}'dir".format(sayı1**sayı2))
    
elif işlem=="q" or işlem=="Q":
    print("kendinize iyi bakınız :)")
    
else:
    print("hatalı tuşlama yaptınız.lütfen tekrar deneyiniz.")
    
input()