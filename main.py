# Displays user's choices
def displayMenu():

  print("1. Add a Student")

  print("2. Remove a Student")

  print("3. Add Quiz Grade for Student")

  print("4. List a Student's Quiz Grades")

  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts user to enter numeric grade, which is converted to float
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

# Adds student name to studentList dictionary
def addStudent():

# Prompt user to enter student name
  student = input("Enter student name: ")

# Initialize student list for grades
  studentList[student] = []

# Display successfully added message
  print(f"{student} added!")

# Removes student name from dictionary
def removeStudent():

# Prompt user for name and check to see if student exists in dictionary
  student = input("Enter student name: ")
  if (student in studentList):
    
# if student exists, then remove from dictionary and display a message
    studentList.pop(student)
    print(f"{student} removed!")

  else:
# if student is not in dictionary, display message
    print(f"{student} not in dictionary!")

# Adds quiz grades to list
def addQuizGrade():

# Prompt user for name and check to see if student exists in dictionary
  student = input("Enter student name: ")
  print()
  
  if (student in studentList):
    
# Prompt for grade to enter  
    print()
    grade = getNumberGradeFromUser()
    
# Loop until valid grade has been entered
    while not ((grade >= 0) and (grade <= 100.0)):
      print()
      grade = getNumberGradeFromUser()
      print()
      
# Add grade to student's list of grades and display a message
    studentList[student].append(grade)
    print(f"Added {grade} to {student}'s quizzes")
  else:
# Display a message when student's name does not exist in studentList dictionary
    print(f"Cannot add quiz for student not in database : {student}")

# Displays student's grades
def listStudentGrades():

# Prompt user for name and check to see if student exists in dictionary
  student = input("Enter student name: ")
  if (student in studentList):
    
# Display message if no quizzes have been entered    
    if (studentList[student] == []):
      print(f"{student} has no quiz grades entered")
    elif (student in studentList):
      
# Display quizzes, if they exist
      print(f"{student}'s Quizzes:'")
      if (studentList[student] != []):
        for grade in studentList[student]:
          print(grade)
  else:
# Display message if student's name does not exist
    print(f"{student} does not exist in database")

# Calculates grades and determines letter grade
def getStudentLetterGrade():

# initialize variables
  grades = 0.0
  counter = 0
  average = 0.0

# Prompt user for name and check to see if student exists in dictionary
  student = input("Enter student name: ")
  if (student in studentList):

# Check to see if student has quizzes entered
    if (studentList[student] != []):

# If quizzes have been entered, add all grades and count number of grades
      for grade in studentList[student]:
        grades += grade
        counter += 1
        
# calculate average grade
      average = grades / counter

# Assign correct letter grade 
      if (average >= 90):
        letterGrade = "A"
      elif (average >= 80):
        letterGrade = "B"
      elif (average >= 70):
        letterGrade = "C"
      elif (average >= 60):
        letterGrade = "D"
      elif (average >= 50):
        letterGrade = "E"
      else:
        letterGrade = "F"
        
# display letter grade
      print(f"{student}'s current grade is a {letterGrade}")
    else:

# display message if no quizzes exist
      print(f"{student} does not have any quiz grades entered")
  else:

# display message if student's name is not in dictionary
    print(f"{student} does not exist in database")
    
################ Main ################

# create student dictionary
studentList = {}

# initialize selection, student, grade variables
selection = ""

# Application Loop
while(selection != "6"):

# Prompt the user to select an option
  print()
  displayMenu()
  print()
  
  selection = input("Select an Option: ")
  print()

  if (selection == "1"):
    addStudent()
    
  elif (selection == "2"):
    removeStudent()
    
  elif (selection == "3"):
    addQuizGrade()
      
  elif (selection == "4"):
    listStudentGrades()
    
  elif (selection == "5"):
    getStudentLetterGrade()