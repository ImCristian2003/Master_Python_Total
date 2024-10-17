#imports
from utilidades.decoradores import decorate_turn

#generators

#generator for the perfumery area
@decorate_turn
def perfumery_turn():

    n = 0

    while True:

        n += 1
    
        yield f"P-{n}"


#generator for the pharmacy area
@decorate_turn
def pharmacy_turn():

    n = 0

    while True:

        n += 1

        yield f"F-{n}"


#generator for the cosmetic area
@decorate_turn
def cosmetic_turn():

    n = 0

    while True:

        n += 1

        yield f"C-{n}"