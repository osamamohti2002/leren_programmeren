dagen =('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')
#dagen van de week
print(dagen)

#werk dagen
werk_dagen = dagen[:5]
print(werk_dagen)

#werk dagen omgekeerd
for dag in reversed(werk_dagen):
    print(dag , end=',')
print()

#weekend
weekend_dagen = dagen[5:]
print(weekend_dagen)
for weeken in reversed(weekend_dagen):
    print(weeken , end=',')
print()







