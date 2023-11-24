Les types en Python
===================

Chaque variable en Python possède un **type**. Selon la valeur attribuée à une variable, Python lui associe un type.

Il existe différents types de variables qu’on peut classer en 2 catégories:

1. le type de base : entier, flottant, chaine de caractères, booléen, …
2. le type construit : liste, dictionnaire, objet, …

.. important::

    En python, le type d'une variable peut changer selon le contexte. Une variable peut être un nombre puis devenir une chaine de caractères ou inversement.

Les types de nombres
--------------------

Une variable peut désigner un nombre. Ce nombre peut être de type **entier** ou de type **flottant** c’est à dire écrit avec une virgule (un point en fait).

En Python, le type entier se note **int** et le type flottant se note **float**.

On peut utiliser des **opérateurs** mathématiques comme la somme (+), la différence (-), le produit (*) et le quotient (/) pour effectuer des calculs.

Selon l’opérateur, le résultat peut avoir un type différent des valeurs avant le calcul. Par exemple, le quotient de 2 nombres entiers peut donner un résultat à virgule, donc un flottant.

En plus des 4 opérations mathématiques, il existe en Python des opérateurs mathématiques tels que:

.. csv-table:: Opérateurs python
   :header: "Opérateur", "Description"
   :align: center
   :widths: 10, 30
   :file: operateur.csv
      
   
.. admonition:: Exemple

    1. Les variables `a` et `b` ont des valeurs entières donc sont de type **int**

    >>> a,b = 8,5
    
    2. On calcule le quotient des variables `a` et `b` que l'on affecte à la variable `c`:
    
    >>> c = a/b
    
    La variable `c` a pour valeur :math:`1.6` donc elle de type **float**

    3. On calcule le quotient entier des variables `a` et `b` que l'on affecte à la variable `d`:
    
    >>> d = a // b
    
    La variable `d` vaut :math:`1` donc elle est de type **int**.
    
    4. On calcule le reste entier des variables `a` et `b` que l'on affecte à la variable `r`: 
    
    >>> r = a%b
    
    La variable `r` a pour valeur 3 donc elle est de type entier.

Le type chaine de caractères
----------------------------

Une variable de type **string** est une variable dont la valeur est
constitué de lettres, chiffres, espaces et de tout caractère
alphanumérique et de symboles.

L’affectation d’une chaîne de caratère à une variable se fait en notant
la chaine entre guillemets doubles “*chaine de caratères*” ou simples
‘*chaine de caratères*’.

Des chaines de caratères peuvent être réunies en une seule chaine de
caratères par **concaténation**.

Les opérateurs de concaténation sont la somme (+) et la multiplication
(*).

.. admonition:: Exemple

    1. On crée les variables txt1 et txt2 de type string:

    >>> txt1 = "La vie est belle "
    >>> txt2 = 'mais cruelle parfois!'
    
    On concatène ces deux chaines dans la variable `txt`:
    
    >>> txt = txt1 + txt2
    
    La variable `txt` contient la chaine "La vie est belle mais cruelle parfois!".

    2. On crée la variable `motif` qui contient 10 fois le caractère \#.
    
    >>> motif = '#' * 10

Un type construit : la liste
----------------------------

En Python, il existe le type **list** qui permet de regrouper **plusieurs valeurs** dans une même variable. Les valeurs d’une liste sont notées entre crochets et séparées par une virgule.

.. admonition:: Exemple

    On veut regrouper les nombres 4, 5 et 6 dans une même variable `L`:
    
    >>> L = [4,5,6]

Chaque valeur d’une liste est repérée par sa position appelée
**indice**.

-  La première valeur a pour indice ``0``,
-  la deuxième valeur a pour indice ``1`` et
-  la dernière valeur a pour indice ``le nombre de valeurs - 1``

.. tip::

   On peut aussi utiliser des indices négatifs ! La dernière valeur d'une liste a pour indice `-1`, l'avant dernière a pour indice `-2`, etc.

On peut modifier les valeurs d’une liste en utilisant les indices et en
réalisant une nouvelle affectation.

.. admonition:: Exemple

    La liste `L` contient les valeurs 4, 5 et 6.
    
    >>> L = [4,5,6]
    
    1. On modifie la première valeur de la liste `L`:
    
    >>> L[0] = 8
    
    La liste `L` contient les valeurs 8, 5 et 6.
    
    2. On change la seconde valeur de la liste en la multipliant par 2:
    
    >>> L[1] = L[1] * 2
    
    La liste contient les valeurs 8, 10 et 6.
