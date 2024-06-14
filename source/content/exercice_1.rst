Exercices : variables et types
===============================

.. exercice::

    L'aire et le périmètre d'un rectangle se calcule avec les formules suivantes:

    -   Aire du rectangle : ``aire = Largeur * longueur``
    -   Périmètre du rectangle : ``perimetre = 2 * (Largeur + longueur)``

    On va écrire un programme qui calcule et affiche l'aire et le périmètre d'un rectangle.

    #.  Créer les variables ``largeur`` et ``longueur`` de valeurs initiales égales à 0.
    #.  Créer une variable ``perimetre`` qui calcule le périmètre du rectangle.
    #.  Créer une variable ``aire`` qui calcule l'aire du rectangle.
    #.  Ajouter l'instruction d'affichage suivante:

        .. code:: python

            print(f'Le rectangle de largeur {largeur} et de longueur {longueur} a un périmètre de {perimetre} et une aire de {aire}.')

    #.  Exécuter votre programme et vérifier les valeurs affichées.
    #.  Modifier les valeurs de la largueur et de la longueur du rectangle puis exécuter votre programme. Vérifier que l'affichage est conforme aux mesures données.

.. exercice::

    On cherche d'abord les réponses et seulement ensuite on vérifie avec l'interpréteur Python !

    #.  Quelle est la valeur finale de la variable ``a`` si on saisit les lignes suivantes dans l'interpréteur :

        >>> a = 3
        >>> a = a*2    
        >>> a = a+2    
        >>> a

    #.  Refaire de même avec :

        >>> a = 2
        >>> b = a*a
        >>> a = a*b
        >>> b = b*a
        >>> b

.. exercice::

    On considère la variable ``a`` de valeur 15 et la variable ``b`` de valeur 7.

    #.  La variable ``q`` est définie par l'instruction:
    
        >>> q = a // b 
        
        À quoi correspond la valeur de la variable ``q``? Quel est le type de la variable ``q`` ?

    #.  La variable ``r`` est définie par l'instruction:
    
        >>> r = a % b
        
        À quoi correspond la valeur de la variable ``r``? Quel est le type de la variable ``r`` ?

    #.  La variable ``s`` est définie par l'instruction:
    
        >>> a / 2 + b / 3
        
        Quel est le type de la variable ``s`` ? Modifier ce calcul pour avoir la varible ``s`` de type ``int`` ?

    #.  La variable ``p`` est définie par l'instruction:
    
        >>> a**2-b**2
        
        Quel est le calcul effectué pour la variable ``p`` ? Quel est le type de la variable ``p`` ?

.. exercice::

    Dans le monde des shadoks, il n'y a que 4 mots : GA, BU, ZO et MEU. Tous les mots de leur langage s'obtiennent par combinaison de ces mots.

    On considère les variables ``a``, ``b``, ``c`` et ``d`` de valeurs respectives ``ga``, ``bu``, ``zo`` et ``meu``.

    .. note::

        #.  Les chaines de caractères sont **concaténables**. Cela signifie qu'on peut coller 2 chaines de caractères ensemble. Pour réaliser une **concaténation**, on utilise le signe d'addition ``+``.

            >>> 'a' + 'b'
            'ab'

        #.  Comme en mathématiques, lorsqu'on additionne plusieurs fois le même nombre, on peut utiliser la multiplication.

            >>> 'a'*3
            'aaa'

    Donner les instructions Python qui permettent en utilisant les variables ``a``, ``b``, ``c`` et ``d`` d'obtenir:

    #.  le mot ``meuga``
    #.  le mot ``zobuga``
    #.  le bébé qui dit ses premiers mots ``zozozozozo``
    #.  le shadock mécontent qui dit ``zobuzobuzobu``
    #.  la phrase ``meumeu gaga``
    #.  la pensée du jour exclamée ``zo bumeu gaga, ga meubu zozo!``

.. exercice::

    On considère les variables suivantes:

    -   ``n`` de type ``int`` (nombre entier) initialisée à 150.
    -   ``x`` de type booléen qui vaut ``True`` si ``n`` est divisible par 2. 
    -   ``y`` de type booléen qui vaut ``True`` si ``n`` est divisible par 3. 
    -   ``z`` de type booléen qui vaut ``True`` si ``n`` est divisible par 5. 

    Cet exercice se fait dans l'éditeur python Thonny. Vous devez avoir les fenêtres d'édition, console et variables affichées.

    #.  Créer un fichier nommé ``variables.py``.
    #.  Dans l'éditeur, créez les variables ``n``, ``x``, ``y`` et ``z``.
    #.  Exécuter le code et vérifier les valeurs des variables affichées.
    #.  Modifiez la valeur de la variable ``n`` avec le nombre 173 et exécutez le code. Les variables sont-elles toutes égales à ``False``.
    #.  On fixe le nombre ``n`` à 170. Calculer dans l'interpréteur les valeurs des expressions booléennes suivantes:

        a.  ``x and y``
        b.  ``x or z``
        c.  ``x and y and z``

        A quoi correspondent ces valeurs booléennes ?