add_library('minim') #Add minim




def setup():
     global imgBoard, BoardW,BoardH,BoardX,BoardY
     global imgBall,BallW,BallH,BallX,BallY,dY,dX
     global imgExit,ExitX,ExitY,ExitW,ExitH
     global imgRestart,RestartX,RestartY,RestartW,RestartH
     global img,PillX,PillY,PillW,PillH,dy,present
     global imgCap,CapX,CapY,CapW,CapH,DY
     global stageNum,score

     global minim,player,player1,player2
     #Creat minim object
     minim=Minim(this)
     player1=minim.loadFile("song1.mp3")
     player=minim.loadFile("song.mp3")
     player2=minim.loadFile("song2.mp3")
     
     size(1000,800)
     background(0)
     
     imgExit=loadImage("Exit_Button.png")
     imgRestart=loadImage("Restart_button.png")
     imgBoard=loadImage("rectangular_board.png")
     imgBall=loadImage("Ball0.png")
     ExitW=imgExit.width
     ExitH=imgExit.height
     ExitX=width/2-3*imgExit.width
     ExitY=height/2     
     RestartW=imgExit.width
     RestartH=imgExit.height
     RestartX=(width/2)+3*imgRestart.width
     RestartY=height/2
     BoardW=120
     BoardH=30     
     BallW=30
     BallH=30
     BoardX=mouseX-BoardW/2
     BoardY=height-BoardH
     BallX=random(0,width-(2*BallW))
     BallY=0
     dX=random(3,5)
     dY=random(3,5)
     stageNum=0
     score=0
     img=[]     
     dy=[]
     PillX=[]
     PillY=[]
     present=[]
     PillW=[]
     PillH=[]
     for i in range(10):
         img.append(loadImage("Pill"+str(i)+".png"))
         PillW.append(30)
         PillH.append(50)
         PillX.append(random(0,width-PillW[i]))
         PillY.append(random(0,height/2))         
         dy.append(random(0.1,0.5))
         present.append(True)
     imgCap=[]
     CapX=[]
     CapY=[]
     CapW=30
     CapH=50
     DY=[]
     for i in range(8):                  
         imgCap.append(loadImage("Cap"+str(i)+".png"))
         CapX.append(random(0,width-CapW))
         CapY.append(random(0,height/2))
         DY.append(random(0.5,1))
        
     
     
def draw():
    if stageNum==0:        
        displayWelcomePage()
    elif stageNum==1:        
        displayGameMode()
    elif stageNum==2:
        displayGameOver()
    elif stageNum==3:
        displayGamePlay()        
    elif stageNum==4:
        displayGamePlay1()        
    elif stageNum==5:
        displayGamePlay2()
        



def displayWelcomePage():
    background(0)
    fill(0,0,255)
    textSize(30)
    text('Instruction:',0,40)
    fill(250,50,0)
    textSize(30)
    text("Use the mouse to move the board horizontally to hit ",170,40)       
    text("the red pills with the ball and earn points",170,80) 
    fill(0,100,255)
    text("Avoid consuming the blue pills with the board",170,120)  
    fill(255,0,0)
    text("The Game ends when the ball touches the ground",170,170)  
    fill(random(0,255),random(0,255),random(0,255))
    textSize(30)
    text('Press Z to start the game',(3*width)/10,height/2+100 )   
    image(imgBoard,width/2-BoardW/2,height-imgBoard.height,BoardW,BoardH)
    image(imgBall,width/2-BallW/2 ,height-imgBoard.height-BallH,BallW,BallH)
    image(imgCap[0],180,250,CapW,CapH)
    textSize(30)
    fill(0,0,255)
    text("= Score decreases by 10",220,250+CapH/2)
    image(img[0],180,350,PillW[0],PillH[0])
    textSize(30)
    fill(255,0,0)
    text("=Score increases by 10",220,350+PillH[0]/2)



def displayGameMode():
    background(255)
    textSize(40)
    fill(255,0,0)
    text("'Press A to opt for EASY game mode'", 100,250)
    fill(255,69,0)
    text("'Press B to opt for MEDIUM game mode'",100,300)
    fill(255,69,0)
    text("'Press C to opt for HARD game mode'",100,350)
    





    
        
def displayGamePlay():
    BoardX=mouseX-BoardW/2
    BoardY=height-BoardH
    global BallY,dY,dX,BallX,BallW,BallH,dy,score,stageNum
    background(0)
    fill(0,0,255)
    #rect(mouseX-BoardW/2,BoardY,BoardW,BoardH)    
    image(imgBoard,mouseX-BoardW/2,BoardY,BoardW,BoardH)
    image(imgBall,BallX,BallY,BallW,BallH)
    BallY=BallY+dY
    BallX=BallX+dX
    textSize(30)
    text("Score:" +str(score), 10,30)
    
    #Code for displaying the pills
    for i in range(10):
        if (present[i]==True):            
            image(img[i],PillX[i],PillY[i],PillW[i],PillH[i])
            PillY[i]+=dy[i]    
                
            if (PillY[i] > height):                          
                PillY[i] = -PillH[i]
                PillX[i] = random(0, width-PillW[i])
                dy[i]+=0.1
                
            
                        
           
            
           # Variables for determing the sides of the pills and the ball 
            aLeft  = BallX
            aRight = BallX + BallW
            aTop   = BallY
            aBottom = BallY+BallH
        
            bLeft =  PillX[i]
            bRight = PillX[i] + PillW[i]
            bTop =  PillY[i]
            bBottom = PillY[i]+PillH[i]
    
    #Code for detecting collision between ball and the pill    
            if (aTop < bBottom and bTop < aBottom and aLeft < bRight and bLeft < aRight):
                PillY[i] = -PillH[i]
                PillX[i] = random(0, width-PillW[i])
                dy[i]+=0.1                                                                       
                score=score+10
                
                
    # Code for bringing in the blue capsules in the display    
    for i in range(3):                            
        if (present[i]==True):            
            image(imgCap[i],CapX[i],CapY[i],CapW,CapH)
            CapY[i]+=DY[i]    
                
            if (CapY[i] > height):                          
                CapY[i] = -CapH
                CapX[i] = random(0, width-CapW)                
                DY[i]+=0.1
            
                        
           
            
           # Code for determining the sides of the blue capsule
        
            bLeft3 =  CapX[i]
            bRight3 = CapX[i] + CapW
            bTop3 =  CapY[i]
            bBottom3 = CapY[i]+CapH
                
    #Code for detecting collision between board and the blue capsule   
            if (bBottom3 > BoardY and bTop3 < BoardY + BoardH and bRight3 > BoardX and bLeft3 < BoardX + BoardW):                  
                CapY[i] = -CapH
                CapX[i] = random(0, width-CapW)
                DY[i]+=0.5                                                             
                score=score-10
                     
        
            
            
    

    # Code for the ball to bounce of the board
    if (BallY+BallH > BoardY and BallX< BoardX + BoardW and (BallX > BoardX or BallX+BallW>BoardX) and BallY<BoardY +BoardH):        
        dY+=0.5          
        dY=-dY
     
    # Code for the ball to bounce of the left and right wall of the display
    if(BallX<0 or BallX>width-BallW):
        dX=-dX
        
    # Code for the ball to bounce of the top wall of the display    
    if(BallY<0):
        dY=-dY
        
    # Code for the game to be over when the ball touches the bottom/ground of the display
    if(BallY+BallH>height):
        #displayGameOver()
        player.close()
        minim.stop()
        stageNum=2    
        
    
        
  # Code for medium game mode        
def displayGamePlay1():
    global BallY,dY,dX,BallX,BallW,BallH,dy,score,stageNum
    background(0)
    fill(0,0,255)
    BoardX=mouseX-BoardW/2
    BoardY=height-BoardH
    #rect(mouseX-BoardW/2,BoardY,BoardW,BoardH)
    
    image(imgBoard,mouseX-BoardW/2,BoardY,BoardW,BoardH)
    image(imgBall,BallX ,BallY,BallW,BallH)
    BallY=BallY+(3*dY)/2
    BallX=BallX+(3*dX)/2
    textSize(30)
    text("Score:" +str(score), 10,30)
    
    
    #Code for displaying the pills
    for i in range(10):
        if (present[i]==True):            
            image(img[i],PillX[i],PillY[i],PillW[i],PillH[i])
            PillY[i]+=(3*dy[i])/2    
                
            if (PillY[i] > height):                          
                PillY[i] = -PillH[i]
                PillX[i] = random(0, width-PillW[i])
                dy[i]+=0.2
                
            
                        
           
            
           # Variables for determing the sides of the pills and the ball 
            aLeft  = BallX
            aRight = BallX + BallW
            aTop   = BallY
            aBottom = BallY+BallH
        
            bLeft =  PillX[i]
            bRight = PillX[i] + PillW[i]
            bTop =  PillY[i]
            bBottom = PillY[i]+PillH[i]
    
    #Code for detecting collision between ball and the pill    
            if (aTop < bBottom and bTop < aBottom and aLeft < bRight and bLeft < aRight):
                PillY[i] = -PillH[i]
                PillX[i] = random(0, width-PillW[i])
                dy[i]+=0.2                                                                         
                score=score+10
                
     #Code for displaying the blue capsule but this time greater in number           
    for i in range(4):                            
        if (present[i]==True):            
            image(imgCap[i],CapX[i],CapY[i],CapW,CapH)
            CapY[i]+=DY[i]    
                
            if (CapY[i] > height):                          
                CapY[i] = -CapH
                CapX[i] = random(0, width-CapW)
                DY[i]+=0.2
                
            
                        
           
            
        #Code for determining the sides of the blue capsule
            bLeft1 =  CapX[i]
            bRight1 = CapX[i] + CapW
            bTop1 =  CapY[i]
            bBottom1 = CapY[i]+CapH
                
    #Code for detecting collision between board and the capsule   
            if (bBottom1 > BoardY and bTop1 < BoardY + BoardH and bRight1 > BoardX and bLeft1 < BoardX + BoardW):                  
                CapY[i] = -CapH
                CapX[i] = random(0, width-CapW)
                DY[i]+=0.75                                                            
                score=score-10
                
           
           
                
            
                
            
        
            
            
        

    # Code for the ball to bounce of the board
    if (BallY+BallH > BoardY and BallX< BoardX + BoardW and (BallX > BoardX or BallX+BallW>BoardX) and BallY<BoardY +BoardH):
        dY+=0.8          
        dY=-dY 
    # Code for the ball to bounce of the left and right wall of the display
    if(BallX<0 or BallX>width-BallW):
        dX=-dX
        
    # Code for the ball to bounce of the top wall of the display    
    if(BallY<0):
        dY=-dY
        
    # Code for the game to be over when the ball touches the bottom/ground of the display
    if(BallY+BallH>height):
        #displayGameOver()
        player2.close()
        minim.stop()
        stageNum=2    
 
        
 #Code for hard game mode                     
def displayGamePlay2(): 
    BoardX=mouseX-BoardW/2
    BoardY=height-BoardH    
    global BallY,dY,dX,BallX,BallW,BallH,dy,score,stageNum
    background(0)
    fill(0,0,255)
    #rect(mouseX-BoardW/2,BoardY,BoardW,BoardH
    image(imgBoard,mouseX-BoardW/2,BoardY,BoardW,BoardH)
    image(imgBall,BallX,BallY,BallW,BallH)
    BallY=BallY+(3*dY)/2
    BallX=BallX+(3*dX)/2
    textSize(30)
    text("Score:" +str(score), 10,30)
    
    
    
    
    
    
    #Code for displaying the pills
    for i in range(10):
        if (present[i]==True):            
            image(img[i],PillX[i],PillY[i],PillW[i],PillH[i])
            PillY[i]+=dy[i]    
                
            if (PillY[i] > height):                          
                PillY[i] = -PillH[i]
                PillX[i] = random(0, width-PillW[i])
                dy[i]+=0.3
                
            
                        
    
            
           # Variables for determing the sides of the pills and the ball 
            aLeft  = BallX
            aRight = BallX + BallW
            aTop   = BallY
            aBottom = BallY+BallH
        
            bLeft =  PillX[i]
            bRight = PillX[i] + PillW[i]
            bTop =  PillY[i]
            bBottom = PillY[i]+PillH[i]
    
    #Code for detecting collision between ball and the pill    
            if (aTop < bBottom and bTop < aBottom and aLeft < bRight and bLeft < aRight):
                PillY[i] = -PillH[i]
                PillX[i] = random(0, width-PillW[i])
                dy[i]+=0.3                                                                        
                score=score+10
                
                
    
                
                    
                
    #Code for displaying the blue capsules
    for i in range(5):
        if (present[i]==True):            
            image(imgCap[i],CapX[i],CapY[i],CapW,CapH)
            CapY[i]+=DY[i]   
                
            if (CapY[i] > height):                          
                CapY[i] = -CapH
                CapX[i] = random(0, width-CapW)
                DY[i]+=0.3
                  
            
    
       #Code for determining the sides of the blue capsule 
            bLeft2 =  CapX[i]
            bRight2 = CapX[i] + CapW
            bTop2 =  CapY[i]
            bBottom2 = CapY[i]+CapH
                
    #Code for detecting collision between board and the blue capsule    
            if (bBottom2 > BoardY and bTop2 < BoardY + BoardH and bRight2 > BoardX and bLeft2 < BoardX + BoardW):
                
                CapY[i] = -CapH
                CapX[i] = random(0, width-CapW)
                DY[i]+=1                                                             
                score=score-10
                
                

    
            
                
            
        
            
            
        

    # Code for the first ball to bounce of the board
    if (BallY+BallH > BoardY and BallX< BoardX + BoardW and (BallX > BoardX or BallX+BallW>BoardX) and BallY<BoardY +BoardH):
        dY+=1.2         
        dY=-dY 
        
    # Code for the first ball to bounce of the left and right wall of the display
    if(BallX<0 or BallX>width-BallW):
        dX=-dX
        
        
    # Code for the first ball to bounce of the top wall of the display    
    if(BallY<0):        
        dY=-dY
        
        
    # Code for the game to be over when the first ball touches the bottom/ground of the display
    if(BallY+BallH>height):
        #displayGameOver()
        player1.close()
        minim.stop()
        stageNum=2
        
    
        
        
        
          
        
    
    


        
def displayGameOver():
    background(0)
    image(imgExit,ExitX,ExitY,ExitW,ExitH)
    image(imgRestart,RestartX,RestartY,RestartW,RestartH)
    fill(255,0,0)
    textSize(60)
    text('GAME OVER!', width/2-100,100)
    textSize(30)
    text('Click to restart',RestartX,RestartY+150)
    text('Click to exit', ExitX,ExitY+150)
    textSize(50)
    text('Score='+str(score),width/2-100,200)
    
    
def mousePressed():
    global stageNum
    #Mouse click on restart button
    if (mouseX>RestartX and mouseX<RestartX+RestartW) and (mouseY>RestartY and mouseY<RestartY+RestartH):
        setup()
    # Mouse click on exit button
    if(mouseX>ExitX and mouseX<ExitX+ExitW) and (mouseY>ExitY and mouseY<ExitY+ExitH):
        exit()
    
    
def keyPressed():
    global stageNum    
    if stageNum==0 and (key=='z' or key=='Z'):
        stageNum+=1        
    if stageNum==1 and (key=='a' or key=='A'):
        stageNum+=2
        player.rewind()
        player.loop()
    if stageNum==1 and (key=='b' or key=='B'):
        stageNum+=3
        player2.rewind()
        player2.loop()
    if stageNum==1 and (key=='c' or key=='C'):
        stageNum+=4
        player1.rewind()
        player1.loop()
    
    
    
    
    
    
    
    
    
