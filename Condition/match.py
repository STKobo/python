nb_bananes: int = 4

match nb_bananes:
    case 1:
        print("manger une banane")
    case 2:
        print("manger les bananes")
    case _:
        print("on en mange pas")