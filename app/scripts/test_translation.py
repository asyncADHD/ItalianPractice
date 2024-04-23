import mlconjug

# Default setup for Italian
default_conjugator = mlconjug.Conjugator(language='it')

# Conjugate a verb
verb_to_conjugate = 'parlare'
conjugated_verb = default_conjugator.conjugate(verb_to_conjugate)

# Print all conjugated forms
all_conjugations = conjugated_verb.iterate()
for tense, persons in all_conjugations.items():
    print(tense)
    for person, conjugation in persons.items():
        print(f'{person}: {conjugation}')
