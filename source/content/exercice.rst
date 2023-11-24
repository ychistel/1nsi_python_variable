Exercices
=========

Exercice 1
----------

On cherche les réponses sur feuille et on vérifie après sur machine !

1. Quelle est la valeur finale de la variable ``a`` si on saisit les lignes suivantes dans l'interpréteur :

   >>> a = 3
   >>> a = a*2    
   >>> a = a+2    
   >>> a

2. Refaire de même avec :

   >>> a = 2
   >>> b = a*a
   >>> a = a*b
   >>> b = b*a
   >>> b

Exercice 2
----------

On considère la variable ``a`` de valeur 15 et la variable ``b`` de valeur 7 a créer dans l'interpréteur Python ou dans un Notebook CAPYTALE.

#. La variable ``q`` contient la valeur ``a//b``. A quoi correspond la valeur de la variable ``q``?
#. La variable ``r`` contient la valeur ``a%b``. A quoi correspond la valeur de la variable ``r``?
#. La variable ``s`` contient la valeur ``a/2+b/3``. Quel est le type numérique de la variable ``s`` ?
#. La variable ``p`` contient la valeur ``a**2-b**2``. Quel est le calcul effectué pour la variable ``p`` ?

Exercice 3
----------
Dans le monde des shadoks, il n'y a que 4 mots : GA, BU, ZO et MEU. Tous les mots de leur langage s'obtiennent par combinaison de ces mots.

On considère les variables ``a``, ``b``, ``c`` et ``d`` de valeurs respectives 'ga', 'bu', 'zo' et 'meu'.

.. note::

   #. Les chaines de caractères sont **concaténables**. Cela signifie qu'on peut coller 2 chaines de caractères ensemble. Pour réaliser une **concaténation**, on utilise le signe de l'addition ``+``.
   #. Comme en mathématiques, lorsqu'on additionne plusieurs fois le même nombre, on peut utiliser la multiplication.

#. Saisir dans l'interpréteur Python l'instruction : "bon" + "jour". Quelle est la valeur renvoyée ?
#. Donner les instructions Python qui permettent en utilisant les variables ``a``, ``b``, ``c`` et ``d`` d'obtenir:

   a) le mot 'meuga'
   b) le mot 'zobuga'
   c) le bébé qui dit ses premiers mots 'zozozozozo'
   d) le shadock mécontent qui dit 'zobuzobuzobu'
   e) la phrase 'meumeu gaga'
   f) la pensée du jour ponctuée 'zo bumeu gaga, ga meubu zozo!'

Exercice 4
----------

On considère les variables suivantes:

-  ``n`` de type ``int`` (nombre entier) initialisée à 150.

-  ``x`` de type booléen qui vaut ``True`` si ``n`` est divisible par 2. 
-  ``y`` de type booléen qui vaut ``True`` si ``n`` est divisible par 3. 
-  ``z`` de type booléen qui vaut ``True`` si ``n`` est divisible par 5. 

Cet exercice se fait dans l'éditeur python Thonny. Vous devez avoir les fenêtres d'édition, console et variables affichées.

#. Créer un fichier nommé ``variables.py``.
#. Dans l'éditeur, créez les variables ``n``, ``x``, ``y`` et ``z``.
#. Exécuter le code et vérifiez les valeurs des variables affichées.
#. Modifiez la valeur de la variable ``n`` avec le nombre 173 et exécutez le code. Les variables sont-elles toutes égales à ``False``.
#. On fixe le nombre ``n`` à 170. Calculer dans l'interpréteur les valeurs des expressions booléennes suivantes:

   a) ``x and y``
   b) ``x or z``
   c) ``x and y and z``

   A quoi correspondent ces valeurs booléennes ?

Exercice 5
----------

On considère les variables ``jour``, ``date`` et ``mois``.

-  La variable ``jour`` contient des chaines de caractère associées aux jours de la semaine.
-  La variable ``date`` contient des nombres entiers de 1 à 31
-  La variable ``mois`` contient des chaines de caractère associées aux mois de l'année.

#. De quels types sont les variables ``jour``, ``date`` et ``mois``?
#. Créez ces trois variables dans un éditeur Python ou un notebook CAPYTALE.
#. Dans l'interpréteur, écrire les instructions Python qui permettent d'obtenir les valeurs:

   a) lundi
   b) 30
   c) septembre

#. On donne l'instruction suivante:

   >>> jour[3] + " " + str(date[27]) + " " + mois[8]

   a) Que renvoie la commande dans l'interpréteur.
   b) Modifier cette commande pour écrire la date du "samedi 20 mai".