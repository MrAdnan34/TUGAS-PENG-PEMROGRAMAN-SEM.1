# program menghitung luas bangunan

print('RUMUS MENCARI LUAS BANGUN DATAR')
print('---Pilih Bangun Datar---')
print('1. Persegi')
print('2. Persegi Panjang')
print('3. Segitiga')
print('4. Jajar Genjang')
print('5. Layang-Layang')
print('6. Lingkaran')

a= int(input('Silahkan pilih bangun datar (input angkanya saja): '))

if a== 1:
    print('--Rumus Luas Persegi--')
    s1= int(input('Sisi persegi: '))
    luas_persegi= int(s1*s1)
    print('Hasilnya adalah: ', luas_persegi)
elif a== 2:
    print('--Rumus Luas Persegi Panjang--')
    p2= int(input('Panjang persegi panjang: '))
    l2= int(input('Lebar persegi panjang: '))
    luas_persegi_panjang= int(p2*l2)
    print("Hasilnya adalah: ", luas_persegi_panjang)
elif a== 3:
    print('--Rumus Luas Segitiga--')
    a3= int(input('Alas segitiga: '))
    t3= int(input('Tiggi segitiga: '))
    luas_segitiga= int(a3*t3/2)
    print('Hasilnya adalah: ', luas_segitiga)
elif a== 4:
    print('--Rumus Luas Jajar Genjang--')
    a4= int(input('Alas jajar genjang: '))
    t4= int(input('Tinggi jajar genjang: '))
    luas_jajar_genjang= int(a4*t4)
    print('Hasilnya adalah: ', luas_jajar_genjang)
elif a== 5:
    print('--Rumus Layang-Layang--')
    d1_5= int(input('Diagonal 1 layang-layang: '))
    d2_5= int(input('Diagonal 2 layang-layang: '))
    luas_layang_layang= int(d1_5*d2_5/2)
    print('Hasilnya adalah: ', luas_layang_layang)
elif a== 6:
    print('--Rumus Lingkaran')
    phi= 3.14
    r6= float(input('Jari-jari lingkaran: '))
    luas_lingkaran1= float(phi * r6 * r6)
    luas_lingkaran2= round(luas_lingkaran1, 1)
    print('Hasilnya adalah: ', luas_lingkaran1)
else:
    print('Data tidak diketahui, silahkan input angka yang benar')