# memb-curve

## Courbure de membrane

Proposition d'une méthode :

Courbure d'une membrane avec trois points qui représentent des atomes de phosphore :

$$A \space (x_A;y_A;z_A), \space B \space (x_B;y_B;z_B)\space et\space C \space (x_C;y_C;z_C)$$
* La membrane est dans le plan $xOy$
* $A$, $B$ et $C$ sont à moins de $5 \mathring{A}$ de la protéine. On estime qu'ils sont donc  interaction avec la surface.
* $B$ est le point qui a sa coordonnée $z$ la plus faible et est donc le plus inséré dans la membrane.

On calcule toutes les distances $AC$ possibles :
$$AC=\sqrt{(x_C-x_A)^2+(y_C-y_A)^2+(z_C-z_A)^2} $$
On sélectionne les points $A$ et $C$ pour lequel la distance $AC$ est maximale

On calcule les deux autres distances:
$$AB=\sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2} $$
$$BC=\sqrt{(x_C-x_B)^2+(y_C-y_B)^2+(z_C-z_B)^2} $$
On calcule le demi-périmètre $p$ :
$$p=\frac{AB+BC+AC}{2}$$
On détermine la surface $S$ du triangle par la formule de Héron:
$$S=\sqrt{p(p-BC)(p-AC)(p-AB)}$$
On calcule alors le rayon du cercle $R$ circonscrit à ce triangle $ABC$ par la formule:
$$R=\frac{BC\times AC\times AB}{4S}$$
