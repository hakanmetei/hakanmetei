isim=input("lütfen isminizi giriniz:")
soy_isim=input("lütfen soyisminizi giriniz:")
yaş=  2025 -  int(input("lütfen doğum tarihini giriniz:"))
doğum_yeri= input("doğum yerinizi yazar mısınız:")

print(50*"-")
print(""" Merhaba, {} {}.
      Bugün sizlere bir süprizimiz var..
      Acaba {}. yaş gününüzü kutlamak için memleketiniz {}'ya yarın gelebilir misiniz?""".format(isim,soy_isim,yaş,doğum_yeri))
print(50*"-")