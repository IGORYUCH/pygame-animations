import pygame,random
pygame.init()
sizex,sizey= 1366,768
centerx,centery = int(sizex/2),int(sizey/2)
screen = pygame.display.set_mode([sizex,sizey])
screen.fill([0,0,0])
pygame.display.flip()

class Star():
    def __init__(self,yspeed,xspeed,time):
        self.pos = [centerx,centery]
        self.yspeed= yspeed
        self.xspeed = xspeed
        self.time = time
        self.color = [255,255,255]
        self.inverted = True
    def move(self):
        if self.time <300:
            self.time+=1
        else:
            self.pos[0]+=self.xspeed
            self.pos[1]+=self.yspeed
            if self.pos[0]>sizex or self.pos[0] <1:
                self.pos = [centerx,centery]
                self.inverted = not self.inverted
                self.color = [255*self.inverted,255*self.inverted,255*self.inverted]
            if self.pos[1]>sizey or self.pos[1]<1:
                self.inverted = not self.inverted
                self.color = [255*self.inverted,255*self.inverted,255*self.inverted]
                self.pos = [centerx,centery]
def animate():
    pygame.time.delay(30)
    #screen.fill([0,0,0])
    for star in stars:
        star.move()
        pygame.draw.rect(screen,star.color,[int(star.pos[0]),int(star.pos[1]),1,1],0)
        pygame.draw.circle(screen,[0,0,0],[centerx,centery],4,0)
    pygame.display.flip()
speed = [-5,-4,-3,-2,1,1,2,3,4,5]
stars = []
for i in range(200):
    star = Star(random.choice(speed)+(random.random()*random.choice([True,False])),
                random.choice(speed)+(random.random()*random.choice([True,False])),
                random.randint(1,300))
    stars.append(star)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    animate()
pygame.quit()
