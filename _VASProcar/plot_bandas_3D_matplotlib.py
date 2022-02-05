#########################################################################################
## VASProcar -- https://github.com/Augusto-Dlelis/VASProcar-Tools-Python ################
## Autores: #############################################################################
## =================================================================================== ##
## Augusto de Lelis Araujo - Federal University of Uberlandia (Uberlândia/MG - Brazil) ##
## e-mail: augusto-lelis@outlook.com                                                   ##
## =================================================================================== ##
## Renan da Paixão Maciel - Uppsala University (Uppsala/Sweden) #########################
## e-mail: renan.maciel@physics.uu.se                           #########################
#########################################################################################

import os
import shutil
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.colors as mcolors
from scipy.interpolate import griddata
import pandas as pd

print(" ")
print("========== Plotando as Bandas 3D (Matplotlib): ==========")

#======================================================================
#======================================================================
# Gerando o arquivo para Plot 3D via Matplotlib =======================
#======================================================================
#======================================================================

#-----------------------------------------------------------------
# Parâmetros para que este código possa ser executado isoladamente
#-----------------------------------------------------------------
# escolha = ???; tipo_plot = ???; Band_i = ???; Band_f = ???; Plano_k = ???; Dimensao = ??? 

#----------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado
#----------------------------------------------------------------
if os.path.isdir('saida'):
   Diretorio_saida = 'saida/Bandas_3D/'
else:
   Diretorio_saida = ''
#----------------------

banda = np.loadtxt(Diretorio_saida + 'Bandas_3D.dat') 
banda.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(". Pode demorar um pouco .")
print(".........................")

if (Plano_k == 1):     # Plano (kx,ky) ou (k1,k2)     
   eixo1 = banda[:,0]
   eixo2 = banda[:,1]
if (Plano_k == 2):     # Plano (kx,kz) ou (k1,k3)     
   eixo1 = banda[:,0]
   eixo2 = banda[:,2]
if (Plano_k == 3):     # Plano (ky,kz) ou (k2,k3)    
   eixo1 = banda[:,1]
   eixo2 = banda[:,2]

#----------------------------------------------------------------------

E = [0]*((Band_f - Band_i)+2)
number = 0
# E_min = +1000.0
# E_max = -1000.0

#----------------------------------------------------------------------

font = {'family' : 'arial',  
        'color'  : 'black',  
        'weight' : 'normal',  
        'size'   : 13,  
        } 

fig = plt.figure()

# ax = fig.add_subplot(projection="3d")
ax = plt.axes(projection='3d')

# colormap = plt.cm.get_cmap('coolwarm')
# normalize = mcolors.Normalize(vmin = E_min, vmax = E_max)

for i in range (1,(Band_f - Band_i +2)):
    #-----------------------
    energ = banda[:,(i + 2)]
    #-----------------------
    if ((escolha == 6 or escolha == -6) and tipo_plot == 0):
       ax.scatter(eixo1, eixo2, energ, s = 1.0, alpha = 0.9, antialiased = False)
    if ((escolha == 6 or escolha == -6) and tipo_plot == 1):
       ax.plot_trisurf(eixo1, eixo2, energ, alpha = 0.9, cmap = 'coolwarm', edgecolor='black', linewidth = 0.0, antialiased = False)
       # ax.plot_trisurf(eixo1, eixo2, E[number], alpha = 0.9, cmap = colormap, norm = normalize, edgecolor='black', linewidth = 0.0, antialiased = False)
    if ((escolha == 6 or escolha == -6) and tipo_plot == 2):
       ax.plot_trisurf(eixo1, eixo2, energ, alpha = 0.9, cmap = 'coolwarm', edgecolor='black', linewidth = 0.0, antialiased = False)
       ax.scatter(eixo1, eixo2, energ, s = 0.1, alpha = 0.25, color = 'gray', antialiased = False)

    # ax.contourf(X, Y, Z[i], zdir = 'z', alpha = 0.9, offset = #####, cmap = cmap1)

if (Plano_k == 1 and Dimensao != 4):             # Plano (kx,ky)      
   ax.set_xlabel(r'${k}_{x}$', fontdict = font)
   ax.set_ylabel(r'${k}_{y}$', fontdict = font)
if (Plano_k == 2 and Dimensao != 4):             # Plano (kx,kz)      
   ax.set_xlabel(r'${k}_{x}$', fontdict = font)
   ax.set_ylabel(r'${k}_{z}$', fontdict = font)
if (Plano_k == 3 and Dimensao != 4):             # Plano (ky,kz)      
   ax.set_xlabel(r'${k}_{y}$', fontdict = font)
   ax.set_ylabel(r'${k}_{z}$', fontdict = font)

if (Plano_k == 1 and Dimensao == 4):             # Plano (k1,k2)      
   ax.set_xlabel(r'${k}_{1}$', fontdict = font)
   ax.set_ylabel(r'${k}_{2}$', fontdict = font)
if (Plano_k == 2 and Dimensao == 4):             # Plano (k1,k3)      
   ax.set_xlabel(r'${k}_{1}$', fontdict = font)
   ax.set_ylabel(r'${k}_{3}$', fontdict = font)
if (Plano_k == 3 and Dimensao == 4):             # Plano (k2,k3)      
   ax.set_xlabel(r'${k}_{2}$', fontdict = font)
   ax.set_ylabel(r'${k}_{3}$', fontdict = font)   

ax.set_zlabel(r'$E(eV)$', fontdict = font)

# ax.set_xlim((-5,5))
# ax.set_zylim((-5,5))
# ax.set_zlim((-5,5))

ax.view_init(elev = 5, azim = 45)
  
fig = plt.gcf()
fig.set_size_inches(8,6)

plt.savefig(Diretorio_saida + "Bandas_3d.png", dpi = 300, pad_inches = 0)
plt.savefig(Diretorio_saida + "Bandas_3d.pdf", dpi = 300, pad_inches = 0)
# plt.savefig(Diretorio_saida + "Bandas_3d.eps"', dpi = 300, pad_inches = 0)

plt.show()

#-----------------------------------------------------------------------------------------------------------------------------
# Verificando se o arquivo plot_bandas_3D_matplotlib.py ou bandas_3D_matplotlib.py foram copiados para o diretório de saida --
#-----------------------------------------------------------------------------------------------------------------------------

try: f = open(Diretorio_saida + 'plot_bandas_3D_matplotlib.py'); f.close(); Plot_3D = 1
except: Plot_3D = 0

if (Plot_3D == 0):
   try: f = open(Diretorio_saida + 'bandas_3D_matplotlib.py'); f.close(); Plot_3D = 1
   except: Plot_3D = 0

if (Plot_3D == 0):
   source = Diretorio + '\plot_bandas_3D_matplotlib.py'
   destination = r'saida/Bandas_3D\plot_bandas_3D_matplotlib.py'
   shutil.copyfile(source, destination)


#-------------------------------------------------------------------------------------------
# Editando o código no diretório de saida para que ele possa ser executado isoladamente ----
#-------------------------------------------------------------------------------------------

try: f = open(Diretorio_saida + 'plot_bandas_3D_matplotlib.py'); f.close(); Plot_3D = 1
except: Plot_3D = 0 

if (Plot_3D == 1):
   #---------------------------------------------------------------
   codigo = open(Diretorio_saida + 'plot_bandas_3D_matplotlib.py', "r")
   codigo_new = open(Diretorio_saida + 'temp.py', "w")
   #---------------------------------------------------------------
   OLD = '# escolha = ???; tipo_plot = ???; Band_i = ???; Band_f = ???; Plano_k = ???; Dimensao = ???'
   NEW = 'escolha = ' + str(escolha) + '; ' 'tipo_plot = ' + str(tipo_plot) + '; ' 'Band_i = ' + str(Band_i) + '; ' 'Band_f = ' + str(Band_f) + '; ' 
   NEW = NEW + 'Plano_k = ' + str(Plano_k) + '; '  'Dimensao = ' + str(Dimensao)
   #---------------------------------------------------------------
   for line in codigo: codigo_new.write(line.replace(OLD, NEW))  # replacing the string and write to output file
   codigo.close(); codigo_new.close()
   #---------------------------------------------------------------
   os.remove(Diretorio_saida + 'plot_bandas_3D_matplotlib.py')
   os.rename(Diretorio_saida + 'temp.py', Diretorio_saida + 'bandas_3D_matplotlib.py')


#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################
