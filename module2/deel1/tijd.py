for uur in range(1, 25):
    # periode = 'AM' if uur < 12 else 'PM'
    if uur < 12:
        periode = 'AM'
    else:
        periode = 'PM'
    omgezet_uur = uur if uur == 12 else uur % 12
    print(f"{omgezet_uur:02d}:00 {periode}")

