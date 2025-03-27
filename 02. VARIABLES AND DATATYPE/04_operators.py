# Arithmetic operators: +, -, *, / etc.

a = 10
b = 4
c = a+b
print(c)


#  Assignment operators:  =, +=, -= etc. 

a = 5-2 # Assign 5-2 in a 
print(a)

# b += 3   # Increment the value of b by 3 and then assign it to b
b -= 3     # Decrement the value of b by 3 and then assign it to b
print(b)


# Comparison operators: ==, >, >=, <,  != etc.

d = 5<4
print(d)

e = 5>=5
print(e)

f = 5!=7
print(f)

g = 5==5
print(g)


#  Logical operators: and, or, not.

g1 = True or False

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and' 
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(False))
print(not(True))