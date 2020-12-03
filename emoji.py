import pygame

x, y = int(input()), int(input())
pygame.init()
size = width, height = x, y
screen = pygame.display.set_mode(size)

drawing = False
running = True

v = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 83, 138))
    if event.type == pygame.MOUSEBUTTONUP:
        drawing = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        a = event.pos
        clock = pygame.time.Clock()
        x_pos = 0
        drawing = False
    if drawing:
        pygame.draw.circle(screen, (255, 255, 0), a, int(x_pos))
        x_pos += v * clock.tick() / 1000  # v * t в секундах
    pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
