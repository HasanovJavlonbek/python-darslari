# 1-misol. ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning 
# ismini kiriting
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
ismlar = ["mehriddin", "Javohir", "Azizbek"]
print("Assalomu alaykum" + "  " + ismlar[2] + " " + "yaxshimisiz ")
print(ismlar[1],  "sen ham yaxshimi. Rassiyaga ketgan hozir", ismlar[0].title())

# 2-misol. sonlar deb nomlangan ro'yxat yarating va paydo bo'ladigan 
# turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).

sonlar = [25, 52, -9, -85, 0, -56, 6.2, 5.1]
print(sonlar)

# 3-misol. Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik
# amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlar qiymatini xususiyatlarini
# o'zgartiring, ba'zilarini esa almashtiring.

print(sonlar[0+2])
sonlar[5]=55
del sonlar[-1]
print(sonlar)

# 4-misol. t_shaxslarva z_shaxslardegan 2 ta ro'yxat yarating va biriga 
# o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, unga asosan
 # zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.

t_shaxslar =["Alesher Navoiy", "Amir Temur", "Mirzo Ulug'bek"]
z_shaxslar =["Abdulloh domla", "Shukrulloh domla", "Abror Muxtor Ali domla"]
print("Tarixdagi bizga o'rnak bo'luvchi kishilar \n>>>>", t_shaxslar, "va hokozolar")
print("Hozirda bizga o'rnak bo'luvchi kishilar \n>>>", z_shaxslar, "va hokozolar")

# 5-misol. Yuqoridagi ro'yxatlarning har biridan bittadan qiymatini
# sug'urib olib ( .pop()), ko'rinishda chiqaring
bobomiz = t_shaxslar.pop(1)
ustozimiz = z_shaxslar.pop(0)
print(bobomiz)
print(ustozimiz)

# 6-misol. friends nomli bo'sh ro'xat tuzing va unga .append()yordam 5-6 ta
#  mehmonga chaqirmoqchi bo'lgan do'stingizni kiriting.
friends = []
friends.append("Mehriddin")
friends.append("Komeljon")
friends.append("Javohir")
friends.append("Azizbek")
friends.append("Asadbek")
friends.append("Dilmurod")
print(friends)

# 7-misol. yuqdagi ro'yxatdan mehmonga kela olmaydigan odamlarni 
# .remove()metodi yordamida o'chrib Yuqoring.

friends.remove("Asadbek")
friends.remove("Mehriddin")
print(friends)

# 8-misol. Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

friends.append("Abdulaziz")
friends.insert(3, "Og'abek")
friends.insert(0, "Abdulvohid")

print(friends)

# 9-misol. Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop()va 
# .append()metodlari olib mehmonga kelgan do'stlaringizning 
# ismini friends ro'yxatidan sug'urib, mehmonlar ro'yxatiga qo'shing.
mehmonlar =[]
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(-2))
mehmonlar.append(friends.pop(0))

print(mehmonlar)





