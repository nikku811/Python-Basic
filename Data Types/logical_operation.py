a = False and True    							# Output: False
b = True or False      							# Output: True
c = False and print("This won't print")  		# Output: False
d = True or print("This won't print either")  	# Output: True

a = 10
b = 20
c = 30

print(a < b and b < c)  	# Output: True
print(a < b or b > c)   	# Output: True
print(not a > b)           	# Output: True
