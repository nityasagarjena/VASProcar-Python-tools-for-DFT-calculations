
import os
import scipy.interpolate as interp
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objects as go

print(" ")
print("========== Plotting Spin Texture isosurfaces (Plotly) ==========")

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
print(". It might take a while .")
print(".........................")

n_d = 31
n_iso = 15

#----------------------------------------------------------------------

xs = spin_textura[:,0]
ys = spin_textura[:,1]
zs = spin_textura[:,2]

points = np.array([xs, ys, zs]).T
xi = np.linspace(min(xs), max(xs), n_d)
yi = np.linspace(min(ys), max(ys), n_d)
zi = np.linspace(min(zs), max(zs), n_d)
xi, yi, zi = np.meshgrid(xi, yi, zi, indexing='ij')
newpts = np.array([xi, yi, zi]).T

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

for i in range (1,(3+1)):
    
    fig = go.Figure()

#----------------------------------------------------------------------

    if (i == 1):
       #-------------------------------------------
       cs = spin_textura[:,(i+3)]  #  Componente Sx
       #-------------------------------------------
       c1 = sa + ca + cd
       c2 = cb + cd
       c3 = cc + cd
       rotulo = 'Sx'
       r1 = 'Sx min'; r2 = 'Sx max'
    if (i == 2):
       #-------------------------------------------
       cs = spin_textura[:,(i+3)]  #  Componente Sy
       #-------------------------------------------
       c1 = ca + cd
       c2 = sb + cb + cd
       c3 = cc + cd
       rotulo = 'Sy'
       r1 = 'Sy min'; r2 = 'Sy max'
    if (i == 3):
       #-------------------------------------------
       cs = spin_textura[:,(i+3)]  #  Componente Sz
       #-------------------------------------------
       c1 = ca + cd
       c2 = cb + cd
       c3 = sc + cc + cd
       rotulo = 'Sz'
       r1 = 'Sz min'; r2 = 'Sz max'

    spin_nulo = (0.0 - min(cs))/(max(cs) - min(cs))    

    cs = (cs - min(cs))/(max(cs) - min(cs))   # Normalizes values of cs within the range [0,1]
    
    iso_minimo = min(cs)
    iso_maximo = max(cs)

    ci = interp.griddata(points, cs, newpts)
    ci.shape  

#--------------------------------------------------------------------------------------------------------       

    # colorscale:
    # Greys, YlGnBu, Greens, YlOrRd, Bluered, RdBu, Reds, Blues, Picnic, Rainbow, Portland, Jet
    # Hot, Blackbody, Earth, Electric, Viridis, Cividis

    # Colorscale with continuous color grading:
    # [(0, "blue"), (spin_nulo, "white"), (1, "red")]
    
    # Colorscale highlighting the contrast between Spin Up (Red) and Spin Down (Blue):
    # [(0, "blue"), ((spin_nulo - 0.01), "blue"), (spin_nulo, "white"), ((spin_nulo + 0.01), "red"), (1, "red")]

    fig.add_trace(go.Volume(x = xi.flatten(), y = yi.flatten(), z = zi.flatten(),
                            value = ci.T.flatten(), isomin = iso_minimo, isomax = iso_maximo,
                            opacity = 0.1,         # needs to be small to see through all surfaces
                            surface_count = n_iso, # needs to be a large number for good volume rendering
                            colorscale = [(0, "blue"), ((spin_nulo - 0.01), "blue"), (spin_nulo, "white"), ((spin_nulo + 0.01), "red"), (1, "red")],
                            caps = dict(x_show = True, y_show = True, z_show = True),
                            colorbar = dict(tickvals = [0, 1], ticktext = [r1, r2])))
    
    fig.update_layout(scene = dict(xaxis_title = c1, yaxis_title = c2, zaxis_title = c3, aspectmode = 'cube'),
                      margin = dict(r = 20, b = 10, l = 10, t = 10))

    fig.update_layout(xaxis_range=[min(xs), max(xs)])
    fig.update_layout(yaxis_range=[min(ys), max(ys)])

    fig.write_html(dir_output + 'Spin_Texture_4D_[iso]_' + rotulo + '.html')

    # fig.write_image(dir_output + 'Spin_Texture_4D_[iso]_.png')
    # fig.write_image(dir_output + 'Spin_Texture_4D_[iso]_.pdf')
    # fig.write_image(dir_output + 'Spin_Texture_4D_[iso]_.svg')
    # fig.write_image(dir_output + 'Spin_Texture_4D_[iso]_.eps')

    # fig.show() 

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------
 
# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license