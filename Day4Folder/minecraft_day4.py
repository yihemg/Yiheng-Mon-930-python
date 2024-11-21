def Teleport():
    agent.teleport_to_player()

player.on_chat("come",Teleport)

def moveForward(steps):
     agent.move(FORWARD, steps)

def moveBack(steps):
    agent.move(BACK, steps)

def moveUp(steps):
    agent.move(UP,steps)

def moveDown(steps):
    agent.move(DOWN,steps)   

def moveLeft(steps):
    agent.move(LEFT,steps)

def moveRight(steps):
    agent.move(RIGHT,steps)

def turnRight():
    agent.turn(RIGHT)

def turnLeft():
    agent.turn(LEFT)

player.on_chat("fw",moveForward)    
player.on_chat("bk",moveBack)
player.on_chat("ml",moveLeft)
player.on_chat("mr",moveRight)
player.on_chat("up",moveUp)
player.on_chat("down",moveDown)
player.on_chat("tl",turnLeft)
player.on_chat("tr",turnRight)



def destroytree(steps):
    for i in range(steps):
        agent.destroy(FORWARD)
        agent.move(UP,1)
    agent.move(DOWN,steps)
    agent.collect_all()
player.on_chat("tree",destroytree)  



def destroystone(steps):
    for i in range(steps):
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(FORWARD)
        agent.destroy(DOWN)
        agent.collect_all()     
        agent.move(FORWARD,1)
    
player.on_chat("df",destroystone)       


def buildwall():
    for i in range(5):
        for i in range(3):
            agent.place(FORWARD)
            agent.move(UP,1)
        agent.move(DOWN,3)
        agent.move(RIGHT,1)

player.on_chat("wall", buildwall)

def solvespiral():
    while agent.inspect(AgentInspection.BLOCK,DOWN) != DIAMOND_BLOCK:
        if not agent.detect(AgentDetection.BLOCK,RIGHT):
            agent.turn(RIGHT)

        agent.move(FORWARD,1)

player.on_chat("findway",solvespiral) 

def solvemaze():
    while agent.detect(AgentDetection.BLOCK,DOWN) == True:
        if not agent.detect(AgentDetection.BLOCK, LEFT):
            agent.turn(LEFT)
            agent.move(FORWARD,1)
        elif not agent.detect(AgentDetection.BLOCK,FORWARD):
            agent.move(FORWARD,1)
        else:
            agent.turn(RIGHT)
            agent.move(FORWARD,1) 
    
player.on_chat("maze",solvemaze)

def digunderground():
    while agent.detect(AgentDetection.BLOCK,DOWN):
        agent.destroy(DOWN)
        agent.move(DOWN,1)

player.on_chat("under",digunderground)
