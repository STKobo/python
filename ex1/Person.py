import math


class Person: 
    _nom : str 
    _prenom : str
    _sexe : str 
    _taille : float
    _age : int
    _silhouette : str 
    _poid : float
    
    #Constructeur
    def __init__(self, nom : str, prenom : str):
        self._nom = nom
        self._prenom = prenom
        self._age = 0
        self._sexe = 'Masculin'
        self._taille = 0.5 
        self._silhouette = 'Sportive'
        self._poid = 0.5

    #methode
    def imc(self):
        return self._poid / math.pow(self._taille, 2)

    