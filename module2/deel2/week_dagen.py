dagen =('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')
#dagen van de week

for dag in dagen:
    print(dag)

print()
# werk dagen
for dag in range(0, 5, 1):
    print(dagen[dag])

print()

#weekend dagen
for dag in range(5, 7, 1):
    print(dagen[dag])

print()

#week dagen omgekeerd
for dag in dagen[-7:]:
    print(dag)

print()
#
for dag in dagen[:-2]:
    print(dag)
#

print()

for i in dagen[-2:]:
    print(i)


