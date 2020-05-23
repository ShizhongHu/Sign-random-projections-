import random


features = int(input("How many features of the two objects do you wish to compare: "))

vectorone = []
vectortwo = []

i = 0
numberone = 0
numbertwo = 0

while i < features:
    numberone = random.randint(-10, 10)
    vectorone.append(numberone)
    numbertwo = random.randint(-10, 10)
    vectortwo.append(numbertwo)
i += 1

normalcomparison = int(input("Select the number of times you want to compare the normal to both the vectors: "))

n = 0
t = 0
z = 0
resultone = 0
resulttwo = 0
normal = []
normalnumber = 0
count = 0

while n < normalcomparison:
    while t < len(vectorone):
        normalnumber = random.randint(-10, 10)
        normal.append(normalnumber)
    t += 1

    while z < len(vectorone):
        resultone += vectorone[z]*normal[z]
        resulttwo += vectortwo[z]*normal[z]
    z += 1

    if resultone < 0 and resulttwo > 0:
        count += 1
    if resultone > 0 and resulttwo < 0:
        count += 1
n += 1

# calculation of angular difference between two vectors in degrees

angulardifference = (count/normalcomparison)*180
