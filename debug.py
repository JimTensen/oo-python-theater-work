import ipdb
from lib import *
from lib import Role, Audition

# Test your code below...

r1 = Role('Cat in the Hat')

a1 = Audition('Bob', 'Los Angeles', r1)
a2 = Audition('Tim', 'Washington D.C.', r1)
a3 = Audition('Julie', 'Seattle', r1)



# the below line allows us to stop & try stuff!
ipdb.set_trace()