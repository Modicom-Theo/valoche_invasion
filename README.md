# Valoche Invasion

Un jeu de course à deux joueurs en Python avec [Pyxel](https://github.com/kitao/pyxel). Traversez l'écran en évitant les rayons qui tombent du ciel, et atteignez l'arrivée avant votre adversaire !

## But du jeu

Les deux vaisseaux partent de la ligne de départ à gauche. Il faut traverser la zone de jeu jusqu'au carré d'arrivée à droite, sans se faire toucher par les obstacles qui tombent.

- Si un obstacle vous touche, vous retournez à votre point de départ.
- Le premier joueur qui touche le carré d'arrivée gagne la partie.
- Le gagnant est affiché en haut à droite (`WINNER`) et au centre de l'écran.

## Installation

Il faut Python 3 et Pyxel :

```bash
pip install pyxel
```

## Lancer le jeu

```bash
python valoche_invasion.py
```

## Commandes

| Joueur | Couleur | Haut | Bas | Gauche | Droite |
|--------|---------|------|-----|--------|--------|
| Joueur 1 | Bleu | ↑ | ↓ | ← | → |
| Joueur 2 | Rose | Z | S | Q | D |

## Structure du code

Tout le jeu tient dans un seul fichier, `valoche_invasion.py` :

- `Joueur` : position, touches, déplacement et collisions d'un vaisseau.
- `Jeu` : création et déplacement des obstacles, détection de la victoire, affichage.
- Les constantes `FUSEE`, `FEU`, `PARTICULES` et `DECOR` décrivent les éléments fixes dessinés à l'écran.
