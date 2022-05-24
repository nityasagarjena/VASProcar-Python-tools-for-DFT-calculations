
import os
import sys
import site
import shutil
import subprocess

#---------------------------------------------------
# Obtendo o diretorio de instalação do VASProcar ---
#---------------------------------------------------

version = 'VASProcar_v1.1.03'

dir_inst = site.USER_SITE + '/vasprocar'

#----------------------------------------------------------------------
# Copiando a pasta VASProcar_v1.1.03 para o diretório de instalação ---
#----------------------------------------------------------------------

if os.path.isdir(dir_inst):
   shutil.rmtree(dir_inst)
else:
   0 == 0

shutil.copytree(version, dir_inst)

print("")
print("##################################")
print("###### Instalacao Concluida ######")
print("##################################")
print("")
print("===================================================================")
print("Para executar o codigo, utilize em qualquer diretorio que contenha ")
print("os arquivos de saida do VASP, o seguinte comando:                  ")
print("-------------------------------------------------                  ")
print("python -m vasprocar   ou   python3.? -m vasprocar                  ")
print("                                                                   ")
print("Substitua python3.? pela versao contida no Diretorio de Instalação ")
print(f'------------------------------------------------------------------')
print(f'{dir_inst}                                                        ')

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
print(" ")

#----------------------------------------------------------------------
# Instalação/Atualização de Modulos Python ----------------------------
#----------------------------------------------------------------------

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
   "numpy", 
   "scipy", 
   "matplotlib", 
   "plotly",
   "moviepy",
   "kaleido"
   ]

   for i in range(len(packages)):
       subprocess.run(["pip", "install", "--upgrade", packages[i]])
       print("[OK] " + packages[i])

   print(" ")
   print("##########################################################")
   print("## Instalacao/Atualizacao dos Modulos Python concluida: ##")
   print("##########################################################")
   print(" ")
