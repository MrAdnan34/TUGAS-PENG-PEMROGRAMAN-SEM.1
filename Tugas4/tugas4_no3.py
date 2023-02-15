# PROGRAM MEMASUKKAN SUB-STRING KE TENGAH STRING UTAMA

x = input('Masukkan String Utama : ')
y = input('Masukkan Sub-String : ')

if len(x) % 2 == 0:
    a = len(x) // 2
    print(x[:a] + y + x[a:])

else:
    print('Operasi tidak dapat dilakukan')