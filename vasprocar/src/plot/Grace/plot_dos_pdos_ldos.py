# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license
                          
# Orbital Label ======================================================= 

if (esc == 0): label_add = ''
if (esc == 1): label_add = 'l-'

r_pdos = [0]*(20)
r_pdos[1]  = 'S'; r_pdos[2] = 'P'; r_pdos[3] = 'D'; r_pdos[4] = 'F'; r_pdos[5] = 'Px'; r_pdos[6] = 'Py'; r_pdos[7] = 'Pz'
r_pdos[8]  = 'Dxy'; r_pdos[9] = 'Dyz'; r_pdos[10] = 'Dz2'; r_pdos[11] = 'Dxz'; r_pdos[12] = 'Dx2'
r_pdos[13] = 'Fyx2'; r_pdos[14] = 'Fxyz'; r_pdos[15] = 'Fyz2'; r_pdos[16] = 'Fzz2'; r_pdos[17] = 'Fxz2'; r_pdos[18] = 'Fzx2'; r_pdos[19] = 'Fxx2'

for i in range(1,(19+1)):
    r_pdos[i] = label_add + r_pdos[i]

#======================================================================

if (n_orb <= 4):  loop = 1          
if (n_orb == 9):  loop = 3
if (n_orb == 16): loop = 4

#======================================================================

for i in range (1,(loop+1)):     # Loop for DOS and pDOS analysis
        
    #-----------------------------------------------------------------------

    if (i == 1):
       if (n_orb == 3 or n_orb == 9): 
          s = 1; t = (3+1); r = (3 +1)
       if (n_orb == 4 or n_orb == 16): 
          s = 1; t = (4+1); r = (4 +1)
       #---------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/DOS_pDOS.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/DOS_lpDOS.agr', 'w')
       #---------------------------------------------------------------------------     
       
    if (i == 2):
       s = 5; t = (7+1); r = (3 +1)
       #-------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/pDOS_P.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/lpDOS_P.agr', 'w') 
       #-------------------------------------------------------------------------
       
    if (i == 3):
       s = 8; t = (12+1); r = (5 +1) 
       #-------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/pDOS_D.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/lpDOS_D.agr', 'w')
       #-------------------------------------------------------------------------

    if (i == 4):
       s = 13; t = (19+1); r = (7 +1) 
       #-------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/pDOS_F.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/lpDOS_F.agr', 'w')
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
    dos_pdos.write(f'@    world {x_inicial}, {y_inicial + dE_fermi}, {x_final}, {y_final + dE_fermi} \n')
    dos_pdos.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    dos_pdos.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    dos_pdos.write(f'@    xaxis  label "Density of States" \n')    
    dos_pdos.write(f'@    yaxis  tick major {escala_y:.2f} \n')

    if (esc_fermi == 0):
       dos_pdos.write(f'@    yaxis  label "E (eV)" \n')
    if (esc_fermi == 1):
       dos_pdos.write(f'@    yaxis  label "E-Ef (eV)" \n')    

    if (esc == 0):
       if (i == 1): Delta = -0.104
       if (i == 2): Delta = -0.080       
       if (i == 3): Delta = -0.099
       if (i == 4): Delta = -0.099
   
    if (esc == 1):
       if (i == 1): Delta = -0.123
       if (i == 2): Delta = -0.098       
       if (i == 3): Delta = -0.117
       if (i == 4): Delta = -0.117
   
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
    if (i == 4): dos_pdos.write(f'@    s0 legend  "F" \n')

    number = 0
    
    if (esc == 1):

       if (n_orb == 3 or n_orb == 9): 
          number = 1; r = (4 +1)
       if (n_orb == 4 or n_orb == 16): 
          number = 1; r = (5 +1)

       dos_pdos.write(f'@    s1 type xy \n')
       dos_pdos.write(f'@    s1 line type 1 \n')
       dos_pdos.write(f'@    s1 line color {c_lDOS} \n')
       dos_pdos.write(f'@    s1 line linewidth 1.5 \n')
       dos_pdos.write(f'@    s1 fill type 1 \n')
       dos_pdos.write(f'@    s1 fill color {c_lDOS} \n')
       dos_pdos.write(f'@    s1 fill pattern 4 \n')      

       if (i == 1): dos_pdos.write(f'@    s1 legend  "l-DOS" \n')
       if (i == 2): dos_pdos.write(f'@    s1 legend  "l-P" \n')
       if (i == 3): dos_pdos.write(f'@    s1 legend  "l-D" \n')    
       if (i == 4): dos_pdos.write(f'@    s1 legend  "l-F" \n') 
      
    for j in range (s,t):
        number += 1
          
        if (j == (s+0)):
           if (i == 1): color = c_S    # pDOS_S color
           if (i == 2): color = c_Px   # pDOS_Px color
           if (i == 3): color = c_Dxy  # pDOS_Dxy color
           if (i == 4): color = c_Fyx2 # pDOS_Fyx2 color
        
        if (j == (s+1)):
           if (i == 1): color = c_P    # pDOS_P color
           if (i == 2): color = c_Py   # pDOS_Py color
           if (i == 3): color = c_Dyz  # pDOS_Dyz color
           if (i == 4): color = c_Fxyz # pDOS_Fxyz color
        
        if (j == (s+2)):
           if (i == 1): color = c_D    # pDOS_D color
           if (i == 2): color = c_Pz   # pDOS_Pz color
           if (i == 3): color = c_Dz2  # pDOS_Dz2 color
           if (i == 4): color = c_Fyz2 # pDOS_Fyz2 color   
    
        if (j == (s+3)):
           if (i == 1): color = c_F    # pDOS_F color
           if (i == 3): color = c_Dxz  # pDOS_Dxz color
           if (i == 4): color = c_Fzz2 # pDOS_Fzz2 color
        
        if (j == (s+4)):        
           if (i == 3): color = c_Dx2  # pDOS_Dx2 color
           if (i == 4): color = c_Fxz2 # pDOS_Fxz2 color

        if (j == (s+5)):        
           if (i == 4): color = c_Fzx2 # pDOS_Fzx2 color

        if (j == (s+6)):        
           if (i == 4): color = c_Fxx2 # pDOS_Fxx2 color
        
        dos_pdos.write(f'@    s{number} type xy \n')
        dos_pdos.write(f'@    s{number} line type 1 \n')
        dos_pdos.write(f'@    s{number} line color {color} \n')
        dos_pdos.write(f'@    s{number} line linewidth 1.5 \n')
        dos_pdos.write(f'@    s{number} fill type 1 \n')
        dos_pdos.write(f'@    s{number} fill color {color} \n')
        dos_pdos.write(f'@    s{number} fill pattern 4 \n')      
        dos_pdos.write(f'@    s{number} legend  "{r_pdos[j]}" \n')  

    dos_pdos.write(f'@    s{r} type xy \n')
    dos_pdos.write(f'@    s{r} line type 1 \n')
    dos_pdos.write(f'@    s{r} line linestyle 3 \n')
    dos_pdos.write(f'@    s{r} line linewidth 2.0 \n')
    dos_pdos.write(f'@    s{r} line color 7 \n')

    dos_pdos.write("@type xy")
    dos_pdos.write(" \n")
      
    # Plot of DOS and pDOS ==================================================================================

    for l in range(1,(9+1)):
        for k in range (1,(NEDOS+1)):
            #================================================================================================
            if (i == 1 and l == 1): dos_pdos.write(f'{dos_tot[k]} {energia[k] + dE_fermi} \n')
            if (esc == 1 and (i == 1 and l == 2)): dos_pdos.write(f'{ldos[k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 3): dos_pdos.write(f'{lpdos_S[k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 4): dos_pdos.write(f'{lpdos_P[k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 5): dos_pdos.write(f'{lpdos_D[k]} {energia[k] + dE_fermi} \n')            
            if (i == 1 and (n_orb == 4 or n_orb == 16) and l == 6): dos_pdos.write(f'{lpdos_F[k]} {energia[k] + dE_fermi} \n') 
            """
            if (esc == 0):
               if (i == 1 and l == 3): dos_pdos.write(f'{pdos_S_tot[k]} {energia[k] + dE_fermi} \n')
               if (i == 1 and l == 4): dos_pdos.write(f'{pdos_P_tot[k]} {energia[k] + dE_fermi} \n')
               if (i == 1 and l == 5): dos_pdos.write(f'{pdos_D_tot[k]} {energia[k] + dE_fermi} \n')
               if (i == 1 and (n_orb == 4 or n_orb == 16) and l == 6): dos_pdos.write(f'{pdos_F_tot[k]} {energia[k] + dE_fermi} \n')
            if (esc == 1):
               if (i == 1 and l == 3): dos_pdos.write(f'{lpdos_S[k]} {energia[k] + dE_fermi} \n')
               if (i == 1 and l == 4): dos_pdos.write(f'{lpdos_P[k]} {energia[k] + dE_fermi} \n')
               if (i == 1 and l == 5): dos_pdos.write(f'{lpdos_D[k]} {energia[k] + dE_fermi} \n')
               if (i == 1 and (n_orb == 4 or n_orb == 16) and l == 6): dos_pdos.write(f'{lpdos_F[k]} {energia[k] + dE_fermi} \n')
            """           
            #================================================================================================
            if (i == 2 and l == 1): dos_pdos.write(f'{pdos_P_tot[k]} {energia[k] + dE_fermi} \n')
            if (esc == 1 and (i == 2 and l == 2)): dos_pdos.write(f'{lpdos_P[k]} {energia[k] + dE_fermi} \n')    
            if (i == 2 and l == 3): dos_pdos.write(f'{lpdos_tot[4][k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 4): dos_pdos.write(f'{lpdos_tot[2][k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 5): dos_pdos.write(f'{lpdos_tot[3][k]} {energia[k] + dE_fermi} \n')
            #================================================================================================
            if (i == 3 and l == 1): dos_pdos.write(f'{pdos_D_tot[k]} {energia[k] + dE_fermi} \n')
            if (esc == 1 and (i == 3 and l == 2)): dos_pdos.write(f'{lpdos_D[k]} {energia[k] + dE_fermi} \n')               
            if (i == 3 and l == 3): dos_pdos.write(f'{lpdos_tot[5][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 4): dos_pdos.write(f'{lpdos_tot[6][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 5): dos_pdos.write(f'{lpdos_tot[7][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 6): dos_pdos.write(f'{lpdos_tot[8][k]} {energia[k] + dE_fermi} \n')           
            if (i == 3 and l == 7): dos_pdos.write(f'{lpdos_tot[9][k]} {energia[k] + dE_fermi} \n')
            #================================================================================================
            if (i == 4 and l == 1): dos_pdos.write(f'{pdos_F_tot[k]} {energia[k] + dE_fermi} \n')
            if (esc == 1 and (i == 4 and l == 2)): dos_pdos.write(f'{lpdos_F[k]} {energia[k] + dE_fermi} \n')               
            if (i == 4 and l == 3): dos_pdos.write(f'{lpdos_tot[10][k]} {energia[k] + dE_fermi} \n')
            if (i == 4 and l == 4): dos_pdos.write(f'{lpdos_tot[11][k]} {energia[k] + dE_fermi} \n')
            if (i == 4 and l == 5): dos_pdos.write(f'{lpdos_tot[12][k]} {energia[k] + dE_fermi} \n')
            if (i == 4 and l == 6): dos_pdos.write(f'{lpdos_tot[13][k]} {energia[k] + dE_fermi} \n')           
            if (i == 4 and l == 7): dos_pdos.write(f'{lpdos_tot[14][k]} {energia[k] + dE_fermi} \n')
            if (i == 4 and l == 8): dos_pdos.write(f'{lpdos_tot[15][k]} {energia[k] + dE_fermi} \n')           
            if (i == 4 and l == 9): dos_pdos.write(f'{lpdos_tot[16][k]} {energia[k] + dE_fermi} \n')
            #================================================================================================

        dos_pdos.write(" \n")

    # Highlighting the Fermi energy in the Band structure ===================================================

    dos_pdos.write(" \n")
    dos_pdos.write(f'{x_inicial} {dest_fermi} \n')
    dos_pdos.write(f'{x_final} {dest_fermi} \n')
      
    #---------------
    dos_pdos.close()
    #---------------
    
