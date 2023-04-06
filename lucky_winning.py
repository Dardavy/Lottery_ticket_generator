





#Question 1 write a function that returns a bool type

x = True
print(type(x))

a= 40
b= 136

print(bool(a==b)) #returns false as a is not equal to b
print(bool(a>b))  #returns false as a is not greater than b
print(bool(a<b))  #returns true as a is greater than b
print(bool(a!=b))  #returns true as a is not equal to b


#Question 2 write a python function that takes 10list and 
#returns true if they have at least one common member 


list1 = ['a', 'b', 'c']
list2 = ['a', 'z', 'c']
list3 = ['a', 'x', 'c']
    
common_elements = list(set(list1).intersection(list2, list3))


def cohort_5():
    if common_elements:
        print("True", "the common elements are", common_elements)
    else:
        print("False", "there are no common")




cohort_5()


#Question 3 create a python function that calculates the age of student,
# if the student age is greater than or equal to 18 it should return true else false

current_year = 2023 
average_age = 18 

def age_cal():
    name_of_student = input("enter student name: ")
    age_calculation = int(input("enter student date of birth: "))
    if age_calculation <= 2005 :
        final_age = current_year - age_calculation
        print('True!',name_of_student, "you are", final_age, "years old and qualified")
    else:
        final_age = current_year - age_calculation
        print('False!',name_of_student, "you are", final_age, "years old and disqualified")
age_cal()









dardavy_lottery_gen()
