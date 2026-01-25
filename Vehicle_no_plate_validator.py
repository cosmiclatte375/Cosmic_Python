num=int(input("How many no plates you need to enter :"))
plates=[]
for i in range(1,num+1) :
    user_input=input(f"Enter 10 digits of plate {i} : ")
    if len(user_input)!=10 :
        print("Error enter correct plate no")
        continue
    plates.append(user_input)
valid_plates=[]
invalid_plates=[]
for i in plates :
    if i[0:2].isalpha()==True :
        if i[2:4].isdigit()==True :
            if i[4:6].isalpha()==True :
                if i[6:10].isdigit()==True :
                    valid_plates.append(i)
                else :
                    invalid_plates.append(i)
            else :
                invalid_plates.append(i)
        else:
            invalid_plates.append(i)
    else :
        invalid_plates.append(i)

state_count={}
for i in valid_plates :
    state=i[0:2]
    if state not in state_count:
        state_count[state]=1
    else :
        state_count[state]+=1
print("Invalid plates")
for i in invalid_plates :
    print(i)
print("Valid plates")
for i in valid_plates :
    print(i)
for i,j in state_count.items():
    print(i,":",j)





