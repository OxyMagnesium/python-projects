import math

pi = 3.14
def avg(a,b):
    c = (a + b)/2
    return c

def calctheta(r,u):
    count = 0
    cutoff = 100
    u2g = u*u/9.8
    high_g = pi/4
    low_g = 0
    while(count <= cutoff):
        guess = avg(high_g,low_g)
        if u2g*math.sin(2*guess) < r:
            low_g = guess
        if u2g*math.sin(2*guess) > r:
            high_g = guess
        if round(u2g*math.sin(2*guess),2) == r:
            break
        count += 1
    if(count < cutoff):
        return str(round(math.degrees(guess),2)) + " degrees"
    else:
        return "It is not possible to hit the target."
                  
r = float(input("Enter the distance to target (m): "))
u = float(input("Enter the projection velocity (m/s): "))

print("")

print("Result:\n" + calctheta(r,u))

print("")

end_stop = input("Press enter to quit")

    
