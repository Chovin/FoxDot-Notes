Scale.default = 'minorPentatonic'

p1 >> pluck([0,1,2,3,5], amp=[.2,.4,.6,.8,1], dur=PDur([3,5],8))



import pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (1080, 850)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def graphics():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pass
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, 
        (int(size[0]/2), int(size[1]/2)), int(p1.amp*size[1]/3), 0)
    pygame.display.update()
    Clock.schedule(graphics, beat=Clock.now()+1/15)
    
graphics()
