# 01-misol. Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi 
# har bir ismga takrorlanuvchi xabar yozing
dustlar = ["mehriddin", "komeljon", "dilmurod", "abdulvohid", "mullajon"]
for dust in dustlar:
    print("Assalomu alaykum", dust.title(), "ishlaringgiz yaxshimi")
    print("Nima gaplar sizlarda")
    
# 02-misol. Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n 
# takrorlandi" degan xabarni chiqaring (n o'rniga kod necha
#  marta takrorlanganini yozing)
print ("Siz", len(dustlar), "ta dustingizni kiritdingiz")

# 03-misol. 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing.
#  Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11,100 ,2))
sonning_kubi =[]
for son in sonlar:
    sonning_kubi.append(son**3)
print(sonlar)    
print(sonning_kubi)

# 04-misol. Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va
# kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.

kinolar = []
print("Siz yoqtirgan 5 ta eng yaxshi kinolar qaysilar?")
for n in range(5):
    kinolar.append(input(f"{n+1}-kino:"))
print(kinolar)

# 05-misol. Foydalanuvchidan bugun nechta odam bilan uchrashganini
# (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini 
# birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

odamlar= int(input("Siz bugun nechta kishi bilan suhbat qildingiz\n>>>"))
ismlar=[] 
for n in range(odamlar):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi:\n>>>> "))
print(ismlar)          

































