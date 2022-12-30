# program menentukan ganjil/genap dan positif/negatif suatu bilangan

print("--Silahkan Masukkan Angka--")
x= int(input("Angka awal: "))
y= int(input("Angka akhir: "))

for a in range (x, y+1):
    if a%2==0 and a>0:
        hasil= "genap dan positif"
    elif a%2==0 and a<0:
        hasil= "genap dan negatif"
    elif a%2==1 and a>0:
        hasil= "ganjil dan positif"
    elif a%2==1 and a<0:
        hasil= "ganjil dan negatif"
    else:
        hasil= "nol"

    print(a, "termasuk bilangan", hasil)