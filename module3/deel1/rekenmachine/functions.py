def optellen(n1, n2):
    return n1 + n2


def aftrekken(n1, n2):
    return n1 - n2


def vermenigvuldigen(n1, n2):
    return n1 * n2


def delen(n1, n2):
    return n1 / n2


def stel_vraag(prompt):
    return input(prompt)


def actie_kiezen(choice, n1, n2):
    if choice == 'a':
        return optellen(n1, n2)
    elif choice == 'b':
        return aftrekken(n1, n2)
    elif choice == 'c':
        return vermenigvuldigen(n1, n2)
    elif choice == 'd':
        return delen(n1, n2)
    elif choice == 'e':
        return optellen(n1, 1)
    elif choice == 'f':
        return aftrekken(n1, 1)
    elif choice == 'g':
        return vermenigvuldigen(n1, 2)
    elif choice == 'h':
        return delen(n1, 2)

    return choice, n1, n2
