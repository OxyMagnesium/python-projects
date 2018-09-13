import math

pi = 3.14
def avg(a,b):
    return (a+b)/2

def clean(x):
    return str(round(x,2))

def calcrange(t,u):
    return clean(u*u*math.sin(2*math.radians(t))/9.8) + " m"

def calcvel(t,r):
    return clean(math.sqrt(r*9.8/math.sin(2*math.radians(t)))) + " m/s"

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
    if count < cutoff:
        return clean(math.degrees(guess)) + " degrees"
    else:
        return "It is not possible to hit the target."

#Program start

func = input("Enter component to calculate (Range/Launch velocity/Launch angle): ")

print("")

if func.lower() == 'range' or func.lower() == 'launch velocity':
    t = float(input("Enter the launch angle (degrees): "))

if func.lower() == 'launch velocity' or func.lower() == 'launch angle':
    r = float(input("Enter the target distance (m): "))

if func.lower() == 'launch angle' or func.lower() == 'range':
    u = float(input("Enter the launch velocity (m/s): "))

print("")

if func.lower() == 'range':
    print("Result: %s"%(calcrange(t,u)))

if func.lower() == 'launch velocity':
    print("Result: %s"%(calcvel(t,r)))

if func.lower() == 'launch angle':
    print("Result: %s"%(calctheta(r,u)))

print("")

end_stop = input("Press enter to quit.")
