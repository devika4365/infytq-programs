string=input()
odd=[]
even=[]
a=False
for i in string:
    if i.isdigit():
        if int(i)%2==0:
            a=True
            if str(i) in even:
                continue
            even.append(i)
        else:
            if str(i) in odd:
                continue
            odd.append(i)
if a:
    min_val=str(min(even))
    even.remove(min(even))
    odd.extend(even)
out=''
while (len(odd)>0) and a:
    out+=str(max(odd))
    odd.remove(max(odd))
if a:
    print(int(out+min_val))
else:
    print('-1')
             
