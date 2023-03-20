# Program memodifikasi suatu Set xyz

xyz = set()

while True:
    print('\nPilih Opsi:')
    print('1. Masukkan satu data ke set xyz')
    print('2. Masukkan lebih dari satu data ke set xyz')
    print('3. Hapus satu data dari xyz')
    print('4. Hapus seluruh elemen dari set xyz')
    print('5. Keluar dari program')
    print()
    print('Set xyz sekarang:',xyz)

    print()
    opsi = input('Masukkan opsi >> ')

    if opsi == '1':
        x = int(input('Masukkan data set baru >> '))
        xyz.add(x)
    elif opsi == '2':
        x = map(int, input('Masukkan banyak data baru >> ').split())
        set_x = set(x)
        xyz.update(set_x)
    elif opsi == '3':
        x = int(input('Masukkan satu data yang ingin dihapus >> '))
        xyz.discard(x)
    elif opsi == '4':
        xyz.clear()
        print('Menghapus semua data...')
    elif opsi == '5':
        print('Keluar dari program...')
        break
    else:
        print('Inputan opsi salah')
