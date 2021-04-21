#importing DecDef decorator module

from Decorators import DecDef

def ordinary():
    print('i am from ordinary')


result = DecDef.make_pretty(ordinary)
result()