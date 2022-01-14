#computing a person's income tax
print('enter your gross income(should be entered in $)')
a1=input()
print('enter the no.of dependents')
a2=input()
#var1 defines standard deduction
var1=10000
#var2 defines dependent deduction
var2=3000
#var3 defines net taxable income
var3=int(a1)-var1-(var2*int(a2))
print('your net taxable income is',var3)
print('your tax amount is',(int(var3)/100)*20)
#code end here
