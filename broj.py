import pygame
import sys

# Inicijalizacija pygame-a
pygame.init()

# Postavljanje ekrana u full-screen režim
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()  # Dinamično dohvati dimenzije ekrana
pygame.display.set_caption("7-segment Display Fullscreen")

# Boje
green = (0, 255, 0)
black = (0, 0, 0)
highlight_color = (255, 255, 0)  # Boja za označavanje odabrane znamenke

# Brojevi za prikaz (početni)
broj = ["1", "2", "3", "4", "5", "6", "7"]

# Izračun dinamičke veličine fonta na temelju širine ekrana
font_size = width // len(broj) - 20  # Oduzimamo malo prostora za marginu
font = pygame.font.Font("7seg.ttf", font_size)

# Varijable za praćenje odabrane znamenke
selected_index = 0

# Funkcija za prikaz brojeva
def draw_numbers():
    screen.fill(black)  # Pozadina crna
    segment_width = width // len(broj)  # Izračun širine svakog broja za ravnomjerni razmak
    
    for i, digit in enumerate(broj):
        # Ako je trenutna znamenka odabrana, prikaži je drugačijom bojom
        color = highlight_color if i == selected_index else green
        text_surface = font.render(digit, True, color)
        text_rect = text_surface.get_rect(center=(i * segment_width + segment_width // 2, height // 2))
        screen.blit(text_surface, text_rect)  # Prikaz broja

# Glavna petlja
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # Izađi iz full-screen režima pritiskom na ESC
            elif event.key == pygame.K_LEFT:
                # Pomiči odabranu znamenku ulijevo
                selected_index = (selected_index - 1) % len(broj)
            elif event.key == pygame.K_RIGHT:
                # Pomiči odabranu znamenku udesno
                selected_index = (selected_index + 1) % len(broj)
            elif event.key == pygame.K_UP:
                # Povećaj vrijednost odabrane znamenke
                broj[selected_index] = str((int(broj[selected_index]) + 1) % 10)
            elif event.key == pygame.K_DOWN:
                # Smanji vrijednost odabrane znamenke
                broj[selected_index] = str((int(broj[selected_index]) - 1) % 10)

    draw_numbers()
    pygame.display.flip()

# Zatvaranje pygame-a
pygame.quit()
sys.exit()
