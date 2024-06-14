Une variable à valeurs multiples
=================================

En python, il existe différents types qui permettent d'avoir des valeurs multiples dans une seule variable. Ce sont les types ``tuple`` et ``list``.

Le n-uplet ou le type ``tuple``
----------------------------------

En python, on peut donner plusieurs valeurs à une variable en les notant entre parenthèses, les valeurs étant séparées par des virgules. C'est ce qu'on appelle un n-uplet de type ``tuple``.

>>> t = (1,2,3)
>>> type(t)
<class 'tuple'>

La variable ``t`` ci-dessus contient 3 valeurs. L'accès à une des valeurs peut se faire de différentes façons.

#.  En utilisant des variables pour chaque valeur du n-uplet:

    >>> a,b,c = t
    >>> print(a)
    1
    >>> print(b)
    2
    >>> print(c)
    3

#.  Chaque valeur a une position précise appelée ``indice``. La première valeur est d'indice ``0``, la seconde valeur est d'indice ``1`` et la troisième valeur est d'indice ``2``. 

    On accède à une valeur en écrivant l'indice de la valeur entre crochets juste après le nom de la variable.

    >>> t[0]
    1
    >>> t[1]
    2
    >>> t[2]
    3

Le tableau ou le type ``list``
-------------------------------

On peut donner plusieurs valeurs à une variable en les écrivant entre crochets, les valeurs étant séparées par des virgules. C'est ce qu'on appelle un tableau de type ``list``.

>>> t = [3,4,5]
>>> type(t)
<class 'list'>

On accède aux valeurs du tableau de la même manière qu'un n-uplet.

#.  En utilisant des variables pour chaque valeur:

    >>> x,y,z = t
    >>> x
    3
    >>> y
    4
    >>> z
    5

#.  En utilisant l'indice de position des valeurs:

    >>> t[0]
    3
    >>> t[1]
    4
    >>> t[2]
    5

Quelle différence entre le type ``tuple`` et le type ``list`` ?
----------------------------------------------------------------

.. note::
    
    En Python, il y a des types **mutables** et des types **immutables**. 
    
    -   Un type est mutable lorsqu'on peut modifier une de ces valeurs. 
    -   Un type est immutable quand on ne peut pas modifier une de ces valeurs.

Les types ``int``, ``float``, ``str`` et ``bool`` sont immutables. Il n'est pas possible de modifier une valeur sans recréer la valeur entière. Par exemple, on ne peut pas changer un chiffre dans un nombre. On ne peut pas non plus changer une lettre dans une chaine de caractères. Il faut réaffecter la variable avec un nouveau nombre ou une nouvelle chaine de caractères.

.. rubric:: L'immutabilité du tuple

Le type ``tuple`` est immutable. Il n'est pas possible de changer une ou plusieurs valeurs du n-uplet. Il faut réaffecter la variable avec un nouveau ``tuple``.

>>> t=(1,2,3)
>>> t[0] = 7
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

L'interpréteur Python renvoie une erreur qui affirme que l'on ne peut pas assigner une valeur à un ``tuple``.

.. rubric:: La mutabilité de list

Le type ``list`` est mutable. Il est possible de changer une valeur du tableau en utilisant son indice.

>>> t = [3,4,5]
>>> t[0] = 1
>>> t
[1,4,5]