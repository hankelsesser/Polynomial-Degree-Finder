dataset = open("poly_finder_data.txt","w")

degree = 242

for i in range(degree*2):
    dataset.write(str(i) + "\t" + str(10*i**degree)+"\n")