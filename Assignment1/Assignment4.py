#Give your name : John Smith
#Which year you were born: 1980
#Hello, John Smith. You are 30 years in 2010.

name = str(raw_input("Give your name:"))
birth = int(raw_input("Which year you were born:"))
age = (2010 - birth)
print('Hello, %s. You are %s years in 2010'%(name, age))