woordenboek = {
    'python': 'slang',
    'programma': 'code',
    'tekst': 'woord',
    'hertaling': 'vertaling',
    'machine': 'apparaat',
}
print("Beschikbare woorden om te vertalen:", ', '.join(woordenboek))
tekst = input("Voer een stukje tekst in: ")
vertaalde_tekst = []
for woord in tekst.split():
    vertaalde_tekst.append(woordenboek.get(woord, woord))
print("Vertaalde tekst:", ' '.join(vertaalde_tekst))
