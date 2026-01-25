from tokenize import String

from numpy.ma.core import empty

def grade(avg):
    if avg>=90:
        return  "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
       return "C"
    elif avg>=60:
        return "D"
    else:
       return "Fail"


no_of_students=int(input("No of students :\n"))
students={} #It is an empty dictionary
no_of_subjects=int(input("Enter no  of Subject : \n"))
 #List to store students scores
for i in range(1,no_of_students+1):
    name_of_student=input(f"Enter Name of Student {i} : ")
    scores = []
    for k in range(1,no_of_subjects+1):
        score=int(input("Enter score of subject "+str(k)+" :"))
        scores.append(score)
    students[name_of_student] = scores


print("----------------Results----------------------")
class_total=0
topper_name=""
highest_avg=0
for i,j in students.items():
    print("Student "+i+" :"+" ".join(map(str,j)))
    total=sum(j)
    avg=total/len(j)
    grade_of_stu= grade(avg)
    print(f"Total : {total},Average :{avg},Grade:{grade_of_stu}")
    class_total+=avg
    if avg>highest_avg:
        highest_avg=avg
        topper_name=i


print(f"Class topper {topper_name} ,avg : {highest_avg}")
print(f"Class Average : {class_total/no_of_students}")









