
import os
import sys
import site
import shutil
import subprocess

#---------------------------------------------------
# Instalation directory ----------------------------
#---------------------------------------------------

version = 'VASProcar_v1.1.10'

dir_inst = site.USER_SITE + '/vasprocar'

#----------------------------------------------------------------------
# Copying VASProcar folder to the main directory ----------------------
#----------------------------------------------------------------------

if os.path.isdir(dir_inst):
   shutil.rmtree(dir_inst)
else:
   0 == 0

shutil.copytree(version, dir_inst)

print("")
print("###################################################################")
print("#################  Instalation was completed !!!  #################")
print("###################################################################")
print("")
print("===================================================================")
print("Instructions to execute:                                           ")
print("                                                                   ")
print(">>  Go to a directory containing the DFT outpout files             ")
print("                                                                   ")
print(">>  Type the following comand:                                     ")
print("    python -m vasprocar   or   python3 -m vasprocar   or   python3.? -m vasprocar ")
print("                                                                   ")
print("*** RUN IT WITH YOUR PYTHON VERSION OR WITH ***                    ")
print("*** THE VERSION OF YOUR INSTALLATION DIRECTORY ***                 ")
print("--------------------------------------------------                 ")
print(f'Installation Directory: {dir_inst}                                ')
print("--------------------------------------------------                 ")
print("END !                                                              ")
print("===================================================================")
print("")
      
print("##########################################################")
print("# Manual software installation is recommended:           #")
print("# ====================================================== #")
print("# VESTA: http://jp-minerals.org/vesta/en/download.html   #")
print("# ------------------------------------------------------ #")
print("# 3D Visualization of the Crystalline lattice (CONTCAR), #")
print("# charge density (PARCHG) and Potential (LOCPOT)         #")
print("# ====================================================== #")
print("# Grace: https://plasma-gate.weizmann.ac.il/Grace/       #")
print("#        or https://www.onworks.net/software/app-qtgrace #")   
print("# ------------------------------------------------------ #")  
print("# Plot, Edit and View 2D Graphs                          #")
print("##########################################################")
print(" ")

#----------------------------------------------------------------------
# Installation / Updating the necessary modules -----------------------
#----------------------------------------------------------------------

print("===================================================================")
print(" Would you like to update and install all necessary dependencies?  ")
print(" modules: numpy|scipy|matplotlib|plotly|moviepy|kaleido            ")
print(" ----------------------------------------------------------------- ")
print(" [0] NO                                                            ")
print(" [1] YES                                                           ")
print("===================================================================")
modulos = input(" "); modulos = int(modulos)
print(" ")

if (modulos == 1):

   # ---------------------------------------------------------
   # package_list_to_instal ----------------------------------
   # ---------------------------------------------------------
   
   packages = [
   "pip",
   "numpy", 
   "scipy", 
   "matplotlib", 
   "moviepy",
   "plotly",
   "kaleido"
   ]

   for i in range(len(packages)):
       subprocess.run(["pip", "install", "--upgrade", packages[i]])
       print("[OK] " + packages[i])

   print(" ")
   print("##########################################################")
   print("################ Everything is up to date ################")
   print("##########################################################")
   print(" ")
