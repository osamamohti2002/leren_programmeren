# for uur in range(1,25):
#     if uur < 12:
#         periode = 'PM'
#     else:
#         periode = 'AM'
#     omgezete_uren = uur if uur <= 12 else uur - 12
#     print(f"{omgezete_uren:02d}:00 {periode}")
#

# for uur in range(1, 25):
#     period = 'AM' if uur <= 12 else 'PM'
#     omgezte_uren = uur if uur <= 12 else uur - 12
#     print(f"{omgezte_uren:02d}:00 {period}")

uur = 1

while uur <= 24:
    if uur <= 12:
        periode = 'AM'
    else:
        periode = 'PM'

    omgezete_uren = uur if uur <= 12 else uur - 12
    print(f"{omgezete_uren:02d}:00 {periode}")

    uur += 1
