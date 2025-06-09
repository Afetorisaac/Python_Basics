# A simple program to determin the elegibility to vote
print("Author: Afetor Isaac Yao\n")

print("To determine whether you are elegible to vote.\n")

first_name = input("First Name:\n")
surname = input("Surname: ")
age = int(input("Age: "))

if age < 18:
    print(first_name, surname, "at age", age, ",you are too young to vote.")
elif age >=18 :
    print(first_name, surname, "at age", age, ",you are elegible to vote.")
elif age > 100 :
    print("Error, enter a valid age")