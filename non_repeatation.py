


a='sagar' #printing only unique characters 
a1=list(a)
b=0
for i in a1:
  if a1.count(i)>=2:
    continue
  else:
    print(i,end='')
#a1=set(a)
#print(a1)
#dupilicate key word is unique()