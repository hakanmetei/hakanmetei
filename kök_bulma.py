import math  # import'u en başa taşıyoruz, bir kere import etmek yeterli

def fonk_delta(a,b,c):
    print("*"*50)
    print("DENKLEM = ",f"{a}x^2 + {b}x + {c}")
    
    # Delta hesaplamasını bir kere yapıp değişkende saklıyoruz
    delta = b**2 - 4*a*c
    print("DELTA   = ", delta)
    
    # Kök hesaplama formülünü fonksiyon olarak tanımlıyoruz
    def kok_hesapla(b, delta, a):
        kok1 = (-b + math.sqrt(delta))/(2*a)  # 2*a parantez içine alındı
        kok2 = (-b - math.sqrt(delta))/(2*a)
        return kok1, kok2
    
    if delta == 0:
        print("Denklemin çakışık iki kökü var...")
        kok1, kok2 = kok_hesapla(b, delta, a)
        print(f"kök1: {kok1}\nkök2: {kok2}")
    
    elif delta < 0:
        print("Denklemin reel kökü yok, sadece karmaşık kökleri var...")
    
    else: 
        print("Denklemin iki farklı reel kökü var...")
        kok1, kok2 = kok_hesapla(b, delta, a)
        print(f"kök1: {kok1}\nkök2: {kok2}")
    
    print("*"*50)
