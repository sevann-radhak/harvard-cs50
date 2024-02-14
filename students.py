from logic import *

# Symbols
math = Symbol("math")  # The student has taken Math
physics = Symbol("physics")  # The student has taken Physics
chemistry = Symbol("chemistry")  # The student has taken Chemistry
biology = Symbol("biology")  # The student has taken Biology
cs = Symbol("cs")  # The student wants to take Computer Science
biochem = Symbol("biochem")  # The student wants to take Biochemistry
quantum = Symbol("quantum")  # The student wants to take Quantum Physics

# Knowledge
knowledge = And(
    # If the student has taken Math and Physics, then they can take Computer Science
    Implication(And(math, physics), cs),
    # If the student has taken Chemistry and Biology, then they can take Biochemistry
    Implication(And(chemistry, biology), biochem),
    # If the student has taken Math and Physics, then they can take Quantum Physics
    Implication(And(math, physics), quantum),
    # The student has taken Math, Physics, and Chemistry
    And(math, physics, chemistry)
)

# Check which courses the student can take
print("Can the student take Computer Science?", model_check(knowledge, cs))
print("Can the student take Biochemistry?", model_check(knowledge, biochem))
print("Can the student take Quantum Physics?", model_check(knowledge, quantum))