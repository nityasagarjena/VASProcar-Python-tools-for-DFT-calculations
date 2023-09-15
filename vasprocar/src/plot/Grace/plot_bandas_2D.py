# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import numpy as np

banda = np.loadtxt(dir_files + '/output/Bandas/Bandas.dat') 
banda.shape

point_k = banda[:,0]

#======================================================================
# Grace parameters ====================================================
#======================================================================    

x_inicial = point_k[0]
x_final = point_k[len(point_k) -1]

if (esc_fermi == 0):
   y_inicial = E_min + Efermi
   y_final   = E_max + Efermi
   
if (esc_fermi == 1):
   y_inicial = E_min
   y_final   = E_max

#----------------------------------------------------------
bandas = open(dir_files + '/output/Bandas/Bandas.agr', 'w')
#----------------------------------------------------------

bandas.write("# Grace project file \n")
bandas.write("# ========================================================================== \n")
bandas.write(f'# written using {VASProcar_name} \n')
bandas.write(f'# {url_1} \n')
bandas.write(f'# {url_2} \n')
bandas.write("# ========================================================================== \n")
bandas.write("@version 50122 \n")
bandas.write("@with g0 \n")
bandas.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
bandas.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

escala_x = (x_final - x_inicial)/5
escala_y = (y_final - y_inicial)/5

bandas.write(f'@    xaxis  tick major {escala_x:.2f} \n')

palavra = '"\\f{Symbol}2p/\\f{Times-Italic}a"'

if (Dimensao == 1 and dest_k != 2): bandas.write(f'@    xaxis  label {palavra} \n') 
if (Dimensao == 2 and dest_k != 2): bandas.write(f'@    xaxis  label "1/Angs." \n') 
if (Dimensao == 3 and dest_k != 2): bandas.write(f'@    xaxis  label "1/nm" \n')

if (dest_k == 2):
   bandas.write(f'@    xaxis  tick spec type both \n')
   bandas.write(f'@    xaxis  tick spec {contador2} \n')
   for i in range (contador2):   
       bandas.write(f'@    xaxis  tick major {i}, {dest_pk[i]} \n')
       temp_r = label_pk[i]
       for j in range(34):
           if (temp_r == '#' + str(j+1)): temp_r = r_grace[j]
       if (DFT == '_QE/' and l_symmetry == 1):
          temp_r = temp_r + '\\f{Times-Roman}(' + symmetry_pk[i] + ')'
       #--------------------------------------------------------------        
       bandas.write(f'@    xaxis  ticklabel {i}, "{temp_r}" \n')    
 
bandas.write(f'@    yaxis  tick major {escala_y:.2f} \n')

if (esc_fermi == 0):
   bandas.write(f'@    yaxis  label "E (eV)" \n')
if (esc_fermi == 1):
   bandas.write(f'@    yaxis  label "E-Ef (eV)" \n')

bandas.write(f'@    legend loctype view \n')
bandas.write(f'@    legend {fig_xmin}, {fig_ymax} \n')
bandas.write(f'@    legend box fill pattern 4 \n')
bandas.write(f'@    legend length 1 \n')   
   
#======================================================================

bands_sn = ["nao"]*(nb + 1)

selected_bands = bands_range.replace(':', ' ').replace('-', ' ').split()
loop = int(len(selected_bands)/2) 

for i in range (1,(loop+1)):
    #-----------------------------------------
    loop_i = int(selected_bands[(i-1)*2])
    loop_f = int(selected_bands[((i-1)*2) +1])
    #-----------------------------------------
    for j in range(loop_i, (loop_f + 1)):
        bands_sn[j] = "sim"

#======================================================================

for i in range(nb + 1 + contador2):

    if (ispin == 1):
       if (i <= (nb-1)): color = 1 # color Black
       if (i == nb):     color = 2 # color Red

    if (ispin == 2):
       if (i <= ((nb/2)-1)):                 color = 2 # color Red
       if (i > ((nb/2)-1) and i <= (nb-1)):  color = 4 # color Blue
       if (i == nb):                         color = 7 # color Gray
     
    if (i > nb):      color = 7 # color Gray 
   
    bandas.write(f'@    s{i} type xy \n')
    bandas.write(f'@    s{i} line type 1 \n')
    bandas.write(f'@    s{i} line color {color} \n')
    
    if (ispin == 2 and i == ((nb/2)-1)):  bandas.write(f'@    s{i} legend  "Spin 1" \n') 
    if (ispin == 2 and i == (nb-1)):      bandas.write(f'@    s{i} legend  "Spin 2" \n')
    
bandas.write(f'@type xy \n')   

# Band plot ===========================================================

for i in range (1,(nb+1)):
    band = banda[:,i] 
    bandas.write(" \n")       
    if (bands_sn[i] == "nao"):
       bandas.write(f'{point_k[1]} {band[1] + dE_fermi} \n')
    if (bands_sn[i] == "sim"):
       for j in range (n_procar*nk):
           bandas.write(f'{point_k[j]} {band[j] + dE_fermi} \n')

# Highlight the Fermi energy in the band structure ====================
      
bandas.write(" \n")
bandas.write(f'{x_inicial} {dest_fermi} \n')
bandas.write(f'{x_final} {dest_fermi} \n')

# Highlight k-points in the band structure ============================

if (dest_k > 0):
   for loop in range (contador2):
       bandas.write(" \n")
       bandas.write(f'{dest_pk[loop]} {energ_min + dE_fermi} \n')
       bandas.write(f'{dest_pk[loop]} {energ_max + dE_fermi} \n')     

#-------------
bandas.close()
#-------------
