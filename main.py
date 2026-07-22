print("Hello Python")

# variables
x=1  # No need for a datatype, holds any type.

   # 1. Dynamic typing, same variable stores different values during execution
y=2   # holds an integer value
print(y)  # print 2
y="two" # holds a string
print(y)  # print two

  # 2. same value can be assigned to multiple variables in single line
a=b=c=100
print(a,b,c)

  #3. multiple values can be assigned to multiple variables in a single line.
x,y,z=1.5,2,"A third value"
print(x,y,z)

# Data Types
print(type(y))
print(type(x))
print(type(z))

 #String
print(z[0])
print(z[-1])

 #List  // ordered, mutable
list=[1,2,3]
print(list)
print(list[0])
print(list[-1])

  #Tuples // ordered, immutable
t=(1,)  # trailing comma is required to treat it as tuple
print(type(t))
print(t[0])
print(t)

  #Boolean Datatype
print(type(True))  # bool type
print(type(False))

  # Set // unordered, mutable, unique values, since unordered cannot be accessed via index use a loop
s1={"a","b","c","a"}
print(s1)
for i in s1:
    print(i)

  # Dictionary  // key-value pairs, keys are unique and case sensitive
d={1:"apple",2:"orange",3:"guava"}
print(d[2])
print(d.get(3))

  