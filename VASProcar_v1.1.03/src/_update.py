
import os
import sys
import site
import shutil
import subprocess                                                   

print("##########################################################")
print("# Recomenda-se a instalacao manual dos softwares:        #")
print("# ====================================================== #")
print("# VESTA: http://jp-minerals.org/vesta/en/download.html   #")
print("# ------------------------------------------------------ #")
print("# Visualizacao 3D da Rede Cristalina (CONTCAR),          #")
print("# Densidade de carga (PARCHG) e do Potencial (LOCPOT)    #")
print("# ====================================================== #")
print("# Grace: https://plasma-gate.weizmann.ac.il/Grace/       #")
print("#        or https://www.onworks.net/software/app-qtgrace #")   
print("# ------------------------------------------------------ #")  
print("# Plot, Edicao e Visualizacao de Graficos 2D             #")
print("##########################################################")

#----------------------------------------------------------------------
# Instalação/Atualização de Modulos Python ----------------------------
#----------------------------------------------------------------------

print(" ")
print("===================================================================")
print("Deseja Instalar/Atualizar os modulos Python necessarios a correta  ")
print("execucao de todas as funcionalidades do VASProcar ?                ")
print("-------------------------------------------------------------------")
print("[0] NAO                                                            ")
print("[1] SIM                                                            ")
print("===================================================================")
modulos = input(" "); modulos = int(modulos)
print(" ")

if (modulos == 1):

   # ---------------------------------------------------------
   # package_list_to_instal ----------------------------------
   # ---------------------------------------------------------
   
   packages = [
   "pip",
   "os", 
   "sys",
   "shutil",
   "numpy", 
   "scipy", 
   "matplotlib", 
   "plotly",
   "moviepy"
   ]

   for i in range(len(packages)):
       subprocess.run(["pip", "install", "--upgrade", packages[i]])
       print("[OK] " + packages[i])

   print(" ")
   print("##########################################################")
   print("## Instalacao/Atualizacao dos Modulos Python concluida: ##")
   print("##########################################################")
   print(" ")

#=======================================================================
# Opcao do usuario de realizar outro calculo ou finalizar o codigo =====
#=======================================================================
execute_python_file(filename = '_loop.py')   
