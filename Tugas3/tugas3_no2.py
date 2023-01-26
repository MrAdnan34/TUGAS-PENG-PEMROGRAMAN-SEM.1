# program mengembalikan FBB (Faktor Pembagi Terbesar) dari dua bilangan inputan

print('---Menentukan FPB dua bilangan---')

try:
    def bilangan(a, b):
        if a>b:
            nilai_terkecil= b
        elif a<b:
            nilai_terkecil= a
        else:
            nilai_terkecil= a or b

        for i in range (1, nilai_terkecil+1):
            if (a % i == 0) and (b % i == 0):
                FPB= i

        return FPB

    bilangan1= int(input('Nilai a : '))
    bilangan2= int(input('Nilai b : '))
    
    bilangan(bilangan1, bilangan2)

    print('FPB dari', bilangan1, 'dan', bilangan2, 'adalah', bilangan(bilangan1, bilangan2))

except:
    print('Input hanya terdiri dari angka saja')