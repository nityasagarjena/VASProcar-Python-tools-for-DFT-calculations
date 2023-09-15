
import os
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.colors as colors
from scipy.interpolate import griddata

print(" ")
print("========== 2D Plot of Spin Projection (Level Contours): ==========")

if (tipo_contour < 2):
   levels_n = [0.0]*n_contour

#--------------------------------------------------------------------------
# Variables that define the thickness and length of vectors in the plot ---
#--------------------------------------------------------------------------
if ((fator > -1.0 and fator < 1.0) or fator == -1.0):
   fator == 1.0
   
if (fator > 0.0):
   fator = 1/fator
   
if (fator < 0.0):
   fator = (fator**2)**0.5

espessura = 0.005        #  Use espessura = 100 if you only want to plot the triangular head of the arrow and eliminate the tail, 
comprimento = 2.0*fator  #  which makes it easier to adjust the size/volume of the vectors by adjusting the comprimento variable.

#------------------------------------------------------------------------
# Test to know which directories must be correctly informed -------------
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/Spin_Texture/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# File Structure for Plot via Matplotlib ==============================
#======================================================================
#====================================================================== 

spin = np.loadtxt(dir_output + 'Spin_Texture.dat') 
spin.shape

print(" ")
print(".........................")
print("..... Wait a moment .....")
print(".........................")  
print(". It might take a while .")
print(".........................")

#------------------------------------------------

if (esc_fermi == 0): dE_fermi = 0.0
if (esc_fermi == 1): dE_fermi = (Efermi)*(-1)

#------------------------------------------------

if (Plano_k == 1):     # Plane (kx,ky) or (k1,k2)     
   eixo1 = spin[:,0]
   eixo2 = spin[:,1]
   
if (Plano_k == 2):     # Plane (kx,kz) or (k1,k3)     
   eixo1 = spin[:,0]
   eixo2 = spin[:,2]
   
if (Plano_k == 3):     # Plane (ky,kz) or (k2,k3)    
   eixo1 = spin[:,1]
   eixo2 = spin[:,2]

#---------------------------------------------------------
   
if (Plano_k == 1):
   s1 = 'Sx'; s2 = 'Sy'; s3 = 'Sz'
   sa = r'${S}_{x}$'; sb = r'${S}_{y}$'; sc = r'${S}_{z}$' 
if (Plano_k == 2):
   s1 = 'Sx'; s2 = 'Sz'; s3 = 'Sy'
   sa = r'${S}_{x}$'; sb = r'${S}_{z}$'; sc = r'${S}_{y}$'
if (Plano_k == 3):
   s1 = 'Sy'; s2 = 'Sz'; s3 = 'Sx'
   sa = r'${S}_{y}$'; sb = r'${S}_{z}$'; sc = r'${S}_{x}$'

#---------------------------------------------------------
   
if (Dimensao < 4 and Plano_k == 1):
   ca = r'${k}_{x}$'; cb = r'${k}_{y}$'
if (Dimensao < 4 and Plano_k == 2):
   ca = r'${k}_{x}$'; cb = r'${k}_{z}$'
if (Dimensao < 4 and Plano_k == 3):
   ca = r'${k}_{y}$'; cb = r'${k}_{z}$'
   
#--------------------------------------   

if (Dimensao == 4 and Plano_k == 1):
   ca = r'${k}_{1}$'; cb = r'${k}_{2}$'
if (Dimensao == 4 and Plano_k == 2):
   ca = r'${k}_{1}$'; cb = r'${k}_{3}$'
if (Dimensao == 4 and Plano_k == 3):
   ca = r'${k}_{2}$'; cb = r'${k}_{3}$'

#------------------------------------------

if (Dimensao == 1): cc = r' $(2{\pi}/{a})$'
if (Dimensao == 2): cc = r' $({\AA}^{-1})$'
if (Dimensao == 3): cc = r' $({nm}^{-1})$'
if (Dimensao == 4): cc = ' '

#------------------------------------------
# Create meshgrid for x,y -----------------
#------------------------------------------

xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)

#------------------------------------------
# Color Maps ------------------------------
#------------------------------------------

map_black    = colors.LinearSegmentedColormap.from_list("", ["black","black"])
map_red      = colors.LinearSegmentedColormap.from_list("", ["red","red"])
map_blue     = colors.LinearSegmentedColormap.from_list("", ["blue","blue"])
map_green    = colors.LinearSegmentedColormap.from_list("", ["green","green"])
map_magenta  = colors.LinearSegmentedColormap.from_list("", ["magenta","magenta"])
map_cyan     = colors.LinearSegmentedColormap.from_list("", ["cyan","cyan"])
map_pink     = colors.LinearSegmentedColormap.from_list("", ["pink","pink"])
map_yellow   = colors.LinearSegmentedColormap.from_list("", ["yellow","yellow"])
map_red_blue = colors.LinearSegmentedColormap.from_list("", ["red","pink","pink","pink","red","magenta","magenta","magenta","blue",
                                                              "cyan","cyan","cyan","blue","magenta","magenta","magenta","red"])
map_color = map_red_blue

#=========================================================================
# 2D Plot of Spin Projection on Level Contours: ==========================
#=========================================================================

for i in range (1,(6+1)):

    map_gray = (mpl.colors.ListedColormap(['darkgray', 'darkgray']))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    #-----------------------------------------------------------------------

    if (i == 1):
       c1 = sa + '  |  ' + ca + cc
       c2 = cb + cc
       L1 = sa + r'${\uparrow}$'
       L2 = sa + r'${\downarrow}$'
       rotulo = s1
      
    if (i == 2):
       c1 = ca + cc
       c2 = sb + '  |  ' + cb + cc      
       L1 = sb + r'${\uparrow}$'
       L2 = sb + r'${\downarrow}$'
       rotulo = s2
      
    if (i == 3):
       c1 = sc + '  |  ' + ca + cc
       c2 = cb + cc      
       L1 = sc + r'${\uparrow}$'
       L2 = sc + r'${\downarrow}$'
       rotulo = s3
      
    if (i == 4):     
       c1 = sa + '  |  ' + ca + cc
       c2 = sb + '  |  ' + cb + cc
       rotulo = s1 + s2

    if (i == 5):     
       rotulo = s1 + s3
       c1 = sa + '  |  ' + ca + cc
       c2 = sc + '  |  ' + cb + cc

    if (i == 6):     
       rotulo = s2 + s3
       c1 = sc + '  |  ' + ca + cc
       c2 = sb + '  |  ' + cb + cc
      
    if ((Plano_k == 1 and i == 4) or (Plano_k == 2 and i == 5) or (Plano_k == 3 and i == 5)):             
       L1 = r'${S}_{x}{\uparrow} + {S}_{y}{\uparrow}$'
       L2 = r'${S}_{x|y}{\uparrow}$'
       L3 = r'${S}_{x|y}{\uparrow} + {S}_{y|x}{\downarrow}$'
       L4 = r'${S}_{x|y}{\downarrow}$'
       L5 = r'${S}_{x}{\downarrow} + {S}_{y}{\downarrow}$'

    if ((Plano_k == 1 and i == 5) or (Plano_k == 2 and i == 4) or (Plano_k == 3 and i == 6)): 
       L1 = r'${S}_{x}{\uparrow} + {S}_{z}{\uparrow}$'
       L2 = r'${S}_{x|z}{\uparrow}$'
       L3 = r'${S}_{x|z}{\uparrow} + {S}_{z|x}{\downarrow}$'
       L4 = r'${S}_{x|z}{\downarrow}$'
       L5 = r'${S}_{x}{\downarrow} + {S}_{z}{\downarrow}$'

    if ((Plano_k == 1 and i == 6) or (Plano_k == 2 and i == 6) or (Plano_k == 3 and i == 4)):             
       L1 = r'${S}_{y}{\uparrow} + {S}_{z}{\uparrow}$'
       L2 = r'${S}_{y|z}{\uparrow}$'
       L3 = r'${S}_{y|z}{\uparrow} + {S}_{z|y}{\downarrow}$'
       L4 = r'${S}_{y|z}{\downarrow}$'
       L5 = r'${S}_{y}{\downarrow} + {S}_{z}{\downarrow}$'      
      
    #------------------------------------------

    for b in range(n_band_f - n_band_i + 1):

        energia = spin[:,(3 + b*4)] + dE_fermi
        Spin_Sx = spin[:,(4 + b*4)]
        Spin_Sy = spin[:,(5 + b*4)]
        Spin_Sz = spin[:,(6 + b*4)]

        pulo = (pulo + 1)
        levels = [0]*1

        #------------------------------------------------------------------------------

        if (tipo_contour == 0):
           energ_i = min(energia)
           energ_f = max(energia)
           for i in range(n_contour + 2):
               if (i != 0 and i != (n_contour + 1)):
                  levels_n[i-1] = energ_i + ((energ_f - energ_i)/(n_contour + 1))*(i-1)    

        if (tipo_contour == 1):
           for i in range(n_contour):
               levels_n[i] = energ_i + ((energ_f - energ_i)/(n_contour - 1))*(i)
       
        # Realizando a interpolação de [Kx, Ky, Energia] -------------------------

        e_grid = griddata((eixo1,eixo2), energia, (x_grid,y_grid), method = 'cubic')

        #------------------------------------------------------------------------------

        for j in range(n_contour):

            # plt.contourf(x_grid, y_grid, e_grid, levels_n, cmap = "bwr", alpha = 0.05, antialiased = True)

            if (min(energia) < levels_n[j] and max(energia) > levels_n[j]):
       
               #---------------------------------------------------------------------------------------------------------------------------------------
               levels[0] = levels_n[j]
               cs = plt.contour(x_grid, y_grid, e_grid, levels, linestyles = '-', cmap = map_gray, linewidths = 0.5, alpha = 1.0, antialiased = True)
               #---------------------------------------------------------------------------------------------------------------------------------------
               paths = cs.collections[0].get_paths()
               verts = [xx.vertices for xx in paths]
               points = np.concatenate(verts)         
               #---------------------------------------------------------------------------------------------------------------------------------------
               new_Sx = griddata((eixo1,eixo2), Spin_Sx, (points[::pulo,0], points[::pulo,1]))
               new_Sy = griddata((eixo1,eixo2), Spin_Sy, (points[::pulo,0], points[::pulo,1]))
               new_Sz = griddata((eixo1,eixo2), Spin_Sz, (points[::pulo,0], points[::pulo,1]))
               #---------------------------------------------------------------------------------------------------------------------------------------

               if (Plano_k == 1):  # Plane (kx,ky) or (k1,k2)       
                  Spin_S1 = new_Sx
                  Spin_S2 = new_Sy
                  Spin_S3 = new_Sz
         
               if (Plano_k == 2):  # Plane (kx,kz) or (k1,k3)
                  Spin_S1 = new_Sx
                  Spin_S2 = new_Sz
                  Spin_S3 = new_Sy
         
               if (Plano_k == 3):  # Plane (ky,kz) or (k2,k3)
                  Spin_S1 = new_Sy
                  Spin_S2 = new_Sz
                  Spin_S3 = new_Sx          
         
               #---------------------------------------------------------------------------------------------------------------------------------------          
       
               passo = len(new_Sx)
               nulo  = [0.0]*passo
               angle = [0]*passo
   
               for k in range(passo):
                   #----------------------------------------
                   if (i == 1):
                      v_spin = [Spin_S1[k], 0.0]
                 
                   if (i == 2):
                      v_spin = [0.0, Spin_S2[k]]
                 
                   if (i == 3):
                      v_spin = [Spin_S3[k], 0.0]
                
                   if (i == 4):
                      v_spin = [Spin_S1[k], Spin_S2[k]]

                   if (i == 5):
                      v_spin = [Spin_S1[k], Spin_S3[k]]

                   if (i == 6):
                      v_spin = [Spin_S3[k], Spin_S2[k]]   

                   #---------------------------------------------------------------------------------------------------
                   # Obtaining the rotation angle (counter clockwise) of the Spin vector with respect to the x-axis ---
                   #---------------------------------------------------------------------------------------------------
                   u = v_spin / np.linalg.norm(v_spin)
                   v = [1.0, 0.0]   # Reference vector for the angle. Must be kept fixed.
                   dot_product = np.dot(u, v)
                   angle[k] = np.arccos(dot_product) / np.pi * 180
                   if (u[1] < 0.0):
                      angle[k] = 360 - angle[k]

               #-------------------------------
               norma = colors.Normalize(0, 360)
               #-------------------------------

               if (i == 1):
                  cp = ax.quiver(points[::pulo,0], points[::pulo,1], Spin_S1, nulo, angle, cmap = map_color, norm = norma, linewidths = 0.25, edgecolor = 'black',
                                 alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'tail', minlength = 0.0)
             
               if (i == 2):
                  cp = ax.quiver(points[::pulo,0], points[::pulo,1], nulo, Spin_S2, angle, cmap = map_color, norm = norma, linewidths = 0.25, edgecolor = 'black',
                                 alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'tail', minlength = 0.0)
             
               if (i == 3):
                  cp = ax.quiver(points[::pulo,0], points[::pulo,1], Spin_S3, nulo, angle, cmap = map_color, norm = norma, linewidths = 0.25, edgecolor = 'black',
                                 alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'tail', minlength = 0.0)
             
               if (i == 4):
                  cp = ax.quiver(points[::pulo,0], points[::pulo,1], Spin_S1, Spin_S2, angle, cmap = map_color, norm = norma, linewidths = 0.25, edgecolor = 'black',
                                 alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'tail', minlength = 0.0)
               
               # if (i == 4):
               #    #--------------------------------------
               #    norma_sz = colors.Normalize(-0.5, +0.5)
               #    map_sz   = colors.LinearSegmentedColormap.from_list("", ["blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","white",
               #                                                             "red","red","red","red","red","red","red","red","red","red"])
               #    #------------------------------------------------------------------------------
               #    cp = ax.quiver(points[::pulo,0], points[::pulo,1], Spin_S1, Spin_S2, Spin_S3, cmap = map_sz, norm = norma_sz, linewidths = 0.25, edgecolor = 'black',
               #                   alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'tail', minlength = 0.0)

               if (i == 5):
                  cp = ax.quiver(points[::pulo,0], points[::pulo,1], Spin_S1, Spin_S3, angle, cmap = map_color, norm = norma, linewidths = 0.25, edgecolor = 'black',
                                 alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'tail', minlength = 0.0)

               if (i == 6):
                  cp = ax.quiver(points[::pulo,0], points[::pulo,1], Spin_S3, Spin_S2, angle, cmap = map_color, norm = norma, linewidths = 0.25, edgecolor = 'black',
                                 alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'tail', minlength = 0.0)   

               #---------------------------------------------------------------------------------------------------------------------------------------       
               # plt.quiver(points[::pulo,0], points[::pulo,1], Spin_S1, Spin_S2, angle,
               #            scale_units = "xy", angles = "xy", pivot = 'tail', cmap = map_red_blue, norm = norma, linewidths = 0.5, edgecolor = 'black', alpha = transp)   
               #---------------------------------------------------------------------------------------------------------------------------------------

               if (j == 1 and b == 1 and i < 4):   
                  cbar = fig.colorbar(cp, orientation = 'vertical', shrink = 1.0, boundaries = [0, 180, 360], ticks = [90, 270])
                  cbar.ax.set_yticklabels([L1, L2])

               if (j == 1 and b == 1 and i > 3):   
                  cbar = fig.colorbar(cp, orientation = 'vertical', shrink = 1.0, values = [45, 90, 135, 180, 225], ticks = [45, 90, 135, 180, 225])
                  cbar.ax.set_yticklabels([L1, L2, L3, L4, L5])

               if (rot_energ == 1): ax.clabel(cs, inline = True, colors = 'black', fontsize = 8)   

        #----------------------------------------------------------------------
        ax.set_xlabel(c1)
        ax.set_ylabel(c2)
        ax.set_box_aspect(1.0/1)   
        #----------------------------------------------------------------------

        if (save_png == 1): plt.savefig(dir_output + 'Spin_Texture_Contour_' + rotulo + '.png', dpi = 600, pad_inches = 0)
        if (save_pdf == 1): plt.savefig(dir_output + 'Spin_Texture_Contour_' + rotulo + '.pdf', dpi = 600, pad_inches = 0)
        if (save_svg == 1): plt.savefig(dir_output + 'Spin_Texture_Contour_' + rotulo + '.svg', dpi = 600, pad_inches = 0)
        if (save_eps == 1): plt.savefig(dir_output + 'Spin_Texture_Contour_' + rotulo + '.eps', dpi = 600, pad_inches = 0)

        fig = plt.gcf()
        fig.set_size_inches(8,6)
        # plt.show()

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------
 
# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license