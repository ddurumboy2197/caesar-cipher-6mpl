def caesar_shifrlash(matn, shift):
    natija = ""
    for harf in matn:
        if harf.isalpha():
            asosiy_harf = 'a' if harf.islower() else 'A'
            natija += chr((ord(harf) - ord(asosiy_harf) + shift) % 26 + ord(asosiy_harf))
        else:
            natija += harf
    return natija

def caesar_ochirish(matn, shift):
    return caesar_shifrlash(matn, -shift)

matn = input("Matn kiriting: ")
shift = int(input("Shifrlash uchun shift qiymatini kiriting: "))

shifrlangan_matn = caesar_shifrlash(matn, shift)
ochirilgan_matn = caesar_ochirish(shifrlangan_matn, shift)

print("Shifrlangan matn:", shifrlangan_matn)
print("Ochirilgan matn:", ochirilgan_matn)
