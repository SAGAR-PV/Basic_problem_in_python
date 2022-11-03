n = int(input())
name = []
mark = []
for x in range(n):
    temp,temp2 = input().split()
    name.append(temp)
    temp2 = int(temp2)
    mark.append(temp2)

print(name,mark)
first = mark[0]
second = mark[0]
keys = []
for x in range(n):
    if(first < mark[x]):
        second = first
        first = mark[x]
    elif(mark[x] > second and mark[x] != first):
        second = mark[x]
        
for x in range(n):
    if(mark[x] == second):
        temp = name[x]
        keys.append(temp)

print(keys)