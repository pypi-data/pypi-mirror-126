.. ezcolors documentation master file, created by
   sphinx-quickstart on Fri Nov  5 22:57:17 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ezcolors's documentation!
====================================
| A simple library that contains a Color/Colour class for fast and easy definition of colours in python.  

| you can define a colour from:  

| hex -- Colour("#ff00ff")
| RGB -- Colour(255, 0, 255)  
| rgba -- Colour(255, 0, 255, 128)  
| hsl -- Colour(hsl = [270, 100, 50])  
| hsv -- Colour(hsv = [270, 100, 100])  
| colour name -- Colour("Light Purple")  

| with these colours you can then:  

| perform math upon it  
| translate it to any color space  
| compare it to other colours  
| colour a string with ANSI escape sequences  
| generate a colour palette with various different colour harmonies (see palettes module)  

| This package was entirely authored on a Samsung A5 so please excuse any spelling errors etc and let me know if you find any issues  

.. automodule:: ezcolors
    :members:
.. automodule:: ezcolors.Colors
    :members:
.. automodule:: ezcolors.utilities
    :members:
.. automodule:: ezcolors.palettes
    :members:
	
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   readme
	
.. include:: ../README.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
