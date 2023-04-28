# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import os
import sys
import shutil

version = '1.1.15'
VASProcar_name = 'VASProcar version ' + version
url_1 = 'https://pypi.org/project/vasprocar'
url_2 = 'https://doi.org/10.5281/zenodo.6343960'
url_3 = 'https://github.com/Augusto-de-Lelis-Araujo/VASProcar-Python-tools-VASP'

print(" ")
print("######################################################################")
print(f'# {VASProcar_name} Copyright (C) 2023')
print(f'# GNU GPL-3.0 license')
print("# ====================================================================")
print(f'# {url_1} ')
print(f'# {url_2} ')
print(f'# {url_3} ')
print("######################################################################")
print("# Authors:                                                            ")
print("# ====================================================================")
print("# Augusto de Lelis Araujo                                             ")
print("# [2022-2023] CNPEM|Ilum|LNNano (Campinas-SP/Brazil)                  ")
print("# [2007-2022] Federal University of Uberlandia (Uberlândia-MG/Brazil) ")
print("# e-mail: augusto-lelis@outlook.com                                   ")
print("# ====================================================================")
print("# Renan da Paixao Maciel                                              ")
print("# Uppsala University (Uppsala/Sweden)                                 ")
print("# e-mail: renan.maciel@physics.uu.se                                  ")
print("######################################################################")
print(" ")

"""
print("######################################################################")
print("# Which package was used for the DFT calculations? ===================")
print("# [1] VASP (Vienna Ab initio Simulation Package)                      ")
print("# [2] QE   (Quantum ESPRESSO)  !!! In Tests (Not Functional) !!!      ")
print("######################################################################")   
pacote_dft = input(" "); pacote_dft = int(pacote_dft)
print(" ")
"""

pacote_dft = 1

if (pacote_dft == 1):
   DFT = '_VASP/' 
   print("######################################################################")
   print("## VASP =========================================================== ##")
   print("## ================================================================ ##")
   print("# Basic files to execute the code: CONTCAR, KPOINTS, OUTCAR, PROCAR ##")
   print("# For other features: DOSCAR, LOCPOT, WAVECAR or vasprun.xml        ##")
   print("######################################################################")   
   print(" ")

if (pacote_dft == 2):
   DFT = '_QE/'
   print("######################################################################")
   print("## QE ============================================================= ##")
   print("## ================================================================ ##")
   print("# Basic files to execute the code: ???????????????????????????????? ##")
   print("# For other features: ????????????????????????????????????????????? ##")
   print("######################################################################")   
   print(" ")

#====================================================

dir_files = os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#----------------------------------------------------
# src directory to the main python codes ------------
#----------------------------------------------------

main_dir = 'src/'
run = main_dir + '_settings.py'
exec(open(run).read())
