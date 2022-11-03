


small=9999
small1=9998
list=[10,11,7,8,9,4,9]
for i in list:
    if i<small:
        small=i
for i in list:
    if i<small1 and i>small:
        small1=i
print(small1)  
