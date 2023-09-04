
import os
import numpy as np
import scipy.interpolate as interp
from scipy.interpolate import griddata
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#----------------------------------------------------------------------

print(" ")
print("============ Plotting the Spin 3D Texture (Plotly): ============")

#------------------------------------------------------------------------

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
# File Structure for Plot via Plotly ==================================
#======================================================================
#======================================================================

spin_textura = np.loadtxt(dir_output + 'Spin_Texture.dat')
spin_textura.shape

print(" ")
print("===================================================================")
print("Note: The result is found in .html files, which are opened via an =")
print("      internet browser. ===========================================") 
print("===================================================================")

print(" ")
print(".........................")
print("..... Wait a moment .....")
print(".........................")  

#----------------------------------------------------------------------

if (esc_fermi == 0): dE_fermi = 0.0
if (esc_fermi == 1): dE_fermi = (Efermi)*(-1)

#---------------------------------------------------------------------- 

energia = spin_textura[:,3] + dE_fermi
Spin_Sx = spin_textura[:,4]
Spin_Sy = spin_textura[:,5]
Spin_Sz = spin_textura[:,6]

S1_u = [0.0]*n_procar*nk;  S1_d = [0.0]*n_procar*nk
S2_u = [0.0]*n_procar*nk;  S2_d = [0.0]*n_procar*nk
S3_u = [0.0]*n_procar*nk;  S3_d = [0.0]*n_procar*nk
nulo = [0.0]*n_procar*nk

#---------------------------------------------

if (Plano_k == 1):  # Plano (kx,ky) ou (k1,k2)
   eixo1  = spin_textura[:,0]
   eixo2  = spin_textura[:,1]     
   rotulo1 = 'SxSy'
   
if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3)
   eixo1  = spin_textura[:,0]
   eixo2  = spin_textura[:,2]  
   rotulo1 = 'SxSz'
   
if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3)
   eixo1  = spin_textura[:,1]
   eixo2  = spin_textura[:,2]      
   rotulo1 = 'SySz'     

#----------------------------------------------------------------------

# Create meshgrid for x,y
xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)

# Grid data
z_grid = griddata((eixo1,eixo2), energia, (x_grid,y_grid), method = 'cubic')

#----------------------------------------------------------------------

if (esc_fermi == 0): rot_energ = 'E (eV)'
if (esc_fermi == 1): rot_energ = 'E-E<sub>f</sub> (eV)'

if (Plano_k == 1 and Dimensao < 4):                
   ca = 'k<sub>x</sub>'; cb = 'k<sub>y</sub>'; cc = rot_energ
   sa = 'S<sub>x</sub>  |  '; sb = 'S<sub>y</sub>  |  '; sc = 'S<sub>z</sub>  |  '
if (Plano_k == 2 and Dimensao < 4):                  
   ca = 'k<sub>x</sub>'; cb = 'k<sub>z</sub>'; cc = rot_energ   
   sa = 'S<sub>x</sub>  |  '; sb = 'S<sub>z</sub>  |  '; sc = 'S<sub>y</sub>  |  '   
if (Plano_k == 3 and Dimensao < 4):                  
   ca = 'k<sub>y</sub>'; cb = 'k<sub>z</sub>'; cc = rot_energ   
   sa = 'S<sub>y</sub>  |  '; sb = 'S<sub>z</sub>  |  '; sc = 'S<sub>x</sub>  |  ' 

if (Plano_k == 1 and Dimensao == 4):                 
   ca = 'k<sub>1</sub>'; cb = 'k<sub>2</sub>'; cc = rot_energ
   sa = 'S<sub>x</sub>  |  '; sb = 'S<sub>y</sub>  |  '; sc = 'S<sub>z</sub>  |  '
if (Plano_k == 2 and Dimensao == 4):                 
   ca = 'k<sub>1</sub>'; cb = 'k<sub>3</sub>'; cc = rot_energ   
   sa = 'S<sub>x</sub>  |  '; sb = 'S<sub>z</sub>  |  '; sc = 'S<sub>y</sub>  |  ' 
if (Plano_k == 3 and Dimensao == 4):                
   ca = 'k<sub>2</sub>'; cb = 'k<sub>3</sub>'; cc = rot_energ   
   sa = 'S<sub>y</sub>  |  '; sb = 'S<sub>z</sub>  |  '; sc = 'S<sub>x</sub>  |  '

#-------------------------------------- 

if (Dimensao == 1): cd = ' (2' + '\u03C0' + '/a)'             #  (2pi/a)
if (Dimensao == 2): cd = ' (' + '\u212B' + '<sup>-1</sup>)'   #  (Angs.^-1)
if (Dimensao == 3): cd = ' (nm<sup>-1</sup>)'                 #  (nm^-1)
if (Dimensao == 4): cd = ' '
   
#----------------------------------------------------------------------

for i in range(n_procar*nk):
   
    if (Plano_k == 1):  # Plano (kx,ky) ou (k1,k2) 
       if (Spin_Sx[i] > 0.0): S1_u[i] = Spin_Sx[i]
       if (Spin_Sx[i] < 0.0): S1_d[i] = Spin_Sx[i]
       if (Spin_Sy[i] > 0.0): S2_u[i] = Spin_Sy[i]
       if (Spin_Sy[i] < 0.0): S2_d[i] = Spin_Sy[i]
       if (Spin_Sz[i] > 0.0): S3_u[i] = Spin_Sz[i]
       if (Spin_Sz[i] < 0.0): S3_d[i] = Spin_Sz[i]
       
    if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3) 
       if (Spin_Sx[i] > 0.0): S1_u[i] = Spin_Sx[i]
       if (Spin_Sx[i] < 0.0): S1_d[i] = Spin_Sx[i]
       if (Spin_Sz[i] > 0.0): S2_u[i] = Spin_Sz[i]
       if (Spin_Sz[i] < 0.0): S2_d[i] = Spin_Sz[i]
       if (Spin_Sy[i] > 0.0): S3_u[i] = Spin_Sy[i]
       if (Spin_Sy[i] < 0.0): S3_d[i] = Spin_Sy[i]
       
    if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3) 
       if (Spin_Sy[i] > 0.0): S1_u[i] = Spin_Sy[i]
       if (Spin_Sy[i] < 0.0): S1_d[i] = Spin_Sy[i]
       if (Spin_Sz[i] > 0.0): S2_u[i] = Spin_Sz[i]
       if (Spin_Sz[i] < 0.0): S2_d[i] = Spin_Sz[i]
       if (Spin_Sx[i] > 0.0): S3_u[i] = Spin_Sx[i]
       if (Spin_Sx[i] < 0.0): S3_d[i] = Spin_Sx[i]    

#----------------------------------------------------------------------

for i in range (1,(4+1)):
    
    fig = go.Figure()

#----------------------------------------------------------------------

    if (i == 1):
       c1 = sa + ca + cd
       c2 = cb + cd
       c3 = cc
       rotulo = 'Sx'
    if (i == 2):
       c1 = ca + cd
       c2 = sb + cb + cd
       c3 = cc
       rotulo = 'Sy'
    if (i == 3):
       c1 = ca + cd
       c2 = cb + cd
       c3 = sc + cc
       rotulo = 'Sz'
      
    if (i == 4):
      
       c1 = sa + ca + cd
       c2 = sb + cb + cd
       c3 = sc + cc

       if (Plano_k == 1):  # Plano (kx,ky) ou (k1,k2)       
          Spin_S1 = Spin_Sx
          Spin_S2 = Spin_Sy
          Spin_S3 = Spin_Sz
          rotulo = 'SxSy'
         
       if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3)
          Spin_S1 = Spin_Sx
          Spin_S2 = Spin_Sz
          Spin_S3 = Spin_Sy
          rotulo = 'SxSz'
         
       if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3)
          Spin_S1 = Spin_Sy
          Spin_S2 = Spin_Sz
          Spin_S3 = Spin_Sx
          rotulo = 'SySz'

#-----------------------------------------------------------------------    

    fig.add_trace(go.Surface(x = x_grid, y = y_grid, z = z_grid, opacity = 0.25, colorscale = ["gray", "gray"], showscale = False))

    
    if (i == 1): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = S1_d, v = nulo, w = nulo, opacity = 0.75,
                                       colorscale = ["blue", "blue"], showscale = False, sizemode = "absolute", sizeref = 1.0))
    if (i == 1): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = S1_u, v = nulo, w = nulo, opacity = 0.75,
                                       colorscale = ["red", "red"], showscale = False, sizemode = "absolute", sizeref = 1.0))

    if (i == 2): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = nulo, v = S2_d, w = nulo, opacity = 0.75,
                                       colorscale = ["blue", "blue"], showscale = False, sizemode = "absolute", sizeref = 1.0))
    if (i == 2): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = nulo, v = S2_u, w = nulo, opacity = 0.75,
                                       colorscale = ["red", "red"], showscale = False, sizemode = "absolute", sizeref = 1.0))

    if (i == 3): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = nulo, v = nulo, w = S3_d, opacity = 0.75,
                                       colorscale = ["blue", "blue"], showscale = False, sizemode = "absolute", sizeref = 1.0))
    if (i == 3): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = nulo, v = nulo, w = S3_u, opacity = 0.75,
                                       colorscale = ["red", "red"], showscale = False, sizemode = "absolute", sizeref = 1.0))

    if (i == 4): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = Spin_S1, v = Spin_S2, w = Spin_S3, opacity = 0.75,
                                       colorscale = ["black", "black"], showscale = False, sizemode = "absolute", sizeref = 1.0))
     
    fig.update_layout(scene = dict(xaxis_title = c1, yaxis_title = c2, zaxis_title = c3, aspectmode = 'cube'),
                      margin = dict(r = 20, b = 10, l = 10, t = 10))

    fig.update_layout(xaxis_range=[min(eixo1), max(eixo1)])
    fig.update_layout(yaxis_range=[min(eixo2), max(eixo2)])

    fig.write_html(dir_output + 'Spin_Texture_3D_' + rotulo + '.html')

    # fig.write_image(dir_output + 'Spin_Texture_3D_' + rotulo + '.png')
    # fig.write_image(dir_output + 'Spin_Texture_3D_' + rotulo + '.pdf')
    # fig.write_image(dir_output + 'Spin_Texture_3D_' + rotulo + '.svg')
    # fig.write_image(dir_output + 'Spin_Texture_3D_' + rotulo + '.eps')

    # fig.show()

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------
 
# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license