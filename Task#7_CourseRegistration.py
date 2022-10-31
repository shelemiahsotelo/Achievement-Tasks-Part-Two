#Achievement Task #7 - Course Registration
# Shelemiah Sotelo - 8823190


# Empty dictionary.
student = {}   

# Add keys and values to dictionary
student["First Name"] = input("Please enter First Name: ")           
student["Last Name"] = input("Please enter Last Name: ")
student["Student Number"] = input("Please enter Student Number: ")

#Used .get to assign values to a variable.
firstname = student.get("First Name")
lastname = student.get("Last Name")
studentnumber = student.get("Student Number")

# Dictionary of courses available. (Course Code for keys, Course Name for values.)
courses = {
   "PROG1783" : "IT Support Programming Fundamentals",
   "CON0101" : "Conestoga 101",
   "CDEV1830" : "Career Success",
   "INFO1385" : "Network Infrastructure I"
}

for code in courses:
   print(code, ":", courses.get(code))

print("Please enter Course Codes separated by comma. ")
courseCode = input().upper()
finalList = courseCode.split(',')

print("First Name: ", firstname, "\nLast Name: ", lastname, "\nStudent Number: ", studentnumber)
for list in finalList:
   print(list, ":", courses.get(list))



