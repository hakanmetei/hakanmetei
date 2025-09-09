print(50*"-")         # programın daha net anlaşılmasını sağlamak için 
vize=float(input("lütfen vize notunuzu giriniz:")) # kullanıcıdan veri alma ve dönüştürme
final=float(input("final notunuzu giriniz:"))  # kullanıcıdan veri alma ve dönüştürme
hesap= (vize*40)/100 + (final*60)/100  # vize ve final notunu hesaplama


if 85 <= hesap <= 100:      # koşul 1 
    print("AA")
    print(50*"-")
elif 65 <= hesap < 85:      # koşul 2
    print("BB")
    print(50*"-")
elif 45 <= hesap < 65:        # koşul 3
    print("CC")
    print(50*"-")
elif 22<= hesap < 45:
    print("DD şartlı geçiş...")  # koşul 4
    print(50*"-")
elif hesap<22:                   # koşul 5
    print("FF")
    print(50*"-")
