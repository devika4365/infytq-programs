s=input().split(',')
list1=[]
for i in range(len(s)):
    list1.append(int(s[i]))
num1=sum(list1[:list1.index(5)])+sum(list1[(list1.index(8)+1):])
num2=list1[list1.index(5):list1.index(8)+1]
r=''
for i in num2:
    r+=str(i)
print(int(r)+num1)    
