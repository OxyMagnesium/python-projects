from matplotlib import pyplot as plt
from math import atan, cos

#Constants and functions
A = 3.141*1.410**2
d = 1.223
P = 2150
g = 9.810

def C(m):
    return (2*A*d*P**2)**(1/3)/m

def k(v):
    return (100.796 - 1.481*v - 0.201*v**2 + 0.017*v**3)/100

def turn_radius(m, v):
    return (v**2*k(v)**(2/3))/(C(m)**2 - g**2*k(v)**(4/3))**(1/2)

def bank_angle(m, v):
    return atan((v**2)/(g*turn_radius(m, v)))

def g_force(m, v):
    return 1/cos(bank_angle(m, v))

dx = 0.1
lb = 0.1
ub = 25

x = lb
m = 25

x_vals = []
y_turn_radius = []
y_bank_angle = []
y_g_force = []

while x <= ub:
    x_vals.append(x)
    y_turn_radius.append(turn_radius(m, x))
    y_bank_angle.append((180/3.14)*bank_angle(m, x))
    y_g_force.append(g_force(m, x))
    x += dx

fig = plt.figure()

plt.style.use(['science', 'no-latex'])
plt.grid(True, which = 'major', color = 'black')
plt.grid(True, which = 'minor')

ax1 = fig.add_subplot()
ax2 = ax1.twinx()
ax2._get_lines.prop_cycler = ax1._get_lines.prop_cycler

ax1.plot(x_vals, y_turn_radius, label = 'Turn radius (m)', linewidth = 2)
ax1.plot(x_vals, y_bank_angle, label = 'Bank angle (°)', linewidth = 2)
ax2.plot(x_vals, y_g_force, label = 'G force (g)', linewidth = 2)

ax1.set_xlabel('Forward speed (m/s)')
ax1.set_ylabel('Turn radius (m), Bank angle (°)')
ax2.set_ylabel('G force (g)')

ax1.set_xlim([0, 25])
ax1.set_ylim([0, 80])
ax2.set_ylim([0, 8])

plt.title("Variation of turn radius, bank angle, and G force with velocity")
fig.legend()
plt.show()
