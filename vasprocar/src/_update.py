# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import os
import sys
import site
import shutil
import subprocess                                                   

print("##########################################################")
print("# It is recommended to install the software:             #")
print("# ====================================================== #")
print("# VESTA: http://jp-minerals.org/vesta/en/download.html   #")
print("# ------------------------------------------------------ #")
print("# 3D Visualization of the Crystalline Network (CONTCAR), #")
print("# Charge Density (PARCHG) and Potential (LOCPOT)         #")
print("# ====================================================== #")
print("# Grace: https://plasma-gate.weizmann.ac.il/Grace/       #")
print("#        or https://www.onworks.net/software/app-qtgrace #")   
print("# ------------------------------------------------------ #")  
print("# Plot, Edit and View 2D Graphs                          #")
print("##########################################################")

#------------------------------------------------------------------
# Installing/Updating Python Modules ------------------------------
#------------------------------------------------------------------

print(" ")
print("===================================================================")
print("Do you want to install/update the Python modules necessary for the ")
print("correct execution of all VASProcar functionalities?                ")
print("-------------------------------------------------------------------")
print("[0] NOT                                                            ")
print("[1] YES                                                            ")
print("===================================================================")
modulos = input(" "); modulos = int(modulos)
print(" ")

if (modulos == 1):

   # ---------------------------------------------------------
   # package_list_to_instal ----------------------------------
   # ---------------------------------------------------------
   
   packages = [
   'numpy',
   'scipy',
   'matplotlib',
   'plotly',
   'moviepy,
   'kaleido'
   ]  

   for i in range(len(packages)):
       subprocess.run(["pip", "install", "--upgrade", packages[i]])
       print("[OK] " + packages[i])

   print(" ")
   print("##########################################################")
   print("## Installation/Update of Python Modules completed:     ##")
   print("##########################################################")
   print(" ")

#=====================================================================
# User option to perform another calculation or end the code =========
#=====================================================================
execute_python_file(filename = '_loop.py')   
