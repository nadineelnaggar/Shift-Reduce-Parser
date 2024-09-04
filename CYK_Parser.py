from nltk.ccg.chart import CCGChartParser, ApplicationRuleSet, CompositionRuleSet, SubstitutionRuleSet, TypeRaiseRuleSet, printCCGDerivation
from nltk.ccg import chart, lexicon



lex1 =  """
    :- S,  NP, N, VP 
    
    Det :: NP/N
    Pro :: NP
    Modal :: S\\NP/VP
    
    TV :: VP/NP
    DTV :: TV/NP
    
    the => Det
    
    that => Det
    that => NP
    
    I => Pro
    you => Pro
    we => Pro
    
    chef => N
    cake => N
    children => N
    dough => N
    
    will => Modal 
    should => Modal
    might => Modal
    must => Modal
    
    and => var\\.,var/.,var
    
    to => VP[to]/VP
    
    without => (VP\\VP)/VP[ing]
    
    be => TV
    cook => TV
    
    eat => TV
    
    cooking => VP[ing]/NP
    
    give => DTV
    
    is => (S\\NP)/NP
    prefer => (S\\NP)/NP
    
    which => (N\\N)/(S/NP)
    
    persuade => (VP/VP[to])/NP
    """

lex = lexicon.fromstring(lex1)

parser = chart.CCGChartParser(lex, chart.DefaultRuleSet)
for parse in parser.parse("you prefer that cake".split()):
    chart.printCCGDerivation(parse)
    break


for parse in parser.parse("that is the cake which you prefer".split()):
    chart.printCCGDerivation(parse)
    break

for parse in parser.parse("that is the cake which we will persuade the chef to cook".split()):
    chart.printCCGDerivation(parse)
    break

for parse in parser.parse("that is the cake which we will persuade the chef to give the children".split()):
    chart.printCCGDerivation(parse)
    break

for parse in parser.parse("that is the dough which you will eat without cooking".split()):
    chart.printCCGDerivation(parse)
    break




test1_lex = '''
    :- S,N,NP,VP
    I => NP
    you => NP
    will => S\\NP/VP
    cook => VP/NP
    which => (N\\N)/(S/NP)
    and => var\\.,var/.,var
    might => S\\NP/VP
    eat => VP/NP
    the => NP/N
    mushrooms => N
    parsnips => N
    '''


test2_lex = '''
    :- N, S, NP, VP
    articles => N
    the => NP/N
    and => var\\.,var/.,var
    which => (N\\N)/(S/NP)
    I => NP
    anyone => NP
    will => (S/VP)\\NP
    file => VP/NP
    without => (VP\\VP)/VP[ing]
    forget => VP/NP
    reading => VP[ing]/NP
    '''


lex = lexicon.fromstring(test1_lex)
parser = CCGChartParser(lex, ApplicationRuleSet + CompositionRuleSet + SubstitutionRuleSet)
for parse in parser.parse("I will cook and might eat the mushrooms and parsnips".split()):
    printCCGDerivation(parse)



lex = lexicon.fromstring(test2_lex)
parser = CCGChartParser(lex, ApplicationRuleSet + CompositionRuleSet + SubstitutionRuleSet)
for parse in parser.parse("articles which I will file and forget without reading".split()):
    printCCGDerivation(parse)
