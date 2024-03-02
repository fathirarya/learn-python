# Contoh Perulangan for di python
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

# Contoh Perulangan while di python
counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment

# Contoh Perulangan bersarang dan mengontrol perulangan dengan break
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1