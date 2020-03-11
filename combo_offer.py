dic = {"a"  : 123 , "b" : 100 , "c":50  , "d" : 47, "e"  : 23 , "f" : 120 , "g":90  , "h" : 42}

import random as r
result = set()
ref = set()
ref2 = set()
for i in range(10000):
    ra =r.randint(0,7)
    li = list(dic.values())
    val = r.sample(li,ra)
    val.sort()
    val1 = tuple(val)
    if(sum(val1)>=150 ):
        if(sum(val1)<=170):
            result.add(val1)
li2 = list(dic.keys())           
print(result)
a=0 
dic2 = {}          
for i in li:
    for j in range(a,a+1):
        dic2[i] = li2[j]
        a= a+1
#print(dic2)

for k in result:
    for i in range(len(k)):
        ref.add(dic2[k[i]])
    z = tuple(ref)
    ref2.add(z)
    ref.clear()
print(ref2)