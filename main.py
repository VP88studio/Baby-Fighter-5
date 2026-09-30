import random, pygame, sys, time
sw, sh = 1000, 1000
display = pygame.display.set_mode((sw, sh))
#gameclock
clock = pygame.time.Clock()
pygame.display.set_caption('Baby Fighter 5')

#game loop 
running = True
while running:
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
