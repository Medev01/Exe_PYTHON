# function that create a menu
def TheMenu(Items, lw, rw):
    print(" Menu ".center(lw + rw, '='))
    for k, v in Items.items():
        print(str(k).ljust(lw, '.') + str(v).rjust(rw) + ' $')

meals = {'sandwich': 15,
          'mini Takos': 20,
          'Big Takos': 30,
          'Burger king': 40,
          'panini': 12,
          'Cripe': 17}

TheMenu(meals, 15, 6)

