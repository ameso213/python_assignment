#2. Initialize the list of student names
studentNames = ['Patrice', 'Faith', 'Phionah', 'Anita']

# Print Patrice, Faith, Phionah, and Anita Using Slicing
print(studentNames[1:5])

#Add Masha at the Fourth Position
studentNames[3] = 'Masha'
print(studentNames)

#Update Name Phionah to Phionah Aladinah
studentNames[4] = 'Phionah Aladinah'
print(studentNames)

# Display the Length of the Students List
length = len(studentNames)
print(f"The number of students is: {length}")

# Print All the Students' Names Using a For Loop
for each_student_name in studentNames:
    print(each_student_name)

# Calculate the Total Marks for the Students Marks Variable
def total_marks():
    student_marks = [80, 56, 78, 90]
    return sum(student_marks)

student_total_marks = total_marks()
print(f'Total student marks are: {student_total_marks}')




# 1. Define the list of student names and other lists
studentNames = ['sandra', 'patricia', 'Anita', 'phionah']  
studentMarks = [80, 56, 78, 90]  
data = ['sandra', 60, 'Anitah']  

# Access the whole list
print("A list of Students:", studentNames, type(studentNames))

# Access list items using positive indexing
print("First Student:", studentNames[0])  # First item
print("Second Student:", studentNames[1])  # Second item
print("Third Student:", studentNames[2])  # Third item
print("Fourth Student:", studentNames[3])  # Fourth item

# Using negative indexing
print("Second Last Student:", studentNames[-2])
print("Last Student:", studentNames[-1])

# Appending and Inserting elements
# Append 'Mishelle' at the end of the list
studentNames.append('Mishelle')
print("Appending Mishelle:", studentNames)

# Insert 'Faith' at the second position (index 2)
studentNames.insert(2, 'faith')
print("Inserting Faith at Index 2:", studentNames)
