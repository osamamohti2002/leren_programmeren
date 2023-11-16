from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
# for i in range(7):
#     robotArm.moveRight()
#
# for x in range(7):
#     robotArm.grab()
#     robotArm.moveRight()
#     robotArm.drop()
#     for i in range(1):
#         robotArm.moveLeft()
# robotArm.grab()
# robotArm.moveRight()
# robotArm.drop()

# Jouw python instructies zet je vanaf hier:
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







# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()