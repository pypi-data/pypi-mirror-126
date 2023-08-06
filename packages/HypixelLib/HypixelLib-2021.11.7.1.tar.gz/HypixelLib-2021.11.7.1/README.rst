.. image:: https://github.com/Kejax/Hypixel-Lib/blob/main/doc/Main.png
	:target: https://hypixel.net
	:alt: Hypixel Lib


The Lib to request Hypixel API
===============================

With this API you're able to get much more info from the public Hypixel API
as from hypixelaPY


Why I should use it?
---------------------

You should use it, because it's a friendly Lib, wich is able to be added by functions


What is included in this Lib?
-----------------------------

This Lib includes nearly all features from the Hypixel API
some features of the Mojang API and the Mojang SessionServer
returns pictures from the `plancke.io <https://plancke.io>`__ picture generator

Import Hypixel-Lib in Python
-----------------------------

.. code:: sh
    
    pip install HypixelLib

.. code:: python

    import HypixelLib
    
Code Examples
^^^^^^^^^^^^^

.. code:: python
    
    import HypixelLib
    
    hypixel = HypixelLib.Hypixel("<APIKEY>")
    
    player = hypixel.player.get(name="name", uuid="uuid")
    print(player.name)
    print(player.rank.name)
    print(player.uuid)