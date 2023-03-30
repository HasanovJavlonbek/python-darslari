# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu 
# inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, 
# manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring
# :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan


'''

dadam = {'ismi':'begali','t_yil':1979, 't_kun':'04-Aprel'}
ayam = {'ismi':'xursheda','t_yil':1980, 't_kun':'11-Aprel'}
akam = {'ismi':'javohir','t_yil':2000, 't_kun':'26-Oktabr'}
singlim_1 = {'ismi':'gulsevar','t_yil':2005, 't_kun':'16-Yanvar'}
singlim_2 = {'ismi':'zaynura','t_yil':2014, 't_kun':'07-Yanvar'}
ukam = {'ismi':'kamronbek','t_yil':2016, 't_kun':'27-Oktabr'}
print(f"Mening dadamning ismi {dadam['ismi'].title()}, {dadam['t_yil']}-yil\
  {dadam['t_kun']}da  tug'ilgan")
print(f"Ayamning ismi {ayam['ismi'].title()}, {ayam['t_yil']}-yil\
    {ayam['t_kun']}da  tug'ilgan")
print(f"Akamning ismi {akam['ismi'].title()}, {akam['t_yil']}-yil\
      {akam['t_kun']}da  tug'ilgan")
print(f"Katta singlimning ismi {singlim_1['ismi'].title()}, {singlim_1['t_yil']}-yil\
        {singlim_1['t_kun']}da  tug'ilgan")
print(f"Kichik sinlimning ismi {singlim_2['ismi'].title()}, {singlim_2['t_yil']}-yil\
  {singlim_2['t_kun']}da  tug'ilgan")
print(f"Ukamning ismi {ukam['ismi'].title()}, {ukam['t_yil']}-yil\
  {ukam['t_kun']}da  tug'ilgan")
  

  
# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida
# 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga
# chiqaring: Alining sevimli taomi osh.
  


taom = {1:'yupqa', 2:'shurbo',3:'manti',4:'shirguruch',5:'osh',6:'somsa',
        7:'somsa'}
print(f"Dadam  {taom[1].title()}ni, Ayam {taom[2].title()}ni \
   Akam {taom[3].title()}ni  yoqtirishadi")
   
   
   '''
   
#   Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta 
#   so'z (atamani) kiriting (masalan integer, float, string, if, else va
#   hokazo) va har birining qisqacha tarjimasini yozing



lugat={'int':'butun','float':'haqiqiy','string':'matn', 'input':'kiritish',
       'if':'agar', 'else':'aks holda','for':'uchun', 'in':'ichida',
       'and':'va', 'or':'yoki'}
print(lugat)   


# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini
# yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, 
# "Bunda so'z mavjud emas" degan xabarni chiqaring.

in_uz=input("Biror so'z kiriting \n>>>")
tarjima = lugat.get(in_uz, "Bunday so'z bizda mavjud emas")
print(tarjima)



# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga
# tushunarli ko'rinishda chiqaring.



in_oz=input("Biror so'z kiriting \n>>>")
tarjima = lugat.get(in_oz)
if tarjima ==None:
    print("Bunday kalit so'z yuq bizda")
else:
    print(f"{in_oz}ning tarjimasi {tarjima} bo'ladi")

















  