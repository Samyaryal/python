
#assignment"2_1
'''string = str(raw_input("Give a string :"))
length = len(string)

print("length of the string: %s" %length)
print("first character: %s" %string[0])
print("last character: %s" %string[-1])'''


#assignment2_2


'''letter = str(raw_input("Give a 4 letter word :"))

print("word in reverse order: %s" %letter[::-1])

print("word in reverse order: %s" %letter[-1:-5:-1])

print("word in reverse order: %s" %letter[4:0])

txt = "Hello World"[::-1]
print(txt)'''


#assignment2_3

'''word =str(raw_input("Enter a two word sentence:"))
x = word.find(" ")
next_index = word[x+1:]
print("The second word of the sentence is %s" %next_index)'''

#assignment2_4

'''
str1 = str(raw_input("give the first string:"))
str2 = str(raw_input("give the second string:"))

x = str2.count(str1)
print("The first string can be found %s times in the second string." %x)
y = str1.count(str2)
print("The second string can be found %s times in the first string." %y)  '''




#assignment2_5


'''str1 = str(raw_input("Give the first string:"))
str2 = str(raw_input("Give the second string:"))
capital = str2.upper()
output = str1.replace(str2,capital)


print("Replaced string %s" %output) '''

#assignment2_6

str1 = str(raw_input("Give the string A:"))
str2 = str(raw_input("Give the string B:"))

##result = str1.index(str2)
final = str1.rfind(str2)
print(final)



print('The index of the 2nd occurance of B in A is %s' %final)





