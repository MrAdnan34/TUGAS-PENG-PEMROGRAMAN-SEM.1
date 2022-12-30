# program mencari akar sampai 1

x= int(input('Masukkan x : '))
if x>0:
    for x in reversed(range(0, x)):
        x+= 1
        print("Akar kuadrat dari", x, '=', x**0.5)

elif x<0:
    for x in range(x, 2):
        print("Akar kuadrat dari", x, '=', x**0.5)

else:
    for x in range(x, 2):
        print('Akar kuadrat dari', x, "=", x**0.5)