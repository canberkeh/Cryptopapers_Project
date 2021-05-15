'''
100 gr x260= 26000 tl
150 gr x290= 43500 tl
200 gr x320= 64000 tl
50 gr x375= 18750 tl
Toplam: 152250 tl
Son olarak 152250 lirayı aldığımız gram miktarına bölüyoruz ve ortalamamızı buluyoruz...
 152250/500=304,5 yani sizin altın alım ortalamanız 304,5 tl.

'''

loop = int(input("kaç kere alım yaptın = "))
counter = 0
alim = 0
total = 0
while counter < loop:
    a = int(input(" alım adeti  = "))
    b = int(input(" alım maliyeti  = "))
    alim += a
    sum = a * b
    total += sum
    counter += 1
maliyet = total / alim
print("toplam alım : ", total)
print("maliyet = ", maliyet)