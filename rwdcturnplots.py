from matplotlib import pyplot as plt
from math import atan, cos

#Constants and functions
A = 3.141*1.410**2
d = 1.223
P = 1500
g = 9.810
s = 1.2

def C(m):
    return (2*A*d*P**2/s**2)**(1/3)/m

def k(v):
    return (  144.0 + 1.196*v - 9.726e-1*v**2
            + 6.640e-2*v**3 - 1.798e-3*v**4 + 1.781e-5*v**5)/144

def turn_radius(m, v):
    return (v**2*k(v)**(2/3))/(C(m)**2 - g**2*k(v)**(4/3))**(1/2)

def bank_angle(m, v):
    return atan((v**2)/(g*turn_radius(m, v)))

def load_factor(m, v):
    return 1/cos(bank_angle(m, v))

dx = 1e-3
lb = dx
ub = 30

x = lb
m = 25

x_vals = []
y_turn_radius = []
y_bank_angle = []
y_load_factor = []

while x <= ub:
    try:
        x_vals.append(x)
        y_turn_radius.append(turn_radius(m, x))
        y_bank_angle.append((180/3.14)*bank_angle(m, x))
        y_load_factor.append(load_factor(m, x))
        x += dx
    except TypeError:
        x_vals = x_vals[ :len(x_vals) - 1]
        y_turn_radius = y_turn_radius[ :len(x_vals)]
        y_bank_angle = y_bank_angle[ :len(x_vals)]
        y_load_factor = y_load_factor[ :len(x_vals)]
        break

fig = plt.figure()

plt.style.use(['science', 'no-latex'])
plt.grid(True, which = 'major', color = 'black')
plt.grid(True, which = 'minor')

ax1 = fig.add_subplot()
ax2 = ax1.twinx()
ax2._get_lines.prop_cycler = ax1._get_lines.prop_cycler

ax1.plot(x_vals, y_turn_radius, label = 'Turn radius', linewidth = 2)
ax1.plot(x_vals, y_bank_angle, label = 'Bank angle', linewidth = 2)
ax2.plot(x_vals, y_load_factor, label = 'Load factor', linewidth = 2)

ax1.set_xlabel('Forward speed (m/s)')
ax1.set_ylabel('Turn radius (m), Bank angle (°)')
ax2.set_ylabel('Load factor')

ax1.set_xlim([0, ub])
ax1.set_ylim([0, 60])
ax2.set_ylim([0, 6])

plt.title("Variation of turn radius, bank angle, and load factor with velocity")
fig.legend()
plt.show()
