'''subjects = ['Eng','Maths','Statistics','Urdu','Physics']
total_obtain_marks = 0
total = 500
for sub in subjects:
    sub = int(input('Enter marks of '+ sub + ' : '))
    total_obtain_marks += sub
print('Total obtained marks: ' + str(total_obtain_marks) +'/500')
percentage = (total_obtain_marks/total) * 100
print('Percentage: '+str(percentage) + '%')
if(percentage >= 80):
    grade = 'A+'
elif(percentage > 70 and percentage <= 79):
    grade = 'A'
elif(percentage > 60 and percentage <= 69):
    grade = 'B'
elif(percentage > 50 and percentage <= 59):
    grade = 'C'
elif(percentage < 50):
    grade = 'Try Again'
print('Grade : ' + grade)'''

'''
num = int(input('Enter no.: '))
if(num%2 == 0):
    print("Even")
else:
    print('Odd')
'''


'''
subjects = ['Eng','Maths','Statistics','Urdu','Physics']
print(len(subjects))
'''

'''
numbers_list = [1, 1, 2, 3, 5]
num = 0
for no in numbers_list:
    num += no
print(num)
'''


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in a:
    if(num < 5):
        print(num)


















