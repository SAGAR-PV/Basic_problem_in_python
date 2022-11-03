#n=input("enter the number")
#arr=list(map(int,n.split()))
#print(arr)
#n=input("enter the number")
#arr=list(map(int,n.split()))
#arr.sort()
#print(arr[-2])
#score=int(input())
#score1=list(score)
#for i in range(0,len(score1)):
  #  if score1.count(i)>=2:
 #       print("score1")
n=int(input())
res=[]
grade=[]
for i in range(n):
    name=input()
    mark=float(input())
    res.append([name,mark])
    grade.append(mark)   #calculation 2nd lowest
#print(res)   
#print(grade)
grade=sorted(set(grade))  #sorted unique
#print(grade)
m=grade[1]
#print(m)
name=[]
for val in res:
    if m==val[1]:
        name.append(val[0])
#print(name)   #unsorted     
name.sort()
#print(name)   #sorted
for nm in name:
    print(nm)
           

