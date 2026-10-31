import pyxel, random

LARGEUR, HAUTEUR = 700, 210

# (x, y, largeur, hauteur, couleur)

FUSEE = [
    (450, 2, 35, 4, 1), (450, 16, 35, 4, 1), (485, 5, 6, 4, 1),
    (485, 13, 6, 4, 1), (491, 8, 10, 6, 1), (450, 5, 4, 11, 1),
]
FEU = [
    (420, 5, 30, 4, 3), (425, 9, 25, 4, 7), (420, 9, 5, 6, 3),
    (420, 13, 30, 4, 3), (415, 9, 5, 4, 3),
]
PARTICULES = [
    (410, 9), (400, 10), (405, 12), (395, 6), (392, 11),
    (390, 5), (386, 13), (382, 9), (376, 14), (407, 6),
]
DECOR = [
    # limites
    (0, 22, 2, 190, 3), (0, 20, 700, 2, 3), (0, 208, 700, 2, 3), (698, 22, 2, 190, 3),
    # cadre
    (0, 0, 2, 20, 3), (0, 0, 700, 2, 3), (698, 0, 2, 20, 3),
    (295, 2, 2, 18, 12), (295, 2, 75, 2, 12), (295, 18, 75, 2, 12),
    (370, 2, 2, 18, 12), (615, 2, 2, 18, 3),
    # ligne de départ
    (25, 22, 4, 186, 10),
]


class Joueur:
    def __init__(self, nom, x, y, touches, couleur):
        self.nom = nom
        self.depart = (x, y)
        self.x, self.y = x, y
        self.droite, self.gauche, self.bas, self.haut = touches
        self.couleur = couleur

    def deplacer(self):
        if pyxel.btn(self.droite) and self.x < 685:
            self.x += 2
        if pyxel.btn(self.gauche) and self.x > 2:
            self.x -= 2
        if pyxel.btn(self.bas) and self.y < 199:
            self.y += 2
        if pyxel.btn(self.haut) and self.y > 23:
            self.y -= 2

    def toucher(self, objet, largeur, hauteur):
        return (objet[0] <= self.x + 13 and objet[1] <= self.y + 9
                and objet[0] + largeur >= self.x and objet[1] + hauteur >= self.y)


class Jeu:
    def __init__(self):
        pyxel.init(LARGEUR, HAUTEUR, title="Valoche invasion")

        self.joueur1 = Joueur("PLAYER 1", 6, 100,
                              (pyxel.KEY_RIGHT, pyxel.KEY_LEFT, pyxel.KEY_DOWN, pyxel.KEY_UP), 12)
        self.joueur2 = Joueur("PLAYER 2", 6, 139,
                              (pyxel.KEY_D, pyxel.KEY_Q, pyxel.KEY_S, pyxel.KEY_Z), 14)
        self.joueurs = [self.joueur1, self.joueur2]

        self.gagnant = None
        self.ennemis_liste = []
        self.fin_liste = []

        pyxel.run(self.update, self.draw)

    def ennemis_creation(self):
        if pyxel.frame_count % 5 == 0:
            self.ennemis_liste.append([random.randint(35, 665), 22])

    def fin_creation(self):
        if pyxel.frame_count % 100000 == 0:
            self.fin_liste.append([688, 115])

    def ennemis_deplacement(self):
        for ennemi in self.ennemis_liste:
            ennemi[1] += 1.9
        self.ennemis_liste = [e for e in self.ennemis_liste if e[1] <= 220]

    def collisions(self):
        for joueur in self.joueurs:
            for ennemi in self.ennemis_liste:
                if joueur.toucher(ennemi, 8, 40):
                    joueur.x, joueur.y = joueur.depart
            if self.gagnant is None:
                for fin in self.fin_liste:
                    if joueur.toucher(fin, 10, 10):
                        self.gagnant = joueur

    def ecran_fin(self):
        if self.gagnant is not None:
            for joueur in self.joueurs:
                if joueur is not self.gagnant:
                    joueur.x, joueur.y = 1900, 1900
            self.gagnant.x, self.gagnant.y = 465, 7

    def update(self):
        for joueur in self.joueurs:
            joueur.deplacer()

        self.ennemis_creation()
        self.fin_creation()
        self.ennemis_deplacement()
        self.collisions()
        self.ecran_fin()

    def draw(self):
        pyxel.cls(0)

        for joueur in self.joueurs:
            pyxel.rect(joueur.x, joueur.y, 13, 9, joueur.couleur)

        for r in FUSEE + FEU + DECOR:
            pyxel.rect(*r)
        for x, y in PARTICULES:
            pyxel.rect(x, y, 2, 2, 7)

        for ennemi in self.ennemis_liste:
            pyxel.rect(ennemi[0], ennemi[1], 8, 40, 13)
        for fin in self.fin_liste:
            pyxel.rect(fin[0], fin[1], 10, 10, 10)

        pyxel.text(5, 8, 'PLAYER 1: FLECHES DIRECTIONNELLES', 12)
        pyxel.text(150, 8, 'PLAYER 2: Z Q S D', 14)
        pyxel.text(302, 8, 'VALOCHE INVASION', 8)
        pyxel.text(620, 8, 'WINNER: ', 10)

        if self.gagnant is not None:
            pyxel.text(650, 8, self.gagnant.nom, self.gagnant.couleur)
            pyxel.text(305, 115, self.gagnant.nom + ' WINS', self.gagnant.couleur)


Jeu()