from collections import Counter

dosya=open("test.log")
d={}
i=0

for satir in dosya.readlines():
    splitline = satir.split(' ') #bosluklara gore parcaliyor
    d[i]=splitline[6] #url log dosyasinda yer aliyor
    i=i+1

cnt = Counter()

for j in d.values():
    cnt[j]=cnt[j]+1

# print cnt
print cnt.most_common(1)

dosya.close()
