# I rippped those code offline to use the algorithm for the challenge
# http://stackoverflow.com/questions/8484802/conways-game-of-life-with-python



import numpy

# this function does all the work
def play_life(a):
    xmax, ymax = a.shape
    b = a.copy() # copy grid & Rule 2
    for x in range(xmax):
        for y in range(ymax):
            n = numpy.sum(a[max(x - 1, 0):min(x + 2, xmax), max(y - 1, 0):min(y + 2, ymax)]) - a[x, y]
            if a[x, y]:
                if n < 2 or n > 3:
                    b[x, y] = 0 # Rule 1 and 3
            elif n == 3:
                b[x, y] = 1 # Rule 4
    return(b)

# replace (5, 5) with the desired dimensions
life = numpy.zeros((5, 5), dtype=numpy.byte)
print life

# place starting conditions here
life[2, 1:4] = 1 # a simple "spinner"

# now let's play
print(life)
for i in range(3):
    life = play_life(life)
    print ""
    print(life)