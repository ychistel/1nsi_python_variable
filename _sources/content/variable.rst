.. 1NSI

La variable en Python
=====================

.. toctree::
   :maxdepth: 1
   
Dans les langages de programmation, une **variable** est définie par un nom et associée à un espace mémoire.

-  le nom de la variable peut être une lettre, un mot de plusieurs lettres ou une combinaison alphanumérique (lettres et chiffres) mais qui ne commence pas par un chiffre.
-  l’espace mémoire permet de stocker la valeur associée à la variable pendant l’exécution du programme.

.. admonition:: Exemple

   Voici des exemples de variables:

   - Une variable qui représente un nombre : `i`, `n`, `x`, `y`, etc.
   - Une variable qui représente une chaine de caractères : `mot`, `nom`, `texte`, etc.
   - Deux variables qui représentent des grandeurs similaires peuvent avoir des noms proches mais qui se différencient par un chiffre placé à la fin : `mot1` et `mot2` ou `x_1` et `x_2`, etc.

Créer une variable en python
----------------------------

Donner une valeur à une variable est une **affectation**. L’affectation se fait avec le signe mathématique égal ``=``.

Pour affecter une valeur à une variable, on écrit toujours en premier le nom de la variable, puis le signe ``=`` et enfin la valeur qu’on lui
attribue.

.. admonition:: Exemple

   On déclare trois variables `a`, `b` et `c` en affectant respectivement les valeurs 4, 5 et 6.

   >>> a=4
   >>> b=5
   >>> c=6

.. note::

   Souvent, on écrit une affection par ligne. Il est possible d’affecter plusieurs variables sur une même ligne.

   >>> a,b,c = 4,5,6 # a vaut 4, b vaut 5 et c vaut 6
   >>> x,y = 1 # x vaut 1 et y vaut 1

Les types de variables
----------------------

Une variable peut mémoriser différents **types** de valeurs :

-  des nombres entiers : la variable est de type ``int``

   >>> n = 7 # n est de type int
   
-  des nombres à virgule : la variable est de type ``float``

   >>> x = 1.25 # x est de type float; attention la virgule est un point!
   
-  des chaines de caractères : la variable est de type ``str`` ; un chaine de caractères se note entre quote simple ou double!

   >>> m = "bonjour" # m est de type str

-  des booléens ``True`` ou ``False``: la variable est de type ``bool``.

   >>> t = False


Modifier la valeur d'une variable
---------------------------------

On peut modifier la valeur d'une variable

#. Sans tenir compte de sa valeur actuelle. Il suffit de lui affecter une nouvelle valeur.

   >>> a = 2
   >>> a = 3 # on a modifié la variable ``a``

#. En tenant compte de sa valeur. Par exemple, on souhaite ajouter 2 à la valeur d'une variable ``x``. On écrit alors l'instruction:

   >>> x = 3
   >>> x = x + 2

   Le langage procède de droite à gauche:

   - il calcule d'abord la valeur ``x+2`` avec la valeur actuelle de la variable ``x``;
   - ensuite il affecte la nouvelle valeur à la variable ``x``.

Plusieurs valeurs dans une variable
-----------------------------------

Une variable peut contenir plusieur valeurs. Dans ce cas, la variable est de type ``tableau``. On accède aux valeurs avec les **indices** de leur position dans le tableau.

Les valeurs d'un tableau se notent entre crochets et chaque valeur est séparée des autres par une virgule.

.. admonition:: Exemple

   On veut une variable qui contient les valeurs 3, 4 et 5:

   >>> t = [3,4,5]
   >>> t[0]
   3
   >>> t[1]
   4
   >>> t[2]
   5
