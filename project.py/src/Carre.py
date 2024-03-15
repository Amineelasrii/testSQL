from src.Rectangle import Rectangle
class Carre(Rectangle):
    def __init__(self, longuer=0):
        super().__init__(longuer, languer)
        if self.langeur==self.longeur:
         self.nom = "carré"