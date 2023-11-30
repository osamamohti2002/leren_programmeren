from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
color = robotArm.scan()
if color == 'red':
    robotArm.moveRight()
    robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()