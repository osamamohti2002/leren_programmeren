from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

robotArm.moveRight()
for _ in range(7):
    robotArm.grab()
    for a in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(8):
        robotArm.moveLeft()
robotArm.wait()
