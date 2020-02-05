
G = 6.674e-11
M = 5.972e24
ri = int(input("Enter the height from which the object is dropped (km): "))*1e3
rf = int(input("Enter the height until which the time has to be calculated (km): "))*1e3

class Object:
    def __init__(self, start_height):
        self.v = 0
        self.h = start_height

    def update(self, dt):
        self.a = (G*M)/(self.h**2)
        self.h -= self.v*dt
        self.v += self.a*dt

ob = Object(ri)
t = 0
dt = 1e-3

while ob.h > rf:
    ob.update(dt)
    t += dt

print(f"Time taken: {t} seconds/{t/3600} hours.")
