from random import choice

nouns = ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 'extroert', 'gorilla']
verbs = ['kiks', 'jingles', 'bounces', 'slurps','meows', 'explpodes', 'curdles' ]
adjectives = ['furry', 'balding', 'incredulous', 'fragrant', 'exuberant', 'glistening']
preposition = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within']
adverbs = ['curiosly', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously']

def make_poem():
    #pull three different noun
    n1 = choice(nouns)
    n2 = choice(nouns)
    n3 = choice(nouns)

    while n1 == n2:
        n2 = choice(nouns)
    while n1 == n3 or n2 == n3:
        n3 = choice(nouns)

    #pull three different verb
    v1 = choice(verbs)
    v2 = choice(verbs)
    v3 = choice(verbs)

    while v1 == v2:
        v2 = choice(verbs)
    while v1 == v3 or v2 == v3:
        v3 = choice(verbs)


    # Pull three different adjectives
    adj1 = choice(adjectives)
    adj2 = choice(adjectives)
    adj3 = choice(adjectives)
    while adj1 == adj2:
        adj2 = choice(adjectives)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = choice(adjectives)

    # Pull two different prepositions
    prep1 = choice(preposition)
    prep2 = choice(preposition)
    while prep1 == prep2:
        prep2 = choice(preposition)

    # Pull one adverb
    adv1 = choice(adverbs)

    if "aeiou".find(adj1[0]) != -1:
        article = 'An'
    else:
        article = 'A'

    poem = "{} {} {}\n\n".format(article, adj1, n1)
    poem = poem + "{} {} {} {} {} the {} {}\n".format(
        article, adj1, n1, v1, prep1, adj2, n2
    )
    poem = poem + "{}, the {} {}\n".format(adv1, n1, v2)
    poem = poem + "the {} {} {} a {} {}".format(n2, v3, prep2, adj3, n3)

    return poem

print(make_poem())
    
        
        
    
    
