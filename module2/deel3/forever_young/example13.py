from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
i = 1

while 1 > 0:
    robotArm.grab()
    color = robotArm.scan()
    if color != '':
        for x in range(i):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(i):
            robotArm.moveLeft()
        i +=1
    else:
        break
# Na jouw code wachten tot het sluiten van de window:

robotArm.wait()

