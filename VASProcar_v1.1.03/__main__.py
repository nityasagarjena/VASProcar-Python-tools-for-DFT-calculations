
import os
import sys
import shutil

version = '1.1.03'
url_1 = 'https://doi.org/10.5281/zenodo.6343960'
url_2 = 'https://github.com/Augusto-Dlelis/VASProcar-Tools-Python'

print(" ")
print("######################################################################")
print(f'# VASProcar versão {version} - Python tools for VASP                 ')
print(f'# {url_1}                                                            ')
print(f'# {url_2}                                                            ')
print("######################################################################")
print("# authors:                                                            ")
print("# ====================================================================")
print("# Augusto de Lelis Araujo                                             ")
print("# Federal University of Uberlandia (Uberlândia/MG - Brazil)           ")
print("# e-mail: augusto-lelis@outlook.com                                   ")
print("# ====================================================================")
print("# Renan da Paixao Maciel                                              ")
print("# Uppsala University (Uppsala/Sweden)                                 ")
print("# e-mail: renan.maciel@physics.uu.se                                  ")
print("######################################################################")
print(" ")

print("######################################################################")
print("# Arquivos basicos para execucao: CONTCAR, KPOINTS, OUTCAR e PROCAR   ")
print("# Dependendo do calculo: DOSCAR, LOCPOT, WAVECAR ou vasprun.xml       ")
print("######################################################################")   
print(" ")

dir_files = os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#----------------------------------------------------
# src directory to the main python codes ------------
#----------------------------------------------------

main_dir = 'src/'
run = main_dir + '_settings.py'
exec(open(run).read())
