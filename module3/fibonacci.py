def fibonacci(aantal_getallen):
    fibonacci_reeks = [0, 1]

    for _ in range(2, aantal_getallen):
        volgend_getal = fibonacci_reeks[-1] + fibonacci_reeks[-2]
        fibonacci_reeks.append(volgend_getal)

    return fibonacci_reeks


aantal = int(input("Voer het aantal gewenste getallen in de Fibonacci-reeks in: "))
fib_result = fibonacci(aantal)

print(f"De Fibonacci-reeks tot het {aantal}e getal is: {fib_result}")
