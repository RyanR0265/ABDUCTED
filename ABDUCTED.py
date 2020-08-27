import pygame
from gamelib import *

game=Game(700,480,"Game")
pygame.init()

win = pygame.display.set_mode((700,480))
pygame.display.set_caption("Game")

#GRAPHICS___________________________________________________________________________

walkRight = [pygame.image.load('RunFrame1.png'),pygame.image.load('RunFrame2.png'),pygame.image.load('RunFrame3.png'),pygame.image.load('RunFrame4.png'),pygame.image.load('RunFrame5.png'),pygame.image.load('RunFrame6.png'),pygame.image.load('RunFrame7.png'),pygame.image.load('RunFrame1.png'),pygame.image.load('RunFrame2.png'),]
walkLeft = [pygame.image.load('BRunFrame1.png'),pygame.image.load('BRunFrame2.png'),pygame.image.load('BRunFrame3.png'),pygame.image.load('BRunFrame4.png'),pygame.image.load('BRunFrame5.png'),pygame.image.load('BRunFrame6.png'),pygame.image.load('BRunFrame7.png'),pygame.image.load('BRunFrame1.png'),pygame.image.load('BRunFrame2.png'),]

bg =  pygame.image.load('level1.png')
bg = pygame.transform.scale(bg,(700,480))
spacelvl = pygame.image.load("spaceshiplevel.png")
spacelvl = pygame.transform.scale(spacelvl,(700,480))
spacelvl2 = pygame.image.load("spaceshiplevel2.png")
bossroom = pygame.image.load("bossroom.png")
bossroom = pygame.transform.scale(bossroom,(700,480))
endroom = pygame.image.load("endroom.png")
endroom = pygame.transform.scale(endroom,(700,480))
spacelvl2 = pygame.transform.scale(spacelvl2,(700,480))
char = pygame.image.load('StanceFrame.png')
bchar = pygame.image.load('BStanceFrame.png')
shadow = Image("shadow.png",game)
shadow2 = Image("shadow2.png",game)
shadow3 = Image("shadow3.png",game)
shadow4 = Image("shadow4.png",game)
shadow5 = Image("shadow4.png",game)

#INITIALIZING IMAGES___________________________________________________________________________

bk2=Image("bgnight.png",game)
instructions = Image("instructions.png",game)
back=Image("BACK.png",game)
Tutorialtext=Image("instructionsT.png",game)
storybg = Image("storybg.png",game)
storybg2 = Image("storybg.png",game)
storybg3 = Image("storybg.png",game)
usebg = Image("usebg.png",game)
endg = Image("QUIT.png",game)
endg2 = Image("QUIT2.png",game)
play = Image("play.png",game)
lucas = Image("BStanceFrame.png",game)
theend = Image("theend.png",game)
tutbg = Image("tutorialbg.png",game)
trybg = Image("trybg.png",game)
title = Image("TITLE.png",game)
Win = Image("victory.png",game)
Lose = Image("gameover.png",game)
playnext = Image("NEXT.png",game)
playnext2 = Image("NEXT.png",game)
playnext3 = Image("NEXT.png",game)
finish = Image("finish.png",game)
cont = Image("continue.png",game)
usearrow = Image("usearrows.png",game)
useshoot = Image("useshoot.png",game)
goufo = Image("goufo.png",game)
shootalien = Image("shootalien.png",game)
findlucky = Image("findlucky.png",game)
healthpack = Image("health.png",game)
healthpack2 = Image("health.png",game)
healthpack3 = Image("health2.png",game)
lucky = Image("lucky.png",game)
victory = Image("victory.png",game)
defeat = Image("defeat.png",game)
tryagain = Image("tryagain.png",game)
tryagain2 = Image("tryagain.png",game)
tryagain3 = Image("tryagain.png",game)
tryagain4 = Image("tryagain.png",game)
menu = Image("menu.png",game)

lasergunt = Image("lasergunt.png",game)
lasergun = Image("lasergun.png",game)
lgun = Image("lgun.png",game)
blgun = Image("blgun.png",game)

laser = Image("laser2.png",game)
laser2 = Image("laser2.png",game)
laser3 = Image("laser2.png",game)
laser4 = Image("laser2.png",game)
laser5 = Image("laser2.png",game)
laser6 = Image("laser2.png",game)
laser7 = Image("laser2.png",game)
laser8 = Image("laser2.png",game)
laser9 = Image("laser2.png",game)
laser10 = Image("laser2.png",game)
laser11 = Image("laser2.png",game)
laser12 = Image("laser3.png",game)
laser13 = Image("laser3.png",game)
laser14 = Image("laser3.png",game)
laser15 = Image("laser2.png",game)

story1 = Image("story1.png",game)
story2 = Image("story2.png",game)
story3 = Image("story3.png",game)
story4 = Image("story4.png",game)
story5 = Image("story5.png",game)
story6 = Image("story6.png",game)
story1pic = Image("leash.png",game)
face = Image("face.png",game)

alienstand = Image("BAlienFrame2.png",game)
alienstand2 = Image("BAlienFrame2.png",game)
alienstand3 = Image("BAlienFrame2.png",game)
alienstand4 = Image("BAlienFrame2.png",game)


#SOUND_______________________________________________________________________________
titlemusic = pygame.mixer.music.load("titlemusic.mp3")
pygame.mixer.music.play(-1)
clicksound = Sound("clicksound.wav",2)
clank = Sound("clank.wav",3)
bark = Sound("bark.wav",4)
lasersound = Sound("laser.wav",5)
footstep = Sound("footstep.wav",6)
footstep2 = Sound("footstep2.wav",6)
teleport = Sound("teleport.wav",3)
jumpsound = Sound("jump.wav",3)
hitsound = Sound("hitsound.wav",4)
hitsound2 = Sound("hitsound2.wav",1)

#RESIZING AND MOVING ________________________________________________________________

story1.moveTo(story1.x,game.height-400)
story2.moveTo(story1.x,story1.y+70)
story1.resizeBy(-77)
story2.resizeBy(-76)

story3.moveTo(story3.x,game.height-410)
story4.moveTo(story3.x,story3.y+310)
story3.resizeBy(-76)
story4.resizeBy(-76)

story5.moveTo(story5.x,game.height-395)
story6.moveTo(story5.x,story5.y+125)
story5.resizeBy(-77)
story6.resizeBy(-76)

story1pic.resizeBy(150)
story1pic.moveTo(story1pic.x+26,story1pic.y+76)
face.resizeBy(140)
face.moveTo(face.x,face.y-30)

playnext.resizeBy(-40)
playnext.moveTo(game.width-200,game.height-40)
playnext2.resizeBy(-40)
playnext2.moveTo(game.width-80,game.height-40)
playnext3.resizeBy(-40)
playnext3.moveTo(game.width-80,game.height-40)

lgun.resizeBy(-65)
blgun.resizeBy(-65)
lasergunt.resizeBy(150)
lasergunt.moveTo(lasergunt.x-40,lasergunt.y-40)

a = randint(10,440)
b = randint(10,660)

laser.resizeBy(-65)
laser2.resizeBy(-65)
laser3.resizeBy(-65)
laser4.resizeBy(-65)
laser5.resizeBy(-50)
laser6.resizeBy(-50)
laser7.resizeBy(-50)
laser8.resizeBy(-50)
laser9.resizeBy(-60)
laser10.resizeBy(-60)
laser11.resizeBy(-50)
laser12.resizeBy(-50)
laser13.resizeBy(-60)
laser14.resizeBy(-50)
laser15.resizeBy(-50)

lucky.moveTo(500,389)
lucky.resizeBy(30)
shadow.resizeBy(-45)
shadow2.resizeBy(-45)
shadow3.resizeBy(-45)
shadow4.resizeBy(-45)
shadow5.resizeBy(-35)
shadow5.moveTo(lucky.x+43,lucky.y+70)

healthpack.moveTo(healthpack.x,healthpack.y+200)
healthpack2.moveTo(healthpack2.x+200,healthpack2.y-1000)
findlucky.resizeBy(-60)
shootalien.resizeBy(-60)
goufo.resizeBy(-60)
usearrow.resizeBy(-60)
useshoot.resizeBy(-60)
findlucky.moveTo(findlucky.x,findlucky.y-175)
shootalien.moveTo(useshoot.x+230,shootalien.y-180)
usearrow.moveTo(usearrow.x-195,usearrow.y-180)
useshoot.moveTo(usearrow.x+235,useshoot.y-180)
goufo.moveTo(goufo.x,goufo.y-180)

theend.moveTo(theend.x,theend.y-100)
tryagain.moveTo(tryagain.x,tryagain.y+100)
tryagain2.moveTo(tryagain2.x,tryagain2.y+100)
tryagain3.moveTo(tryagain3.x,tryagain3.y+100)
tryagain4.moveTo(tryagain4.x,tryagain4.y+100)
menu.moveTo(menu.x+150,menu.y+200)
victory.moveTo(victory.x,victory.y-100)
defeat.moveTo(victory.x,victory.y-100)
finish.moveTo(finish.x+150,finish.y)
cont.resizeBy(-40)
cont.moveTo(cont.x+150,cont.y)
usebg.resizeTo(650,120)
usebg.moveTo(usebg.x-10,usebg.y-175)
tutbg.resizeTo(700,480)
trybg.resizeTo(700,480)
storybg.resizeTo(700,480)
storybg2.resizeTo(700,480)
storybg3.resizeTo(700,480)
back.resizeBy(-40)
back.moveTo(game.width-100,game.height-45)
back.visible=False
Tutorialtext.visible=False
bk2.resizeTo(700,480)
Tutorialtext.resizeBy(-53)
Tutorialtext.moveTo(game.width-350,game.height-240)
play.resizeBy(-40)
play.y +=138
title.y -=30
instructions.resizeBy(-55)
instructions.moveTo(game.width-600,game.height-20)
endg.moveTo(game.width-50,game.height-20)
endg.resizeBy(-55)

#LASERS_______________________________________________________________________________

#LEVEL2
laser.moveTo(500,300)
laser.setSpeed(15,400)

laser2.moveTo(283,200)
laser2.setSpeed(15,382)

laser3.moveTo(291,230)
laser3.setSpeed(15,710)

laser4.moveTo(145,125)
laser4.setSpeed(15,459)


#LEVEL3
laser5.moveTo(500,300)
laser5.setSpeed(15,400)

laser6.moveTo(283,200)
laser6.setSpeed(15,382)

laser7.moveTo(291,230)
laser7.setSpeed(15,710)

laser8.moveTo(145,125)
laser8.setSpeed(15,459)

#LEVEL4FINAL
laser9.moveTo(672,30)
laser9.setSpeed(15,55)

laser10.moveTo(291,230)
laser10.setSpeed(15,710)

laser11.moveTo(660,470)
laser11.setSpeed(8,90)

laser12.moveTo(150,420)
laser12.setSpeed(20,180)

laser13.moveTo(350,420)
laser13.setSpeed(20,180)

laser14.moveTo(550,420)
laser14.setSpeed(20,180)


#TITLESCREEN___________________________________________________________________________

def titlescreen():
    while not game.over:
        game.processInput()
        tutbg.draw()
        bk2.draw()
        title.draw()
        instructions.draw()
        endg.draw()
        play.draw()
        Tutorialtext.draw()
        back.draw()
    
        if play.collidedWith(mouse) and mouse.LeftClick:
            clicksound.play()
            bark.play()
            game.over = True

        if endg.collidedWith(mouse) and mouse.LeftClick:
            clicksound.play()
            game.quit()

        if instructions.collidedWith(mouse) and mouse.LeftClick:
            title.visible=False
            bk2.visible=False
            play.visible=False
            endg.visible=False
            instructions.visible=False
            back.visible=True
            Tutorialtext.visible=True
            clicksound.play()

        if back.collidedWith(mouse) and mouse.LeftClick:
            bk2.visible=True
            title.visible=True
            play.visible=True
            endg.visible=True
            instructions.visible=True
            back.visible=False
            Tutorialtext.visible=False
            clicksound.play()

        game.update(30)

    game.over = False

#STORY_CUTSCENE____________________________________________________________________

def story():
    while not game.over:

        game.processInput()
        
        storybg2.draw()
        story3.draw()
        story4.draw()
        playnext2.draw()
        lasergunt.draw()
        
        storybg.draw()
        story1pic.draw()
        playnext.draw()
        story1.draw()
        story2.draw()

        if playnext.collidedWith(mouse) and mouse.LeftClick:
            clicksound.play()
            clank.play()
            playnext.visible = False
            story1.visible = False
            story2.visible = False
            story1pic.visible = False
            storybg.visible = False
            lasergunt.visible = True

        if playnext2.collidedWith(mouse) and mouse.LeftClick:
            game.over = True

        game.update(30)

    game.over = False

    while not game.over:

        game.processInput()

        storybg3.draw()
        face.draw()
        story5.draw()
        story6.draw()
        playnext2.draw()

        if playnext2.collidedWith(mouse) and mouse.LeftClick:
            game.over = True

        game.update(30)

    game.over = False

    

#PLAYER________________________________________________________________________________

x= 50
y= 320
width= 40
height= 60
vel= 5

clock = pygame.time.Clock()


isJump = False
jumpCount = 10


left = False
right =  False
walkCount= 0

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.health = 10
        self.standing = True
        self.hitbox = (self.x, self.y-2, 29, 37)
        self.visible = True

        

    def draw(self, win):

        if self.visible:
            if shadow.visible == True:
                shadow.moveTo(man.x+29,430)
            else:
                shadow3.moveTo(man.x+29,481)
        
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if (self.standing):
                lgun.moveTo(man.x+48,man.y+20)
                lgun.visible = True

            if not(self.standing):
                if self.left:
                    lgun.visible = False
                    blgun.visible = True
                    blgun.moveTo(man.x-3,man.y+20)
                    win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1

                elif self.right:
                    lgun.visible = True
                    blgun.visible = False
                    lgun.moveTo(man.x+48,man.y+20)
                    win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount +=1
            else:
                if self.right:
                    lgun.visible = True
                    blgun.visible = False
                    lgun.moveTo(man.x+48,man.y+20)
                    win.blit(char, (self.x, self.y))
                else:
                    lgun.visible = False
                    blgun.visible = True
                    blgun.moveTo(man.x-3,man.y+20)
                    win.blit(bchar, (self.x, self.y))

            pygame.draw.rect(win,(255,0,0), (self.hitbox[0]-6, self.hitbox[1] - 10, 45, 4))
            pygame.draw.rect(win,(0,255,0), (self.hitbox[0]-6, self.hitbox[1] - 10, 45 - (5 * (10 - self.health)), 4))
            self.hitbox = (self.x+6, self.y-2, 33, 53)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)#DRAW HITBOX

    def hit(self):
        self.x = self.x-50
        font1 = pygame.font.SysFont('comicsans',20)
        pygame.display.update()
            
        if self.health > 1:
            self.health -= 2
            hitsound2.play()
        else:
            hitsound2.play()
            self.visible = False
            print('hit')

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        if self.facing == 1:
            pygame.draw.circle(win, (12,247,174), (self.x+37,self.y-14), self.radius-3)
        elif self.facing == -1:
            pygame.draw.circle(win, (12,247,174), (self.x-53,self.y-14), self.radius-3)


#ENEMY____________________________________________________________________________________

class enemy(object):
    walkRight = [pygame.image.load('AlienRunFrame1.png'),pygame.image.load('AlienRunFrame2.png'),pygame.image.load('AlienRunFrame3.png')]
    walkLeft = [pygame.image.load('BAlienFrame1.png'),pygame.image.load('BAlienFrame2.png'),pygame.image.load('BAlienFrame3.png')]
    

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        

    def draw(self,win):
        self.move()
        
        if self.visible:
            if shadow2.visible == True:
                shadow2.moveTo(alien.x+29,433)
            else:
                shadow4.moveTo(alien.x+29,alien.y+65)
                
            if self.walkCount + 1 >= 9:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win,(255,0,0), (self.hitbox[0]-6, self.hitbox[1] - 10, 45, 4))
            pygame.draw.rect(win,(0,255,0), (self.hitbox[0]-6, self.hitbox[1] - 10, 45 - (5 * (10 - self.health)), 4))
            self.hitbox = (self.x+2, self.y, 38, 55)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 1:
            self.health -=1
            hitsound.play()
        else:
            hitsound.play()
            self.visible = False

#ALIEN2___________________________________

class enemy2(object):
    walkRight = [pygame.image.load('2AlienRunFrame1.png'),pygame.image.load('2AlienRunFrame2.png'),pygame.image.load('2AlienRunFrame3.png')]
    walkLeft = [pygame.image.load('2BAlienRunFrame1.png'),pygame.image.load('2BAlienRunFrame2.png'),pygame.image.load('2BAlienRunFrame3.png')]
    

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 15
        self.visible = True
        

    def draw(self,win):
        self.move()
        
        if self.visible:
            if shadow4.visible == True:
                shadow4.moveTo(alien2.x+29,alien2.y+65)
                
            if self.walkCount + 1 >= 9:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win,(255,0,0), (self.hitbox[0]-6, self.hitbox[1] - 10, 60, 6))
            pygame.draw.rect(win,(0,255,0), (self.hitbox[0]-6, self.hitbox[1] - 10, 60 - ( (4) * (15 - self.health) ), 6))
            self.hitbox = (self.x+2, self.y, 38, 55)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 1:
            self.health -=1
            hitsound.play()
        else:
            hitsound.play()
            self.visible = False
        print('hit')

#ALIEN3____________________________________________________
class enemy3(object):
    walkRight = [pygame.image.load('3AlienRunFrame1.png'),pygame.image.load('3AlienRunFrame2.png'),pygame.image.load('3AlienRunFrame3.png')]
    walkLeft = [pygame.image.load('3BAlienRunFrame1.png'),pygame.image.load('3BAlienRunFrame2.png'),pygame.image.load('3BAlienRunFrame3.png')]
    

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x + 17, self.y + 2, 63, 93)
        self.health = 40
        self.visible = True
        

    def draw(self,win):
        self.move()
        
        if self.visible:
            if shadow2.visible == True:
                shadow2.moveTo(alien3.x+29,433)
            else:
                shadow4.moveTo(alien3.x+29,490)
                
            if self.walkCount + 1 >= 9:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win,(255,0,0), (self.hitbox[0]-6, self.hitbox[1] - 10, 80, 8))
            pygame.draw.rect(win,(0,255,0), (self.hitbox[0]-6, self.hitbox[1] - 10, 80 - (2 * (40 - self.health)), 8))
            self.hitbox = (self.x+2, self.y, 63, 93)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 1:
            self.health -=1
            hitsound.play()
        else:
            hitsound.play()
            self.visible = False
        print('hit')

#LEVELS_____________________________________________________________________
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    alien.draw(win)
    usebg.draw()
    usearrow.draw()
    useshoot.draw()
    shootalien.draw()
    trybg.draw()
    trybg.visible = False
    defeat.draw()
    defeat.visible = False
    endg2.draw()
    endg2.visible = False

    if alien.visible == False:
        usearrow.visible = False
        useshoot.visible = False
        shootalien.visible = False
        usebg.resizeTo(250,100)
        usebg.moveTo(usebg.x,65)
        goufo.draw()
       
    for bullet in bullets:
        bullet.draw(win)

    
    pygame.display.update()

def Level2draw():
    win.blit(spacelvl, (0,0))
    man.draw(win)
    alien.draw(win)
    aliencopy.draw(win)
    aliencopy2.draw(win)
    laser.draw()
    laser.move(True)
    laser2.draw()
    laser2.move(True)
    laser3.draw()
    laser3.move(True)
    laser4.draw()
    laser4.move(True)
    cont.draw()
    cont.visible = False
    trybg.draw()
    trybg.visible = False
    defeat.draw()
    defeat.visible = False
    endg2.draw()
    endg2.visible = False
    #usebg.draw()
    #usebg.resizeTo(250,100)
    #usebg.moveTo(usebg.x,65)
    #findlucky.draw()
       
    for bullet in bullets:
        bullet.draw(win)

    
    pygame.display.update()

def Level3draw():
    win.blit(spacelvl2, (0,0))
    healthpack.draw()
    healthpack2.draw()
    man.draw(win)
    alien2.draw(win)
    alien2copy.draw(win)
    laser5.draw()
    laser5.move(True)
    laser6.draw()
    laser6.move(True)
    laser7.draw()
    laser7.move(True)
    laser8.draw()
    laser8.move(True)
    cont.draw()
    cont.visible = False
    trybg.draw()
    trybg.visible = False
    defeat.draw()
    defeat.visible = False
    endg2.draw()
    endg2.visible = False
    
       
    for bullet in bullets:
        bullet.draw(win)

    
    pygame.display.update()

def Level4draw():
    win.blit(bossroom, (0,0))
    healthpack.draw()
    finish.draw()
    healthpack3.draw()
    man.draw(win)
    alien3.draw(win)
    laser9.draw()
    laser9.move(True)
    laser10.draw()
    laser10.move(True)
    laser11.draw()
    laser11.move(True)
    laser12.draw()
    laser12.move(True)
    laser13.draw()
    laser13.move(True)
    laser14.draw()
    laser14.move(True)
    finish.visible = False
    trybg.draw()
    trybg.visible = False
    defeat.draw()
    defeat.visible = False
    endg2.draw()
    endg2.visible = False
    
       
    for bullet in bullets:
        bullet.draw(win)

    
    pygame.display.update()

def Level5draw():

    win.blit(endroom, (0,0))
    man.draw(win)
    victory.draw()
    shadow5.draw()
    lucky.draw()

    pygame.display.update()

#MAIN LOOP___________________________________________________________________________________
def level1():
    while not game.over:
        game.processInput()

        clock.tick(33)

        shootLoop = 0

        if man.visible == False:
            trybg.visible = True
            defeat.visible = True
            endg2.visible = True

        if endg2.visible == True and endg2.collidedWith(mouse) and mouse.LeftClick:
            pygame.quit()

        if man.hitbox[1] < alien.hitbox[1] + alien.hitbox[3] and man.hitbox[1] + man.hitbox[3] > alien.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > alien.hitbox[0] and man.hitbox[0] < alien.hitbox[0] + alien.hitbox[2]:
                if man.visible and alien.visible:
                    man.hit()
                    

        if shootLoop > 0:
            shootLoop +=1
        if shootLoop >3:
            shootLoop = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.over = True

        for bullet in bullets:
            if bullet.y - bullet.radius < alien.hitbox[1] + alien.hitbox[3] and bullet.y + bullet.radius > alien.hitbox[1]:
                if bullet.x+53 + bullet.radius > alien.hitbox[0]and bullet.x+53 - bullet.radius < alien.hitbox[0] + alien.hitbox[2]:
                    if alien.visible:
                        alien.hit()
                        bullets.pop(bullets.index(bullet))

            if bullet.x < 700 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:
            if man.left:
                lasersound.play()
                facing = -1
            else:
                lasersound.play()
                facing = 1
            
            if len(bullets) < 4:
                bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

            shootLoop = 1

        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            footstep.play()
            man.left = True
            man.right = False
            man.standing = False
        
        elif keys[pygame.K_RIGHT] and man.x < 700 - man.width - man.vel: 
            man.x += man.vel
            footstep.play()
            man.right = True
            man.left = False
            man.standing = False
        
        else:
            man.standing = True
            man.walkCount = 0
        
        if not(man.isJump):
            if keys[pygame.K_UP] and man.left:
                jumpsound.play()
                man.isJump = True
                man.left = True
                man.right = False
                man.walkCount = 0
            elif keys[pygame.K_UP] and man.right:
                jumpsound.play()
                man.isJump = True
                man.left = False
                man.right = True
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) //4 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        if man.x > 570 and alien.visible == False:
            game.over = True
            teleport.play()
            man.x = 50
            man.y = 369
        
        redrawGameWindow()

    game.over=False

if tryagain.collidedWith(mouse) and mouse.LeftClick:
    print('hello')
    titlescreen()

#LEVEL2________________________________________________________________________________
def level2():
    while not game.over:
        game.processInput()

        clock.tick(33)

        shootLoop = 0

        if man.visible == False:
            trybg.visible = True
            defeat.visible = True
            endg2.visible = True

        if endg2.visible == True and endg2.collidedWith(mouse) and mouse.LeftClick:
            pygame.quit()


        if man.hitbox[1] < laser.y + laser.height and man.hitbox[1] + man.hitbox[3] > laser.y:
            if man.hitbox[0] + man.hitbox[2] > laser.x and man.hitbox[0] < laser.x + laser.width:
                if man.visible and laser.visible:
                    laser.y = laser.y - 40
                    man.hit()
                    man.x = man.x - 30
                    

        if man.hitbox[1] < laser2.y + laser2.height and man.hitbox[1] + man.hitbox[3] > laser2.y:
            if man.hitbox[0] + man.hitbox[2] > laser2.x and man.hitbox[0] < laser2.x + laser2.width:
                if man.visible and laser2.visible:
                    laser2.y = laser2.y - 40
                    man.hit()
                    

        if man.hitbox[1] < laser3.y + laser3.height and man.hitbox[1] + man.hitbox[3] > laser3.y:
            if man.hitbox[0] + man.hitbox[2] > laser3.x and man.hitbox[0] < laser3.x + laser3.width:
                if man.visible and laser3.visible:
                    laser3.y = laser3.y - 40
                    man.hit()

        if man.hitbox[1] < laser4.y + laser4.height and man.hitbox[1] + man.hitbox[3] > laser4.y:
            if man.hitbox[0] + man.hitbox[2] > laser4.x and man.hitbox[0] < laser4.x + laser4.width:
                if man.visible and laser4.visible:
                    laser4.y = laser4.y - 40
                    man.hit()
                        

        if man.hitbox[1] < alien.hitbox[1] + alien.hitbox[3] and man.hitbox[1] + man.hitbox[3] > alien.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > alien.hitbox[0] and man.hitbox[0] < alien.hitbox[0] + alien.hitbox[2]:
                if man.visible and alien.visible:
                    man.hit()
                    

        if man.hitbox[1] < aliencopy.hitbox[1] + aliencopy.hitbox[3] and man.hitbox[1] + man.hitbox[3] > aliencopy.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > aliencopy.hitbox[0] and man.hitbox[0] < aliencopy.hitbox[0] + aliencopy.hitbox[2]:
                if man.visible and aliencopy.visible:
                    man.hit()
                    

        if man.hitbox[1] < aliencopy2.hitbox[1] + aliencopy2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > aliencopy2.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > aliencopy2.hitbox[0] and man.hitbox[0] < aliencopy2.hitbox[0] + aliencopy2.hitbox[2]:
                if man.visible and aliencopy2.visible:
                    man.hit()
                    

        shadow.visible = False
        shadow2.visible = False

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.over = True

        for bullet in bullets:

            if bullet.x < 700 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
            
            
            if bullet.y - bullet.radius < alien.hitbox[1] + alien.hitbox[3] and bullet.y + bullet.radius > alien.hitbox[1]:
                if bullet.x+53 + bullet.radius > alien.hitbox[0]and bullet.x+53 - bullet.radius < alien.hitbox[0] + alien.hitbox[2]:
                    if alien.visible:
                        alien.hit()
                        bullets.pop(bullets.index(bullet))
                        
            if bullet.y - bullet.radius < aliencopy.hitbox[1] + aliencopy.hitbox[3] and bullet.y + bullet.radius > aliencopy.hitbox[1]:
                if bullet.x+53 + bullet.radius > aliencopy.hitbox[0]and bullet.x+53 - bullet.radius < aliencopy.hitbox[0] + aliencopy.hitbox[2]:
                    if aliencopy.visible:
                        aliencopy.hit()
                        bullets.pop(bullets.index(bullet))

            if bullet.y - bullet.radius < aliencopy2.hitbox[1] + aliencopy2.hitbox[3] and bullet.y + bullet.radius > aliencopy2.hitbox[1]:
                if bullet.x+53 + bullet.radius > aliencopy2.hitbox[0]and bullet.x+53 - bullet.radius < aliencopy2.hitbox[0] + aliencopy2.hitbox[2]:
                    if aliencopy2.visible:
                        aliencopy2.hit()
                        bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0 and man.visible:
            if man.left:
                lasersound.play()
                facing = -1
            else:
                lasersound.play()
                facing = 1
                
            if len(bullets) < 4:
                bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

            shootLoop = 1

        if keys[pygame.K_LEFT] and man.x > man.vel and man.visible:
            man.x -= man.vel
            footstep2.play()
            man.left = True
            man.right = False
            man.standing = False
            
        elif keys[pygame.K_RIGHT] and man.x < 700 - man.width - man.vel and man.visible: 
            man.x += man.vel
            footstep2.play()
            man.right = True
            man.left = False
            man.standing = False
            
        else:
            man.standing = True
            man.walkCount = 0
            
        if not(man.isJump) and man.visible:
            if keys[pygame.K_UP] and man.left:
                jumpsound.play()
                man.isJump = True
                man.left = True
                man.right = False
                man.walkCount = 0
            elif keys[pygame.K_UP] and man.right and man.visible:
                jumpsound.play()
                man.isJump = True
                man.left = False
                man.right = True
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) //4 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        if alien.visible == False and aliencopy.visible == False and aliencopy2.visible == False:
            cont.visible = True
            laser.visible = False
            laser2.visible = False
            laser3.visible = False
            laser4.visible = False

        if man.x > 590 and alien.visible == False and aliencopy.visible == False and aliencopy2.visible == False:
            game.over = True

        Level2draw()

    game.over = False

#LEVEL3_____________________________________________________________________________
def level3():
    while not game.over:
        game.processInput()
    
        clock.tick(33)

        if man.visible == False:
            trybg.visible = True
            defeat.visible = True
            endg2.visible = True

        if endg2.visible == True and endg2.collidedWith(mouse) and mouse.LeftClick:
            pygame.quit()

        shootLoop = 0

        if man.hitbox[1] < laser5.y + laser5.height and man.hitbox[1] + man.hitbox[3] > laser5.y:
            if man.hitbox[0] + man.hitbox[2] > laser5.x and man.hitbox[0] < laser5.x + laser.width:
                if man.visible and laser5.visible:
                    laser5.y = laser5.y - 40
                    man.hit()
                    man.x = man.x - 30
                    

        if man.hitbox[1] < laser6.y + laser6.height and man.hitbox[1] + man.hitbox[3] > laser6.y:
            if man.hitbox[0] + man.hitbox[2] > laser6.x and man.hitbox[0] < laser6.x + laser6.width:
                if man.visible and laser6.visible:
                    laser6.y = laser6.y - 40
                    man.hit()
                    

        if man.hitbox[1] < laser7.y + laser7.height and man.hitbox[1] + man.hitbox[3] > laser7.y:
            if man.hitbox[0] + man.hitbox[2] > laser7.x and man.hitbox[0] < laser7.x + laser7.width:
                if man.visible and laser7.visible:
                    laser7.y = laser7.y - 40
                    man.hit()
                    

        if man.hitbox[1] < laser8.y + laser8.height and man.hitbox[1] + man.hitbox[3] > laser8.y:
            if man.hitbox[0] + man.hitbox[2] > laser8.x and man.hitbox[0] < laser8.x + laser8.width:
                if man.visible and laser8.visible:
                    laser8.y = laser8.y - 40
                    man.hit()
                            

        if man.hitbox[1] < alien2.hitbox[1] + alien2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > alien2.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > alien2.hitbox[0] and man.hitbox[0] < alien2.hitbox[0] + alien2.hitbox[2]:
                if man.visible and alien2.visible:
                    man.hit()
                    

        if man.hitbox[1] < alien2copy.hitbox[1] + alien2copy.hitbox[3] and man.hitbox[1] + man.hitbox[3] > alien2copy.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > alien2copy.hitbox[0] and man.hitbox[0] < alien2copy.hitbox[0] + alien2copy.hitbox[2]:
                if man.visible and alien2copy.visible:
                    man.hit()
                    

        if man.hitbox[1] < healthpack.y + healthpack.height and man.hitbox[1] + man.hitbox[3] > healthpack.y:
            if man.hitbox[0] + man.hitbox[2] > healthpack.x and man.hitbox[0] < healthpack.x + healthpack.width:
                if man.visible and healthpack.visible:
                    man.health+=4
                    healthpack.visible = False
                    if man.health >10:
                        man.health = 10
        

        shadow.visible = False
        shadow2.visible = False

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.over = True

        for bullet in bullets:

            if bullet.x < 700 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
            
            
            if bullet.y - bullet.radius < alien2.hitbox[1] + alien2.hitbox[3] and bullet.y + bullet.radius > alien2.hitbox[1]:
                if bullet.x+53 + bullet.radius > alien2.hitbox[0]and bullet.x+53 - bullet.radius < alien2.hitbox[0] + alien2.hitbox[2]:
                    if alien2.visible:
                        alien2.hit()
                        bullets.pop(bullets.index(bullet))
                        
            if bullet.y - bullet.radius < alien2copy.hitbox[1] + alien2copy.hitbox[3] and bullet.y + bullet.radius > alien2copy.hitbox[1]:
                if bullet.x+53 + bullet.radius > alien2copy.hitbox[0]and bullet.x+53 - bullet.radius < alien2copy.hitbox[0] + alien2copy.hitbox[2]:
                    if alien2copy.visible:
                        alien2copy.hit()
                        bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0 and man.visible:
            if man.left:
                lasersound.play()
                facing = -1
            else:
                lasersound.play()
                facing = 1
                
            if len(bullets) < 4:
                bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

            shootLoop = 1

        if keys[pygame.K_LEFT] and man.x > man.vel and man.visible:
            man.x -= man.vel
            footstep2.play()
            man.left = True
            man.right = False
            man.standing = False
            
        elif keys[pygame.K_RIGHT] and man.x < 700 - man.width - man.vel and man.visible: 
            man.x += man.vel
            footstep2.play()
            man.right = True
            man.left = False
            man.standing = False
            
        else:
            man.standing = True
            man.walkCount = 0
            
        if not(man.isJump):
            if keys[pygame.K_UP] and man.left and man.visible:
                jumpsound.play()
                man.isJump = True
                man.left = True
                man.right = False
                man.walkCount = 0
            elif keys[pygame.K_UP] and man.right and man.visible:
                jumpsound.play()
                man.isJump = True
                man.left = False
                man.right = True
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) //4 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        if alien2.visible == False and alien2copy.visible == False:
            cont.visible = True
            laser5.visible = False
            laser6.visible = False
            laser7.visible = False
            laser8.visible = False
            healthpack2.moveTo(500,400)

            if man.hitbox[1] < healthpack2.y + healthpack2.height and man.hitbox[1] + man.hitbox[3] > healthpack2.y:
                if man.hitbox[0] + man.hitbox[2] > healthpack2.x and man.hitbox[0] < healthpack2.x + healthpack2.width:
                    if man.visible:
                        man.health+=4
                        healthpack2.visible = False
                        if man.health >10:
                            man.health = 10

        if man.x > 590 and alien2.visible == False and alien2copy.visible == False:
            game.over = True
        
        

        Level3draw()

    game.over = False

#FINALLEVEL BOSS__________________________________________________________________________
def level4():
    while not game.over:
        game.processInput()

        clock.tick(33)

        if man.visible == False:
            trybg.visible = True
            defeat.visible = True
            endg2.visible = True

        if endg2.visible == True and endg2.collidedWith(mouse) and mouse.LeftClick:
            pygame.quit()
        
        shootLoop = 0

        if man.hitbox[1] < laser9.y + laser9.height and man.hitbox[1] + man.hitbox[3] > laser9.y:
            if man.hitbox[0] + man.hitbox[2] > laser9.x and man.hitbox[0] < laser9.x + laser9.width:
                if man.visible and laser9.visible:
                    laser9.y = laser9.y -40
                    man.hit()
                    man.health-=1
                    man.x = man.x - 30
                    

                    laser9.x = laser.x + 400
                    if laser9.x > 650:
                        laser9.x = 650

        if man.hitbox[1] < laser10.y + laser10.height and man.hitbox[1] + man.hitbox[3] > laser10.y:
            if man.hitbox[0] + man.hitbox[2] > laser10.x and man.hitbox[0] < laser10.x + laser10.width:
                if man.visible and laser10.visible:
                    laser10.y = laser10.y - 40
                    man.hit()
                    man.health-=1
                    

        if man.hitbox[1] < laser11.y + laser11.height and man.hitbox[1] + man.hitbox[3] > laser11.y:
            if man.hitbox[0] + man.hitbox[2] > laser11.x and man.hitbox[0] < laser11.x + laser11.width:
                if man.visible and laser11.visible:
                    man.hit()
                    man.health-=1
                    

        if man.hitbox[1] < laser12.y + laser12.height and man.hitbox[1] + man.hitbox[3] > laser12.y:
            if man.hitbox[0] + man.hitbox[2] > laser12.x and man.hitbox[0] < laser12.x + laser12.width:
                if man.visible and laser12.visible:
                    laser12.y = laser12.y - 40
                    man.hit()
                    man.health-=1
                    

        if man.hitbox[1] < laser13.y + laser13.height and man.hitbox[1] + man.hitbox[3] > laser13.y:
            if man.hitbox[0] + man.hitbox[2] > laser13.x and man.hitbox[0] < laser13.x + laser13.width:
                if man.visible and laser13.visible:
                    laser13.y = laser13.y - 40
                    man.hit()
                    man.health-=1
                    

        if man.hitbox[1] < laser14.y + laser14.height and man.hitbox[1] + man.hitbox[3] > laser14.y:
            if man.hitbox[0] + man.hitbox[2] > laser14.x and man.hitbox[0] < laser14.x + laser14.width:
                if man.visible and laser14.visible:
                    laser14.y = laser14.y - 40
                    man.hit()
                    man.health-=1
                    
        

        if man.hitbox[1] < alien3.hitbox[1] + alien3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > alien3.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > alien3.hitbox[0] and man.hitbox[0] < alien3.hitbox[0] + alien3.hitbox[2]:
                if man.visible and alien3.visible:
                    man.hit()
                    man.health-=5
                    

        if healthpack.visible:
            if man.hitbox[1] < healthpack.y + healthpack.height and man.hitbox[1] + man.hitbox[3] > healthpack.y:
                if man.hitbox[0] + man.hitbox[2] > healthpack.x and man.hitbox[0] < healthpack.x + healthpack.width:
                    if man.visible:
                        man.health+=4
                        healthpack.visible = False
                        if man.health >10:
                            man.health = 10

        if healthpack3.visible:
            if man.hitbox[1] < healthpack3.y + healthpack3.height and man.hitbox[1] + man.hitbox[3] > healthpack3.y:
                if man.hitbox[0] + man.hitbox[2] > healthpack3.x and man.hitbox[0] < healthpack3.x + healthpack3.width:
                    if man.visible:
                        man.health+=10
                        healthpack3.visible = False
                        if man.health >10:
                            man.health = 10
        

        shadow.visible = False
        shadow2.visible = False

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.over = True

        for bullet in bullets:

            if bullet.x < 700 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
            
            
            if bullet.y - bullet.radius < alien3.hitbox[1] + alien3.hitbox[3] and bullet.y + bullet.radius > alien3.hitbox[1]:
                if bullet.x+53 + bullet.radius > alien3.hitbox[0]and bullet.x+53 - bullet.radius < alien3.hitbox[0] + alien3.hitbox[2]:
                    if alien3.visible:
                        alien3.hit()
                        bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0 and man.visible:
            if man.left:
                lasersound.play()
                facing = -1
            else:
                lasersound.play()
                facing = 1
                
            if len(bullets) < 5:
                bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

            shootLoop = 1

        if keys[pygame.K_LEFT] and man.x > man.vel and man.visible:
            man.x -= man.vel
            footstep2.play()
            man.left = True
            man.right = False
            man.standing = False
            
        elif keys[pygame.K_RIGHT] and man.x < 700 - man.width - man.vel and man.visible: 
            man.x += man.vel
            footstep2.play()
            man.right = True
            man.left = False
            man.standing = False
            
        else:
            man.standing = True
            man.walkCount = 0
            
        if not(man.isJump):
            if keys[pygame.K_UP] and man.left and man.visible:
                jumpsound.play()
                man.isJump = True
                man.left = True
                man.right = False
                man.walkCount = 0
            elif keys[pygame.K_UP] and man.right and man.visible:
                jumpsound.play()
                man.isJump = True
                man.left = False
                man.right = True
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) //4 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        if alien3.visible == False:
            laser9.visible = False
            laser10.visible = False
            laser11.visible = False
            laser12.visible = False
            laser13.visible = False
            laser14.visible = False
            finish.visible = True
            
        if man.x > 590 and alien3.visible == False:
            game.over = True

        Level4draw()

    game.over = False

#ENDING SCENE____________________________________________________________________
def level5():
    while not game.over:
        clock.tick(33)
        game.processInput()

        blgun.visible = False
        lgun.visible = False
        shadow.visible = True
        shadow3.visible = False                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.over = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and man.x > man.vel and man.visible:
            man.x -= man.vel
            footstep2.play()
            man.left = True
            man.right = False
            man.standing = False
            
        elif keys[pygame.K_RIGHT] and man.x < 700 - man.width - man.vel and man.visible: 
            man.x += man.vel
            footstep2.play()
            man.right = True
            man.left = False
            man.standing = False
            
        else:
            man.standing = True
            man.walkCount = 0
            
        if not(man.isJump):
            if keys[pygame.K_UP] and man.left and man.visible:
                jumpsound.play()
                man.isJump = True
                man.left = True
                man.right = False
                man.walkCount = 0
            elif keys[pygame.K_UP] and man.right and man.visible:
                jumpsound.play()
                man.isJump = True
                man.left = False
                man.right = True
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) //4 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        if man.x > 450:
            game.over = True
        

        Level5draw()

    game.over = False

#ENDSTORY

lucas.moveTo(500,420)
lucky.moveTo(540,410)

def level6():
    while not game.over:
        game.processInput()

        bk2.draw()
        lucky.draw()
        lucas.draw()
        theend.draw()
        endg.draw()

        

        if endg.collidedWith(mouse) and mouse.LeftClick:
            pygame.quit()
        
        
        game.update(30)
#_________________________________________________________________________________

titlescreen()
story()

man = player(50, 369, 64,64)
alien = enemy(300, 369, 64, 64, 650)
bullets = []

level1()

shadow3.draw()
shadow4.draw()
man = player(50, 420, 64,64)
alien = enemy(300, 415, 64, 64, 655)
aliencopy = enemy(265, 420, 64, 64, 660)
aliencopy2 = enemy(150, 410, 64, 64, 680)
bullets = []


level2()

alien2copy = enemy2(120, 420, 64, 64, 650)
alien2 = enemy2(200, 360, 64, 64, 650)
man.x = 50


level3()

alien3 = enemy3(330, 360, 64, 64, 650)
man.x = 30
healthpack.x = 150
healthpack3.moveTo(250,450)
healthpack.visible = True
healthpack3.visible = True


level4()

man.x = 50
man.y = 369

level5()

lucas.moveTo(500,420)
lucky.moveTo(520,380)

level6()
    
pygame.quit()

