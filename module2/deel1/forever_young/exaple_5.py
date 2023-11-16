from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

for i in range(7):
    robotArm.moveRight()

for i in range(7):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    for i in range(2):
        robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()


robotArm.wait()
