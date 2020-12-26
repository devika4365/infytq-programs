s=input() #python
g=[]
for i in range(0,len(s)): #0--5
    c=1
    for j in range(0,len(s)):
        if j!=i:
            if s[j]==s[i]:
                c=c+1
    if s[i] not in g:
        g.append(s[i])
        print(s[i],'-->',c)
            
            
