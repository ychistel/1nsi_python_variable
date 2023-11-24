Structure conditionnelle en Python
==================================

Les tests
---------

Un test compare des valeurs et renvoie un booléen : **True** ou **False**

Les opérateurs de comparaison sont:

-  :math:`==` pour comparer deux valeurs égales : :math:`a==3`,
-  :math:`!=` pour comparer deux valeurs non égales.
-  :math:`<`, :math:`>`, :math:`<=` et :math:`>=` pour comparer comme en maths : :math:`<`, :math:`>`, :math:`\leqslant` et :math:`\geqslant`.

Les opérateurs NOT, AND et OR peuvent être utilisés avec les tests donnant des expressions booléennes.

.. admonition:: Exemple

   Soit la variable :code:`a=5` :

   - :code:`a < 3` est `False`
   - :code:`a != 0` est `True`
   - :code:`a > 0 and a <= 5` est `True`
   - :code:`a < 0 or a != 5` est `False`
   - :code:`not a == 5`  est `False`

si / if
-------

On peut soumettre l’exécution d’une instruction à une condition.

La structure est de la forme:

.. code:: python

   if test:
      instructions

Le test renvoie une valeur booléenne.

-  Si la valeur du test est **True**, les instructions sont exécutées;
-  Si la valeur du test est **False**, aucune instruction est exécutée.

.. admonition:: Exemple

   .. code-block:: python
   
      if a >= 0:
            print("Le nombre a est positif")
   
   Si la variable `a` est positive ou nulle, alors l'affichage du message est réalisé.
   Dans le cas contraire, aucune instruction n'est exécutée.

si … sinon / if … else
----------------------

Lorsque le test de la condition **if** est **False**, il est possible d’exécuter d’autres instructions. Elles sont introduites par le mot **else**. La structure ``if ... else`` permet de gérer les exceptions à la condition.

La structure devient :

.. code:: python

   if test:
      instructions # le test a renvoyé True
   else:
      autres instructions # le test a renvoyé False

.. admonition:: Exemple

   .. code-block:: python
    
      if a >= 0:
         print("Le nombre a est positif")
      else:
         print("Le nombre a est négatif")
    
   Si la variable ``a`` est positive ou nulle, alors l'affichage du message "Le nombre a est positif" est réalisé.
   Sinon (le nombre est négatif) le message "Le nombre a est négatif" est réalisé.

.. warning::

   Il n'y a pas de test placé après le ``else``. Cela correspond à tous les autres cas de figures ne vérifiant pas le test.

si … sinon si / if … elif
-------------------------

La commande else **ne contient pas de test**. Il est possible de soumettre un nouveau test avec la commande **elif**. La structure est alors de la forme:

.. code:: python

   if test 1:
      instructions # test 1 est vrai
   elif test 2:
      autres instructions # test 1 est faux et test 2 est vrai
   elif test 3:
      encore des instructions # test 2 faux et test 3 vrai
   else:
      les dernières instructions # les 3 tests sont faux

.. warning::

   Le dernier ``else`` traitant les autres cas de figure n'est pas obligatoire.

.. admonition:: Exemple

   .. code-block:: python
   
      if a>0:
         print("Le nombre a est strictement positif")
      elif a<0:
         print("Le nombre a est strictement négatif")
      else:
         print("Le nombre a est nul")  
