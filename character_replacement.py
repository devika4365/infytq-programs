input_str1=input()
input_str2=input()
input_str3=input()
list_str1=list(input_str1)
list_str2=list(input_str2)
output_str=''
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in range(0,len(list_str1)):
    if list_str1[i] in vowels:
        list_str1[i]='%'
    output_str+=list_str1[i]
for j in range(0,len(list_str2)):
    if list_str2[j] in vowels:
        output_str+=list_str2[j]
        continue
    list_str2[j]='%'
    output_str+=list_str2[j]
output_str+=input_str3.upper()
print(output_str)
    
    
