import numpy as np
import matplotlib.pyplot as plt

# Circle radius
R = 1

# Number of random chords to generate
N = 50000

# --- Method 1: Random Endpoints on Circle ---
def random_endpoints_method(N):
    angles1 = np.random.uniform(0, 2*np.pi, N)
    angles2 = np.random.uniform(0, 2*np.pi, N)
    lengths = 2 * R * np.sin(np.abs(angles1 - angles2) / 2)
    return np.mean(lengths > np.sqrt(3))

# ---  Method 2: Random Radius + Point on it ---
def random_radius_method(N):
    d = np.random.uniform(0, R, N)  # distance from center
    lengths = 2 * np.sqrt(R**2 - d**2)
    return np.mean(lengths > np.sqrt(3))

# ---  Method 3: Random Midpoint inside Circle ---
def random_midpoint_method(N):
    r = np.sqrt(np.random.uniform(0, 1, N)) * R
    lengths = 2 * np.sqrt(R**2 - r**2)
    return np.mean(lengths > np.sqrt(3))

# --- Compute probabilities ---
p1 = random_endpoints_method(N)
p2 = random_radius_method(N)
p3 = random_midpoint_method(N)

print(" Probability (Method 1: Random Endpoints):", round(p1, 3))
print(" Probability (Method 2: Random Radius):   ", round(p2, 3))
print(" Probability (Method 3: Random Midpoint): ", round(p3, 3))

# --- Visualization for Method 3 (Midpoints) ---
fig, ax = plt.subplots(figsize=(6,6))
circle = plt.Circle((0, 0), R, color='lightgray', fill=False, lw=2)

# Chords visualization for Method 3
r = np.sqrt(np.random.uniform(0, 1, 200))
theta = np.random.uniform(0, 2*np.pi, 200)
x = r * np.cos(theta)
y = r * np.sin(theta)

for i in range(200):
    midx, midy = x[i], y[i]
    dist = np.sqrt(midx**2 + midy**2)
    half_len = np.sqrt(R**2 - dist**2)
    angle = np.arctan2(midy, midx)
    x1 = midx + half_len * np.sin(angle)
    y1 = midy - half_len * np.cos(angle)
    x2 = midx - half_len * np.sin(angle)
    y2 = midy + half_len * np.cos(angle)
    color = 'green' if 2*half_len > np.sqrt(3) else 'red'
    ax.plot([x1, x2], [y1, y2], color=color, alpha=0.5)

ax.add_artist(circle)
ax.set_aspect('equal')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_title("Bertrand Paradox – Method 3 (Random Midpoints)")
plt.show()
