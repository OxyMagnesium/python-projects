from math import sqrt, pi

G = 6.67408e-11
dt = 1e-1

m1 = float(input("Enter the mass of the first object (kg): "))
m2 = float(input("Enter the mass of the second object (kg): "))

r = float(input("Enter the distance between the objects (m): "))

class obj:
    def __init__(self, m):
        self.m = m
        self.v = 0

    def tick(self):
        global r
        self.v += ((G*self.m)/r**2)*dt
        r -= self.v*dt

o1 = obj(m1)
o2 = obj(m2)
ts = 0
tc = sqrt((r**3)/(8*G*(m1 + m2)))*pi

print("\nCalculating...")

while r > 0:
    o1.tick()
    o2.tick()
    ts += dt

print(f"Simulated collision time: {ts} seconds")
print(f"Calculated collision time: {tc} seconds")
print(f"Error: {abs(1 - ts/tc)*100}%")
