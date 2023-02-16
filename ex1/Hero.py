from ex1.Person import Person


class Hero(Person): 
    _power : str 

    def __init__ (self, nom : str, prenom : str, power : str):
        super().__init__(nom, prenom)
        self._power = power 
        
