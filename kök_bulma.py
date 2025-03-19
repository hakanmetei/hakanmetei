 def fonk_delta(a,b,c):
    print("*"*50)
    print("DENKLEM = ",f"{a}x^2 + {b}x + {c}")
    print("DELTA   = ",b**2 - 4*a*c)
    delta = b**2 - 4*a*c
    if delta  == 0 :
        print("denklemin çakışık iki kökü var...")
        import math
        kök1 = (-b + math.sqrt(delta))/2*a
        kök2 = (-b - math.sqrt(delta))/2*a
        print(kök1,kök2)
    elif delta < 0 :
        print("denklemin reel kökü yok yanlız karmaşık kökleri var...")
    else: 
        print("denklemin pozitif 2 kökü var...")
        import math
        kök1 = (-b + math.sqrt(delta))/2*a
        kök2 = (-b - math.sqrt(delta))/2*a
        print(kök1,kök2)
     print("*"*50)
