#list sorting
lst=[]
n1=input('marks of student1:')
n2=input('marks of student2:')
n3=input('marks of student3:')
n4=input('marks of student4:')
n5=input('marks of student5:')
lst.insert(1,n1)
lst.insert(2,n2)
lst.insert(3,n3)
lst.insert(4,n4)
lst.insert(5,n5)
lst.sort()
print('the marks of students in sorted way : ',lst)