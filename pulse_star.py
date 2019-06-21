import pygame,itertools
pygame.init()

def make_shining(to_int,times):
    list2 = []
    for num in range(1,to_int+1):
        list2.extend([num for i in range(times)])
    for num in range(to_int-1,1,-1):
        list2.extend([num for i in range(times)])
    return list2


def animate():
    pygame.time.delay(10)
    screen.fill((0,0,0))
    next_s = next(shining)
    color_s = next(color_shining)
    pygame.draw.circle(screen,[10,10,0],[centerX,centerY],43+next_s,0)
    pygame.draw.circle(screen,[16,16,0],[centerX,centerY],36+next_s,0)
    pygame.draw.circle(screen,[20,20,0],[centerX,centerY],26+next_s,0)
    pygame.draw.circle(screen,[250,250,0],[centerX,centerY],28,0)
    
    pygame.display.flip()

sizeX,sizeY = 640,480
centerX,centerY = int(sizeX/2),int(sizeY/2)
screen = pygame.display.set_mode([sizeX,sizeY])
pygame.display.set_caption('A game')
shining_slow = 15
shining_range = 15
shining = itertools.cycle(make_shining(shining_range,shining_slow))
running = True
color_shining = itertools.cycle(make_shining(60,10))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    animate()
pygame.quit()
    
