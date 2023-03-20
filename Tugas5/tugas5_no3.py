# PROGRAM MENGITUNG SELISIH DARI JUMLAH DIAGONAL SEBUAH MATRIKS YANG DIINPUT

x = int(input('Masukkan Jumlah Baris dan Kolom: '))
matriks = [[int(input(f'Matriks baris-{a+1} kolom-{b+1}: ')) for a in range(x)] for b in range(x)]
diagonal1 = []
for i in range(x):
    matriks1 = matriks[i][i]
    diagonal1.append(matriks1)
print(f'Diagonal 1 = {sum(diagonal1)}')

matriks.reverse()
diagonal2 = []
for j in range(x):
    matriks2 = matriks[j][j]
    diagonal2.append(matriks2)
print(f'Diagonal 2 = {sum(diagonal2)}')

if sum(diagonal1) <= sum(diagonal2):
    print(f'Selisih Diagonal 1 dan 2 = {sum(diagonal2) - sum(diagonal1)}')
elif sum(diagonal1) > sum(diagonal2):
    print(f'Selisih Diagonal 1 dan 2 = {sum(diagonal1) - sum(diagonal2)}')