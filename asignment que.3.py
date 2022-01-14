#storing different data type values ia a list
student=['SID','name','gender','course name','CGPA']
lst=[]
n1=input('enter SID of the student:',)
n2=input('name:')
n3=input('gender:')
n4=input('course name:')
n5=input('CGPA:')
lst.insert(1,int(n1))
lst.insert(2,n2)
lst.insert(3,n3)
lst.insert(4,n4)
lst.insert(5,float(n5))
print('this is your required list: ',lst)