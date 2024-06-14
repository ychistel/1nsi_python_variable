La variable en programmation
=============================

Dans les langages de programmation, une ``variable`` est associée à un espace mémoire qui va contenir une valeur. Toute variable possède un ``type``. Il existe de nombreux types dont les plus courants sont les nombres entiers ``int``, les nombres flottants (à virgule) ``float`` et les chaines de caractères ``str``.

Une ``variable`` est définie par un nom. Le nom peut être une lettre, un mot de plusieurs lettres ou une combinaison alphanumérique c'est à dire un mélange de lettres et de chiffres.

Voici quelques exemples de noms de variables:

-   Pour représenter un nombre : ``i``, ``n``, ``x``, ``y``.
-   Pour représenter une chaine de caractères : ``mot``, ``nom``, ``texte``.

.. note::

    Lorsque deux variables représentent des grandeurs similaires, on choisit des noms proches mais qui se différencient par un chiffre placé à la fin : ``mot1`` et ``mot2`` ou ``x_1`` et ``x_2``.

La variable en python
----------------------

On crée une variable en Python en écrivant une instruction qui contient le ``nom`` de la variable suivi du signe ``=`` et d'une ``valeur initiale``.

.. code:: python

    variable = valeur initiale


Par exemple, on crée les variables ``a`` et ``b`` en affectant respectivement les valeurs 4 et 5.

>>> a = 4
>>> b = 5

.. note::
    
     Donner une valeur à une variable est une **affectation**. 

Souvent, on écrit une affection par ligne. Il est possible d’affecter plusieurs variables sur une même ligne comme sur l'exemple suivant:

>>> a,b = 4,5 # a vaut 4 et b vaut 5


Les types de variables
-----------------------

Une variable est de type unique. Ce type est attribué avec la valeur donnée à la variable.

-   Si on affecte un nombre entier à une variable alors elle est de type ``int`` (abréviation de integer).

    >>> n = 8
    >>> type(n)
    <class 'int'>

-   Si on affecte un nombre à virgule à une variable, alors elle est de type ``float``.

    >>> a = 1.36
    >>> type(a)
    <class 'float'>

-   Si on affecte une chaine de caractères qui se note entre des guillemets, alors elle est de type ``str`` (abréviation de string).

    >>> mot = 'bonjour'
    >>> type(mot)
    <class 'str'>

-   Si on affecte la valeur ``True`` ou ``False`` à une variable, alors est de type ``bool`` qui signifie **booléen**.

    >>> b = True
    >>> type(b)
    <class 'bool'>

.. caution::

    -   La virgule d'un nombre de type ``float`` est notée par un point. Par exemple ``2,5`` se note ``2.5``.
    -   Les guillemets se notent avec l'apostrophe (single quote) ou avec les guillemets (double quote). Par exemple, la chaine de valeur "bonjour" se note ``'bonjour'`` ou ``"bonjour"``.


Valeurs d'une variable
-----------------------

Une variable créée dans un programme peut changer de valeur. Voici différentes situations conduisant à un changement de valeur.

#.  Une variable peut changer de valeur en lui affectant une nouvelle valeur. Par exemple, une variable ``x`` peut être initialisée à 0 puis modifiée avec la valeur 5.

    >>> x = 0
    >>> x = 5

#.  Une variable peut changer de valeur en tenant compte de sa valeur actuelle. Par exemple, une variable ``x`` est initialisée avec la valeur 3, puis modifiée en lui ajoutant la valeur 2. On écrit alors l'instruction:

    >>> x = 3
    >>> x = x + 2
    >>> x
    5

    Le langage procède de droite à gauche:

    -   il calcule d'abord la valeur ``x+2`` avec la valeur actuelle de la variable ``x``;
    -   ensuite il affecte la nouvelle valeur à la variable ``x``.

#.  En changeant de valeur, une variable peut changer de type. Par exemple, une variable ``x`` initialisée à 0 est de type ``int``. Si on divise la valeur de la variable ``x`` par le nombre 2, le type de la variable ``x`` est alors ``float``.

    >>> x = 0
    >>> x = x / 2
    >>> x
    0.0
    >>> type(x)
    <class 'float'>

.. note::

    Python est un langage à typage dynamique. Cela signifie que les variables créées peuvent changer de type au cours du programme. Il faut y être attentif car cela peut engendrer des erreurs (bugs).

    Certains langages de programmation sont de typage statique ce qui interdit le changement de type des variables.
