# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:08:54 2018

@author: schiejak
"""

import os

cesta = os.getcwd()
nazvy_souboru = os.listdir(cesta)
#sem dat vsechny soubory a adresare kterejch se to netyka
nazvy_souboru.remove('prejmenovavac.py')

for nazev in nazvy_souboru:
    os.chdir(cesta + '\\{}'.format(nazev))
    cestaa = cesta + '\\{}'.format(nazev)
    soubory = os.listdir(cestaa)
    for index, soubor in enumerate(soubory):
        stary_meno = soubor
        novy_meno = '{}_{}.png'.format(nazev, index)
        os.rename(stary_meno, novy_meno)