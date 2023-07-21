# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license
                         
# Orbital Label ======================================================= 

if (esc == 0): label_add = ''
if (esc == 1): label_add = 'l-'

r_pdos = ['']*(23)
#-----------------
r_pdos[1]  = label_add + 'S';   r_pdos[2]  = label_add + 'P';   r_pdos[3]  = label_add + 'D'
r_pdos[7]  = label_add + 'Px';  r_pdos[8]  = label_add + 'Py';  r_pdos[9]  = label_add + 'Pz'
r_pdos[13] = label_add + 'Dxy'; r_pdos[14] = label_add + 'Dyz'; r_pdos[15] = label_add + 'Dz2'; r_pdos[16] = label_add + 'Dxz'; r_pdos[17] = label_add + 'Dx2'

# Color of Orbitals ===================================================

cor_orb = [7]*(23)
#-----------------
cor_orb[1]  = c_S;   cor_orb[2]  = c_P;   cor_orb[3]  = c_D     # pDOS S|P|D (Up) color
cor_orb[4]  = c_S;   cor_orb[5]  = c_P;   cor_orb[6]  = c_D     # pDOS S|P|D (Down) color
cor_orb[7]  = c_Px;  cor_orb[8]  = c_Py;  cor_orb[9]  = c_Pz    # pDOS Px|Py|Pz (Up) color
cor_orb[10] = c_Px;  cor_orb[11] = c_Py;  cor_orb[12] = c_Pz    # pDOS Px|Py|Pz (Down) color
cor_orb[13] = c_Dxy; cor_orb[14] = c_Dyz; cor_orb[15] = c_Dz2; cor_orb[16] = c_Dxz; cor_orb[17] = c_Dx2    # pDOS Dxy|Dyz|Dz2|Dxz|Dx2 (Up) color
cor_orb[18] = c_Dxy; cor_orb[19] = c_Dyz; cor_orb[20] = c_Dz2; cor_orb[21] = c_Dxz; cor_orb[22] = c_Dx2    # pDOS Dxy|Dyz|Dz2|Dxz|Dx2 (Down) color

#======================================================================

if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

for i in range (1,(loop+1)):     # Loop for DOS and pDOS analysis
        
#-----------------------------------------------------------------------

    if (i == 1):
       s = 1; t = (6+1)
       #---------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/DOS_pDOS.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/DOS_lpDOS.agr', 'w')
       #---------------------------------------------------------------------------      
       
    if (i == 2):
       s = 7; t = (12+1) 
       #-------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/pDOS_P.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/lpDOS_P.agr', 'w') 
       #-------------------------------------------------------------------------
              
    if (i == 3):
       s = 13; t = (22+1)  
       #-------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/pDOS_D.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/lpDOS_D.agr', 'w')
       #-------------------------------------------------------------------------      

    # Writing GRACE ".agr" files ===============================================================

    dos_pdos.write("# Grace project file \n")
    dos_pdos.write("# ========================================================================== \n")
    dos_pdos.write(f'# written using {VASProcar_name} \n')
    dos_pdos.write(f'# {url_1} \n')
    dos_pdos.write(f'# {url_2} \n') 
    dos_pdos.write("# ========================================================================== \n")
    dos_pdos.write("@version 50122 \n")
    dos_pdos.write("@with g0 \n")

    escala_x = ( x_final + (x_inicial*(-1)) )/5
    escala_y = (y_final - y_inicial)/5

    if (escala_x == 0.0):
       x_inicial = -0.01
       x_final   = +0.01
       escala_x  = 0.004 

    dos_pdos.write(f'@    world {x_inicial}, {y_inicial + dE_fermi}, {x_final}, {y_final + dE_fermi} \n')
    dos_pdos.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')     
    dos_pdos.write(f'@    xaxis  tick major {escala_x} \n')
    dos_pdos.write(f'@    xaxis  label "Density of States" \n')    
    dos_pdos.write(f'@    yaxis  tick major {escala_y:.2f} \n')

    if (esc_fermi == 0):
       dos_pdos.write(f'@    yaxis  label "E (eV)" \n')
    if (esc_fermi == 1):
       dos_pdos.write(f'@    yaxis  label "E-Ef (eV)" \n')    

    if (esc == 0):
       if (i == 1): Delta = -0.105
       if (i == 2): Delta = -0.080       
       if (i == 3): Delta = -0.098
       
    if (esc == 1):
       if (i == 1): Delta = -0.122
       if (i == 2): Delta = -0.098       
       if (i == 3): Delta = -0.116

    dos_pdos.write(f'@    legend loctype view \n')
    dos_pdos.write(f'@    legend {fig_xmax + Delta}, {fig_ymax} \n')
    dos_pdos.write(f'@    legend box fill pattern 4 \n')
    dos_pdos.write(f'@    legend length 1 \n') 

    dos_pdos.write(f'@    s0 type xy \n')
    dos_pdos.write(f'@    s0 line type 1 \n')
    dos_pdos.write(f'@    s0 line color {c_DOS} \n')
    dos_pdos.write(f'@    s0 line linewidth 1.5 \n')
    dos_pdos.write(f'@    s0 fill type 1 \n')
    dos_pdos.write(f'@    s0 fill color {c_DOS} \n')
    dos_pdos.write(f'@    s0 fill pattern 4 \n')

    if (i == 1): dos_pdos.write(f'@    s0 legend  "DOS" \n')
    if (i == 2): dos_pdos.write(f'@    s0 legend  "P" \n')
    if (i == 3): dos_pdos.write(f'@    s0 legend  "D" \n')

    dos_pdos.write(f'@    s1 type xy \n')
    dos_pdos.write(f'@    s1 line type 1 \n')
    dos_pdos.write(f'@    s1 line color {c_DOS} \n')
    dos_pdos.write(f'@    s1 line linewidth 1.5 \n')
    dos_pdos.write(f'@    s1 fill type 1 \n')
    dos_pdos.write(f'@    s1 fill color {c_DOS} \n')
    dos_pdos.write(f'@    s1 fill pattern 4 \n')

    number = 1
    
    if (esc == 1):
       number = 3
     
       #---------------------------------------------------------
       dos_pdos.write(f'@    s2 type xy \n')
       dos_pdos.write(f'@    s2 line type 1 \n')
       dos_pdos.write(f'@    s2 line color {c_lDOS} \n')
       dos_pdos.write(f'@    s2 line linewidth 1.5 \n')
       dos_pdos.write(f'@    s2 fill type 1 \n')
       dos_pdos.write(f'@    s2 fill color {c_lDOS} \n')
       dos_pdos.write(f'@    s2 fill pattern 4 \n')
       if (i == 1): dos_pdos.write(f'@    s2 legend  "l-DOS" \n')
       if (i == 2): dos_pdos.write(f'@    s2 legend  "l-P" \n')
       if (i == 3): dos_pdos.write(f'@    s2 legend  "l-D" \n')             
       #---------------------------------------------------------
       dos_pdos.write(f'@    s3 type xy \n')
       dos_pdos.write(f'@    s3 line type 1 \n')
       dos_pdos.write(f'@    s3 line color {c_lDOS} \n')
       dos_pdos.write(f'@    s3 line linewidth 1.5 \n')
       dos_pdos.write(f'@    s3 fill type 1 \n')
       dos_pdos.write(f'@    s3 fill color {c_lDOS} \n')
       dos_pdos.write(f'@    s3 fill pattern 4 \n')      
       
    for j in range (s,t):
        number += 1
           
        dos_pdos.write(f'@    s{number} type xy \n')
        dos_pdos.write(f'@    s{number} line type 1 \n')
        dos_pdos.write(f'@    s{number} line color {cor_orb[j]} \n')
        dos_pdos.write(f'@    s{number} line linewidth 1.5 \n')
        dos_pdos.write(f'@    s{number} fill type 1 \n')
        dos_pdos.write(f'@    s{number} fill color {cor_orb[j]} \n')
        dos_pdos.write(f'@    s{number} fill pattern 4 \n')      
        dos_pdos.write(f'@    s{number} legend  "{r_pdos[j]}" \n')  

    dos_pdos.write(f'@    s{number + 1} type xy \n')
    dos_pdos.write(f'@    s{number + 1} line type 1 \n')
    dos_pdos.write(f'@    s{number + 1} line linestyle 3 \n')
    dos_pdos.write(f'@    s{number + 1} line linewidth 2.0 \n')
    dos_pdos.write(f'@    s{number + 1} line color 7 \n')

    dos_pdos.write("@type xy")
    dos_pdos.write(" \n")
      
    # Plot of DOS and pDOS ====================================================================================

    for l in range(1,(14+1)):
        for k in range (1,(NEDOS+1)):
            #==================================================================================================
            if (i == 1 and l == 1): dos_pdos.write(f'{dos_u_tot[k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 2): dos_pdos.write(f'{dos_d_tot[k]} {energia[k] + dE_fermi} \n')
            #--------------------------------------------------------------------------------------------------
            if (esc == 1 and (i == 1 and l == 3)): dos_pdos.write(f'{ldos_u[k]} {energia[k] + dE_fermi} \n')
            if (esc == 1 and (i == 1 and l == 4)): dos_pdos.write(f'{ldos_d[k]} {energia[k] + dE_fermi} \n')  
            #--------------------------------------------------------------------------------------------------
            if (i == 1 and l == 5): dos_pdos.write(f'{lpdos_u_S[k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 6): dos_pdos.write(f'{lpdos_u_P[k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 7): dos_pdos.write(f'{lpdos_u_D[k]} {energia[k] + dE_fermi} \n')
            #--------------------------------------------------------------------------------------------------
            if (i == 1 and l == 8):  dos_pdos.write(f'{lpdos_d_S[k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 9):  dos_pdos.write(f'{lpdos_d_P[k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 10): dos_pdos.write(f'{lpdos_d_D[k]} {energia[k] + dE_fermi} \n')
            #==================================================================================================
            if (i == 2 and l == 1): dos_pdos.write(f'{pdos_u_P_tot[k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 2): dos_pdos.write(f'{pdos_d_P_tot[k]} {energia[k] + dE_fermi} \n')
            #--------------------------------------------------------------------------------------------------
            if (esc == 1 and (i == 2 and l == 3)): dos_pdos.write(f'{lpdos_u_P[k]} {energia[k] + dE_fermi} \n')
            if (esc == 1 and (i == 2 and l == 4)): dos_pdos.write(f'{lpdos_d_P[k]} {energia[k] + dE_fermi} \n') 
            #--------------------------------------------------------------------------------------------------
            if (i == 2 and l == 5): dos_pdos.write(f'{lpdos_u_tot[4][k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 6): dos_pdos.write(f'{lpdos_u_tot[2][k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 7): dos_pdos.write(f'{lpdos_u_tot[3][k]} {energia[k] + dE_fermi} \n')
            #--------------------------------------------------------------------------------------------------
            if (i == 2 and l == 8):  dos_pdos.write(f'{lpdos_d_tot[4][k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 9):  dos_pdos.write(f'{lpdos_d_tot[2][k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 10): dos_pdos.write(f'{lpdos_d_tot[3][k]} {energia[k] + dE_fermi} \n')
            #==================================================================================================
            if (i == 3 and l == 1): dos_pdos.write(f'{pdos_u_D_tot[k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 2): dos_pdos.write(f'{pdos_d_D_tot[k]} {energia[k] + dE_fermi} \n')
            #--------------------------------------------------------------------------------------------------
            if (esc == 1 and (i == 3 and l == 3)): dos_pdos.write(f'{lpdos_u_D[k]} {energia[k] + dE_fermi} \n')
            if (esc == 1 and (i == 3 and l == 4)): dos_pdos.write(f'{lpdos_d_D[k]} {energia[k] + dE_fermi} \n')
            #-------------------------------------------------------------------------------------------------- 
            if (i == 3 and l == 5): dos_pdos.write(f'{lpdos_u_tot[5][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 6): dos_pdos.write(f'{lpdos_u_tot[6][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 7): dos_pdos.write(f'{lpdos_u_tot[7][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 8): dos_pdos.write(f'{lpdos_u_tot[8][k]} {energia[k] + dE_fermi} \n')           
            if (i == 3 and l == 9): dos_pdos.write(f'{lpdos_u_tot[9][k]} {energia[k] + dE_fermi} \n')
            #--------------------------------------------------------------------------------------------------           
            if (i == 3 and l == 10): dos_pdos.write(f'{lpdos_d_tot[5][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 11): dos_pdos.write(f'{lpdos_d_tot[6][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 12): dos_pdos.write(f'{lpdos_d_tot[7][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 13): dos_pdos.write(f'{lpdos_d_tot[8][k]} {energia[k] + dE_fermi} \n')           
            if (i == 3 and l == 14): dos_pdos.write(f'{lpdos_d_tot[9][k]} {energia[k] + dE_fermi} \n')
            #==================================================================================================
        dos_pdos.write(" \n")

    # Highlighting the Fermi energy in the Band structure =====================================================

    dos_pdos.write(" \n")
    dos_pdos.write(f'{x_inicial} {dest_fermi} \n')
    dos_pdos.write(f'{x_final} {dest_fermi} \n')
      
    #---------------
    dos_pdos.close()
    #---------------
    
