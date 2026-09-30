import random, pygame, sys, time, gif_pygame
import imgrender, playerclass
sw, sh = 1000, 1000
display = pygame.display.set_mode((sw, sh))
#gameclock
clock = pygame.time.Clock()
pygame.display.set_caption('Baby Fighter 5')
imgrender.renderimg()
#gamevars
#baby1test
babyy = -155
babyx = -180
playery = 400
lgifduration = 600
rgifduration = 1000
lactionstarttime = 0
ractionstarttime = 0
player1 = playerclass.player()
#gamefunc
def hitstatus():
    if player1.status == 0:
        player1.imgstatus = 0
    elif player1.status == 1:
        player1.imgstatus = 1
    elif player1.status == 2:
        player1.imgstatus = 2
#game loop 
running = True
while running:
    #babys 
    babymask = pygame.mask.from_surface(imgrender.bb1.get_current_surface())
    current_time = pygame.time.get_ticks()
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if player1.status == 0:
                if event.key == pygame.K_d:
                    playery = 380
                    player1.status = 1
                    lactionstarttime = current_time
                if event.key == pygame.K_a:
                    player1.status = 2
                    playery = 350
                    ractionstarttime = current_time
                if event.key == pygame.K_w:
                    player1.status = 0
    hitstatus()
    if babyx <= 50:
        babyx += 2
        babyy += 2
    elif babyx >= 50 and babyx < 275: 
        babyx += 2
        babyy += 1
    elif babyx >= 275:
        babyy += 2
    if babyy == 501:
        babyx = -180
        babyy = -155
    print(f'bbx: {babyx}')
    if player1.status == 1 and (current_time - lactionstarttime > lgifduration):
        player1.status = 0 
        playery = 400
    if player1.status == 2 and (current_time - ractionstarttime > rgifduration):
        player1.status = 0
        playery = 400 
    display.blit(imgrender.bg, (0, 0))
    #offset (my life is a lie)

    if player1.imgstatus == 0:
        imgrender.static.render(display, (300, playery))
    if player1.imgstatus == 1:
        imgrender.lefthit.render(display, (325, playery))
        imgrender.lb.render(display, (325, playery))
    if player1.imgstatus == 2:
        imgrender.righthit.render(display, (300, playery))
        imgrender.rb.render(display, (300, playery))
    imgrender.bb1.render(display, (babyx, babyy))
    pygame.display.flip()
    clock.tick(60)
