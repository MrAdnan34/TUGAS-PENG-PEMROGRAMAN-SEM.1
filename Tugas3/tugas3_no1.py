# program konversi rupiah ke dollar

print('---Konversi Dollar ke Rupiah---')

def dollar(a):
    b= float(a * 14935.40)
    if a<0:
        print('Inputan nilai dolar tidak boleh bernilai negatif')
    elif a>=0:
        print('Konversi', float(a), '$ ke rupiah : Rp.',b)

dollar(int(input('Input uang dollar untuk dikonversi ke nilai rupiah : ')))