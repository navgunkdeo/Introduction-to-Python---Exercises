# ====================
# 1. Student Info Card
# ====================
# Write a Python program that takes the following inputs:
# Full Name (string)
# Age (int)
# Height in meters (float)
# Is the student present today? (boolean input as True/False)
# Print a formatted student ID card like:
"""
-------- STUDENT ID CARD --------
Name      : John Doe
Age       : 20 years
Height    : 1.75 m
Present   : True
---------------------------------
"""
# Use f-strings
# Print the datatype of each input using type()

name = input("Enter your full name:")
age = int(input("Enter your age:"))
height = float(input("Enter your height in meters:"))
s = input("Are you present today? (True/False):").strip().lower()
if s == "true":
  s = True
elif s == "false":
  s = False
else:
  print("Invalid input. Please enter True or False.")
print("-------- STUDENT ID CARD --------")
print(f"Name\t:{name}")
print(f"Age\t:{age}")
print(f"Height\t:{height}m")
print(f"Present\t:{s}")
print(type(name))
print(type(age))
print(type(height))
print(type(s))





# =================
# 2. Bill generator
# =================
# Product name (string)
# Quantity (int)
# Price per item (float)
# Calculate total = quantity × price
# Print output like:
"""
------ BILL ------
Product   : Pen
Quantity  : 5
Rate      : 10.50
Total     : 52.50
------------------
"""
#Total must be shown with 2 decimal places

prodname = input("Enter the name of the product:")
quant = int(input("Enter product quantity:"))
price = float(input("Enter price of product:"))
total = quant * price
print(f"------ BILL ------\nProduct:\t{prodname}\nQuantity:\t{quant}\nRate:\t{price:.2f}\nTotal:\t{total:.2f}\n------------------")





# ========================================
# 3. Take multiple inputs in a single line
# ========================================
# Read 3 marks in one line using split() + map(int, ...)
# Print:
# Total
# Average (2 decimals)
a,b,c = map(float,input("Enter marks in English, Mathematics and Science (out of 100) separated by spaces:").split())
total = a + b + c
avg = total/3
print("Total:", total)
print(f"Average: {avg:.2f}")





# =============================
# 4. Personal details formatter
# =============================
# Take input:
# First name
# Last name
# City
# Pin code (int)
# Phone number (string) (don’t use int for phone)
# Output Requirements:
# Print this using str.format():
"""
---- PROFILE ----
Full Name : Lastname, Firstname
City      : CITYNAME (in uppercase)
Pincode   : 6 digits (example: 000123)
Phone     : +91-XXXXXXXXXX
--------------
"""
# Convert city to uppercase using .upper()
# Pincode must always show 6 digits (zero padding)
fn = input("Enter your first name:")
ln = input("Enter your last name:")
city = input("Enter your city:")
pc = int(input("Enter your pincode:"))
pn = input("Enter your phone number:").strip()
if len(pn)!= 10 or not pn.isdigit():
  print("Phone number must contain exactly ten digits.")
else:
  print("---- PROFILE ----")
  print("Full Name : {}, {}".format(ln, fn))
  print("City : {}".format(city.upper()))
  print("Pincode : {:06d}".format(pc))
  print("Phone : +91-{}".format(pn))
  print("-----------------")





# ===================
# 5. Mini Report Card
# ===================
sn = input("Enter student name: ")
rn = int(input("Enter student roll number: "))
marks = list(map(int, input("Enter marks in English, Mathematics, Science, History and Geography separated by commas: ").split(",")))
total = sum(marks)
percentage = (total/500)*100
result = "PASS" if percentage >= 40 else "FAIL"
print("========= REPORT CARD =========")
print(f"Name\t:{sn}")
print(f"Roll No\t:{rn}")
print(f"Marks\t:{marks}")
print(f"Total\t:{total}")
print(f"Percentage\t:{percentage:.2f}%")
print(f"Result\t:{result}")
print("==============================")





# ==========
# 6
# ==========
a, b, c = map(int,input("Enter three numbers separated by commas:").split(","))
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("Sum = ", a + b + c)
