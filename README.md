# memb-curve

## Theory
<img src="images/sphere.jpg" alt="" width="300">
The aim of this programme is to determine a value for the local curvature of a membrane induced by the adsorption of an agent (protein, DNA, molecule, molecular aggregate, etc.) on its surface. The radius of curvature is identified through a spherical fit of the contacting moities at the membrane vicinity.
Three points $A,B,C$ are considered:
$$
\left\{
    \begin{aligned}
         & A \space (x_A;y_A;z_A)\\
         & B \space (x_B;y_B;z_B) \\
         & C \space (x_C;y_C;z_C) \\
    \end{aligned}
\right.
$$
Two criteria must be taken into account. First, the membrane is located in the xOy plane. Second, points $A$, $B$, and $C$ must be within $5 \mathring{A}$ of the molecule for which you wish to calculate the local curvature. For representing the polar moieties of phospholipicds, only phorsphorus atoms are considered. It is important to note that these criteria may vary depending on the initial orientation of the membrane or the type of macromolecule of interest. A network of points are then obtained and displayed below.


The program identifies point $B$ as the one that is the most deeply embedded in the membrane. Points $A$ and $C$ are then selected so that their distance $AC$ is as large as possible. The $AC$ distances are computed through:
$$AC=\sqrt{(x_C-x_A)^2+(y_C-y_A)^2+(z_C-z_A)^2} $$
With the three points, the two other distances are then computed:
$$\left\{
    \begin{aligned}
         &AB=\sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}\\
         & BC=\sqrt{(x_C-x_B)^2+(y_C-y_B)^2+(z_C-z_B)^2} \\
    \end{aligned}
\right.
$$
Using the Heron property, we can directly obtained the radius of the sphere $R$ which pass through the $A$, $B$ and $C$ points using the following formula:
$$R=\frac{BC\times AC\times AB}{4\sqrt{p\left(p-BC\right)\left(p-AC\right)\left(p-AB\right)}}$$
Where $p$ is defined by:
$$p=\frac{\left(AB+BC+AC\right)}{2}$$

## Method

