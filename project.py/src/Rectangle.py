class Rectangle:
    def __init__(self, longuer=0, largeur=0,nom= "rectangle"):
        self.nom =nom
        self.longuer = longuer
        self.largeur = largeur

    def surface(self):
        return self.longuer * self.largeur

    def affichage(self):
        print(f"Nom{self.nom},Longueur{self.longuer},Largeur{self.largeur},Surface{self.surface()}")