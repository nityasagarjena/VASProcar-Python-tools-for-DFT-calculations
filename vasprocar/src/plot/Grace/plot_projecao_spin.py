# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import numpy as np

banda = np.loadtxt(dir_files + '/output/Spin/Bandas.dat') 
banda.shape

spin = np.loadtxt(dir_files + '/output/Spin/Spin.dat') 
spin.shape

point_k   = banda[:,0]
spin_pk   = spin[:,0]
spin_band = spin[:,1]

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

for t in range (1,(3+1)):            # Loop for analysis of projections
        
#----------------------------------------------------------------------

    if (t == 1):
       #-------------------------------------------------------------
       projection = open(dir_files + '/output/Spin/Spin_Sx.agr', 'w')
       #-------------------------------------------------------------
       letras = 'Sx'

    if (t == 2):
       #-------------------------------------------------------------
       projection = open(dir_files + '/output/Spin/Spin_Sy.agr', 'w')
       #-------------------------------------------------------------
       letras = 'Sy'

    if (t == 3):
       #-------------------------------------------------------------
       projection = open(dir_files + '/output/Spin/Spin_Sz.agr', 'w')
       #-------------------------------------------------------------
       letras = 'Sz'

    # Writing GRACE ".agr" files =================================================================

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
    if (Dimensao == 2 and dest_k != 2): projection.write(f'@    xaxis  label "(1/Angs.)" \n') 
    if (Dimensao == 3 and dest_k != 2): projection.write(f'@    xaxis  label "(1/nm)" \n')

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

    for i in range (1,(3+1)):

        if (i == 1):
           grac='s0'; color = c_spin_up; legenda = letras + ' \\f{Symbol}\\c-\\C'    # Color (Red) of the Up component of Spins Sx, Sy and Sz.
        if (i == 2):
           grac='s1'; color = c_spin_down; legenda = letras + ' \\f{Symbol}\\c/\\C'  # Color (Blue) of the Down component of Spins Sx, Sy and Sz.
        if (i == 3):
           grac='s2'; c_spin_null; legenda = ''                                      # Color (Black) of the Null component of Spins Sx, Sy and Sz.

        projection.write(f'@    {grac} type xysize \n')
        projection.write(f'@    {grac} symbol 1 \n')
        projection.write(f'@    {grac} symbol color {color} \n')
        projection.write(f'@    {grac} symbol fill color {color} \n')
        projection.write(f'@    {grac} symbol fill pattern 1 \n')
        projection.write(f'@    {grac} line type 0 \n')
        projection.write(f'@    {grac} line color {color} \n')
        if (i <= 3): projection.write(f'@    {grac} legend  "{legenda}" \n')

    for j in range(nb+1+contador2):

        if (j <= (nb-1)): color = 1  # Black color
        if (j == nb):     color = 2  # Red color
        if (j > nb):      color = 7  # Gray color        
   
        projection.write(f'@    s{j+3} type xysize \n')
        projection.write(f'@    s{j+3} line type 1 \n')
        projection.write(f'@    s{j+3} line color {color} \n')         
           
    projection.write("@type xysize")
    projection.write(" \n")
                          
    # Plot of Spin Components (Sx,Sy,Sz) ===================================

    for i in range (1,(3+1)):  # Loop search for up, down and null components (Sx,Sy,Sz)
      
    #-----------------------------------------------------------------------

        if (t == 1):

           if (i == 1):  # Sx > 0
              Si = spin[:,2]*peso_total
              for k in range (n_procar*nk*num_bands):
                  if (k == 1):    
                     projection.write(f'{spin_pk[0]} {spin_band[0] + dE_fermi} 0.0 \n')                  
                  if (Si[k] > 0.0):
                     projection.write(f'{spin_pk[k]} {spin_band[k] + dE_fermi} {Si[k]} \n')

           if (i == 2):  # Sx < 0
              Si = spin[:,3]*peso_total
              for k in range (n_procar*nk*num_bands):
                  if (k == 1):    
                     projection.write(f'{spin_pk[0]} {spin_band[0] + dE_fermi} 0.0 \n')                  
                  if (Si[k] < 0.0):
                     projection.write(f'{spin_pk[k]} {spin_band[k] + dE_fermi} {Si[k]} \n')

           if (i == 3):  # Sx = 0
              Si = (spin[:,2] + spin[:,3])*peso_total
              for k in range (n_procar*nk*num_bands):
                  if (k == 1):    
                     projection.write(f'{spin_pk[0]} {spin_band[0] + dE_fermi} 0.0 \n')                  
                  if (Si[k] == 0.0):
                     projection.write(f'{spin_pk[k]} {spin_band[k] + dE_fermi} {Si[k]} \n')

        if (t == 2):

           if (i == 1):  # Sy > 0
              Si = spin[:,4]*peso_total
              for k in range (n_procar*nk*num_bands):
                  if (k == 1):    
                     projection.write(f'{spin_pk[0]} {spin_band[0] + dE_fermi} 0.0 \n')                  
                  if (Si[k] > 0.0):
                     projection.write(f'{spin_pk[k]} {spin_band[k] + dE_fermi} {Si[k]} \n')

           if (i == 2):  # Sy < 0
              Si = spin[:,5]*peso_total
              for k in range (n_procar*nk*num_bands):
                  if (k == 1):    
                     projection.write(f'{spin_pk[0]} {spin_band[0] + dE_fermi} 0.0 \n')                  
                  if (Si[k] < 0.0):
                     projection.write(f'{spin_pk[k]} {spin_band[k] + dE_fermi} {Si[k]} \n')

           if (i == 3):  # Sy = 0
              Si = (spin[:,4] + spin[:,5])*peso_total
              for k in range (n_procar*nk*num_bands):
                  if (k == 1):    
                     projection.write(f'{spin_pk[0]} {spin_band[0] + dE_fermi} 0.0 \n')                  
                  if (Si[k] == 0.0):
                     projection.write(f'{spin_pk[k]} {spin_band[k] + dE_fermi} {Si[k]} \n')

        if (t == 3):

           if (i == 1):  # Sz > 0
              Si = spin[:,6]*peso_total
              for k in range (n_procar*nk*num_bands):
                  if (k == 1):    
                     projection.write(f'{spin_pk[0]} {spin_band[0] + dE_fermi} 0.0 \n')                  
                  if (Si[k] > 0.0):
                     projection.write(f'{spin_pk[k]} {spin_band[k] + dE_fermi} {Si[k]} \n')

           if (i == 2):  # Sz < 0
              Si = spin[:,7]*peso_total
              for k in range (n_procar*nk*num_bands):
                  if (k == 1):    
                     projection.write(f'{spin_pk[0]} {spin_band[0] + dE_fermi} 0.0 \n')                  
                  if (Si[k] < 0.0):
                     projection.write(f'{spin_pk[k]} {spin_band[k] + dE_fermi} {Si[k]} \n')

           if (i == 3):  # Sz = 0
              Si = (spin[:,6] + spin[:,7])*peso_total
              for k in range (n_procar*nk*num_bands):
                  if (k == 1):    
                     projection.write(f'{spin_pk[0]} {spin_band[0] + dE_fermi} 0.0 \n')                  
                  if (Si[k] == 0.0):
                     projection.write(f'{spin_pk[k]} {spin_band[k] + dE_fermi} {Si[k]} \n')

        #-----------------------------------------------------------------------
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
                
# Highlighting the Fermi energy in the Textures plot ==================

    projection.write(" \n")
    projection.write(f'{x_inicial} {dest_fermi} 0.0 \n')
    projection.write(f'{x_final} {dest_fermi} 0.0 \n')

# Highlighting k-points of interest in the Textures plot ==============

    if (dest_k > 0):
       for loop in range (contador2):
           projection.write(" \n")
           projection.write(f'{dest_pk[loop]} {energ_min + dE_fermi} 0.0 \n')
           projection.write(f'{dest_pk[loop]} {energ_max + dE_fermi} 0.0 \n')

    #-----------------
    projection.close()
    #-----------------
