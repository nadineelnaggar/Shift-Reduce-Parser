import nltk
from nltk.parse.shiftreduce import ShiftReduceParser
# from nltk import grammar, parse
from nltk import CFG, parse

grammar = CFG.fromstring(
    """
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    NP -> 'I'
    N -> 'man' | 'park' | 'telescope' | 'dog'
    Det -> 'the' | 'a'
    P -> 'in' | 'with'
    V -> 'saw'
    """
    )

print(grammar)

sent = "I saw a man in the park".split()
print(sent)


parser = parse.ShiftReduceParser(grammar, trace=2)
# print(parser)
for p in parser.parse(sent):
        print(p)