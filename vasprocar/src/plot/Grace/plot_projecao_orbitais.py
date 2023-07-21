# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import numpy as np

banda = np.loadtxt(dir_files + '/output/Orbitais/Bandas.dat') 
banda.shape

orbitais = np.loadtxt(dir_files + '/output/Orbitais/Orbitais.dat') 
orbitais.shape

point_k  = banda[:,0]
orb_pk   = orbitais[:,0]
orb_band = orbitais[:,1]

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
                          
if (n_orb <= 4):  loop = 1          
if (n_orb == 9):  loop = 3
if (n_orb == 16): loop = 4

# Orbital Label ======================================================= 

t_orb = [0]*(20)
t_orb[1]  = 'S'; t_orb[2] = 'P'; t_orb[3] = 'D'; t_orb[4] = 'F'; t_orb[5] = 'Px'; t_orb[6] = 'Py'; t_orb[7] = 'Pz'
t_orb[8]  = 'Dxy'; t_orb[9] = 'Dyz'; t_orb[10] = 'Dz2'; t_orb[11] = 'Dxz'; t_orb[12] = 'Dx2'
t_orb[13] = 'Fyx2'; t_orb[14] = 'Fxyz'; t_orb[15] = 'Fyz2'; t_orb[16] = 'Fzz2'; t_orb[17] = 'Fxz2'; t_orb[18] = 'Fzx2'; t_orb[19] = 'Fxx2'

#======================================================================

for i in range (1,(loop+1)):     # Loop for analysis of projections
        
#-----------------------------------------------------------------------

    if (i == 1):
       if (n_orb == 3 or n_orb == 9): 
          s = 1; t = (3+1)
          #----------------------------------------------------------------------
          projection = open(dir_files + '/output/Orbitais/Orbitais_SPD.agr', 'w')
          #----------------------------------------------------------------------  
       if (n_orb == 4 or n_orb == 16):
          s = 1; t = (4+1)
          #-----------------------------------------------------------------------
          projection = open(dir_files + '/output/Orbitais/Orbitais_SPDF.agr', 'w')
          #----------------------------------------------------------------------- 
       
    if (i == 2):
       s = 5; t = (7+1)
       #--------------------------------------------------------------------
       projection = open(dir_files + '/output/Orbitais/Orbitais_P.agr', 'w')     
       #--------------------------------------------------------------------
       
    if (i == 3):
       s = 8; t = (12+1)  
       #--------------------------------------------------------------------
       projection = open(dir_files + '/output/Orbitais/Orbitais_D.agr', 'w')
       #--------------------------------------------------------------------

    if (i == 4):
       s = 13; t = (19+1)  
       #--------------------------------------------------------------------
       projection = open(dir_files + '/output/Orbitais/Orbitais_F.agr', 'w')
       #--------------------------------------------------------------------

    # Writing GRACE ".agr" files ===========================================

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
       
    for j in range (s,t):
          
        if (j == (s+0)):
           grac='s0'
           if (i == 1): color = c_S
           if (i == 2): color = c_Px
           if (i == 3): color = c_Dxy
           if (i == 4): color = c_Fyx2

        if (j == (s+1)):
           grac='s1'
           if (i == 1): color = c_P
           if (i == 2): color = c_Py
           if (i == 3): color = c_Dyz
           if (i == 4): color = c_Fxyz

        if (j == (s+2)):
           grac='s2'
           if (i == 1): color = c_D
           if (i == 2): color = c_Pz
           if (i == 3): color = c_Dz2
           if (i == 4): color = c_Fyz2

        if (j == (s+3)):
           grac='s3'
           if (i == 1): color = c_F
           if (i == 3): color = c_Dxz
           if (i == 4): color = c_Fzz2

        if (j == (s+4)):
           grac='s4'
           if (i == 3): color = c_Dx2
           if (i == 4): color = c_Fxz2

        if (j == (s+5)):
           grac='s5'
           if (i == 4): color = c_Fzx2

        if (j == (s+6)):
           grac='s6'
           if (i == 4): color = c_Fxx2
 
        projection.write(f'@    {grac} type xysize \n')
        projection.write(f'@    {grac} symbol 1 \n')
        projection.write(f'@    {grac} symbol color {color} \n')
        projection.write(f'@    {grac} symbol fill color {color} \n')
        projection.write(f'@    {grac} symbol fill pattern 1 \n')
        projection.write(f'@    {grac} line type 0 \n')
        projection.write(f'@    {grac} line color {color} \n')
        projection.write(f'@    {grac} legend  "{t_orb[j]}" \n')

    for j in range(nb+1+contador2):

        if (j <= (nb-1)): color = 1  # Black color
        if (j == nb):     color = 2  # Red color
        if (j > nb):      color = 7  # Gray color
   
        projection.write(f'@    s{j+(t-s)} type xysize \n')
        projection.write(f'@    s{j+(t-s)} line type 1 \n')
        projection.write(f'@    s{j+(t-s)} line color {color} \n') 

    projection.write("@type xysize")
    projection.write(" \n")
      
# Plot of Orbitals ====================================================

    for j in range (s,t):      

        #------------------------------------------------------
        if (j == 1): # Orbital S
           orbital = orbitais[:,2]*peso_total   
        if (j == 2): # Orbital P (P = Px + Py + Pz)
           orbital = orbitais[:,3]*peso_total 
        if (j == 3): # Orbital D (D = Dxy + Dyz + Dz2 + Dxz + Dx2)
           orbital = orbitais[:,4]*peso_total 
        if (j == 4): # Orbital F (F = Fyx2 + Fxyz + Fyz2 + Fzz2 + Fxz2 + Fzx2 + Fxx2)
           orbital = orbitais[:,5]*peso_total 
        #------------------------------------------------------
        if (j == 5): # Orbital Px 
           orbital = orbitais[:,6]*peso_total
        if (j == 6): # Orbital Py 
           orbital = orbitais[:,7]*peso_total
        if (j == 7): # Orbital pz 
           orbital = orbitais[:,8]*peso_total
        #------------------------------------------------------
        if (j == 8):  # Orbital Dxy 
           orbital =  orbitais[:,9]*peso_total
        if (j == 9):  # Orbital Dyz 
           orbital =  orbitais[:,10]*peso_total
        if (j == 10): # Orbital Dz2 
           orbital =  orbitais[:,11]*peso_total
        if (j == 11): # Orbital Dxz 
           orbital =  orbitais[:,12]*peso_total
        if (j == 12): # Orbital Dx2 
           orbital =  orbitais[:,13]*peso_total
        #------------------------------------------------------ 
        if (j == 13): # Orbital Fyx2 
           orbital =  orbitais[:,14]*peso_total
        if (j == 14): # Orbital Fxyz 
           orbital =  orbitais[:,15]*peso_total
        if (j == 15): # Orbital Fyz2 
           orbital =  orbitais[:,16]*peso_total
        if (j == 16): # Orbital Fzz2 
           orbital =  orbitais[:,17]*peso_total
        if (j == 17): # Orbital Fxz2 
           orbital =  orbitais[:,18]*peso_total
        if (j == 18): # Orbital Fzx2 
           orbital =  orbitais[:,19]*peso_total
        if (j == 19): # Orbital Fxx2 
           orbital =  orbitais[:,20]*peso_total
        #------------------------------------------------------ 

        for k in range (n_procar*nk*num_bands):                                      
            if (k == 1):    
               projection.write(f'{orb_pk[0]} {orb_band[0] + dE_fermi} 0.0 \n')
            if (orbital[k] > 0.0):    
               projection.write(f'{orb_pk[k]} {orb_band[k] + dE_fermi} {orbital[k]} \n')

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
