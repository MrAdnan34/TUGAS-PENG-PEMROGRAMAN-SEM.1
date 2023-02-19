# PROGRAM MENGHITUNG ELEMEN TERBESAR, TERKECIL, DAN PENJUMLAHAN SEMUA ELEMEN

range_list = int(input('Panjang List: '))
total = 0
data_list = []

for i in range(1, range_list+1):
    element = int(input(f'Masukkan Element ke {i}: '))
    total = total + element
    data_list.append(element)
    list.sort(data_list)

print(f'Element Terbesar: {data_list[-1]}')
print(f'Element Terkecil: {data_list[0]}')
print(f'Penjumlahan Semua Elemenn: {total}')