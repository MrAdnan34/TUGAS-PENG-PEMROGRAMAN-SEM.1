# PROGRAM MENGUBAH ELEMEN-ELEMEN DARI LIST YANG ADA DENGAN NILAI BARU

daftar_nilai = [87, 90, 67, 88, 98, 73, 81]

a = int(input('Masukkan A: '))
k = int(input('Masukkan K: '))

for i in range(a, k):
    indeks_baru = int(input(f'Masukkan Nilai Baru dari Indeks ke {i}: '))
    daftar_nilai[i]= indeks_baru

print(daftar_nilai)