import numpy as np

results = open("day06.inp", "r")
times, distances = [list(map(float, line.split()[1:])) for line in results.readlines()]

#part A
prod = 1
for time, distance in zip(times, distances):
    #charge = speed
    #travel = charge*(time-charge) i.e. -charge²+time*charge
    #equal the distane record if -charge²-time*charge-distance=0 -> quadratic formula (charge = x, a = 1)
    delta = time**2 - 4*1*distance
    if delta > 0:
        low = np.floor((time - np.sqrt(delta))/(2*1)+1) #np.floor(...+1) modification to yield appropriate ranges
        high = np.ceil((time + np.sqrt(delta))/(2*1)-1)

        prod = prod * (high+1-low)
    else:
        exit("delta <= 0")

print("A: ", int(prod))

#part B
time = float("".join(list(map(str, map(int, times)))))
distance = float("".join(list(map(str, map(int, distances)))))

delta = time**2 - 4*1*distance
if delta > 0:
    low = np.floor((time - np.sqrt(delta))/(2*1)+1) #np.floor(...+1) modification to yield appropriate ranges
    high = np.ceil((time + np.sqrt(delta))/(2*1)-1)

    print("B: ", int(high+1-low))
else:
    exit("delta <= 0")



