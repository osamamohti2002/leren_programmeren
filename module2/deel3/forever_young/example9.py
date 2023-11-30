from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

for aantalblokjes in range(1, 5):  # stapel
    for _ in range(aantalblokjes):
        robotArm.grab()
        for a in range(5): robotArm.moveRight()
        robotArm.drop()
        for b in range(5): robotArm.moveLeft()
    robotArm.moveRight()

robotArm.wait()



