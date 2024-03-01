# Contoh Percabangan di Python
ketersediaan = "Daging Ayam"

if ketersediaan == "Daging Ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")


# Contoh If Elif Else
nilai = int(input("Masukkan Nilai Anda : "))

if nilai >= 80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan !")
elif nilai >= 70:
    print("Hore! Anda mendapat nilai B")
    print("Tingaktkan!")
elif nilai >= 60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semanagat !")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")

# Contoh If Elif Else dengan menanmbhkan And atau Or
result = int(input("Masukkan Nilai  : "))
behavior = input("Masukkan Perilaku : ")

if result >= 80 and behavior == 'baik':
    print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
    print("Pertahankan!")
elif result >= 80 and behavior != 'baik':
    print("Kamu mendapat nilai A, tetapi perilaku Anda kurang baik")
    print("Perbaiki lagi yaa!")
else:
    print("Yuk belajar lebih giat lagi!")
