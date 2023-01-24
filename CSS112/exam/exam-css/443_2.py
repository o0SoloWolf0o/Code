global animals
animals = ['dogs', 'cats', 'birds', 'insects', 'rats']
inbox1 = ['cars', 'keys', 'computers']
inbox2 = ['chairs', 'cats', 'water']
def check_animals(box):
    founds = False
    for animal in box:
        if animal in animals:
            return animal
            founds = True 
    if not founds: 
        return ("not found")
print(check_animals(inbox2))
print(check_animals(inbox1))
