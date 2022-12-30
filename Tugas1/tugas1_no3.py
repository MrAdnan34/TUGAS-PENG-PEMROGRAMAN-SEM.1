a= 8
b= 0

detik= ((1000*a)+(100*b)-(10*a))
print(detik)

sejam= 3600 #detik atau sekon

x= detik//sejam # algoritma jam
y= int((detik/sejam-x)*60) # algoritma menit
z= (float(y))-(y) # algoritma detik(1)
zz= int((float(z)-int(z))*60) #algoritma detik(2)

print(x,'jam', y,'menit', zz,'detik')
