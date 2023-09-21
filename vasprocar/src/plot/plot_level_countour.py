
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
print("============== Plotting the Level Contours ==============")

#------------------------------------------------------------------------
# Test to know which directories must be correctly informed -------------
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/Level_Countour/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# File Structure for Plot via Matplotlib ==============================
#======================================================================
#====================================================================== 

countour = np.loadtxt(dir_output + 'Level_Countour.dat') 
countour.shape

print(" ")
print(".........................")
print("..... Wait a moment .....")
print(".........................")  
print(". It might take a while .")
print(".........................")

#----------------------------------------------------------------------

if (esc_fermi == 0): dE_fermi = 0.0
if (esc_fermi == 1): dE_fermi = (Efermi)*(-1)

#----------------------------------------------------------------------

if (Plano_k == 1):         # Plane (kx,ky) or (k1,k2)     
   eixo1 = countour[:,0]
   eixo2 = countour[:,1]
if (Plano_k == 2):         # Plane (kx,kz) or (k1,k3)     
   eixo1 = countour[:,0]
   eixo2 = countour[:,2]
if (Plano_k == 3):         # Plane (ky,kz) or (k2,k3)    
   eixo1 = countour[:,1]
   eixo2 = countour[:,2]

energ = countour[:,(Banda + 2)] + dE_fermi

#-------------------------------------------------------------------------  

if (tipo_contour == 1):
   levels_n = [0.0]*n_contour
   for i in range(n_contour):
       levels_n[i] = energ_i + ((energ_f - energ_i)/(n_contour - 1))*(i)

# Create meshgrid for x,y,z ----------------------------------------------

xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)
z_grid = griddata((eixo1,eixo2), energ, (x_grid,y_grid), method = 'cubic')

#-------------------------------------------------------------------------

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

   

#=========================================================================
# 2D Plot of Level Contours: =============================================
#=========================================================================

fig, ax = plt.subplots()

cmap_gray = (mpl.colors.ListedColormap(['darkgray', 'darkgray']))

if (tipo_contour == 0):
   cp = plt.contourf(x_grid, y_grid, z_grid, levels = n_contour, cmap = "bwr", alpha = transp, antialiased = True)
   cp = plt.contour(x_grid, y_grid, z_grid, levels = n_contour, linestyles = '-', cmap = cmap_gray, linewidths = 0.5, alpha = 1.0, antialiased = True)

if (tipo_contour > 0):
   cp = plt.contourf(x_grid, y_grid, z_grid, levels = levels_n, cmap = "bwr", alpha = transp, antialiased = True)
   cp = plt.contour(x_grid, y_grid, z_grid, levels = levels_n, linestyles = '-', cmap = cmap_gray, linewidths = 0.5, alpha = 1.0, antialiased = True)

plt.clabel(cp, inline = False, colors = 'black', fontsize = 8)

plt.xlabel(c1)
plt.ylabel(c2)

ax.set_box_aspect(1.0/1)

if (esc_fermi == 0): plt.title('$E$ (eV)')
if (esc_fermi == 1): plt.title('$E-E_{f}$ (eV)')

if (save_png == 1): plt.savefig(dir_output + "Level_Countour_2D.png", dpi = 600, pad_inches = 0)
if (save_pdf == 1): plt.savefig(dir_output + "Level_Countour_2D.pdf", dpi = 600, pad_inches = 0)
if (save_eps == 1): plt.savefig(dir_output + "Level_Countour_2D.eps", dpi = 600, pad_inches = 0)

# plt.show()



#=======================================================================
# 3D Plot of Level Contours: ===========================================
#=======================================================================

fig = plt.figure()
ax = plt.axes(projection='3d')

cmap_black = (mpl.colors.ListedColormap(['black', 'black']))

if (tipo_contour == 0): plt.contour(x_grid, y_grid, z_grid, levels = n_contour, linestyles = '-', cmap = cmap_black, alpha = 1.0, antialiased = True)
if (tipo_contour > 0):  plt.contour(x_grid, y_grid, z_grid, levels = levels_n,  linestyles = '-', cmap = cmap_black, alpha = 1.0, antialiased = True)

plt.xlabel(c1)
plt.ylabel(c2)

if (esc_fermi == 0): ax.set_zlabel(r'$E$ (eV)')
if (esc_fermi == 1): ax.set_zlabel(r'$E-{E}_{f}$ (eV)')

# ax.set_xlim((-5,5))
# ax.set_ylim((-5,5))
# ax.set_zlim((-5,5))
# ax.view_init(elev = 5, azim = 45)
  
fig = plt.gcf()
fig.set_size_inches(8,6)

if (save_png == 1): plt.savefig(dir_output + "Level_Countour_3D.png", dpi = 600, pad_inches = 0)
if (save_pdf == 1): plt.savefig(dir_output + "Level_Countour_3D.pdf", dpi = 600, pad_inches = 0)
if (save_svg == 1): plt.savefig(dir_output + "Level_Countour_3D.svg", dpi = 600, pad_inches = 0)
if (save_eps == 1): plt.savefig(dir_output + "Level_Countour_3D.eps", dpi = 600, pad_inches = 0)

plt.show()

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------
 
# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license