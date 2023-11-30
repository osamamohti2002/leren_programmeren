from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

for getal in range(0, 10, 2):
    robotArm.grab()
    for a in range(9 - getal): robotArm.moveRight()
    robotArm.drop()
    for b in range(8 - getal): robotArm.moveLeft()

robotArm.wait()





