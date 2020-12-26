s=input()
array=[]
for i in range(len(s)):
    for j in range(len(s)):
        array.append(s[i:j+1]) #moomso
#print(array)        
l=0
out=''
for i in array:
    rev=i[::-1]
    if i==rev and len(i)>l:
        l=len(i)
        out=i
print(out)        
