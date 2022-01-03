import pygame
import sys


# from pygame.locals import *

cellsize = 10
deadColor = (255, 255, 255)
liveColor = (0, 0, 255)
sliderwidth = 100

def getPixelLife(frame, x, y):
    w, h = frame.get_size()
    if x<0 or x>=w or y<0 or y>=h:
        return 0
    if frame.get_at((x, y)) == liveColor:
        return 1
    return 0

def countNeighbours(frame, x, y):
    count = 0
    count += getPixelLife(frame,x-cellsize,y-cellsize)
    count += getPixelLife(frame,x,y-cellsize)
    count += getPixelLife(frame,x+cellsize,y-cellsize)
    count += getPixelLife(frame,x+cellsize,y)
    count += getPixelLife(frame,x+cellsize,y+cellsize)
    count += getPixelLife(frame,x,y+cellsize)
    count += getPixelLife(frame,x-cellsize,y+cellsize)
    count += getPixelLife(frame,x-cellsize,y)
    return count


def doNextFrame(frame):
    w, h = frame.get_size()

    newframe = pygame.Surface((w,h))
    newframe.fill((255,255,255))

    x = 0
    while x < w:
        y = 0
        while y < h:
            count = countNeighbours(frame,x,y)
            if count < 2:
                pygame.draw.rect(newframe, deadColor, (x, y, cellsize, cellsize))
            elif count == 2:
                if getPixelLife(frame,x,y)  == 0:
                    pygame.draw.rect(newframe, deadColor, (x, y, cellsize, cellsize))
                else:
                    pygame.draw.rect(newframe, liveColor, (x, y, cellsize, cellsize))
            elif count == 3:
                pygame.draw.rect(newframe, liveColor, (x, y, cellsize, cellsize))
            elif count > 4:
                pygame.draw.rect(newframe, deadColor, (x, y, cellsize, cellsize))
            y+=cellsize
        x+=cellsize

    return newframe

def isOverRect(x,y,rect):
    return rect[0] < x < rect[0] + rect[2] and rect[1] < y < rect[1] + rect[3]


def closestOnGrid(cellsize, x, y):
    return x - x % cellsize, y - y % cellsize;

def drawStart(screen, glidergun = False):
    screen.fill((255,255,255))
    font = pygame.font.SysFont('arial', 30)
    textsurface = font.render('Cellular Automata', True, (0, 0, 0))
    screen.blit(textsurface, (10, 0))
    font = pygame.font.SysFont('arial', 10)
    textsurface = font.render('por Tito Guidotti', True, (0, 0, 0))
    screen.blit(textsurface, (50, 30))

    w, h = pygame.display.get_surface().get_size()

    # playground
    border = 2
    playwidth = w - w%10 -20
    playheight = h - h%10 - 60
    pygame.draw.rect(screen, (0,0,0), (10 - border, 50-border,playwidth+border*2, playheight+border*2))
    pygame.draw.rect(screen, (255,255,255), (10, 50,playwidth, playheight))

    if glidergun:
        surface = pygame.Surface((playwidth, playheight))
        surface.fill((255,255,255))
        pygame.draw.rect(surface, liveColor, (10, 50, cellsize*2, cellsize*2))
        pygame.draw.rect(surface, liveColor, (110, 50, cellsize, cellsize*3))
        pygame.draw.rect(surface, liveColor, (120, 40, cellsize, cellsize))
        pygame.draw.rect(surface, liveColor, (120, 80, cellsize, cellsize))
        pygame.draw.rect(surface, liveColor, (130, 30, cellsize*2, cellsize))
        pygame.draw.rect(surface, liveColor, (130, 90, cellsize*2, cellsize))
        pygame.draw.rect(surface, liveColor, (150, 60, cellsize, cellsize))
        pygame.draw.rect(surface, liveColor, (160, 40, cellsize, cellsize))
        pygame.draw.rect(surface, liveColor, (160, 80, cellsize, cellsize))
        pygame.draw.rect(surface, liveColor, (170, 50, cellsize, cellsize*3))
        pygame.draw.rect(surface, liveColor, (180, 60, cellsize, cellsize))
        pygame.draw.rect(surface, liveColor, (210, 30, cellsize*2, cellsize*3))
        pygame.draw.rect(surface, liveColor, (230, 20, cellsize, cellsize))
        pygame.draw.rect(surface, liveColor, (230, 60, cellsize, cellsize))
        pygame.draw.rect(surface, liveColor, (250, 10, cellsize, cellsize*2))
        pygame.draw.rect(surface, liveColor, (250, 60, cellsize, cellsize*2))
        pygame.draw.rect(surface, liveColor, (350, 30, cellsize*2, cellsize*2))

        screen.blit(surface, (10, 50))

    return (10, 50,playwidth, playheight), drawButton(screen, (0, 255, 0)), drawSlider(screen, 0.5)


def drawButton(screen, color, text='iniciar'):
    w, h = pygame.display.get_surface().get_size()
    border = 1
    pygame.draw.rect(screen, (0, 0, 0), (268, 15, 55, 22))
    pygame.draw.rect(screen, color, (268 + border, 15 + border, 55 - border * 2, 22 - border * 2))
    font = pygame.font.SysFont('arial', 20)
    textsurface = font.render(text, True, (0, 0, 0))
    screen.blit(textsurface, (270, 13))

    # pygame.draw.rect(screen, (255, 255, 255), (10 + border, 50 + border, w - 20 - (2 * border), h - 60 - (2 * border)))

    return (268, 15, 55, 22)

def drawSlider(screen, startingValue):

    pygame.draw.rect(screen, (255,255,255), (325,0, sliderwidth + 40, 40))
    pygame.draw.rect(screen, (0, 0, 0), (340,27, sliderwidth, 4))

    pygame.draw.rect(screen, (0, 0, 0), (330 + startingValue*sliderwidth, 18, 20, 22))
    pygame.draw.rect(screen, (100, 100, 100), (331 + startingValue*sliderwidth, 19, 18, 20))
    pygame.draw.rect(screen, (50, 50, 50), (335 + startingValue*sliderwidth, 21, 1, 16))
    pygame.draw.rect(screen, (50, 50, 50), (343 + startingValue*sliderwidth, 21, 1, 16))


    font = pygame.font.SysFont('arial', 13)
    textsurface = font.render('velocidade', True, (0, 0, 0))
    screen.blit(textsurface, (350, 4))

    return (340,16, sliderwidth, 25)


def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

    playrect, buttonrect, sliderrect = drawStart(screen, True)

    leftmouse = False
    rightmouse = False

    simActive = False

    lasttime = pygame.time.get_ticks()

    minimunTimeGap = 1000 * pow(0.5, 2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                print("resize")
                playrect, buttonrect, sliderrect = drawStart(screen)
                simActive = False
            elif event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                if isOverRect(x,y,buttonrect):
                    if simActive:
                        buttonrect = drawButton(screen,(240,0,0), 'parar')
                    else:
                        buttonrect = drawButton(screen,(0,240,0))

                else:
                    if simActive:
                        buttonrect = drawButton(screen, (255, 0, 0), 'parar')
                    else:
                        buttonrect = drawButton(screen, (0, 255, 0))
                if isOverRect(x,y,sliderrect):
                    if leftmouse:
                        slidevalue = (x - sliderrect[0])/sliderwidth
                        sliderrect = drawSlider(screen, slidevalue)
                        minimunTimeGap = 1000* pow(1-slidevalue, 2)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    leftmouse = True
                if event.button == 3:
                    rightmouse = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    leftmouse = False
                    x, y = pygame.mouse.get_pos()
                    if isOverRect(x,y,buttonrect):
                        simActive = not simActive
                        if simActive:
                            buttonrect = drawButton(screen, (255, 0, 0), 'parar')

                        else:
                            buttonrect = drawButton(screen, (0, 255, 0))
                if event.button == 3:
                    rightmouse = False

        if simActive:
            currenttime = pygame.time.get_ticks()
            if currenttime - lasttime > minimunTimeGap:
                lasttime = currenttime
                cropped = pygame.Surface((playrect[2], playrect[3]))
                cropped.blit(screen, (0, 0), playrect)
                screen.blit(doNextFrame(cropped), (playrect[0],playrect[1]))
            pygame.display.update()
        else:
            x, y = pygame.mouse.get_pos()
            if isOverRect(x, y, playrect):
                    x, y = closestOnGrid(cellsize, x, y)
                    if rightmouse:
                        pygame.draw.rect(screen, deadColor, (x, y, cellsize, cellsize))
                    elif leftmouse:
                        pygame.draw.rect(screen, liveColor, (x, y, cellsize, cellsize))
            pygame.display.update()



main()
