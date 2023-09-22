# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import os
import sys
import site
import shutil
import subprocess                                                   

print("#########################################################################")
print("# DFT2kp: effective kp models from ab-initio data                       #")
print("# --------------------------------------------------------------------- #")
print("# Calculates kp matrix elements from Quantum Expresso ab-initio data    #")
print("# ===================================================================== #")
print("# Authors: Joao Victor V. Cassiano, Augusto L. Araujo,                  #")
print("#          Paulo E. Faria Junior, Gerson J. Ferreira                    #")
print("# ===================================================================== #")
print("# Links:   https://arxiv.org/abs/2306.08554 (Paper)                     #")
print("#          https://gitlab.com/dft2kp/dft2kp (code)                      #")
print("#          https://pypi.org/project/dft2kp  (code)                      #")
print("# ===================================================================== #")
print("# Installation: The installation requires two steps.                    #")
print("# First, one needs to install the python package using pip.             #")
print("# Second, dowload the QE patch and recompile QE with our modifications. #")
print("# For more information, visit the link:                                 #")
print("# https://gitlab.com/dft2kp/dft2kp/-/blob/main/INSTALL.md               #")
print("#########################################################################")

print(" ")
print("=========================================================================")
print("Do you want to install/update the DFT2KP python module?                  ")
print("-------------------------------------------------------------------------")
print("[0] NOT                                                                  ")
print("[1] YES                                                                  ")
print("=========================================================================")
modulo = input(" "); modulo = int(modulo)
print(" ")

if (modulo == 1):
   subprocess.run(["pip", "install", "--upgrade", "dft2kp"])

#=====================================================================
# User option to perform another calculation or end the code =========
#=====================================================================
execute_python_file(filename = '_loop.py')   
