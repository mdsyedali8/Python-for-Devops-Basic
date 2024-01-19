name="syed ali"

print(type(name))

print(len(name))

#multiline string

a= ''' This is,
a
multi line
string2 ''' 

print(a)

#format variable in str

age=29
txt="my name is syed ali, and i am {}"
print(txt.format(age))

quantity=14
itemNo=829
price=199.78

myorder= "i want {} piece of {} for {} dollars"
print(myorder.format(quantity, itemNo, price))

