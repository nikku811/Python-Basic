# 1. Arithmatic operater(=, -, *, /, //, % etc.)
a = 223
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# 2. Assignment operater (=, +=, -=, *=, /=, etc.)

a = 20-3 # assign 17 to a
print(a)

b = 15  # assign 15 to b
b += 3 #Increment of 3 in var b
print(b)
b -= 6 #decrement of 3 in var b
print(b)
b = 15  # assign 15 to b
b *= 5 #first b multiply by 3 after assign the var b
print(b)
b /= 2 # first b divide by 3 after assign var b
print(b)
b //= 3 
print(b)


# 3. Comperision operater (==, >=, <=, >, <, != etc.)

x = 13
y = 2
print(x == y)   #False
print(y != x)   #True
print(x < y)    #False
print(x <= y)   #False
print(x > y)    #True
print(x >= y)   #True



# 4. Logical Operators (and, or, not).

print("Truth table if 'and' ")
print(True and True)  #True
print(True and False)  #False
print(False and True)  #False
print(False and False)  #False

print("Truth table if 'or' ")
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

print("Truth table if 'not' ")
print(not True) #False
print(not False) #True