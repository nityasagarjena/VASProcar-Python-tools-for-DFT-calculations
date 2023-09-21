
import os
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.colors as mcolors
from scipy.interpolate import griddata

print(" ")
print("========== Plotting the 3D Bands (Matplotlib): ==========")

#------------------------------------------------------------------------
# Test to know which directories must be correctly informed -------------
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/Bandas_3D/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# File Structure for Plot via Matplotlib ==============================
#======================================================================
#====================================================================== 

banda = np.loadtxt(dir_output + 'Bandas_3D.dat') 
banda.shape

print(" ")
print(".........................")
print("..... Wait a moment .....")
print(".........................")  
print(". It might take a while .")
print(".........................")

if (Plano_k == 1):     # Plane (kx,ky) or (k1,k2)     
   eixo1 = banda[:,0]
   eixo2 = banda[:,1]
if (Plano_k == 2):     # Plane (kx,kz) or (k1,k3)     
   eixo1 = banda[:,0]
   eixo2 = banda[:,2]
if (Plano_k == 3):     # Plane (ky,kz) or (k2,k3)    
   eixo1 = banda[:,1]
   eixo2 = banda[:,2]

#----------------------------------------------------------------------

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
   
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0

#----------------------------------------------------------------------    

# E = [0]*((Band_f - Band_i)+2)
# number = 0
# E_min = +1000.0; E_max = -1000.0

#----------------------------------------------------------------------

fig = plt.figure()

# ax = fig.add_subplot(projection="3d")
ax = plt.axes(projection='3d')

# colormap = plt.cm.get_cmap('coolwarm')
# normalize = mcolors.Normalize(vmin = E_min, vmax = E_max)

for i in range (1,(Band_f - Band_i +2)):
    #----------------------------------
    energ = banda[:,(i + 2)] + dE_fermi
    #----------------------------------
    if (tipo_plot == 0):
       ax.scatter(eixo1, eixo2, energ, s = 1.0, alpha = 0.9, antialiased = False)
    if (tipo_plot == 1):
       ax.plot_trisurf(eixo1, eixo2, energ, alpha = 0.9, cmap = 'coolwarm', edgecolor='black', linewidth = 0.0, antialiased = False)
       # ax.plot_trisurf(eixo1, eixo2, E[number], alpha = 0.9, cmap = colormap, norm = normalize, edgecolor='black', linewidth = 0.0, antialiased = False)
    if (tipo_plot == 2):
       ax.plot_trisurf(eixo1, eixo2, energ, alpha = 0.9, cmap = 'coolwarm', edgecolor='black', linewidth = 0.0, antialiased = False)
       ax.scatter(eixo1, eixo2, energ, s = 0.1, alpha = 0.25, color = 'gray', antialiased = False)

    # ax.contourf(X, Y, Z[i], zdir = 'z', alpha = 0.9, offset = #####, cmap = cmap1)

if (Dimensao == 1):
   cl = r' $(2{\pi}/{a})$'
if (Dimensao == 2):
   cl = r' $({\AA}^{-1})$'
if (Dimensao == 3):
   cl = r' $({nm}^{-1})$' 

if (Plano_k == 1 and Dimensao != 4):             # Plane (kx,ky)      
   c1 = r'${k}_{x}$' + cl
   c2 = r'${k}_{y}$' + cl
if (Plano_k == 2 and Dimensao != 4):             # Plane (kx,kz)      
   c1 = r'${k}_{x}$' + cl
   c2 = r'${k}_{z}$' + cl
if (Plano_k == 3 and Dimensao != 4):             # Plane (ky,kz)      
   c1 = r'${k}_{y}$' + cl
   c2 = r'${k}_{z}$' + cl

if (Plano_k == 1 and Dimensao == 4):             # Plane (k1,k2)      
   c1 = r'${k}_{1}$'
   c2 = r'${k}_{2}$'
if (Plano_k == 2 and Dimensao == 4):             # Plane (k1,k3)      
   c1 = r'${k}_{1}$'
   c2 = r'${k}_{3}$'
if (Plano_k == 3 and Dimensao == 4):             # Plane (k2,k3)      
   c1 = r'${k}_{2}$'
   c2 = r'${k}_{3}$'

ax.set_xlabel(c1)
ax.set_ylabel(c2)

if (esc_fermi == 0):
   ax.set_zlabel(r'$E (eV)$')
if (esc_fermi == 1):
   ax.set_zlabel(r'$E-{E}_{f} (eV)$')

# ax.set_xlim((-5,5))
# ax.set_ylim((-5,5))
# ax.set_zlim((-5,5))

ax.view_init(elev = 5, azim = 45)
  
fig = plt.gcf()
fig.set_size_inches(8,6)

if (save_png == 1): plt.savefig(dir_output + "Bandas_3d.png", dpi = 600, pad_inches = 0)
if (save_pdf == 1): plt.savefig(dir_output + "Bandas_3d.pdf", dpi = 600, pad_inches = 0)
if (save_svg == 1): plt.savefig(dir_output + "Bandas_3d.svg", dpi = 600, pad_inches = 0)
if (save_eps == 1): plt.savefig(dir_output + "Bandas_3d.eps", dpi = 600, pad_inches = 0)

plt.show()

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------
   
# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license
