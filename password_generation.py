s=input().split(',')
emp_name=[]
emp_num=[]
for i in s:
    name,num=i.split(":")
    emp_name.append(name)
    emp_num.append(num)
def password(name,number):
    l=len(name)#Robert--len=6
    while l!=0:
        if str(l) in number:
            return name[l-1]
        else:
            l-=1
    return "X"        
for j in range(len(emp_num)):
    print(password(emp_name[j],emp_num[j]),end='')
