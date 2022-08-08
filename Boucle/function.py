def say_hello(name, age = 0)
    print('Bonjour' + name)
    if age > 0:
        print('Tu as %d ans' % (age))

def get_full_name(first_name, last_name):
    return first_name +' ' + last_name

say_hello(get_full_name('Romain', 'Delpierre'), 25)