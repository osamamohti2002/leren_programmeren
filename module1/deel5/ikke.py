import re
from test_lib import test, report
def extract_sub_sentences(text):
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    sub_sentences = marked_text.split("|")
    return sub_sentences
 
def calculate_ego_score(text):
    sub_sentences = extract_sub_sentences(text)
    ego_score = 0
    for sentence in sub_sentences:
        sentence = sentence.strip()
        sentence = sentence.lower()
        if len(sentence) > 0:
            words = sentence.split(' ')
            if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1] in ('ik', 'mijn')):
                ego_score += 1
    return ego_score
 
voorbeeld_tekst = """Geachte heer/mevrouw,
Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren. Ik ben buitengewoon slim en in staat om snel nieuwe informatie te verwerken en te gebruiken om de beste beslissingen te nemen voor het bedrijf. Ik ben er zeker van dat ik binnen enkele weken op de hoogte zal zijn van alle zaken die spelen binnen uw bedrijf, en ik zal in staat zijn om snel resultaten te boeken en uw bedrijf naar de top te brengen. Mijn CV is overtuigend! Mijn referenties zijn heel positief over mij. Ik verdien daarom een plek in uw team.
Ik kijk er naar uit om te horen wanneer ik op gesprek mag komen, zodat ik u persoonlijk kan overtuigen van mijn geschiktheid voor deze functie."""
 
ego_score = calculate_ego_score(voorbeeld_tekst)


print(ego_score)
test('ego 1 ' , 14 , ego_score)
report()
 