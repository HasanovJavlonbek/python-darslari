# 1-misol. O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga 
#chiqaring

davlatlatlar = ["O'zbekiston", "Qozog'ston", "Tojikiston", "Ozarbayjon"]

print(davlatlatlar)

#2-misol. Ro'xatning uzunligini konsolga chiqaring
print(len(davlatlatlar))

# 3-misol. sorted()yordam ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlatlar))

# 4-misol. sorted()yordam ro'xtani teskari konsolga chiqaring
print(sorted(davlatlatlar, reverse=True))

# 5-misol. Asl ro'yatni qaytadan konsolga chiqaring

print(davlatlatlar)

# 6-misol. reverse()metodi yordam ro'xatni ortidan chiqaring
davlatlatlar.reverse()
print(davlatlatlar)

# 7-misol.sort()metodi keyin ro'xtani avval alif bo'yicha, 
# esa alifboga teskari tizim konsolga chiqaring. 

davlatlatlar.sort()
print(davlatlatlar)
davlatlatlar.sort(reverse=True)
print(davlatlatlar)

# 8-misol. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

sonlar = list(range(120,1200))
print((sonlar))

# 9-misol. Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print("Barchasining yig'indisi \n=  >>>",sum(sonlar))

# 10-misol. Ro'yxatdagi eng katta va eng kichik son o'zining ayirmani
# hisoblang va konsolga chiqaring
a= max(sonlar)-min(sonlar)
print(a)

# 11-misol. Ro'yxatdagi maqola sonini hisoblang
print(len(sonlar))

# 12-misol. Ro'yxatning narxin, o'rtadan va boshidan 20 ta qiymatni
# konsolga chiqaring
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[1060:])

# 13-misoltaomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh','somsa','norin','shashlik','qozonkabob']

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]


#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('qozonkabob')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')
print(nonushta)

print(taomlar)

# 14-misol. #Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga
# aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring

#nonushta=type(nonushta)
nonushta[0]="qaymoq va non"












