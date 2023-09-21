
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
import linecache 

#------------------------------------------------------------------------
# Test to know which directories must be correctly informed -------------
#------------------------------------------------------------------------
if ((fator > -1.0 and fator < 1.0) or fator == -1.0):
   fator == 1.0
   
if (fator > 0.0):
   fator = 1/fator
   
if (fator < 0.0):
   fator = (fator**2)**0.5

espessura = 0.0025       #  Use espessura = 100 if you only want to plot the triangular head of the arrow and eliminate the tail, 
comprimento = 5.0*fator  #  which makes it easier to adjust the size/volume of the vectors by adjusting the comprimento variable.
#----------------------

print(" ")
print("=========== Plotting the Spin 2D Texture (Matplotlib) ===========")

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

spin_textura = np.loadtxt(dir_output + 'Spin_Texture.dat')
spin_textura.shape

print(" ")
print(".........................")
print("..... Wait a moment .....")
print(".........................")  

#----------------------------------------------------------------------

Spin_Sx = spin_textura[:,4]
Spin_Sy = spin_textura[:,5]
Spin_Sz = spin_textura[:,6]

if (Plano_k == 1):  # Plano (kx,ky) ou (k1,k2)
   eixo1  = spin_textura[:,0]
   eixo2  = spin_textura[:,1]
   Spin_S1 = Spin_Sx
   Spin_S2 = Spin_Sy
   Spin_S3 = Spin_Sz
             
if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3)
   eixo1  = spin_textura[:,0]
   eixo2  = spin_textura[:,2]
   Spin_S1 = Spin_Sx
   Spin_S2 = Spin_Sz
   Spin_S3 = Spin_Sy
             
if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3)
   eixo1  = spin_textura[:,1]
   eixo2  = spin_textura[:,2]
   Spin_S1 = Spin_Sy
   Spin_S2 = Spin_Sz
   Spin_S3 = Spin_Sx           

pulo = (pulo + 1)
transp = 1.0

#----------------------------------------------------------------------
   
if (Plano_k == 1):
   s1 = 'Sx'; s2 = 'Sy'; s3 = 'Sz'
   sa = r'${S}_{x}$'; sb = r'${S}_{y}$'; sc = r'${S}_{z}$' 
if (Plano_k == 2):
   s1 = 'Sx'; s2 = 'Sz'; s3 = 'Sy'
   sa = r'${S}_{x}$'; sb = r'${S}_{z}$'; sc = r'${S}_{y}$'
if (Plano_k == 3):
   s1 = 'Sy'; s2 = 'Sz'; s3 = 'Sx'
   sa = r'${S}_{y}$'; sb = r'${S}_{z}$'; sc = r'${S}_{x}$'

#----------------------------------------------------------------------
   
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

#-------------------------------------- 

if (Dimensao == 1): cc = r' $(2{\pi}/{a})$'
if (Dimensao == 2): cc = r' $({\AA}^{-1})$'
if (Dimensao == 3): cc = r' $({nm}^{-1})$'
if (Dimensao == 4): cc = ' '

#----------------------------------------------------------------------

for i in range (1,(6+1)):

   fig = plt.figure()

   ax = fig.add_subplot(111)
   ax.axis('equal')

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
         
#-----------------------------------------------------------------------

   passo = len(Spin_Sx)
   nulo = [0.0]*passo
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
       #---------------------------------------------------------------------------
       u = v_spin / np.linalg.norm(v_spin)
       v = [1.0, 0.0]  #  Vetor de referencia para o angulo, deve ser mantido fixo.
       dot_product = np.dot(u, v)
       angle[k] = np.arccos(dot_product) / np.pi * 180
       if (u[1] < 0.0):
          angle[k] = 360 - angle[k]
      
#-----------------------------------------------------------------------

   ax.set_xlabel(c1)
   ax.set_ylabel(c2)

#----------------------------------------------------------------------

   # plt.scatter(eixo1, eixo2, color = 'gray', s = 1, alpha = 0.5)

   #---------------------------------------------------------------------------------------------------------------------------------------
   # map_red_blue = colors.LinearSegmentedColormap.from_list("", ["red","white","red","white","blue","white","blue","white","red"])
   # map_red_blue = colors.LinearSegmentedColormap.from_list("", ["red","magenta","red","magenta","blue","magenta","blue","magenta","red"])
   # map_red_blue = colors.LinearSegmentedColormap.from_list("", ["red","pink","red","magenta","blue","cyan","blue","magenta","red"])
   map_red_blue = colors.LinearSegmentedColormap.from_list("", ["red","pink","pink","pink","red","magenta","magenta","magenta","blue",
                                                                       "cyan","cyan","cyan","blue","magenta","magenta","magenta","red"])
   norma = colors.Normalize(0, 360)
   #---------------------------------------------------------------------------------------------------------------------------------------   
   
   if (i == 1):
      cs = ax.quiver(eixo1[::pulo], eixo2[::pulo], Spin_S1[::pulo], nulo[::pulo], angle[::pulo], cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                     alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle', minlength = 0.0)
      
   if (i == 2):
      cs = ax.quiver(eixo1[::pulo], eixo2[::pulo], nulo[::pulo], Spin_S2[::pulo], angle[::pulo], cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                     alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle', minlength = 0.0)
   
   if (i == 3):
      cs = ax.quiver(eixo1[::pulo], eixo2[::pulo], Spin_S3[::pulo], nulo[::pulo], angle[::pulo], cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                     alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle', minlength = 0.0)

   if (i == 4):
      cs = ax.quiver(eixo1[::pulo], eixo2[::pulo], Spin_S1[::pulo], Spin_S2[::pulo], angle[::pulo], cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                     alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle', minlength = 0.0)

   if (i == 5):
      cs = ax.quiver(eixo1[::pulo], eixo2[::pulo], Spin_S1[::pulo], Spin_S3[::pulo], angle[::pulo], cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                     alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle', minlength = 0.0)

   if (i == 6):
      cs = ax.quiver(eixo1[::pulo], eixo2[::pulo], Spin_S3[::pulo], Spin_S2[::pulo], angle[::pulo], cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                     alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle', minlength = 0.0)

   if (i < 4):   
      cbar = fig.colorbar(cs, orientation = 'vertical', shrink = 1.0, boundaries = [0, 180, 360], ticks = [90, 270])
      cbar.ax.set_yticklabels([L1, L2])

   if (i > 3):   
      cbar = fig.colorbar(cs, orientation = 'vertical', shrink = 1.0, values = [45, 90, 135, 180, 225], ticks = [45, 90, 135, 180, 225])
      cbar.ax.set_yticklabels([L1, L2, L3, L4, L5])
 
   fig = plt.gcf()
   fig.set_size_inches(8,6)

   if (save_png == 1): plt.savefig(dir_output + 'Spin_Texture_' + rotulo + '.png', dpi = 600, pad_inches = 0)
   if (save_pdf == 1): plt.savefig(dir_output + 'Spin_Texture_' + rotulo + '.pdf', dpi = 600, pad_inches = 0)
   if (save_svg == 1): plt.savefig(dir_output + 'Spin_Texture_' + rotulo + '.svg', dpi = 600, pad_inches = 0)
   if (save_eps == 1): plt.savefig(dir_output + 'Spin_Texture_' + rotulo + '.eps', dpi = 600, pad_inches = 0)

   # plt.show()

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------
 
# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license