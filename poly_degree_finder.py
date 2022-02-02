import random


class Function:
    def __init__ (self, min, max):
        self.min = min
        self.max = max
        self.degree = random.randint(min, max)
    def get(self, x):
        y = x**self.degree
        return(y)

def get_differences(coords, cycles):
    coords = coords
    for i in range(cycles):
        differences = []
        for n in range(1,len(coords)):
            differences.append(coords[n] - coords[n-1])
        coords = differences
    return(differences)

def check_constant(coords):
    ref = coords[0]
    for i in range(1,len(coords)):
        if coords[i] != ref:
            return(False, ref)
    return(True, ref)


def main():
    coords = []
    is_constant = False
    function = Function(1, 200)
    cycles = 0#trying to find this number difference
    x = 1
    for i in range(3):
        coords.append(function.get(x))
        x+=1
    
    while is_constant == False:
        cycles += 1
        #print(cycles)
        coords.append(function.get(x))
        differences = get_differences(coords, cycles)
        is_constant, ref = check_constant(differences)
        x+=1
    print(cycles, "was the computer's calculation.")
    print(function.degree, "was the degree of the function.")
    #print(ref)

main()

