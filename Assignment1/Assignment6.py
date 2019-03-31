from math import sqrt

a = int(raw_input("give a:"))
b = int(raw_input("give b:"))
c = int(raw_input("give c:"))
 
d = (b**2) - (4*a*c)

square_root= sqrt(d)
print(square_root)
sol1 = (-b+square_root)/(2*a)
sol2 = (-b-sqrt(d))/(2*a )


print('The roots are %s, %s' %(sol1,sol2)) 
   





