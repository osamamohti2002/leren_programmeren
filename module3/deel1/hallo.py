def hallo_py(nummer):
    begroeting = ""
    for i in range(1, nummer + 1):
        begroeting += f"Hello from function town {i}!\n"
    return begroeting

# Test met argument 3
resultaat = hallo_py(10)
print(resultaat)

# Test met argument 7
