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
print(d) # both key and val inside {}
print(d.keys()) # only keys
print(d.values()) # only value
print(d.items())  # both key and val

# Conditional Statement

  # if,elif,else
age =10
if age>=18 and age<=25:
    print("adult")
elif age<18:
    print("child")
else:
    print("post adult")

    # Nested if-else
is_member=False;
if age>18:
    if is_member:
        print("member")
    else:
        print("non member")
else:
    print("Below 18 cannot be a member3")

    # Ternary Operator
s="Adult" if age>18 else "child"
print(s)
   # Match case
number=5
match number:
    case 1:
        print("one")
    case 2 | 3:
        print("two or three")
    case _:
        print("none")

# Loops
  #For
lis=[1,2,3,4]
for i in range(lis[1],len(lis)+1):
    print(i)
for i in lis:
    print(i)

   # while
count=0
while(count<5):
    count=count+1
    print(count)


# Function
def fun():
    print("hello world")
fun()

def evenOrOdd(x):
    if(x%2==0):
        return "even"
    else:
        return "Odd"
print(evenOrOdd(12))
print(evenOrOdd(11))

# Arguments
 # Default args
def myFun(x1,y1=10):
 print("x:", x1, "y:", y1)

myFun(10,20)
myFun(20)

 # keyword args using parameter names, order doesnt matter
def student(fname, lname):
    print(fname,lname)
student(fname="hello",lname="world")
student(lname="world",fname="hello")

 #positional args

def name(name,age):
     print("My name is ", name)
     print("My age is ", age)
name("tom", 4)
name(4,"tom")

 # Arbitrary args
def myfun(*args,**kwargs):
   for i in args:
    print(i)
   for key,val in kwargs.items():
        print(f"{key}:{val}")
myfun("HII","TOM",name='Tom',age=4,Skills='barking')

# Function within function
def outer():
    print("I am out")
    def inner():
        print("I am in")
    inner()
outer()

