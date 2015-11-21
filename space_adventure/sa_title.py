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
        self.image = font_.render(text, 1, (200,200,0))
        self.rect = pygame.Rect(0,0,self.image.get_width(),self.image.get_height())
    
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y-=1
        
        if self.rect.y<=-50:
            self.kill()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def init():
    pygame.display.set_caption("Space Adventure")


def main():
    background = Background("stars.png", (0,0))
    screen.blit(background.image, background.rect)
    pygame.mixer.music.load('starwars.mp3')
    pygame.mixer.music.play(0)

    done = False
    block_group = pygame.sprite.Group()
    intro = ["SPACE ADVENTURE"
             ,"BY"
             ,"SAM SHISSLER"
             ,"SAGE SMITH"
             ,"RYLAND HIGDON"
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,""
             ,"THE NOW INFAMOUS KYLER GNASH HAS"
             ,"THWARTED ANY EFFORTS TO STOP HIM"
             ,"FROM TAKING OVER THE UNIVERSE UNTIL"
             ,"RECENTLY.  THERE HAVE BEEN MANY" 
             ,"ATTEMPTS ON HIS LIFE SINCE HE BEGAN"
             ,"HIS WILD AND RUTHLESS CAMPAIGN FOR"
             ,"UNIVERSAL DOMINATION.  REACHING FOR"
             ,"SUPPORT IN THE MOST ABOMINABLE PARTS"
             ,"OF THE UNIVERSE, HE AMASSED A LARGE"
             ,"ARMY OF VICIOUS THUGS AND UNRELENTING"
             ,"BANDITS DEVOTED TO HIS AGENDA."
             ,""
             ,""
             ,"UPON HIS CAPTURE, GNASH WAS SENTENCED"
             ,"TO CARRY OUT 4580 LIFE SENTANCES"
             ,"HE WAS INJECTED WITH AN IMMORTALITY"
             ,"SERUM TO ALLOW HIS PUNISHMENT TO REACH"
             ,"THE EXTENT OF HIS CRIMES.  AFTER WHICH"
             ,"HE WOULD BE INJECTED WITH THE ANTI-"
             ,"IMMORTALITY SERUM AND DIE INSTANTLY."
             ,""
             ,""
             ,"HAVING HIS PLAN FOR IMMORTALITY"
             ,"FULFILLED, THE CARNIVOROUS GNASH, AS"
             ,"HE IS NOW KNOWN, THEN ESCAPED THE "
             ,"HIGH SECURITY ALIBASTER GALACTIC"
             ,"LOCKDOWN BY BITING OFF THE FINGER OF"
             ,"HIS ONLY GUARD AND MURDERING HIM (BLUNT"
             ,"FORCE TRAUMA TO THE HEAD) WITH THE"
             ,"THUMB.  SOON AFTER HE USED THE THUMB"
             ,"TO OPEN HIS CELL AND HIJACK A CARGO"
             ,"VESSEL.  HE ESCAPED TO A SMALL AND"
             ,"UNINHABITABLE AUTOMATED MINING FACILITY"
             ,"CALLED CAGAU KNOWN FOR AN ABUNDANCE OF"
             ,"CARBON, SILVER AND GOLD."
             ,""
             ,""
             ,"AS THE VESSEL LANDED, THE CARNIVOROUS"
             ,"GNASH DAWNED AN EXO-SUIT AND ONCE SAFELY"
             ,"LANDED, HE STEPPED OUT ONTO THE BARREN"
             ,"SURFACE OF CAGAU, IN SEARCH OF A LONGER"
             ,"RANGE SHIP. "
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
                
        #screen.fill(w)
        screen.blit(background.image, background.rect)
        block_group.update()
        block_group.draw(screen)
        pygame.display.update()
        clock.tick(37)

    pygame.quit()



init()
main()






























