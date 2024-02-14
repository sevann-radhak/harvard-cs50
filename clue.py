import termcolor
from logic import *

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons

knowledge = And(
    (Or(mustard, plum, scarlet)),
    (Or(ballroom, kitchen, library)),
    (Or(knife, revolver, wrench)),
    
    (Implication(mustard, And(Not(plum), Not(scarlet)))),
    (Implication(plum, And(Not(mustard), Not(scarlet)))),
    (Implication(scarlet, And(Not(plum), Not(mustard)))),    
    
    (Implication(ballroom, And(Not(kitchen), Not(library)))),
    (Implication(kitchen, And(Not(ballroom), Not(library)))),
    (Implication(library, And(Not(ballroom), Not(kitchen)))),
    
    (Implication(knife, And(Not(revolver), Not(wrench)))),
    (Implication(revolver, And(Not(knife), Not(wrench)))),
    (Implication(wrench, And(Not(knife), Not(revolver))))
)

knowledge.add(Not(mustard))
knowledge.add(Not(kitchen)) 
knowledge.add(Not(revolver))

knowledge.add(Or(Not(scarlet), Not(library), Not(wrench)))
knowledge.add(Not(plum))
knowledge.add(Not(ballroom))

def check_knoweledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            termcolor.cprint(f"{symbol}: MAYBE", "yellow")
        else:
            termcolor.cprint(f"{symbol}: NO", "red")
    
    
print(knowledge.formula())
print(check_knoweledge(knowledge))