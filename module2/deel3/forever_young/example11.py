from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
# robotArm.grab()
# color = robotArm.scan()
# if color == 'red':
#     robotArm.moveRight()
#     robotArm.drop()
color = robotArm.scan()
for i in range(9):
    robotArm.grab()
    robotArm.scan()
    if color == 'red':
        print(f'{i} {color}')
    robotArm.drop()
    robotArm.moveRight()
    print(color)
    if color == 'red':
        robotArm.moveRight()
        robotArm.drop()
        print(color)
    else:
        print(color)


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()