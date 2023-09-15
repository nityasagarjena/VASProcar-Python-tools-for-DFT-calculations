# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license
                          
# Rotulo dos Orbitais ================================================= 

r_pdos = [0]*(12)
r_pdos[1] = 'S'; r_pdos[2] = 'P'; r_pdos[3] = 'D'; r_pdos[4] = 'Px'; r_pdos[5] = 'Py'; r_pdos[6] = 'Pz'
r_pdos[7] = 'Dxy'; r_pdos[8] = 'Dyz'; r_pdos[9] = 'Dz2'; r_pdos[10] = 'Dxz'; r_pdos[11] = 'Dx2'

#======================================================================

if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

for i in range (1,(loop+1)):     # Loop para a analise da DOS e pDOS
        
#-----------------------------------------------------------------------

    if (i == 1):
       s = 1; t = (3+1); r = 4
       #-------------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/DOS_pDOS.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/DOS_pDOS_lDOs.agr', 'w')
       #-------------------------------------------------------------------------------      
       
    if (i == 2):
       s = 4; t = (6+1); r = 4
       #-----------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/pDOS_P.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/pDOS_lDOS_P.agr', 'w') 
       #-----------------------------------------------------------------------------
       
    if (i == 3):
       s = 7; t = (11+1); r = 6 
       #-----------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/pDOS_D.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/pDOS_lDOS_D.agr', 'w')
       #-----------------------------------------------------------------------------

# Escrita do arquivo ".agr" do GRACE ===================================

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

    dos_pdos.write(f'@    legend loctype world \n')
    #----------------------------------------------
    if (i == 1): d_x = (x_final/5.15)
    if (i == 2): d_x = (x_final/6.25)
    if (i == 3): d_x = (x_final/5.40)
    d_y = (y_final/20)
    dos_pdos.write(f'@    legend {x_final - d_x}, {y_final + dE_fermi - d_y} \n')
    #---------------------------------------------------
    dos_pdos.write(f'@    legend box fill pattern 4 \n')
    dos_pdos.write(f'@    legend length 1 \n')

    dos_pdos.write(f'@    s0 type xy \n')
    dos_pdos.write(f'@    s0 line type 1 \n')
    dos_pdos.write(f'@    s0 line color 1 \n')
    dos_pdos.write(f'@    s0 line linewidth 1.5 \n')
    dos_pdos.write(f'@    s0 fill type 1 \n')
    dos_pdos.write(f'@    s0 fill color 7 \n')
    dos_pdos.write(f'@    s0 fill pattern 4 \n')

    if (i == 1): dos_pdos.write(f'@    s0 legend  "DOS" \n')
    if (i == 2): dos_pdos.write(f'@    s0 legend  "P" \n')
    if (i == 3): dos_pdos.write(f'@    s0 legend  "D" \n')

    number = 0
    
    if (i == 1 and esc == 1):
       number = 1; r = 5
       dos_pdos.write(f'@    s1 type xy \n')
       dos_pdos.write(f'@    s1 line type 1 \n')
       dos_pdos.write(f'@    s1 line color 10 \n')
       dos_pdos.write(f'@    s1 line linewidth 1.5 \n')
       dos_pdos.write(f'@    s1 fill type 1 \n')
       dos_pdos.write(f'@    s1 fill color 10 \n')
       dos_pdos.write(f'@    s1 fill pattern 4 \n')      
       dos_pdos.write(f'@    s1 legend  "l-DOS" \n')     
       
    for j in range (s,t):
        number += 1
          
        if (j == (s+0)): color = cor_orb[j]        # Cor dos Orbitais (S,Px,Dxy)
        if (j == (s+1)): color = cor_orb[j]        # Cor dos Orbitais (P,Py,Dyz)
        if (j == (s+2)): color = cor_orb[j]        # Cor dos Orbitais (D,Pz,Dz2)
        if (j == (s+3)): color = cor_orb[j]        # Cor do Orbital Dxz
        if (j == (s+4)): color = cor_orb[j]        # Cor do Orbital Dx2
           
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
      
# Plot da DOS e pDOS ======================================================

    for l in range(1,(6+1)):
        for k in range (1,(NEDOS+1)):
            #==============================================================================================
            if (i == 1 and l == 1): dos_pdos.write(f'{dos[k]} {energia[k] + dE_fermi} \n')
            if (esc == 1 and (i == 1 and l == 2)): dos_pdos.write(f'{l_dos[k]} {energia[k] + dE_fermi} \n')            
            if (i == 1 and l == 3): dos_pdos.write(f'{pdos_tot[1][k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 4): dos_pdos.write(f'{pdos_P_tot[k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 5): dos_pdos.write(f'{pdos_D_tot[k]} {energia[k] + dE_fermi} \n')
            #==============================================================================================
            if (i == 2 and l == 1): dos_pdos.write(f'{pdos_P_tot[k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 2): dos_pdos.write(f'{pdos_tot[4][k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 3): dos_pdos.write(f'{pdos_tot[2][k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 4): dos_pdos.write(f'{pdos_tot[3][k]} {energia[k] + dE_fermi} \n')
            #==============================================================================================
            if (i == 3 and l == 1): dos_pdos.write(f'{pdos_D_tot[k]} {energia[k] + dE_fermi} \n') 
            if (i == 3 and l == 2): dos_pdos.write(f'{pdos_tot[5][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 3): dos_pdos.write(f'{pdos_tot[6][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 4): dos_pdos.write(f'{pdos_tot[7][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 5): dos_pdos.write(f'{pdos_tot[8][k]} {energia[k] + dE_fermi} \n')           
            if (i == 3 and l == 6): dos_pdos.write(f'{pdos_tot[9][k]} {energia[k] + dE_fermi} \n')
            #==============================================================================================
        dos_pdos.write(" \n")

# Destacando a energia de Fermi na estrutura de Bandas ================

    dos_pdos.write(" \n")
    dos_pdos.write(f'{x_inicial} {dest_fermi} \n')
    dos_pdos.write(f'{x_final} {dest_fermi} \n')
      
    #---------------
    dos_pdos.close()
    #---------------
    
