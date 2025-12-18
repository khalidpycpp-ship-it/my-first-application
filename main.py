import pygame
import requests
from io import BytesIO
import math

# -----------------------------
# INITIALISATION
# -----------------------------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animation Image - Mouvement, Rotation, Zoom")
clock = pygame.time.Clock()

# -----------------------------
# CHARGER IMAGE DEPUIS INTERNET
# -----------------------------
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Example.jpg/640px-Example.jpg"
image_bytes = requests.get(url).content
image_original = pygame.image.load(BytesIO(image_bytes)).convert_alpha()

# -----------------------------
# VARIABLES DE MOUVEMENT
# -----------------------------
x, y = WIDTH // 2, HEIGHT // 2
vx, vy = 3, 2
angle = 0
time = 0

# -----------------------------
# BOUCLE PRINCIPALE
# -----------------------------
running = True
while running:
    clock.tick(60)  # 60 FPS
    screen.fill((20, 20, 20))

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -----------------------------
    # DÉPLACEMENT
    # -----------------------------
    x += vx
    y += vy

    if x < 100 or x > WIDTH - 100:
        vx *= -1
    if y < 100 or y > HEIGHT - 100:
        vy *= -1

    # -----------------------------
    # ROTATION
    # -----------------------------
    angle += 2

    # -----------------------------
    # ZOOM (oscillation sinusoïdale)
    # -----------------------------
    time += 0.05
    scale = 1 + 0.3 * math.sin(time)

    # -----------------------------
    # TRANSFORMATION IMAGE
    # -----------------------------
    image_transformed = pygame.transform.rotozoom(
        image_original,
        angle,
        scale
    )

    rect = image_transformed.get_rect(center=(x, y))
    screen.blit(image_transformed, rect)

    pygame.display.flip()

# -----------------------------
# FERMETURE
# -----------------------------
pygame.quit()
