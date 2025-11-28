a = 0
b = 1

a,b=b,a #(swaping the variables)

print (a,b)


var = "amol"
stri = var #(update the variable)
print (stri)

#mathmatical operation with variable
a = 10
b = 20 #implicit type casting
print (a+b)

x = 100
y = 200
print (x+y,x-y,x*y,x/y) #multiple maths oerations in one print statement
#output : 300 -100 20000 0.5

#type catsing

a = 100
b = 200
print (int(a) , float(b)) #(explicit type casting with data type conversion)

'''✅ Simple Python Variable Problems
Problem 1
Create two variables:name → store your name
age → store your age
Print both on the same line.'''

name = "amol"
age = 32
print(name , age)

'''Problem 2
Create variables:
Swap their values without creating a third variable.
'''

a = 10
b = 20

a, b = b, a #(swapped variable)

a=b
print(a,b)


'''Problem 3
Create a variable price = 199.99.
Print: "The price is 199.99" using the variable.'''


price = 199.99
print (f"The price is {price}") #(used f string will see f strings later in detail practice of string)

a = "city"
b = "country"
c = "pin code"

#print("\n.", a, "\n.", b, "\n.", c) # escape seqence character
print(f"\n.{a}\n.{b}\n.{c}") # used escape sequence and f string.
.city
.country
.pin code

