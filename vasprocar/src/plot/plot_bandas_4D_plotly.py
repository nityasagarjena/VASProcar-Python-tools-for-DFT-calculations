
import os
import shutil
import scipy.interpolate as interp
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objects as go

print(" ")
print("============== Plotting the isosurfaces (Plotly): ==============")

#------------------------------------------------------------------------
# Test to know which directories must be correctly informed -------------
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/Plot_4D/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# File Structure for Plot via Plotly ==================================
#======================================================================
#======================================================================    

if (esc_fermi == 0):
   dE_fermi = 0.0
   
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1)

if (esc == 2):
   dE_fermi = 0.0

data = np.loadtxt(dir_output + 'Plot_4d.dat')
data.shape

xs = data[:,0]
ys = data[:,1]
zs = data[:,2]
cs = data[:,3] + dE_fermi

print(" ")
print("---------------------------")

if (esc == 1 and esc_fermi == 0):
   print(f'E min = {min(cs):.8f}')
   print(f'E max = {max(cs):.8f}')

if (esc == 1 and esc_fermi == 1):
   print(f'(E-Ef) min = {min(cs):.8f}')
   print(f'(E-Ef) max = {max(cs):.8f}')

if (esc == 2):
   print(f'Delta_E = E_Banda_2 - E_Banda_1')
   print(" ")
   print(f'|Delta_E| min = {min(cs):.8f}')
   print(f'|Delta_E| max = {max(cs):.8f}')
  
print("---------------------------")

min_max_cs = 0

if (max(cs) < 0.0):
   min_max_cs = 1
   cs = (cs - min(cs))/(max(cs) - min(cs))   # Normalizes values of cs within the range [0,1]

iso_minimo = min(cs)
iso_maximo = max(cs)

print(" ")
print("===================================================================")
print("Note: If the page on the internet browser is loading infinitely or ")
print("      displays an error message, press the [F5] key to reload the  ")
print("      page, or open the [.html] file.                              ")   
print("===================================================================")

print(" ")
print(".........................")
print("..... Wait a moment .....")
print(".........................")  
print(". It might take a while .")
print(".........................")

points = np.array([xs, ys, zs]).T
xi = np.linspace(min(xs), max(xs), n_d)
yi = np.linspace(min(ys), max(ys), n_d)
zi = np.linspace(min(zs), max(zs), n_d)
xi, yi, zi = np.meshgrid(xi, yi, zi, indexing='ij')
newpts = np.array([xi, yi, zi]).T
ci = interp.griddata(points, cs, newpts)
ci.shape

if (esc == 1):
   if (esc_fermi == 0): titulo_bar = 'E (eV)'
   if (esc_fermi == 1): titulo_bar = 'E-E<sub>f</sub> (eV)' 
   if (min_max_cs == 1): titulo_bar = 'Scale E'

if (esc == 2): titulo_bar = '|\u0394' + 'E| (eV)'

#----------------------------------------------------------------------

fig = go.Figure()

# colorscale:
# Greys, YlGnBu, Greens, YlOrRd, Bluered, RdBu, Reds, Blues, Picnic, Rainbow, Portland, Jet
# Hot, Blackbody, Earth, Electric, Viridis, Cividis

fig.add_trace(go.Volume(x = xi.flatten(), y = yi.flatten(), z = zi.flatten(),
                        value = ci.T.flatten(), isomin = iso_minimo, isomax = iso_maximo,
                        opacity = 0.1,         # needs to be small to see through all surfaces
                        surface_count = n_iso, # needs to be a large number for good volume rendering
                        caps = dict(x_show = False, y_show = False, z_show = False),
                        colorbar = dict(title = titulo_bar), colorscale = 'Jet'))

if (Dimensao == 1): cl = ' (2' + '\u03C0' + '/a)'             #  (2pi/a)
if (Dimensao == 2): cl = ' (' + '\u212B' + '<sup>-1</sup>)'   #  (Angs.^-1)
if (Dimensao == 3): cl = ' (nm<sup>-1</sup>)'                 #  (nm^-1)

if (Dimensao < 4):
   c1 = 'k<sub>x</sub>' + cl
   c2 = 'k<sub>y</sub>' + cl
   c3 = 'k<sub>z</sub>' + cl
if (Dimensao == 4):
   c1 = 'k<sub>1</sub>'
   c2 = 'k<sub>2</sub>'
   c3 = 'k<sub>3</sub>'

fig.update_layout(scene = dict(xaxis_title = c1, yaxis_title = c2, zaxis_title = c3, aspectmode = 'cube'),
                  margin = dict(r = 20, b = 10, l = 10, t = 10))

fig.update_layout(xaxis_range=[min(xs), max(xs)])
fig.update_layout(yaxis_range=[min(ys), max(ys)])

fig.write_html(dir_output + 'plot_4d.html')

# fig.write_image(dir_output + 'plot_4d.png')
# fig.write_image(dir_output + 'plot_4d.pdf')
# fig.write_image(dir_output + 'plot_4d.svg')
# fig.write_image(dir_output + 'plot_4d.eps')

fig.show() 

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------
 
# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license