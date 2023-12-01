from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
beweging = 9
# Jouw python instructies zet je vanaf hier:
for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for x in range(beweging - i):
            robotArm.moveRight()
        robotArm.drop()
        print(f'i {i}')
        print(f'beweging {beweging}')
        i += 1
        for a in range(beweging - i):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
    # i -=1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()