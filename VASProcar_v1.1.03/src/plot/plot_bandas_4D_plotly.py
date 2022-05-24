
import os
import shutil
import scipy.interpolate as interp
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objects as go

print(" ")
print("=============== Plotando as Bandas 4D (Plotly) ===============")

#------------------------------------------------------------------------
# Teste para saber quais diretorios devem ser corretamente informados ---
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
# Estrutura do arquivo para Plot via MPlotly ==========================
#======================================================================
#======================================================================    

data = np.loadtxt(dir_output + 'Plot_4d.dat')
data.shape

xs = data[:,0]
ys = data[:,1]
zs = data[:,2]
cs = data[:,3] + dE_fermi

# cs = (cs - min(cs))/(max(cs) - min(cs))  #  Normaliza os valores de cs dentro do intervalo [0,1]
iso_minimo = min(cs)
iso_maximo = max(cs)

print(" ")
print("===================================================================")
print("Observacao: Caso a pagina no navegador de internet fique em loading")
print("            infinito ou apresente alguma mensagem de erro, aperte  ")
print("            F5 para recarregar a pagina, ou abra o arquivo .html   ")   
print("===================================================================")

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(". Pode demorar um pouco .")
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

fig.write_html(dir_output + 'plot_4d.html')

# fig.write_image(dir_output + 'plot_4d.png')
# fig.write_image(dir_output + 'plot_4d.pdf')
# fig.write_image(dir_output + 'plot_4d.eps')

fig.show() 
                     
#======================================================================

if (dir_output != ''):
   print(" ")
   print("=========================================================")
   print("= Edite o Plot4D por meio do arquivo Plot_4D.py gerado = ")
   print("= na pasta output/Plot_4D ===============================")   
   print("=========================================================")  

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
