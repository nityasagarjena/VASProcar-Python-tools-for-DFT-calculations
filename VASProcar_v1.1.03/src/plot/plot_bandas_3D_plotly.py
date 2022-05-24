
import os
import scipy.interpolate as interp
from scipy.interpolate import griddata
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objects as go

print(" ")
print("=============== Plotando as Bandas 3D (Plotly) ===============")

#------------------------------------------------------------------------
# Teste para saber quais diretorios devem ser corretamente informados ---
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/Bandas_3D/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Plotly ===========================
#======================================================================
#======================================================================  

banda = np.loadtxt(dir_output + 'Bandas_3D.dat') 
banda.shape

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

if (Plano_k == 1):     # Plano (kx,ky) ou (k1,k2)     
   eixo1 = banda[:,0]
   eixo2 = banda[:,1]
if (Plano_k == 2):     # Plano (kx,kz) ou (k1,k3)     
   eixo1 = banda[:,0]
   eixo2 = banda[:,2]
if (Plano_k == 3):     # Plano (ky,kz) ou (k2,k3)    
   eixo1 = banda[:,1]
   eixo2 = banda[:,2]

# Create meshgrid for x,y
xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)

#----------------------------------------------------------------------

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0

#---------------------------------------------------------------------- 

fig = go.Figure()

for i in range (1,(Band_f - Band_i +2)):

    #-------------------------------------
    energ = banda[:,(i + 2)] + dE_fermi 
    label = 'Banda ' + str(Band_i + (i-1))
    #-------------------------------------
    # Grid data
    z_grid = griddata((eixo1,eixo2), energ, (x_grid,y_grid), method = 'cubic')
    #-------------------------------------------------------------------------

    if (tipo_plot == 0):
       fig.add_trace(go.Scatter3d(x = eixo1, y = eixo2, z = energ, name = label, mode = 'markers', marker = dict(size = 2, color = i, opacity = 0.5)))
    if (tipo_plot == 1):
       fig.add_trace(go.Surface(x = x_grid, y = y_grid, z = z_grid, name = label, opacity = 0.8, showscale = False))
       n_contour = 0
       if (n_contour > 0): fig.add_trace(go.Surface(contours = {"z": {"show": True, "start": energ.min(), "end": energ.max(), "size": (energ.max() - energ.min())/n_contour, "color":"black"}}, x = x_grid, y = y_grid, z = z_grid))
    if (tipo_plot == 2):
       fig.add_trace(go.Scatter3d(x = eixo1, y = eixo2, z = energ, name = label, mode = 'markers', marker = dict(size = 2, color = i, opacity = 0.5)))
       fig.add_trace(go.Surface(x = x_grid, y = y_grid, z = z_grid, name = label, opacity = 0.8, showscale = False))      

if (Dimensao == 1): cl = ' (2' + '\u03C0' + '/a)'             #  (2pi/a)
if (Dimensao == 2): cl = ' (' + '\u212B' + '<sup>-1</sup>)'   #  (Angs.^-1)
if (Dimensao == 3): cl = ' (nm<sup>-1</sup>)'                 #  (nm^-1) 

if (Plano_k == 1 and Dimensao != 4):             # Plano (kx,ky)      
   c1 = 'k<sub>x</sub>' + cl
   c2 = 'k<sub>y</sub>' + cl
if (Plano_k == 2 and Dimensao != 4):             # Plano (kx,kz)      
   c1 = 'k<sub>x</sub>' + cl
   c2 = 'k<sub>z</sub>' + cl
if (Plano_k == 3 and Dimensao != 4):             # Plano (ky,kz)      
   c1 = 'k<sub>y</sub>' + cl
   c2 = 'k<sub>z</sub>' + cl

if (Plano_k == 1 and Dimensao == 4):             # Plano (k1,k2)      
   c1 = 'k<sub>1</sub>'
   c2 = 'k<sub>2</sub>'
if (Plano_k == 2 and Dimensao == 4):             # Plano (k1,k3)      
   c1 = 'k<sub>1</sub>'
   c2 = 'k<sub>3</sub>'
if (Plano_k == 3 and Dimensao == 4):             # Plano (k2,k3)      
   c1 = 'k<sub>2</sub>'
   c2 = 'k<sub>3</sub>'

if (esc_fermi == 0):
   energ_title = 'E (eV)'
if (esc_fermi == 1):
   energ_title = 'E-E<sub>f</sub> (eV)'  

fig.update_layout(scene = dict(xaxis_title = c1, yaxis_title = c2, zaxis_title = energ_title, aspectmode = 'cube'),
                  margin = dict(r = 20, b = 10, l = 10, t = 10))

fig.write_html(dir_output + 'Bandas_3d.html')

# fig.write_image(dir_output + 'Bandas_3d.png')
# fig.write_image(dir_output + 'Bandas_3d.pdf')
# fig.write_image(dir_output + 'Bandas_3d.eps')
                     
fig.show()

#======================================================================

if (dir_output != ''):
   print(" ")
   print("=========================================================")
   print("= Edite o Plot3D por meio dos seguintes arquivos gerados ")
   print("= na pasta output/Bandas_3D =============================")   
   print("= Bandas_3D_matplotlib.py e Bandas_3D_plotly.py =========")
   print("=========================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
