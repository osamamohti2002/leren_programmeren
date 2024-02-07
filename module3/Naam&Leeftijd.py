def name_age():
    name = input('wat is je naam')
    age = int(input('wat is je leeftijd'))

    result = {
        'naam': name,
        'leeftijd': age
    }

    return result


result = name_age()
print(f"{result['naam']} is {result['leeftijd']} jaar oud")




