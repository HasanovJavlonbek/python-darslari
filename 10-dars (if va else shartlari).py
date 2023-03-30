# 01-misol. Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan
# ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib
# konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for mashina in cars:
    if mashina=='gm':
        print(mashina.upper())
    else:
        print(mashina.title())
# 02-misol. Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
        cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
        for mashina in cars:
            if mashina!='gm':
                print(mashina.title())
            else:
                print(mashina.upper())
# 03-misol. Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, 
# "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz,
# {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
login = input("Xush kelibsiz login kiriting \n>>>")
ism =input("Isminggizni kiriting.\n>>>")
if ism.title()=="Admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print("Xush kelibsiz,", ism.title() )
# 04-misol. Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga
# teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

x =  int(input("Butun son kiriting\n>>"))

y =  int(input("Butun son kiriting\n>>"))  
if x==y:
   print("Bu sonlar teng")
   
   
# 05-misol. Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy 
# bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni
#  chiqaring.
n =int(input("Istalgan son kiriting\n>>>>"))  
if n<0:
    print("Siz manfiy son kiritdinggiz")
if n>0:
    print("Siz musbat son kiritdinggiz")
if n==0:
    print("Siz nol raqamini kiritdinggiz")
else:
    print("Ana shunaqa gaplar")


# 06-misol. Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa 
# uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, 
# "Musbat son kiriting" degan xabarni chiqaring.

n =int(input("Istalgan son kiriting\n>>>>")) 
if n>=0:
    print("Bu sonning ildizi", pow(n, 1/2), "ga teng" )
else:
    print("Musbat son kiriting!")
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   