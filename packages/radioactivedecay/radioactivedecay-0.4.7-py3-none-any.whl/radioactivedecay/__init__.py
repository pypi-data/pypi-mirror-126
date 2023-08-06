"""
``radioactivedecay`` is a Python package for radioactive decay calculations.
It supports decay chains of radionuclides, metastable states and branching
decays. By default it uses the decay data from ICRP Publication 107, which
contains 1252 radionuclides of 97 elements, and atomic mass data from the
Atomic Mass Data Center.

The code solves the radioactive decay differential equations analytically using
NumPy and SciPy linear algebra routines. There is also a high numerical
precision calculation mode employing SymPy routines. This gives more accurate
results for decay chains containing radionuclides with orders of magnitude
differences between the half-lives.

This is free-to-use open source software. It was created for engineers,
technicians and researchers who work with and study radioactivity, and for
educational use.
"""

__version__ = "0.4.7"

from radioactivedecay.decaydata import DecayData, DEFAULTDATA
from radioactivedecay.inventory import Inventory, InventoryHP
from radioactivedecay.nuclide import Nuclide
