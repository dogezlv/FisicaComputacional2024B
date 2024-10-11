import matplotlib.pyplot as plt
import matplotlib.animation as animation

m = 20
d = 100  
t = 10  
vi = 0.0 
vf = 20.0  

a = (vf - vi) / t
fuerza = m * a

fig, ax = plt.subplots()
ax.set_xlim(0, d)
ax.set_ylim(0, vf + 2)
ax.set_xlabel('Distancia (m)')
ax.set_ylabel('Velocidad (m/s)')
line, = ax.plot([], [], lw=2)
text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    text.set_text('')
    return line, text

def animate(i):
    t_actual = i / 10.0
    if t_actual > t:
        t_actual = t_actual % t
    x = vi * t_actual + 0.5 * a * t_actual**2
    v = vi + a * t_actual
    line.set_data([0, x], [0, v])
    text.set_text(f'Velocidad: {v:.2f} m/s\nFuerza: {fuerza:.2f} N')
    return line, text

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)
plt.show()
