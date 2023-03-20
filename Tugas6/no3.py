# Program mengecek apakah X merupakan anggota dari set Y atau tidak

y = map(int, input('Masukkan set Y: ').split())
x = int(input('Masukkan angka X: '))
set_y = set(y)

if x in set_y:
    print(x in set_y)
else:
    print('False')
