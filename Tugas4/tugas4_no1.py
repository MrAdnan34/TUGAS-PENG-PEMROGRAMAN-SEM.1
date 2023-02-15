# PROGRAM MENGGABUNGKAN 2 KARAKTER PERTAMA DAN 2 KARAKTER TERAKHIR INPUTAN STRING

a = input('Masukkan String : ')

if len(a) >= 4 :
    print(f'{a[:2]} \b{a[-2:]}')

else:
    print('Dibatalkan')