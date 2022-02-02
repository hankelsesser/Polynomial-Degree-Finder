import random

data_txt = open(("poly_finder_data.txt"))
data = data_txt.readlines()

#returns [[x, y],[x.y],...]:

def clean(data, partition): #takes the data and what is between the x and y coords
    clean_data =[]
    for line in data:
        line = line.replace("\n", "")
        space = line.find(partition)
        clean_data.append([line[0:space], line[space+(len(partition))::]])
    return(clean_data)

##if change in x between data points is linear:
#returns [y, y, y...]

def clean(data, partition): #takes the data and what is between the x and y coords
    clean_data =[]
    for line in data:
        line = line.replace("\n", "")
        space = line.find(partition)
        y = line[space+(len(partition))::]
        if "E" in y:
            e_index = y.find("E")
            base = float(y[0:e_index])
            exp = int(y[e_index+1::])
            y = base * 10**exp
        clean_data.append(int(y))
    return(clean_data)

data = clean(data, "\t")

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
    cycles = 0#trying to find this number difference
    x = 4
    coords = data[0:x]
    
    while is_constant == False:
        cycles += 1
        #print(cycles)
        coords = data[0:x]
        differences = get_differences(coords, cycles)
        is_constant, ref = check_constant(differences)
        x+=1
    print(cycles, "was the computer's calculation.")
    #print(, "was the degree of the function.")
    #print(ref)

main()