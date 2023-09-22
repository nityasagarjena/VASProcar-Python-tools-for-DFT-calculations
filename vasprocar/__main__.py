# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import os
import sys
import shutil

version = '1.1.18.7'
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

dir_files = os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#------------------------------------------------------------------------------
# Adding the contribution of all orbitals to the Spin components (Sx|Sy|Sz) ---
#------------------------------------------------------------------------------
Orb_spin = [1]*16

#----------------------------------------------------
# src directory to the main python codes ------------
#----------------------------------------------------

main_dir = 'src/'

run = main_dir + '_dft.py'
exec(open(run).read())

run = main_dir + 'inputs/' + 'inputs.py'
exec(open(run).read())

#----------------------------------------------------
# code execution ------------------------------------
#----------------------------------------------------

if (len(inputs) == 0 and DFT == '_?/'):

   print("######################################################################")
   print("# Which package was used for the DFT calculations? ===================")
   print("# [1] VASP (Vienna Ab initio Simulation Package)                      ")
   print("# [2] QE   (Quantum ESPRESSO)                                         ")
   print("######################################################################")   
   pacote_dft = input(" "); pacote_dft = int(pacote_dft)
   print(" ")

   if (pacote_dft == 1): DFT = '_VASP/' 
   if (pacote_dft == 2): DFT = '_QE/'

if (DFT == '_VASP/'):
   print("######################################################################")
   print("## VASP (Vienna Ab initio Simulation Package) ===================== ##")
   print("## ================================================================ ##")
   print("# Basic files to execute the code: CONTCAR, KPOINTS, OUTCAR, PROCAR ##")
   print("# For other features: DOSCAR, LOCPOT, WAVECAR or vasprun.xml        ##")
   print("######################################################################")   
   print(" ")

if (DFT == '_QE/'):
   print("######################################################################")
   print("## QE (Quantum ESPRESSO) >> Tested version: 6.4.1 ================= ##")
   print("## ================================================================ ##")
   print("# Basic files to execute the code: scf.in, scf.out, nscf.in,        ##")
   print("#                                  nscf.out, bands.in, bands.out    ##")
   print("# For other features: projwfc.in, projwfc.out, "filband",           ##")
   print("#                     "filproj".projwfc_up and "filpdos".pdos_atm   ##")
   print("######################################################################")   
   print(" ")
   #---------------------
   read_contribuicao = 0
   read_projwfc_up = 0

if (len(inputs) == 0):
   run = main_dir + '_settings.py'
   exec(open(run).read())

if (len(inputs) > 0):
   for inp in range(len(inputs)): 
       #---------------------------------------------------------------------------
       exec(open(dir_files + '/inputs/' + 'input.vasprocar.' + inputs[inp]).read())
       #---------------------------------------------------------------------------
       if (inputs[inp] == 'bands'):     opcao = -10
       if (inputs[inp] == 'spin'):      opcao = -20  
       if (inputs[inp] == 'orbitals'):  opcao = -30
       if (inputs[inp] == 'dos'):       opcao = -31  
       if (inputs[inp] == 'location'):  opcao = -32     
       #--------------------------------------------------------------------
       run = main_dir + '_settings.py'
       exec(open(run).read())
