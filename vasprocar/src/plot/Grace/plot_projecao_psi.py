# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import numpy as np

banda = np.loadtxt(dir_files + '/output/Psi/Bandas.dat') 
banda.shape

psi = np.loadtxt(dir_files + '/output/Psi/Psi.dat') 
psi.shape

point_k  = banda[:,0]
psi_pk   = psi[:,0]
psi_band = psi[:,1]

#======================================================================
# Obtaining some Graph adjustment parameters (GRACE) ==================
#======================================================================    

x_inicial = point_k[0]
x_final = point_k[len(point_k) -1]

if (esc_fermi == 0):
   y_inicial = E_min + Efermi
   y_final   = E_max + Efermi
   
if (esc_fermi == 1):
   y_inicial = E_min
   y_final   = E_max

#======================================================================

#----------------------------------------------------------------
projection = open(dir_files + '/output/Psi/Estados_Psi.agr', 'w')    
#----------------------------------------------------------------      

# Writing GRACE ".agr" files ==========================================

projection.write("# Grace project file \n")
projection.write("# ========================================================================== \n")
projection.write(f'# written using {VASProcar_name} \n')
projection.write(f'# {url_1} \n')
projection.write(f'# {url_2} \n') 
projection.write("# ========================================================================== \n")
projection.write("@version 50122 \n")
projection.write("@with g0 \n")
projection.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
projection.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

escala_x = (x_final - x_inicial)/5
escala_y = (y_final - y_inicial)/5

projection.write(f'@    xaxis  tick major {escala_x:.2f} \n')

palavra = '"\\f{Symbol}2p/\\f{Times-Italic}a"'
if (Dimensao == 1 and dest_k != 2): projection.write(f'@    xaxis  label {palavra} \n') 
if (Dimensao == 2 and dest_k != 2): projection.write(f'@    xaxis  label "1/Angs." \n') 
if (Dimensao == 3 and dest_k != 2): projection.write(f'@    xaxis  label "1/nm" \n')

if (dest_k == 2):
   projection.write(f'@    xaxis  tick spec type both \n')
   projection.write(f'@    xaxis  tick spec {contador2} \n')
   for i in range (contador2):
       projection.write(f'@    xaxis  tick major {i}, {dest_pk[i]} \n')
       temp_r = label_pk[i]
       for j in range(34):
           if (temp_r == '#' + str(j+1)): temp_r = r_grace[j]
       if (DFT == '_QE/' and l_symmetry == 1):
          temp_r = temp_r + '\\f{Times-Roman}(' + symmetry_pk[i] + ')'
       #--------------------------------------------------------------             
       projection.write(f'@    xaxis  ticklabel {i}, "{temp_r}" \n')

projection.write(f'@    yaxis  tick major {escala_y:.2f} \n')

if (esc_fermi == 0):
   projection.write(f'@    yaxis  label "E (eV)" \n')
if (esc_fermi == 1):
   projection.write(f'@    yaxis  label "E-Ef (eV)" \n')

projection.write(f'@    legend loctype view \n')
projection.write(f'@    legend {fig_xmin}, {fig_ymax} \n')
projection.write(f'@    legend box fill pattern 4 \n')
projection.write(f'@    legend length 1 \n')

for j in range (1,(n_psi+1)):

    legend = label_psi[j-1]
    grac = 's' + str(j-1)

    # Cor dos estados Psi:
    if (j == 1): color = c_Psi1
    if (j == 2): color = c_Psi2
    if (j == 3): color = c_Psi3
    if (j == 4): color = c_Psi4
    if (j == 5): color = c_Psi5 
    if (j == 6): color = c_Psi6      
          
    projection.write(f'@    {grac} type xysize \n')
    projection.write(f'@    {grac} symbol 1 \n')
    projection.write(f'@    {grac} symbol color {color} \n')
    projection.write(f'@    {grac} symbol fill color {color} \n')
    projection.write(f'@    {grac} symbol fill pattern 1 \n')
    projection.write(f'@    {grac} line type 0 \n')
    projection.write(f'@    {grac} line color {color} \n')   
    projection.write(f'@    {grac} legend  "{legend}" \n')
                     
number = 0

for j in range(nb+1+contador2):

    number += 1

    if (j <= (nb-1)): color = 1  # Black color
    if (j == nb):     color = 2  # Red color
    if (j > nb):      color = 7  # Gray color
   
    projection.write(f'@    s{j + n_psi} type xysize \n')
    projection.write(f'@    s{j + n_psi} line type 1 \n')
    projection.write(f'@    s{j + n_psi} line color {color} \n') 

projection.write("@type xysize")
projection.write(" \n")
      
# Psi_State plot ======================================================

for i in range (1,(n_psi+1)):  
    psi_n = psi[:,(i+1)]  
    for k in range (n_procar*nk*num_bands):
        #-------------------------------------------------------------------------   
        if (k == 1):    
           projection.write(f'{psi_pk[0]} {psi_band[0] + dE_fermi} 0.0 \n')
        if (psi_n[k] > 0.0):    
           projection.write(f'{psi_pk[k]} {psi_band[k] + dE_fermi} {psi_n[k]} \n')
        #-------------------------------------------------------------------------
    projection.write(" \n")
       
# Band Structure Plot =================================================
    
for i in range (1,(nb+1)):
    band = banda[:,i] 
    projection.write(" \n")       
    if (bands_sn[i] == "nao"):
       projection.write(f'{point_k[1]} {band[1] + dE_fermi} 0.0 \n')
    if (bands_sn[i] == "sim"):
       for j in range (n_procar*nk):
           projection.write(f'{point_k[j]} {band[j] + dE_fermi} 0.0 \n')

# Highlighting the Fermi energy in the Band structure =================

projection.write(" \n")
projection.write(f'{x_inicial} {dest_fermi} 0.0 \n')
projection.write(f'{x_final} {dest_fermi} 0.0 \n')

# Highlighting k-points of interest in the Band structure =============

if (dest_k > 0):
   for loop in range (contador2):
       projection.write(" \n")
       projection.write(f'{dest_pk[loop]} {energ_min + dE_fermi} 0.0 \n')
       projection.write(f'{dest_pk[loop]} {energ_max + dE_fermi} 0.0 \n')

#-----------------
projection.close()
#-----------------
