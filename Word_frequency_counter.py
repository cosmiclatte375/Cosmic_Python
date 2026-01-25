user_input=input("Enter an sentence").lower()
split_sentence=user_input.split(" ")
dict={}

for i in split_sentence:
    count=split_sentence.count(i)
    dict[i]=count

for i,j in dict.items():
    print(i,":",j)

most_frequent_word=max(dict,key=dict.get)
print(f"Most frequent word is {most_frequent_word}")
print(f"total Words: {len(split_sentence)}")
print(f"Unique words : {len(set(split_sentence))}")







