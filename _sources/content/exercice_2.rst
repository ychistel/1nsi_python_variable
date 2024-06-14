Exercices : n-plets et tableaux
=================================

.. exercice::

    On donne les variables ``a = (8,6,4,2)`` et ``b = [3,5,7]``.

    #.  Quelle variable est de type ``list`` ? Quel est le type de l'autre variable ?
    #.  Donner une instruction qui accède à la dernière valeur des variables ``a`` et ``b``.
    #.  Est-il possible de modifier la première valeur de la variable ``a`` par la valeur 0 ?
    #.  Est-il possible de modifier la première valeur de la variable ``b`` par la valeur 1 ?
    #.  Soit ``c`` la variable égale à la somme des valeurs de la variable ``a`` divisée par la somme des valeurs de la variable ``b``. Écrire une instruction qui calcule la valeur de ``c``.

.. exercice::

    L'aire et le périmètre d'un rectangle se calcule avec les formules suivantes:

    -   Aire du rectangle : ``aire = Largeur * longueur``
    -   Périmètre du rectangle : ``perimetre = 2 * (Largeur + longueur)``

    La variable ``rectangle`` est un n-uplet qui contient la ``largeur`` et la ``longueur`` du rectangle.

    #.  Initialiser la variable ``rectangle`` avec une largeur et une longueur égales respectivement à 7 et 12.
    #.  Créer une variable ``perimetre`` qui calcule le périmètre du rectangle.
    #.  Créer une variable ``aire`` qui calcule l'aire du rectangle.
    #.  Ajouter une instruction d'affichage qui donne les valeurs des différentes variables.

.. exercice::

    La société "The Box" fabrique des boites en carton recyclable. Elle propose sur son site internet la fabrication de boites de forme parallélépipèdique à partir des trois dimensions ``largeur``, ``longueur`` et ``hauteur``.

    On définit la variable ``boite`` de type ``list`` contenant ces trois dimensions.

    #.  Quelle est la valeur de la variable ``boite`` si on fabrique une boite qui a une largeur de 50 cm, une longueur de 75 cm et une hauteur de 40 cm.
    #.  La variable ``volume`` calcule le volume d'une boite. Écrire une formule qui calcule la valeur du volume de la boite avec les valeurs de la variable ``boite``.
    #.  Le prix en euros d'une boite est calculé à partir du volume de celle-ci avec la formule suivante : ``prix = volume * 0.015 + 1.70``. Créer la variable ``prix`` qui donne le prix d'une boite.
    #.  Compléter l'instruction suivante qui affiche les caractéritiques d'une boite en utilisant les différentes variables ci-dessus.

        .. code:: python

            print(f"Une boite de dimensions ... x ... x ... a un volume de ... pour un prix de ... euros.")

.. exercice::

    Voici quelques exemples de températures annuelles moyennes pour des villes en France :

    -   Paris : 12,2 °C
    -   Lyon : 11,9 °C
    -   Marseille : 14,2 °C
    -   Bordeaux : 13,4 °C
    -   Strasbourg : 10,4 °C
    -   Nice : 14,5 °C
    -   Caen : 11,6 °C

    On rassemble les données ci-dessus dans 2 variables contenant les villes et les températures.

    #.  Créer la variable ``villes`` contenant les différentes villes.
    #.  Créer la variable ``temp`` contenant les tempéraures des différentes villes en respectant le même ordre.
    #.  La variable ``i`` est l'indice de position dans les variables ``villes`` et ``temp``. Quelles sont les valeurs possibles de la variable ``i`` ?
    #.  Écrire un programme qui affiche le nom d'une ville et sa température moyenne.

.. exercice::

    On considère les variables ``jour``, ``date`` et ``mois``.

    -   La variable ``jour`` contient des chaines de caractères associées aux jours de la semaine.
    -   La variable ``date`` contient des nombres entiers de 1 à 31
    -   La variable ``mois`` contient des chaines de caractères associées aux mois de l'année.

    #.  De quels types sont les variables ``jour``, ``date`` et ``mois``?
    #.  Créez ces trois variables dans un éditeur Python ou un notebook CAPYTALE.
    #.  Dans l'interpréteur, écrire les instructions Python qui permettent d'obtenir les valeurs:

        a.  lundi
        b.  30
        c.  septembre

    #.  On donne l'instruction suivante:

        >>> jour[3] + " " + str(date[27]) + " " + mois[8]

        a.  Que renvoie la commande dans l'interpréteur.
        b.  Modifier cette commande pour écrire la date du ce jour.

.. exercice::

    Le type ``tuple`` est immutable et le type ``list`` est mutable.

    #.  On écrit le code suivant :

        .. code::

            a = "Alice"
            b = "Bob"
            t = (a,b)
            print(t)

        Quel est l'affichage après exécution de ce programme ?

    #.  On complète ce programme en ajoutant les 2 instructions suivantes :

        .. code::

            a = "Albert"
            print(t)

        Quel est l'affichage après exécution de ce programme ? Comment le justifier ?

    #.  On recommence avec le code suivant :

        .. code::

            a = [4]
            b = [7]
            t = (a,b)
            print(t)

        Quel est l'affichage après exécution de ce programme ?

    #.  On complète ce programme en ajoutant les 2 instructions suivantes:

        .. code::

            a[0] = 1
            print(t)

        Quel est l'affichage après exécution de ce programme ? Comment le justifier ?
