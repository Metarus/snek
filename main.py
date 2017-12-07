import pygame
import random
import network

pygame.init()

size=[400, 400]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("Machine Learning Snake")

done=False
clock=pygame.time.Clock()

timer=100

score=0
highScore=0

genNum=0
variantNum=0

goalLocations=[]
for i in range(0, 400):
    goalLocations.append([random.randint(0, 9), random.randint(0, 9)])


tiles=[]
for i in range(0, 10):
    tiles.append([])
    for j in range(0, 10):
        tiles[i].append(0)

def scoreadd():
    global timer
    global score
    score+=100-(timer/10)

def settimer(val):
    global timer
    timer=val

def addtimer(val):
    global timer
    timer+=val

class Snake:
    def __init__(self):
        self.snekTiles=[]
        self.skip=0
        for i in range(0, 3):
            self.snekTiles.append([5, 5])

    def updateTiles(self):
        for i in self.snekTiles:
            tiles[i[0]][i[1]]=1
        tiles[self.snekTiles[0][0]][self.snekTiles[0][1]]=2

    def clearSnake(self):
        tiles[1][1] = 1
        for i in self.snekTiles:
            tiles[i[0]][i[1]]=0

    def headX(self): return self.snekTiles[0][0]
    def headY(self): return self.snekTiles[0][1]

    def newGoal(self):
        notDone=True
        while notDone:
            p=goalLocations[len(self.snekTiles)-3+self.skip]
            notDone=False
            for i in self.snekTiles:
                if (i==p):
                    notDone=True
                    self.skip+=1
            if not notDone:
                tiles[p[0]][p[1]]=3

    def move(self, dir):
        temp=self.snekTiles[len(self.snekTiles)-1]
        for i in self.snekTiles:
            tiles[i[0]][i[1]]=0
        for i in range(len(self.snekTiles)-1, 0, -1):
            self.snekTiles[i]=self.snekTiles[i-1]
        if(dir==0):
            self.snekTiles[0]=[self.snekTiles[0][0],(self.snekTiles[0][1]-1)%10]
        if(dir==1):
            self.snekTiles[0]=[(self.snekTiles[0][0]+1)%10,self.snekTiles[0][1]]
        if(dir==2):
            self.snekTiles[0]=[self.snekTiles[0][0],(self.snekTiles[0][1]+1)%10]
        if(dir==3):
            self.snekTiles[0]=[(self.snekTiles[0][0]-1)%10,self.snekTiles[0][1]]

        if (tiles[self.snekTiles[0][0]][self.snekTiles[0][1]]==3):
            self.snekTiles.append(temp)
            self.newGoal()
            scoreadd()
            addtimer(50)

        for i in self.snekTiles[1:]:
            if(self.snekTiles[0]==i):
                settimer(0)

Snek=Snake()
Snek.newGoal()

net=network.NeuralNetwork([300, 4])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            Snek.move(0)
        if event.key == pygame.K_RIGHT:
            Snek.move(1)
        if event.key == pygame.K_DOWN:
            Snek.move(2)
        if event.key == pygame.K_LEFT:
            Snek.move(3)

    netInput=[]
    for i in range(0, len(tiles)):
        for j in range(0, len(tiles[i])):
            temp = tiles[(i + Snek.headX()) % 10][(j + Snek.headY()) % 10]
            if temp >= 2:
                temp -= 1
            for k in range(0, 3):
                if temp==k:
                    netInput.append(1)
                else: netInput.append(0)

    inputs=net.func(netInput)

    if inputs[0]>inputs[1] and inputs[0]>inputs[2] and inputs[0]>inputs[3]:
        Snek.move(0)
    elif inputs[1]>inputs[2] and inputs[1]>inputs[3]:
        Snek.move(1)
    elif inputs[2]>inputs[3]:
        Snek.move(2)
    else: Snek.move(3)

    Snek.updateTiles()

    timer-=1

    if timer<=0:
        if score > highScore:
            highScore = score
            net.bestVals()
            genNum += 1
            variantNum = 0
            text = open("wb.txt", 'w')
            text.write(str(net.wb))
            text.close()
            print("New Generation")
        print("Generation:", genNum,"Variant:", variantNum, "High:", round(highScore), "Length:", len(Snek.snekTiles), "Last:", round(score))
        net.nudge(50)
        Snek.clearSnake()
        Snek.__init__()
        variantNum += 1
        timer=50
        for i in range(0, 10):
            for j in range(0, 10):
                tiles[i][j] = 0
        Snek.newGoal()
        Snek.skip=0
        score=0

    for i in range(0, 10):
        for j in range(0, 10):
            color=(255, 0, 255)
            if tiles[i][j]==0:
                color=(0, 0, 0)
            if tiles[i][j]==1:
                color=(255, 255, 255)
            if tiles[i][j]==2:
                color=(255, 0, 255)
            if tiles[i][j]==3:
                color=(random.random()*255, random.random()*255, random.random()*255)
            pygame.draw.rect(screen, color, [i*40, j*40, 40, 40])

    pygame.display.flip()

pygame.quit()