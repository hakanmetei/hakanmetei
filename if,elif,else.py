parolam=("abcd")                 # veri tabanındaki mevcut parola 
parola= input("parolayı giriniz:")  # kullanıcıdan parola alma 

if parola==parolam:            # eğer doğru ise parola,kullanıcı sisteme girebilir
    print("parola doğru sisteme hoşgeldiniz...")
else:                              # diğer durumlarda sisteme giremez
    print("parola yanlış....")
