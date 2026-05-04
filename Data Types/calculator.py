print("""
Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
""")

ch = int(input("Select operation from 1, 2, or 3: "))

if ch not in (1, 2, 3):
    print("Invalid choice")
    sys.exit()

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

if ch == 1:
    res = n1 + n2
elif ch == 2:
    res = n1 - n2
else:
    res = n1 * n2

print("The result is: ", res) 
