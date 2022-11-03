n='153'
sum=0
for i in range(0,len(n)):
  sum=sum+pow(int(n[i]),len(n))
if int(n)==sum:
  print(n,"is an armstrong number")
else:
  print(n,'is not an armstrong number')