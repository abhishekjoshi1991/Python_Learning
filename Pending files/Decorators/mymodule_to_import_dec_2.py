#importing directly make_pretty decorator definition from DecDef module

from Decorators.DecDef import make_pretty

@make_pretty
def extraordinary():
    print('i am from extraordinary')

extraordinary()
