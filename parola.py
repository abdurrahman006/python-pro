import random


harfer="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk=int(input("parola uzunluğunu girinizi."))
parola=""
for i in range(uzunluk):    
    sembol=random.choice(harfer)
    parola=parola+sembol

print(parola)
