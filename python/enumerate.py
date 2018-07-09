
## Came from: https://www.geeksforgeeks.org/enumerate-in-python/

l1 = ['eat', 'sleep', 'repeat']
s1 = 'geek'

obj1 = enumerate(l1)
obj2 = enumerate(s1)

print "return type: ", type(obj1)

print list(obj1)
print list(enumerate(s1, 2))


## in loops
for ele in enumerate(l1):
    print ele
print

for index, ele in enumerate(l1, 100):
    print index,ele

