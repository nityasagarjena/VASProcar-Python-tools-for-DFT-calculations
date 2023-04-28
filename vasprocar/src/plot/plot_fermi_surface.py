
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
print("============== Plotting the Fermi Surface: ==============")

if (esc_energ < 2):
   E = [0.0]*n_energ

#------------------------------------------------------------------------
# Test to know which directories must be correctly informed -------------
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/Fermi_Surface/'
else:
   dir_files = ''
   dir_output = ''
#----------------- 

#---------------------------------------------------------------------------------------
# Checking if the "figures" subfolder exists, if it doesn't exist it will be created ---
#---------------------------------------------------------------------------------------
if os.path.isdir(dir_output + 'figures'):
   0 == 0
else:
   os.mkdir(dir_output + 'figures')
#----------------------------------
 


#======================================================================
#======================================================================
# File Structure for Plot via Matplotlib ==============================
#======================================================================
#====================================================================== 

sfermi = np.loadtxt(dir_output + 'Fermi_Surface.dat') 
sfermi.shape

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

if (Plano_k == 1):     # Plane (kx,ky) or (k1,k2)     
   eixo1 = sfermi[:,0]
   eixo2 = sfermi[:,1]
if (Plano_k == 2):     # Plane (kx,kz) or (k1,k3)     
   eixo1 = sfermi[:,0]
   eixo2 = sfermi[:,2]
if (Plano_k == 3):     # Plane (ky,kz) or (k2,k3)    
   eixo1 = sfermi[:,1]
   eixo2 = sfermi[:,2]

#----------------------------------------------------------------------

if (esc_energ == 0):
   #---------------- 
   energ_i = +1000.0
   energ_f = -1000.0
   #------------------------------------ 
   for j in range(Band_i,(Band_f+1)):  
       energ  = sfermi[:,(j + 2)] + dE_fermi
       e_i = min(energ)
       e_f = max(energ)
       if (e_i < energ_i): energ_i = e_i
       if (e_f > energ_f): energ_f = e_f
   #------------------------------------      
   for i in range(n_energ + 2):
       if (i != 0 and i != (n_energ + 1)):
          E[i-1] = energ_i + ((energ_f - energ_i)/(n_energ + 1))*(i-1) 

if (esc_energ == 1):
   for i in range(n_energ):
       E[i] = energ_i + ((energ_f - energ_i)/(n_energ - 1))*(i)
       
# Create meshgrid for x,y ---------------------------------------------

xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)

#----------------------------------------------------------------------

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
# 2D Plot of Fermi Surfaces: =============================================
#=========================================================================

levels = [0.0]*1

for i in range(n_energ):

    fig, ax = plt.subplots()

    cmap_black = (mpl.colors.ListedColormap(['black', 'black']))
    cmap_blue = (mpl.colors.ListedColormap(['blue', 'blue']))
    cmap_red = (mpl.colors.ListedColormap(['red', 'red']))

    for j in range(Band_i,(Band_f+1)):
        #----------------------------------------------------------------------------
        energ  = sfermi[:,(j + 2)] + dE_fermi
        levels[0] = E[i]
        #----------------------------------------------------------------------------
        if (min(energ) < E[i] and max(energ) > E[i]):
           # Create meshgrid for z --------------------------------------------------
           z_grid = griddata((eixo1,eixo2), energ, (x_grid,y_grid), method = 'cubic')
           #-------------------------------------------------------------------------
           if (ispin == 1):
              plt.contour(x_grid, y_grid, z_grid, levels, linestyles = '-', cmap = cmap_black, linewidths = 0.5, alpha = 1.0, antialiased = True)
           #-------------------------------------------------------------------------
           if (ispin == 2):             
              if (j <= int(nb/2)):
                 plt.contour(x_grid, y_grid, z_grid, levels, linestyles = '-', cmap = cmap_red, linewidths = 0.5, alpha = 1.0, antialiased = True)
              if (j >  int(nb/2)):
                 plt.contour(x_grid, y_grid, z_grid, levels, linestyles = '-', cmap = cmap_blue, linewidths = 0.5, alpha = 1.0, antialiased = True)                 

    plt.xlabel(c1)
    plt.ylabel(c2)

    ax.set_box_aspect(1.0/1)  
    
    E[i] = round(E[i], 6)
    
    if (E[i] <= 0.0): c_energ = str(E[i])
    if (E[i] > 0.0):  c_energ = '+' + str(E[i])

    if (esc_fermi == 0): plt.title('$E$ = ' + c_energ + ' eV')
    if (esc_fermi == 1): plt.title('$E-E_{f}$ = ' + c_energ + ' eV')

    m = (i + 1)   
    if (m < 10):                number = '[000' + str(m) + ']'
    if (m >= 10 and m < 100):   number = '[00' + str(m) + ']'
    if (m >= 100 and m < 1000): number = '[0' + str(m) + ']'
    if (m > 1000):              number = '[' + str(m) + ']'

    if (video == 0): quality = 600
    if (video == 1): quality = 300

    if (save_png == 1): plt.savefig(dir_output + 'figures/SFermi_' + number + '_[' + c_energ + '].png', dpi = quality, pad_inches = 0)
    if (save_pdf == 1): plt.savefig(dir_output + 'SFermi_' + number + '_[' + c_energ + '].pdf', dpi = quality, pad_inches = 0)
    if (save_svg == 1): plt.savefig(dir_output + 'SFermi_' + number + '_[' + c_energ + '].svg', dpi = quality, pad_inches = 0)
    if (save_eps == 1): plt.savefig(dir_output + 'SFermi_' + number + '_[' + c_energ + '].eps', dpi = quality, pad_inches = 0)

    # plt.show()
    
    plt.close()

print(" ")
print("====== Creating a video (.mp4) of the Fermi Surfaces: ======")
print(" ")

#===================================================================
# Creating a video with the generated images (moviepy): ============
#===================================================================

if (video == 1):
    
   import moviepy.video.io.ImageSequenceClip

   if (dir_output != ''):
      image_output = dir_output + 'figures'
   if (dir_output == ''):
      image_output = os.getcwd() + '/figures'

   image_files = [os.path.join(image_output,img)
                  for img in os.listdir(image_output)
                  if img.endswith('.png')]

   clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps = n_fig)

   clip.write_videofile(dir_output + 'SFermi_video.mp4')

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------
 
# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license