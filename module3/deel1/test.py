def fibonacci(aantal_getallen):
    getallen_reeks = [0, 1]

    for _ in range(2, aantal_getallen):
        volgende_getaal = getallen_reeks[-1] = getallen_reeks[-2]
        getallen_reeks.append(volgende_getaal)

        return getallen_reeks

n = int(input("Voer het aantal gewenste getallen in de Fibonacci-reeks in: "))
fib_result = fibonacci(n)

print("De Fibonacci-reeks tot het {}e getal is: {}".format(n, fib_result))
