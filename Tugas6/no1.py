# Program Menghitung 5 Operasi Himpunan dari Set A dan set B

a = map(int, input('Masukkan Set A: ').split())
b = map(int, input('Masukkan Set B: ').split())

set_a = set(a)
set_b = set(b)

print()
print('Union of set A and set B:',set_a|set_b)
print('Intesection of set A and set B:',set_a&set_b)
print('Difference of set A from set B:',set_a-set_b)
print('Difference of set B from set A:',set_b-set_a)
print('Symmetric Difference of set A from set B:',set_a^set_b)
