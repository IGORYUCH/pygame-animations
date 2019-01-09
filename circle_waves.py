import pygame


class CircleWave():
    def __init__(self,pos_xy):
        self.color = [0,0,0]
        self.x = pos_xy[0]
        self.y = pos_xy[1]
        self.radius = 0
        self.max_radius = 120
        self.speed = 2
        self.color_speed = 255/(self.max_radius / self.speed) * 0.99 # 255.0 * 0.99 to prevent inaccuracy of float

    def move(self):
        self.radius += self.speed
        self.color = [self.color[0] + self.color_speed,
                      self.color[1] + self.color_speed,
                      self.color[2] + self.color_speed]
        print(self.color)
        pygame.draw.circle(screen,
                           (self.color[0],
                            self.color[1],
                            self.color[2]),
                            [self.x, self.y], self.radius, 1)


def animate():
    global waves
    screen.fill([255, 255, 255])
    if waves: # if waves is not empty: draw each wave in loop
        for wave in waves:
            wave.move()
        for wave in waves:
                if wave.radius == wave.max_radius:
                    waves.remove(wave) # delete if r > size x of screen
    pygame.display.flip()
    pygame.time.delay(25)


pygame.init()
size = sizeX, sizeY = 1024,768
center = x0, y0 = sizeX/2, sizeY/2
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
pygame.display.flip()
running = True
waves = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            waves.append(CircleWave(pygame.mouse.get_pos()))
        #if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1: #causes troubles
            #waves.append(CircleWave(pygame.mouse.get_pos()))
    animate()
pygame.quit()