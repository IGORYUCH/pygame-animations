import pygame

class RectMove:
    def __init__(self,x,y,gray):
        self.x = x
        self.y = y
        self.x_spd = 1
        self.y_spd = 2
        self.gray = gray
    def move(self):
        pygame.draw.circle(screen,[self.gray,self.gray,self.gray],
                         [self.x-2,self.y-2],10,0)
        if self.x < 0 or self.x > 630:
            self.x_spd = - self.x_spd
        if self.y < 0 or self.y > 470:
            self.y_spd = -self.y_spd
        self.x += self.x_spd
        self.y += self.y_spd

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.display.flip()
running = True        
rects = [RectMove(10,10,1),]
time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([255,255,255])

    for i in rects:
        i.move()
    if time % 2 == 0 and time < 80:
        rects.append(RectMove(10,10,time*3.2))
    pygame.display.flip()
    pygame.time.delay(3)
    time += 1
pygame.quit()
