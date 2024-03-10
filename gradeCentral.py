from statistics import mean as m
admins = {
    'Ronny' : 'pass123',
    'admin' : 'pass456',
    'user1' : 'pass123'
}

studentDict = {
    'Ronald' : [88,90,100],
    'Allan' : [97, 98, 85],
    'Pagun' : [75, 75, 78]
}

def enterGrade():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')
    
    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.')
        
    print(studentDict)
    
def removeStudent():
    nameToRemove = input('What student you will remove?: ')
    if nameToRemove in studentDict:
        print('Removing student records...')
        del studentDict[nameToRemove]
    else:
        print('Student does not exist.')
        
    print(studentDict)
    
def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
        
        print(eachStudent,'has an average grade of:',avgGrade)
        

def main():
    print("""
    Welcome to Grade Central
    
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit    
    """)
    
    action = input('What would you like to do today? (Enter a number): ')
    
    if action == '1':
       enterGrade()
    elif action == '2':
        removeStudent()
    elif action == '3': 
        studentAVGs()
    elif action == '4': 
        exit()
    else:
        print('No valid choice was given, try again.')



login = input('Username: ')
password = input('Password: ')


if login in admins:
    if admins[login] == password:
        print("\nWelcome", login)
        while True: 
            main()
    else:
        print('Invalid password')
else:
    print('Invalid username')