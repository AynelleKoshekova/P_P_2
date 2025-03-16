import pygame

pygame.init()

width, height = 1000, 500
screen = pygame.display.set_mode((width, height))

x=width//2
y=height//2
velocity = 20
radius = 25

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP] and y - velocity >= radius:
        y -= velocity
    if keys[pygame.K_DOWN] and y + velocity <= height - radius:
        y += velocity
    if keys[pygame.K_LEFT] and x - velocity >= radius:
        x -= velocity
    if keys[pygame.K_RIGHT] and x + velocity <= width - radius:
        x += velocity

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pygame.display.flip()  
    clock.tick(60)  

pygame.quit()