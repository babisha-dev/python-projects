# Implicit - automatic 

a=10
b=2.5
a=b
print(a)
print(type(a))


# Explicit - manual

a=10.9
c=int(a)
print(type(c))
print(type(a))

# boolean conversion

print(bool(0))
print(bool(1))
print(bool("non empty string is true"))
print(bool(""))
print(bool(-3))  # T
print(bool(None)) # F
print(type(None))  # NoneType

# Convert into list

a= "python"
b= list(a)
print(b)

# convert into tuple

a=[10,20,30]
convertTuple=tuple(a)
print(convertTuple)

# Convert into Set

set1=[10,20,30,30,20]
convertSet=set(set1)
print(convertSet)

# Adding two strings

str1="10"
str2="20"
print(int(str1)+ int(str2))

