import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import math

# -----------------------------
# CHARGER IMAGE DEPUIS INTERNET
# -----------------------------
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Example.jpg/640px-Example.jpg"
response = requests.get(url)
image_original = Image.open(BytesIO(response.content)).convert("RGBA")

# -----------------------------
# INITIALISATION FENÊTRE
# -----------------------------
root = tk.Tk()
root.title("Animation Image - Tkinter")
WIDTH, HEIGHT = 800, 600

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# -----------------------------
# VARIABLES D'ANIMATION
# -----------------------------
x = WIDTH // 2
y = HEIGHT // 2
vx = 3
vy = 2
angle = 0
t = 0

photo = None
image_id = None

# -----------------------------
# FONCTION D'ANIMATION
# -----------------------------
def animate():
    global x, y, vx, vy, angle, t, photo, image_id

    # Déplacement
    x += vx
    y += vy

    if x < 100 or x > WIDTH - 100:
        vx *= -1
    if y < 100 or y > HEIGHT - 100:
        vy *= -1

    # Rotation
    angle += 3

    # Zoom (sinusoïdal)
    t += 0.1
    scale = 1 + 0.3 * math.sin(t)

    # Transformation image
    img = image_original.rotate(angle, expand=True)
    w, h = img.size
    img = img.resize((int(w * scale), int(h * scale)))

    photo = ImageTk.PhotoImage(img)

    # Affichage
    canvas.delete("all")
    canvas.create_image(x, y, image=photo)

    # Relancer animation
    root.after(30, animate)

# -----------------------------
# LANCER ANIMATION
# -----------------------------
animate()
root.mainloop()
