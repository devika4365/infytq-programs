input_str=input()
word_list=input_str.split(' ')
position=int(input("position : "))
input_word=input("input word : ")
word_list.insert(position-1,input_word)
output_str=' '.join(word_list)
print(output_str)
