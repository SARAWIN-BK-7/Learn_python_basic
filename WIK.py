def greeting():
    print("Welcome to student Please enter you data.")


def data():
    std_name = list()
    std_age = list()
    for std in range(1, 6):
        std_name.append(input("Please enter your name: "))
        std_age.append(input("Please enter age: "))
        print("Student number: ", std)
    return std_name, std_age

greeting()
std, age = data()
print("List of students and their age")
for i in range(0, 5):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    print("<------------------->")
    print("Name : ", std[i])
    print("Age  : ", age[i])

# print("Age: ",age_std)

# students = {}
# for i in range(10):
#     line = input()
#     strlist = line.split(',')
#     students[ strlist[0] ] = int(strlist[1])

# print(students)
# for std in range(1,6,1):
#     name=input("Please enter your name.")
#     age=input("please enter age.")
# while True:
#     name_1=input("Please enter your name:")
#     try:
#         name_1=str(name_1)
#     except ValueError:
#         print("Error, this is not name!")
