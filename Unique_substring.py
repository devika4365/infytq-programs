s=input()
out=''
substr_list=[]
condition=False
for i in range(len(s)):
    if s[i].lower() in out or s[i].upper() in out:
        if len(out)>=3:
            condition=True
            substr_list.append(out)
            out=''
            out+=s[i]
    else:
        out+=s[i]
        if i==len(s)-1 and len(out)>=3:
            condition=True
            substr_list.append(out)
if condition:
    str_len=0
    output=''
    for i in substr_list:
        if len(i)>str_len:
            str_len=len(i)
            output=i
    print(output)
else:
    print('-1')
