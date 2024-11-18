def Teleport():
    agent.teleport_to_player()

player.on_chat("come",Teleport)

def moveForward():
     agent.move(FORWARD, 1)

def moveBack():
    agent.move(BACK, 1)

def moveUp():
    agent.move(UP,1)

def moveDown():
    agent.move(DOWN,1)   

def moveLeft():
    agent.move(LEFT,1)

def moveRight():
    agent.move(RIGHT,1)

def turnRight():
    agent.move(RIGHT,1)

def turnLeft():
    agent.move(LEFT,1)

player.on_chat("fw",moveForward)    
player.on_chat("bk",moveBack)
player.on_chat("ml",moveLeft)
player.on_chat("mr",moveRight)
player.on_chat("up",moveUp)
player.on_chat("down",moveDown)
player.on_chat("tl",turnLeft)
player.on_chat("tr",turnRight)