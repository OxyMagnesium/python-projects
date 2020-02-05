from time import clock as t

mp = 1.673e-27
qp = 1.602e-19

pi = 3.142e-00
e0 = 8.854e-12
u0 = 1.257e-06

class Vector:
    def __init__(self, i = 0, j = 0, k = 0):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"({self.i:.3f}, {self.j:.3f}, {self.k:.3f})"

    def __abs__(self):
        return (self.i**2 + self.j**2 + self.k**2)**(1/2)

    def __add__(self, other):
        new_vector = Vector()
        new_vector.i = self.i + other.i
        new_vector.j = self.j + other.j
        new_vector.k = self.k + other.k
        return new_vector

    def __sub__(self, other):
        other.i *= -1
        other.j *= -1
        other.k *= -1
        return self.__add__(other)

    def __mul__(self, scalar):
        new_vector = Vector()
        new_vector.i = self.i*scalar
        new_vector.j = self.j*scalar
        new_vector.k = self.k*scalar
        return new_vector

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        scalar_inv = 1/scalar
        return self.__mul__(scalar_inv)

    def dot(self, other):
        return (self.i*other.i) + (self.j*other.j) + (self.k*other.k)

    def cross(self, other):
        new_vector = Vector()
        new_vector.i += (self.j*other.k - self.k*other.j)
        new_vector.j -= (self.i*other.k - self.k*other.i)
        new_vector.k += (self.i*other.j - self.j*other.i)
        return new_vector


class Worldspace:
    def __init__(self):
        self.obj_list = []

    def add_obj(self, new_obj):
        for obj in self.obj_list:
            obj.add_ref(new_obj)
            new_obj.add_ref(obj)
        self.obj_list.append(new_obj)

    def get_objs(self):
        return self.obj_list

    def tick(self, dt):
        for obj in self.obj_list:
            obj.compute_tick()
        for obj in self.obj_list:
            obj.apply_tick(dt)


class Charge:
    def __init__(self, m = mp, q = qp, s = Vector(), v = Vector()):
        self.m = m
        self.q = q
        self.s = s
        self.v = v
        self.refs = []

    def add_ref(self, ref):
        self.refs.append(ref)

    def compute_tick(self):
        self.a = Vector()
        for ref in self.refs:
            k = 4*pi*e0
            q = ref.q
            r = self.s - ref.s
            E = (k*q*r)/(abs(r)**3)
            self.a += (self.q*E)/(self.m)
            v = self.v - ref.v
            B = ref.get_B(v, r)
            self.a += (q*v.cross(B))/(self.m)

    def apply_tick(self, dt):
        self.v += self.a*dt
        self.s += self.v*dt
        del self.a

    def get_B(self, v, r):
        vr = self.v - v
        return (u0*self.q*vr.cross(r))/(4*pi*abs(r)**3)

    def get_params(self):
        return f"s: {self.s} m" #; v: {self.v} m/s"


def main():
    world = Worldspace()

    q1 = 2e-6
    m1 = 50e-3
    q2 = 6e-3
    m2 = 8000e-3

    o1 = Charge(m = m1, q = q1, v = Vector(-0.5), s = Vector(2, 0.25))
    o2 = Charge(m = m2, q = q2)

    world.add_obj(o1)
    world.add_obj(o2)

    t0 = t()
    ds = 0
    et = 0

    print("Starting sim...\n")

    while et < 5:
        dt = 1e-3
        if et > ds:
            info = ""
            for obj in world.get_objs():
                info += obj.get_params() + " | "
            print(info[0:-3])
            ds += 0.1
        world.tick(dt)
        et += dt

    print("\nSimulation terminated.")

main()
