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