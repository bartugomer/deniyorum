#I = 1
#V = 5
#X = 10
#L = 50
#C = 100
#D = 500
#M = 1000

roman = ""

sayi = int(input("kardeşim sayı gir: "))

roman += (sayi // 1000) * "M"
if ((sayi // 100) % 10) == 4:
    roman += "CD"
elif ((sayi // 100) % 10) == 9:
    roman+= "CM"
else:
    roman += ((sayi // 500) % 2) * "D"
    roman += ((sayi // 100) % 5) * "C"
    


if ((sayi // 10) % 10) == 9:
    roman+= "XC"
elif ((sayi // 10) % 10) == 4:
    roman+= "XL"
else:
    roman += ((sayi // 50) % 2) * "L"
    roman += ((sayi // 10) % 5) * "X"

if sayi % 10 == 4:
    roman+= "IV"
elif sayi % 10 == 9:
    roman+= "IX"
else:
    roman += ((sayi // 5) % 2) * "V"
    roman += sayi % 5 * "I"


print(roman)