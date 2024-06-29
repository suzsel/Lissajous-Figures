import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons
from matplotlib.animation import FuncAnimation

# Parameters for the Lissajous figure
t = np.linspace(0, 2 * np.pi, 1000)  # Time for the full cycle

# Initial parameters
a_init, b_init, phi_init, A_init, B_init = 7, 7, np.pi / 2, 200, 100

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)
lissajous_line, = plt.plot([], [], lw=2)
ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)
ax.grid(True)
ax.set_aspect('equal', 'box')
ax.set_title('Interactive Lissajous Figure')

# Function to update the plot when sliders are manually adjusted
def update(val):
    a = s_a.val
    b = s_b.val
    phi = s_phi.val
    A = s_A.val
    B = s_B.val
    x = A * np.sin(a * t + phi)
    y = B * np.sin(b * t)
    lissajous_line.set_data(x, y)
    fig.canvas.draw_idle()

# Animation update function
def animate(i):
    if animate_phi.get_status()[0]:  # Check if animation is enabled
        # Increment phi for animation and update slider value
        new_phi = (s_phi.val + 0.01) % (2 * np.pi)
        s_phi.set_val(new_phi)  # Update the slider value
        a = s_a.val
        b = s_b.val
        A = s_A.val
        B = s_B.val
        x = A * np.sin(a * t + new_phi)
        y = B * np.sin(b * t)
        lissajous_line.set_data(x, y)
    return (lissajous_line,)

# Sliders for parameters
axcolor = 'lightgoldenrodyellow'
ax_a = plt.axes([0.1, 0.25, 0.65, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.1, 0.20, 0.65, 0.03], facecolor=axcolor)
ax_phi = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_A = plt.axes([0.1, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_B = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor=axcolor)

s_a = Slider(ax_a, 'a', 1, 10, valinit=a_init, valstep=1)
s_b = Slider(ax_b, 'b', 1, 10, valinit=b_init, valstep=1)
s_phi = Slider(ax_phi, 'phi', 0, 2*np.pi, valinit=phi_init)
s_A = Slider(ax_A, 'A', 50, 300, valinit=A_init)
s_B = Slider(ax_B, 'B', 50, 300, valinit=B_init)

# apply update functions
s_a.on_changed(update)
s_b.on_changed(update)
s_phi.on_changed(update)
s_A.on_changed(update)
s_B.on_changed(update)

# Checkbox to control animation
ax_check = plt.axes([0.04, 0.5, 0.185, 0.1], facecolor=axcolor)
animate_phi = CheckButtons(ax_check, ['Animate phi'], [True])

# Create animation
ani = FuncAnimation(fig, animate, frames=t.shape[0], blit=False, interval=16, repeat=False)
ani.save('animations/lissajou2.gif')

plt.show()
