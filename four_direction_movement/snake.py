try:
    import pygame
    pygame.init()
except:
    print("----<error>-----\nSomething wrong with pygame\nPlz run with Python 3 and make sure pygame is installed")
    input()
    exit()
a = False

try:
    import random
    a = True
except:
    print("----<error>-----\nProblem with imported modules\nModules|Imported\nRandom |"+str(a)+"Please fix")
class vr:
    gw = 16
    gh = 16
    pxl = 32
    sw = 0
    sh = 0
    points = 0
    coloroffset = 4


    done = False
vr.sw = vr.gw*vr.pxl
vr.sh = vr.gh*vr.pxl
#setup
clock = pygame.time.Clock()
screen = pygame.display.set_mode((vr.sw, vr.sh))
#pressed = pygame.key.get_pressed()
c = 0;
class apple:
    x = 1
    y = 1
    lvl = 0
    
class snake:
    ##x first then y
    leng = 4
    x = 5
    y = 16
    dire = 1
    speed = 60
    tailx = []
    taily = []
class gamef:
    def grid():
        ty = False
        for x in range(int(vr.sw/vr.pxl)):
            for y in range(int(vr.sh/vr.pxl)):
                of = 0
                if (y%2)==0:
                    of = 1
                if (((x+of)%2)==0):
                    pygame.draw.rect(screen, (32,32,32),pygame.Rect(x*vr.pxl,y*vr.pxl,vr.pxl,vr.pxl))
                    
                else:
                    pygame.draw.rect(screen, (64,64,64),pygame.Rect(x*vr.pxl,y*vr.pxl,vr.pxl,vr.pxl))
                ty = not ty
            
    def draw():
        #Framerate of 10
        pygame.draw.rect(screen, (128,128,128),pygame.Rect(0,0,vr.pxl,vr.sh))
        pygame.draw.rect(screen, (128,128,128),pygame.Rect(vr.sw-vr.pxl,0,vr.pxl,vr.sh))
        pygame.draw.rect(screen, (128,128,128),pygame.Rect(0,0,vr.sw,vr.pxl))
        pygame.draw.rect(screen, (128,128,128),pygame.Rect(0,vr.sh-vr.pxl,vr.sw,vr.pxl))
        color=(0,255,0)
        pygame.draw.rect(screen, color, pygame.Rect(vr.pxl*apple.x+2,vr.pxl*apple.y+2, vr.pxl-4, vr.pxl-4))
        
        col = 0
        os = vr.coloroffset
        
        for i in range(len(snake.tailx)):
            if (col+os >= 255):
                os=-vr.coloroffset
            elif(col+os<=0):
                os=vr.coloroffset
            col+=os
            color = (col,col,255)
            pygame.draw.rect(screen, color, pygame.Rect(vr.pxl*snake.tailx[i],vr.pxl*snake.taily[i], vr.pxl, vr.pxl))
        color=(0,0,192)
        pygame.draw.rect(screen, color, pygame.Rect(vr.pxl*snake.x,vr.pxl*snake.y, vr.pxl, vr.pxl))
    def keyd():
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            snake.dire=0
        if pressed[pygame.K_RIGHT]:
            snake.dire=1
        if pressed[pygame.K_DOWN]:
            snake.dire=2
        if pressed[pygame.K_LEFT]:
            snake.dire=3
    def ref():
        gamef.tails()
        if (snake.dire == 0):
            gamef.move(0,-1)
            #snake.y -=1
        elif (snake.dire == 1):
            gamef.move(1,0)
            #snake.x+=1
        elif (snake.dire == 2):
            #snake.y+=1
            gamef.move(0,1)
        elif (snake.dire == 3):
            gamef.move(-1,0)
            #snake.x-=1
    def move(x,y):
        #x check
        if (snake.x+x)>= vr.gw-1:
            print ("out of bounds")
            snake.x = 1;
        elif(snake.x+x)<= 0:
            print ("out of bounds")
            snake.x = vr.gw-2;
        else:
            snake.x+=x
        #y check
        if (snake.y+y)>= vr.gh-1:
            print ("out of bounds")
            snake.y = 1;
        elif(snake.y+y)<= 0:
            print ("out of bounds")
            snake.y = vr.gh-2;
        else:
            snake.y+=y
        #apple
        if (snake.x == apple.x) and (snake.y == apple.y):
            snake.leng+=1
            apple.lvl+=1
            apple.x = random.randint(1,vr.gw-2)
            apple.y = random.randint(1,vr.gh-2)
            print("Apple pos:\nX - "+str(apple.x)+"\nY - "+str(apple.y))
            
    def tails():
        snake.tailx.append(snake.x)
        snake.taily.append(snake.y)
        if (len(snake.tailx) > snake.leng):
            snake.tailx.pop(0)
            snake.taily.pop(0)
        
        
while not vr.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vr.done = True
            exit()
            quit()
            
    
    gamef.grid()
    gamef.keyd()
    c+=1
    gamef.draw()
    if (c >= (200/snake.speed)):
        gamef.ref()
        c=0
        #snake.speed+=1
    pygame.display.flip()
    clock.tick(50)