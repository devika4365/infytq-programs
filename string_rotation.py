s=input().split(',')
string=[]
number=[]
for i in s:
    character,num=i.split(':')
    string.append(character)
    number.append(num)
def rotate(s1,n1):
    n1=list(str(n1))
    c=0
    for i in n1:
        c+=int(i)**2
    if c%2==0:
        return s1[-1:]+s1[:-1] # rotation right side
    else:
        return s1[2:]+s1[:2]   # rotation left
for i in range(len(number)):
    print(rotate(string[i],number[i]))
