
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
print("============= Plotting the Orbital Texture: =============")

#------------------------------------------------------------------------
# Test to know which directories must be correctly informed -------------
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/Orbital_Texture/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# File Structure for Plot via Matplotlib ==============================
#======================================================================
#====================================================================== 

countour = np.loadtxt(dir_output + 'Orbital_Texture.dat') 
countour.shape

print(" ")
print(".........................")
print("..... Wait a moment .....")
print(".........................")  
print(". It might take a while .")
print(".........................")

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

energia = countour[:,3]
energ_i = min(energia)
energ_f = max(energia)

for i in range(6):

    if (i == 0):
       orbital = countour[:,4]; l_orb = '_S'
    if (i == 1):
       orbital = countour[:,5]; l_orb = '_P'
    if (i == 2):
       orbital = countour[:,6]; l_orb = '_D'
    if (i == 3):
       orbital = countour[:,8]; l_orb = '_Px'
    if (i == 4):
       orbital = countour[:,9]; l_orb = '_Py'
    if (i == 5):
       orbital = countour[:,10]; l_orb = '_Pz'

    # Create meshgrid for x,y,z ------------------------------------------------

    xi = np.linspace(min(eixo1), max(eixo1), n_d)
    yi = np.linspace(min(eixo2), max(eixo2), n_d)
    x_grid, y_grid = np.meshgrid(xi,yi)
    z_grid = griddata((eixo1,eixo2), orbital, (x_grid,y_grid), method = 'cubic')
    e_grid = griddata((eixo1,eixo2), energia, (x_grid,y_grid), method = 'cubic')

    #---------------------------------------------------------------------------

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
    # 2D Plot of Orbital Texture: ============================================
    #=========================================================================

    fig, ax = plt.subplots()

    cmap_gray = (mpl.colors.ListedColormap(['darkgray', 'darkgray']))

    cp = plt.contourf(x_grid, y_grid, z_grid, levels = n_contour, cmap = "plasma", alpha = transp, antialiased = True)
    cbar = fig.colorbar(cp, orientation = 'vertical', shrink = 1.0)
    # cp = plt.contour(x_grid, y_grid, z_grid, levels = n_contour, linestyles = '-', cmap = cmap_gray, linewidths = 0.1, alpha = 0.5, antialiased = True)
    # plt.clabel(cp, inline = False, colors = 'black', fontsize = 8)

    levels_e = [0.0]*n_contour_energ

    for n in range(n_contour_energ):
        level = energ_i + ((energ_f - energ_i)/(n_contour_energ - 1))*(n)
        levels_e[n] = level

    cs = plt.contour(x_grid, y_grid, e_grid, levels_e, linestyles = '-', cmap = cmap_gray, linewidths = 0.5, alpha = 1.0, antialiased = True)

    plt.xlabel(c1)
    plt.ylabel(c2)

    ax.set_box_aspect(1.0/1)

    plt.title('$Orbital$')

    if (save_png == 1): plt.savefig(dir_output + 'Orbital_Texture' + l_orb + '.png', dpi = 600, pad_inches = 0)
    if (save_pdf == 1): plt.savefig(dir_output + 'Orbital_Texture' + l_orb + '.pdf', dpi = 600, pad_inches = 0)
    if (save_eps == 1): plt.savefig(dir_output + 'Orbital_Texture' + l_orb + '.eps', dpi = 600, pad_inches = 0)
    if (save_svg == 1): plt.savefig(dir_output + 'Orbital_Texture' + l_orb + '.svg', dpi = 600, pad_inches = 0)

    # plt.show()

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------
 
# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license