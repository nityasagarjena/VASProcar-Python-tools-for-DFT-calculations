
import os
import scipy.interpolate as interp
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objects as go

print(" ")
print("============ Plotting the Spin 4D Texture (Plotly): ============")

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

k1 = spin_textura[:,0]
k2 = spin_textura[:,1]
k3 = spin_textura[:,2]

Spin_Sx = spin_textura[:,4]
Spin_Sy = spin_textura[:,5]
Spin_Sz = spin_textura[:,6]

Sx_u = [0.0]*nk; Sx_d = [0.0]*nk
Sy_u = [0.0]*nk; Sy_d = [0.0]*nk
Sz_u = [0.0]*nk; Sz_d = [0.0]*nk
nulo = [0.0]*nk

#----------------------------------------------------------------------

if (Dimensao < 4):
   ca = 'k<sub>x</sub>'; cb = 'k<sub>y</sub>'; cc = 'k<sub>z</sub>'
if (Dimensao == 4):
   ca = 'k<sub>1</sub>'; cb = 'k<sub>2</sub>'; cc = 'k<sub>3</sub>'

if (Dimensao == 1): cd = ' (2' + '\u03C0' + '/a)'             #  (2pi/a)
if (Dimensao == 2): cd = ' (' + '\u212B' + '<sup>-1</sup>)'   #  (Angs.^-1)
if (Dimensao == 3): cd = ' (nm<sup>-1</sup>)'                 #  (nm^-1)
if (Dimensao == 4): cd = ' '

sa = 'S<sub>x</sub>  |  '; sb = 'S<sub>y</sub>  |  '; sc = 'S<sub>z</sub>  |  '

#----------------------------------------------------------------------

for i in range(nk):
    if (Spin_Sx[i] > 0.0): Sx_u[i] = Spin_Sx[i]
    if (Spin_Sx[i] < 0.0): Sx_d[i] = Spin_Sx[i]
    if (Spin_Sy[i] > 0.0): Sy_u[i] = Spin_Sy[i]
    if (Spin_Sy[i] < 0.0): Sy_d[i] = Spin_Sy[i]
    if (Spin_Sz[i] > 0.0): Sz_u[i] = Spin_Sz[i]
    if (Spin_Sz[i] < 0.0): Sz_d[i] = Spin_Sz[i]

#----------------------------------------------------------------------

for i in range (1,(4+1)):
    
    fig = go.Figure()

#----------------------------------------------------------------------

    if (i == 1):
       c1 = sa + ca + cd
       c2 = cb + cd
       c3 = cc + cd
       rotulo = 'Sx'
    if (i == 2):
       c1 = ca + cd
       c2 = sb + cb + cd
       c3 = cc + cd
       rotulo = 'Sy'
    if (i == 3):
       c1 = ca + cd
       c2 = cb + cd
       c3 = sc + cc + cd
       rotulo = 'Sz'
      
    if (i == 4):     
       c1 = sa + ca + cd
       c2 = sb + cb + cd
       c3 = sc + cc + cd
       rotulo = 'SxSySz'

#----------------------------------------------------------------------       

    if (i == 1): fig.add_trace(go.Cone(x = k1, y = k2, z = k3, u = Sx_d, v = nulo, w = nulo, opacity = 0.1,
                               colorscale = ["blue", "blue"], showscale = False, sizemode = "absolute", sizeref = 0.5))
    if (i == 1): fig.add_trace(go.Cone(x = k1, y = k2, z = k3, u = Sx_u, v = nulo, w = nulo, opacity = 0.1,
                               colorscale = ["red", "red"], showscale = False, sizemode = "absolute", sizeref = 0.5))

    if (i == 2): fig.add_trace(go.Cone(x = k1, y = k2, z = k3, u = nulo, v = Sy_d, w = nulo, opacity = 0.1,
                               colorscale = ["blue", "blue"], showscale = False, sizemode = "absolute", sizeref = 0.5))
    if (i == 2): fig.add_trace(go.Cone(x = k1, y = k2, z = k3, u = nulo, v = Sy_u, w = nulo, opacity = 0.1,
                               colorscale = ["red", "red"], showscale = False, sizemode = "absolute", sizeref = 0.5))

    if (i == 3): fig.add_trace(go.Cone(x = k1, y = k2, z = k3, u = nulo, v = nulo, w = Sz_d, opacity = 0.1,
                               colorscale = ["blue", "blue"], showscale = False, sizemode = "absolute", sizeref = 0.5))
    if (i == 3): fig.add_trace(go.Cone(x = k1, y = k2, z = k3, u = nulo, v = nulo, w = Sz_u, opacity = 0.1,
                               colorscale = ["red", "red"], showscale = False, sizemode = "absolute", sizeref = 0.5))

    if (i == 4): fig.add_trace(go.Cone(x = k1, y = k2, z = k3, u = Spin_Sx, v = Spin_Sy, w = Spin_Sz, opacity = 0.1,
                               colorscale = ["black", "black"], showscale = False, sizemode = "absolute", sizeref = 0.5)) 
    
    fig.update_layout(scene = dict(xaxis_title = c1, yaxis_title = c2, zaxis_title = c3, aspectmode = 'cube'),
                      margin = dict(r = 20, b = 10, l = 10, t = 10))

    fig.update_layout(xaxis_range=[min(k1), max(k1)])
    fig.update_layout(yaxis_range=[min(k2), max(k2)])

    fig.write_html(dir_output + 'Spin_Texture_4D_' + rotulo + '.html')

    # fig.write_image(dir_output + 'Spin_Texture_4D_' + rotulo + '.png')
    # fig.write_image(dir_output + 'Spin_Texture_4D_' + rotulo + '.pdf')
    # fig.write_image(dir_output + 'Spin_Texture_4D_' + rotulo + '.svg')
    # fig.write_image(dir_output + 'Spin_Texture_4D_' + rotulo + '.eps')

    # fig.show() 

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------
 
# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license