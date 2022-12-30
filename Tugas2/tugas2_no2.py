# program menentukan letak koordinat kartesius

x= int(input('Masukkan x: '))
y= int(input('Masukkan y: '))

if x> 0 and y> 0:
    print("Koordinat: ", (x,y), 'berada pada kuadran 1')
elif x<0 and y>0:
    print("Koordinat: ", (x,y), 'berada pada kuadran 2')
elif x<0 and y<0:
    print('Koordinat: ', (x,y), 'berada pada kuadran 3')
elif x>0 and y<0:
    print('Koordinat: ', (x,y), 'berada pada kuadran 4')
elif x==0 and y<0 or y>0:
    print('Koordinat: ', (x,y), 'berada pada garis x')
elif x>0 or x <0 and y== 0:
    print('Koordinat: ', (x,y), "berada pada garis y")
else:
    print('Koordinat: ', (x,y), 'berada pada titik pusat koordinat')