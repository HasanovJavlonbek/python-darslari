# 01-misol. Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi 
# juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" 
# degan xabarni chiqaring.
son = int(input("Juft son kiriting\n>>>"))
if son%2:
    print("Bu son juft emas")
else:
    print("Rahmat")
print(5%2)
print(6%2)
''''# 02-misol. Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta 
# narhini quyidagicha chiqaring:

yosh = int(input("Yoshingizni kiriting\n>>>"))
if yosh<=7 or yosh>=60:
    narx=0
elif yosh<=18:
    narx=5000
elif yosh<=30:
    narx=1000
else:
    narx=15000
print(f"Sizga kirish narxi {narx}  so'm ")

# 03-misol. Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring
#  va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
print("Assalomu alaykum ikki son kiritishinggiz lozim")
son1=int(input("Birinchi sonni kiriting\n>>>"))
son2=int(input("Ikkinchi sonni kiriting\n>>>"))
if son1<son2:
    print(f"{son1} kichik {son2} dan")
elif son1>son2:
    print(f"{son1} katta {son2} dan")
else:
    print(f"{son1} teng {son2} ga")'''