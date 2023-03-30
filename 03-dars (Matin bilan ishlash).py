#  harakatlarni bajaring:
#  o'zgaruvchilarni yarating:
#  kocha="Bog'bon"
#  mahalla="Sog'bon"
#  tuman="Bodomzor"
#  viloyat="Samarqand"
#  Yuqoridagi o'zgaruvchilarni jamlab, ko'rinishda konsolga chiqaring:
#  Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
manzil= f"Men {viloyat} viloyati {tuman} tumani {mahalla} mahallasi {kocha} kochasida yashayman"
print(manzil)
# Yuqoridagi o'zgaruvchilarning ( kocha, mahalla, tuman, viloyat) 
#  foydalanuvchilarni so'rang. Va avvalgi mashqni takrorlang.
kocha=input("ko'cha nomi \n>>>>")
mahalla=input("Mahalla nomi \n>>>>")
tuman=input("mahalla nomi \n>>>>")
viloyat=input("Viloyat nomi \n>>>")
print(kocha +"  ko'chasi  " + mahalla + " mahallasi " + tuman + " tumani " + viloyat + " viloyati")
#  Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
kocha=input("ko'cha nomi \n>>>>")
mahalla=input("Mahalla nomi \n>>>>")
tuman=input("Tuman nomi \n>>>>")
viloyat=input("Viloyat nomi \n>>>")
manzil = (kocha +"  ko'chasi  \n" + mahalla + " mahallasi \n" + tuman + " tumani \n" + viloyat + " viloyati")
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())







































