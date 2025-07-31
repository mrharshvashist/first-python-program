
# all_students = {
#   "student_01" : {
#       "name": "Alice",
#       "age": 20, 

#       "grades": [88, 92, 85],
#       "is_enrolled": True,
#       "courses": ["Math", "Science", "History"]
#   },
#   "student_02" : {
#       "name": "Bob",
#       "age": 22,
#       "grades": [78, 82, 80],
#       "is_enrolled": True,
#       "courses": ["English", "Art", "Math"]
#   }
# }
# student = input("Enter student name: ")

# def display_full_student_info(student):
#     print(f"Name: {all_students[student]}")
    
# display_full_student_info(student)
# input("Press Enter to continue...")
# This line is used to pause the script execution


# create a sample text file
# f = open("students.txt", "a")

# f.write("\nNew student added: Charlie, age 21, enrolled in Math and Science courses.\n")
# f = open("students.txt", "r")
# print(f.read())
# f.close()

# with open("students.txt", "w") as f:
#     f.write("hello world\n")
# with open("students.txt", "r") as f:
#     content = f.read()
# print(content)
# f.close()

# n = open("C:\\\\Users\\HARSH\\Downloads\\greetings.txt")

# content = n.read()
# print(content)
# # The above code reads the content of a file named "greetings.txt" located in the
# f = open("new_file.txt", "x")
# f.write(content)

# f= open("new_file.txt", "r")
# n.close()
# f.close()
# learning_file = open("learning_file.txt", "x")
# learning_file.write("create,open,read,edit files.\n")
# learning_file.close()
# r = open("learning_file.txt", "r")
# print(r.read())
# with open("learning_file.txt", "a") as learning_file:
#     learning_file.write("- deleting files with os module.\n")

# import os
# os.remove("new_file.txt")
# import os
# os.remove("C:\\\\Users\\HARSH\\OneDrive\\Desktop\\Copyer.lnk")
# print("File deleted successfully")
# x  = open("folder/sample.txt", "a")
# x.write("This is a sample text file created in a subfolder.\n")
# def myfunc() :
#  print("Hello, this is a function without parentheses!")
# myfunc()

# def myfunc():
#     print("Hello, this is a function without parentheses!")*int(10)
# myfunc()
# inp = int(input("how many times do you want to print the message:"))
# for i in range(inp):
#     print("python is fun")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_number = int(input("Enter a number to check if it's in the list: "))
if input_number in list:
    print(input_number, "is in the list")
    
else:
    print(input_number, "is not in the list")
    
    