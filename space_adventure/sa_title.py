import pygame
import random
import time
import threading
import thread

pygame.init()

#Init Variable
w = (0,0,0)
clock = pygame.time.Clock()
size = (700,500)
screen = pygame.display.set_mode(size)
screen.fill(w)
font = pygame.font.SysFont("bold", 30)
title = pygame.font.SysFont("bold", 60)

class ScrollingText(pygame.sprite.Sprite):
    def __init__(self,text, font_):
        super(ScrollingText, self).__init__()
        self.image = font_.render(text, 1, (255,255,0))
        self.rect = pygame.Rect(0,0,self.image.get_width(),self.image.get_height())
    
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y-=1
        
        if self.rect.y<=-50:
            self.kill()

def init():
    pygame.display.set_caption("Space Adventure")


def main():
    pygame.mixer.music.load('starwars.mp3')
    pygame.mixer.music.play(0)

    done = False
    block_group = pygame.sprite.Group()
    intro = ["SPACE ADVENTURE"
             , "BY"
             , "SAGE SMITH"
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,"THE INFAMOUS GNASH RIPPER HAS JUST"
             ,"ESCAPED THE HIGH SECURITY ALABASTER"
             ,"GALACTIC LOCKDOWN BY BITING OFF THE"
             ,"THUMB OF HIS GAURD AND MURDERING HIM"
             ,"(BLUNT FORCE TRAUMA TO THE HEAD). HE"
             ,"THEN USED THE THUMB TO OPEN HIS CELL"
             ,"AND HIJACK A CARGO VESSEL. HE ESCAPED"
             ,"TO A SMALL AND UNINHABITED MINING"
             ,"WORLD IN THE GRONKYTE SECTOR."
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""]
    
    for i in range(len(intro)):
        if i == 0:
            s = ScrollingText(intro[i],title)
            s.set_position(screen.get_width()/2-s.rect.width/2, 450+i*50)
            block_group.add(s)

        else:
            s = ScrollingText(intro[i],font)
            s.set_position(screen.get_width()/2-s.rect.width/2, 450+i*50)
            block_group.add(s)

    block_group.draw(screen)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type== pygame.KEYDOWN:
                done = True
                
        screen.fill(w)
        block_group.update()
        block_group.draw(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()



init()
main()






























