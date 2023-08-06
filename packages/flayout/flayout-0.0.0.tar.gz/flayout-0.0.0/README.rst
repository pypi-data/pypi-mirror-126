FLayout
=======

**F**\ unctional k\ **Layout**.

Installation
------------

It’s best to install FLayout with pip using the ``--user`` flag:

.. code:: sh

   pip install --user flayout

Using the ``--user`` flag, will ensure FLayout will be available in all
your conda environments **as well as** the integrated KLayout python
interpreter.

KLayout Requirements
--------------------

Apart from installing FLayout with pip, a few other KLayout requirements
need to be fulfilled:

-  klayout>=0.27
-  a technology in ``~/.klayout/tech`` with:

   -  a (single) ``.lyp`` file (layer properties file)
   -  a (single) ``.lyt`` file (layer thickness file)
   -  a global environment variable ``$FLAYOUT_TECH`` with the name of
      the technology.
