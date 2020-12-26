s=input()
out=''
for i in s:
    if int(i)%2==0:
        continue
    else:
        out+=str(int(i)**2)
print(out[:4])        
