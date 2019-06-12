import pygame,random,math

class Planet(object):
    def __init__(self,center,r,speed,angle,size,color):
        self.r = r
        self.b = 0.3
        self.a= 1
        self.x,self.y = 0,0
        self.center = center
        self.size = size
        self.distance = 0
        self.speed = speed
        self.angle = angle
        self.color = color

    def move(self):
        self.x_ = self.a*math.sin(math.radians(self.distance))*self.r 
        self.y_ = self.b*math.cos(math.radians(self.distance))*self.r
        self.x = self.x_*math.cos(math.radians(self.angle))+self.y_*math.sin(math.radians(self.angle))+self.center[0]
        self.y = -self.x_*math.sin(math.radians(self.angle))+self.y_*math.cos(math.radians(self.angle))+self.center[1]
        self.distance +=self.speed     

    def draw_orbit(self):
        trajectory = []
        for i in range(0,370,5):
            x_ = self.a*math.sin(math.radians(i))*self.r
            y_ = self.b*math.cos(math.radians(i))*self.r
            x  = x_*math.cos(math.radians(self.angle))+y_*math.sin(math.radians(self.angle))+self.center[0]
            y = -x_*math.sin(math.radians(self.angle))+y_*math.cos(math.radians(self.angle))+self.center[1]
            trajectory.append([x,y])
        pygame.draw.lines(screen,self.color,False,trajectory,1)

class Sattelite(object):
    def __init__(self,center,r,speed,angle,size,color):
        self.r = r
        self.b = 1
        self.a= 0.5
        self.x,self.y = 0,0
        self.center = [earth.x,earth.y]
        self.size = size
        self.distance = 0
        self.speed = speed
        self.angle = angle
        self.x_,self.y_ = 0,0
        self.color = color
    def move(self):
        self.center = [earth.x,earth.y]
        self.x_ = self.a*math.sin(math.radians(self.distance))*self.r 
        self.y_ = self.b*math.cos(math.radians(self.distance))*self.r 
        self.x= self.x_*math.cos(math.radians(self.angle))+self.y_*math.sin(math.radians(self.angle))+self.center[0]
        self.y = -self.x_*math.sin(math.radians(self.angle))+self.y_*math.cos(math.radians(self.angle))+self.center[1]
        self.distance +=self.speed

    def draw_orbit(self):
        trajectory = []
        for i in range(0,370,2):
            self.center = [earth.x,earth.y]
            x_ = self.a*math.sin(math.radians(i))*self.r
            y_ = self.b*math.cos(math.radians(i))*self.r
            x  = x_*math.cos(math.radians(self.angle))+y_*math.sin(math.radians(self.angle))+self.center[0]
            y = -x_*math.sin(math.radians(self.angle))+y_*math.cos(math.radians(self.angle))+self.center[1]
            trajectory.append((x,y))
        pygame.draw.lines(screen,self.color,False,trajectory,1)

class Comet(object):
    def __init__(self,center,r,speed,angle,size,color,a,b):
        self.r = r
        self.b = b
        self.a= a
        self.x,self.y = 0,0
        self.center = center
        self.size = size
        self.distance = 0
        self.speed = speed
        self.angle = angle
        self.color = color

    def move(self):
        self.x_ = self.a*math.sin(math.radians(self.distance))*self.r 
        self.y_ = self.b*math.cos(math.radians(self.distance))*self.r
        self.x = self.x_*math.cos(math.radians(self.angle))+self.y_*math.sin(math.radians(self.angle))+self.center[0]
        self.y = -self.x_*math.sin(math.radians(self.angle))+self.y_*math.cos(math.radians(self.angle))+self.center[1]
        self.distance +=self.speed     

    def draw_orbit(self):
        trajectory = []
        for i in range(0,370,5):
            x_ = self.a*math.sin(math.radians(i))*self.r
            y_ = self.b*math.cos(math.radians(i))*self.r
            x  = x_*math.cos(math.radians(self.angle))+y_*math.sin(math.radians(self.angle))+self.center[0]
            y = -x_*math.sin(math.radians(self.angle))+y_*math.cos(math.radians(self.angle))+self.center[1]
            trajectory.append([x,y])
        pygame.draw.lines(screen,self.color,False,trajectory,1)

def draw_orbits():
    if orbits:
        for planet in objects:
            planet.draw_orbit()

def draw_planets():
    for planet in objects:
        pygame.draw.circle(screen,planet.color,[int(planet.x),int(planet.y)],planet.size,0)

def move_planets():
    for planet in objects:
        planet.move()

def turn_orbits():
    pass   

def move_orbits(dst,pos):
    for planet in objects:
        planet.center[pos]+=dst

def draw_stars():
    for star in stars:
        pygame.draw.rect(screen,[255,255,255],[star[0],star[1],1,1],0)
        
def draw_sun():
    pygame.draw.circle(screen,[200,200,0],[earth.center[0],earth.center[1]],20,0)
    pygame.draw.circle(screen,[32,32,0],[earth.center[0],earth.center[1]],22,3)
    pygame.draw.circle(screen,[17,17,0],[earth.center[0],earth.center[1]],24,2)
    pygame.draw.circle(screen,[14,14,0],[earth.center[0],earth.center[1]],27,3)
    pygame.draw.circle(screen,[10,10,0],[earth.center[0],earth.center[1]],32,5)
    pygame.draw.circle(screen,[8,8,0],[earth.center[0],earth.center[1]],33,2)

def animate():
    pygame.time.delay(30)
    screen.fill([0,0,5])
    draw_stars()
    draw_sun()
    draw_orbits()
    move_planets()
    draw_planets()
    pygame.display.flip()

pygame.init()
size = sizeX,sizeY = 1280,700
center = x0,y0 = int(sizeX/2),int(sizeY/2)
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
pygame.display.flip()
stars = [(random.randint(0,sizeX),random.randint(0,sizeY)) for i in range(300)]
earth = Planet([400,350],150,1,0,7,[0,100,0])
mars = Planet([400,350],250,0.8,0,6,[100,0,50])
moon = Sattelite(earth.center[:],30,-3,0,3,[200,0,0])
moon2= Sattelite(earth.center[:],30,3,120,3,[0,200,200])
nibiru = Planet([450,350],320,-0.4,6,5,[25,25,250])
galley = Comet([1550,350],200,-1,0,6,[250,0,25],6,1)
objects = [earth,mars,moon,moon2,nibiru]
down_pressed,up_pressed,right_pressed,left_pressed = False,False,False,False
a_pressed,d_pressed,w_pressed,s_pressed = False,False,False,False
running = True
orbits = True
while running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_UP]:
                up_pressed = True
            if keys[pygame.K_DOWN]:
                down_pressed = True
            if keys[pygame.K_RIGHT]:
                right_pressed = True
            if keys[pygame.K_LEFT]:
                left_pressed = True
            if keys[pygame.K_a]:
                a_pressed = True
            if keys[pygame.K_d]:
                d_pressed = True
            if keys[pygame.K_w]:
                w_pressed = True
            if keys[pygame.K_s]:
                s_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_pressed = False
            elif event.key == pygame.K_DOWN:
                down_pressed = False
            elif event.key == pygame.K_RIGHT:
                right_pressed = False
            elif event.key == pygame.K_LEFT:
                left_pressed = False
            elif event.key == pygame.K_a:
                a_pressed = False
            elif event.key == pygame.K_d:
                d_pressed = False
            elif event.key == pygame.K_w:
                w_pressed = False
            elif event.key == pygame.K_s:
                s_pressed = False
    if down_pressed:
        if earth.b > 0:
            earth.b-=0.05
            mars.b -=0.05
            nibiru.b -=0.05
            galley.b -=0.05
    elif up_pressed:
        if earth.b < 1:
            earth.b+=0.05
            mars.b +=0.05
            nibiru.b +=0.05
            galley.b +=0.05
    elif right_pressed:
        if earth.a >0:
            earth.a -=0.05
            mars.a -=0.05
            nibiru.a -=0.05
    elif left_pressed:
        if earth.a <1:
            earth.a +=0.05
            mars.a +=0.05
            nibiru.a +=0.05
    if a_pressed:
        move_orbits(-4,0)
    elif d_pressed:
        move_orbits(4,0)
    if w_pressed:
        move_orbits(-4,1)
    elif s_pressed:
        move_orbits(4,1)
    animate()
pygame.quit()

"Ellipse example"
##a,b = 2,2
##for j in range(1000):
##    x = a*math.sin(math.radians(j))*r+400
##    y = b*math.cos(math.radians(j))*r+400
##    pygame.draw.rect(screen,[0,0,0],[x,y,1,1],0)
##pygame.display.flip()


"New movement implementation"
##import itertools
## positions = itertools.cyrcle([1,2,3])
## next(positions) # 1,2,3,1,2,3,......


