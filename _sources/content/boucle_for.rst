La boucle for
=============
    
Une instruction répétée 100 fois n’est pas écrite 100 fois dans le programme. On utilise une boucle.

La structure de boucle est appelée une structure **itérative** et chaque répétition est une **itération**.

Une boucle est **bornée** lorsqu'elle répète un **nombre fixe** de fois une ou plusieurs instructions. Ce **nombre fixe** doit être connu avant l’exécution de la boucle.

.. note::

    1. Les instructions contenues dans une **boucle** constituent un mini programme qui sera exécuté autant de fois que la boucle le demande.
    2. Une **boucle** peut contenir d'autres **boucles**. On parle alors de boucles imbriquées.

La boucle ``for`` est une boucle **bornée**. Elle s'utilise avec l'instruction ``range`` qui construit une séquence de nombres entiers régulièrement espacés. L'instruction ``range`` a différents paramètres:

-  ``range(n)`` renvoie la séquence de nombres entiers positifs de :math:`0` jusqu’à :math:`n-1`.
-  ``range(p,n)`` renvoie la séquence de nombres entiers positifs de :math:`p` jusqu’à :math:`n-1`.
-  ``range(p,n,k)`` renvoie la séquence de nombres entiers positifs de :math:`p`, :math:`p+k`, :math:`p+2k`, … jusqu’à :math:`n-1` au plus.

.. admonition:: Exemple

    - :code:`range(8)` est la séquence de nombres entiers de 0 à 7 soit huit valeurs : 0, 1, 2, 3, 4, 5, 6, 7.
    - :code:`range(3,8)` est la séquence de nombres entiers de 3 à 7 soit cinq valeurs : 3, 4, 5, 6, 7.
    - :code:`range(3,8,2)` est la séquence de nombres entiers 3, 5, 7. Elle démarre à 3, progresse de 2 en 2 jusqu'à 8.

.. tip::

    L'exécution de :code:`range(3,8,2)` dans l'interpréteur Python n'affiche pas les valeurs. Pour les afficher, il faut une boucle avec un **print**.



.. admonition:: Exemple

   Pour afficher les 100 premiers nombres entiers, on détermine la séquence de nombres entiers avec range: ``range(1,101)``. Ensuite, avec une boucle ``for`` on peut afficher nos nombres:

   .. code:: python

      for i in range(1,101):
         print(i)

   Ce qui affichera tous les nombres entiers de 1 à 100.
