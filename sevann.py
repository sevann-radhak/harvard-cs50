from logic import *

cold = Symbol("cold")
hot = Symbol("hot")
# rain = Symbol("rain")
snow = Symbol("snow")
# spring = Symbol("spring")
# storm = Symbol("storm")
summer = Symbol("summer")
# winter = Symbol("winter")

knowledge = And(
    Implication(summer, hot),
    Not(And(cold, hot)),
    Or(cold, hot),
    Implication(snow, cold),
    Implication(hot, Not(snow)),
    summer)
                
print(model_check(knowledge, cold))

