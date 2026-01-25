from unicodedata import category

num=int(input("Enter no of entries :\n"))
dict={}
total_spend=0
for i in range(1,num+1):
    category=input("Enter category :")
    spend=float(input("Enter spend :"))
    total_spend+=spend
    if category in dict.keys():
        dict[category]+=spend
    else:
        dict[category]=spend

print("Category Breakdown :")
for key,value in dict.items():
    print(f"{key} amount spend {value}")

most_spend_amount=max(dict.values())

most_spend_category=""
for key,value in dict.items():
    if value==most_spend_amount:
        most_spend_category+=key

print(f"Most spend category : {most_spend_category}")
print(f"Total spent : {total_spend}")
print(f"Category Used :{set(dict.keys())}")


