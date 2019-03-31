
#Assignment1
'''str1 = str(raw_input("Give the first string:"))
str2 = str(raw_input("Give the second string:"))


result = max(str1, str2, key = len)

print('%s is longer'%result)'''

#Assignment2

'''str1 = str(raw_input("Give the first string:"))
str2 = str(raw_input("Give the second string:"))

result = str2[::-1]

print('%s is %s in reverse order' %(str1,result)) 
'''

#Assignment3

'''num1 = int(raw_input("Give the first number :"))
num2 = int(raw_input("Give the second number :"))
num3 = int(raw_input("Give the third number :"))

result = min(num1, num2, num3)

print('%s is the smallest number'%result)'''

#Assignment4

'''bit = str(raw_input("Give a bit pattern :"))
separate = [ ]

for index in range(0, len(bit)):
    take = bit[index]
    result = separate.append(take)
print(separate)
count1 = separate.count("1")

if (count1 % 2 == 0):

    print(separate.pop('1'))
 
else:
    print(separate.pop('0'))'''

#Assignment5

dna = str(raw_input("Enter Sequence :"))
for char in dna: 
 if dna(char) != ["A","C","G","T"]:
    print("Invalid")
 else:
    print("Valid")



 

