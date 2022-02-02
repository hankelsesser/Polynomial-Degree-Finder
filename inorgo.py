import math
from re import L
import random
class Function:
    def __init__ (self, min, max):
        self.min = min
        self.max = max
        self.degree = random.randint(min, max)
    def get(self, x):
        y = x**self.degree
        return(y)

def function(x):
    y = x**random.randint(1, 6)
    return(y)

def find_function(coords):
    is_constant = False
    degree = 0
    check_coords = coords
    for i in range(len(coords)-2):
        degree+= 1
        differences = []
        for n in range(1,len(check_coords)):
            differences.append(check_coords[n] - check_coords[n-1])
            #print(check_coords, differences)
        check_coods = differences
        is_constant = _constant(differences)
        if is_constant== True:
            return([True, degree])
    return([False])
    
            

def _constant(coords):
    reference = coords[0]
    #print(reference, "reference")
    for coord in coords:
        if coord != reference:
            #print (coords, "is not constant")
            return(False)
    #print (coords, "is constant")
    return(True)
        

found = False
coords =[]
x = 0
function = Function(1, 5)
for i in range (3):
    coords.append(function.get(x))
    x+=1
while found == False:
    test = find_function(coords)
    if test[0] == True:
        print("degree is", test[1])
        print("actual degree is", function.degree)
        found = True
    else:
        x+=1
        coords.append(function.get(x))
        print(coords)
        
    


