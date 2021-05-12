from random import uniform
from math import *

# Le compteur de points qui sont dans la courbe de la fonction.
c = 0

# Le nombre de points que l'on veut tirer au hasard.
n = 1000000

# L'intervalle compris entre a et b, soit [a,b] :
a = 0
b = pi/2
# On prend la valeur minimale sur l'intervalle.
fmax = 0
# On crée une liste des f_i(x) calculés.
liste_f_i = []
assert (a < b)
for i in range(0, n):
    x = uniform(a,b)
    # On définie notre fonction et ses valeurs prises.
    f_i = exp(x)*sin(x)
    # On remplie la liste avec les valeurs trouvées.
    liste_f_i.append(f_i)
    # On crée f_max(x), la valeur maximale pour pouvoir créer y. (On compare tous les f_i à la valeur minimale
    # pour trouver la valeur max
    fmax = max(f_i, fmax)
    # On s'assure que les valeurs de f_i sont positives.
    assert (f_i >= 0)
# On crée une boucle sur les valeurs de la liste et on les compare à y, si y est plus petit, alors il est
# dans l'aire de la fonction.
for f_i in liste_f_i:
    # On crée les y, compris entre 0 et fmax.
    y = uniform(0, fmax)
    if y <= f_i:
        # On incrémente le compteur.
        c = c + 1

# Le rapport établi entre la proportion de l'aire_courbe et l'aire_totale. (Points_courbes/Points_totaux).
Aire_courbe = (c / n) * ((b-a)*fmax)
print(Aire_courbe)
print(f"L'aire éstimée sur l'intervalle [{a}, {b}] est : {Aire_courbe} .")
