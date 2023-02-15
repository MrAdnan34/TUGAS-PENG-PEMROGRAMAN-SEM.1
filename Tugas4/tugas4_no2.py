# PROGRAM MENGGANTI SUB-STRING TERTENTU DALAM SEBUAH STRING

x = input('Masukkan String : ')

a = x.replace('a', '_').replace('t', '*').replace('e', '-').replace('o', ';')
b = a.lower()

print(b)