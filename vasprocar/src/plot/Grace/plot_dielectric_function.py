# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

# Labels ============================================================== 

rot = [0]*(8)
rot[0] = 'Mod'; rot[1] = 'Med'
rot[2] = 'X'; rot[3] = 'Y'; rot[4] = 'Z'
# rot[5] = 'XY';     rot[6] = 'YZ';    rot[7] = 'ZX'

# Colors ==============================================================

# GRACE color code
# White  = 0, Black = 1, Red     = 2,  Green  = 3,  Blue   = 4,  Yellow = 5,  Brown     = 6, Gray = 7
# Violet = 8, Cyan  = 9, Magenta = 10, Orange = 11, Indigo = 12, Brown  = 13, Turquoise = 14

color = [0]*(8)
color[0] = '1'; color[1] = '10';  
color[2] = '4'; color[3] = '2'; color[4] = '3'
# color[5] = '9'; color[6] = '12'; color[7] = '14'

# =====================================================================

import numpy as np

func_dielet = np.loadtxt(dir_files + '/output/BSE/BSE.dat') 
func_dielet.shape

energ = func_dielet[:,0]

# =====================================================================

for i in range(2):
   
    y_inicial = +1000.0
    y_final   = -1000.0
   
    #---------------------------------------------------------------------------------
    if (i == 0): BSE = open(dir_files + '/output/BSE/Funcao_Dieletrica_IMAG.agr', 'w')
    if (i == 1): BSE = open(dir_files + '/output/BSE/Funcao_Dieletrica_REAL.agr', 'w')
    #---------------------------------------------------------------------------------

    for j in range(5):
        if (i == 0): m = (j +1)         
        if (i == 1): m = (j +6) 
        temp_min = min(func_dielet[:,m])
        temp_max = max(func_dielet[:,m])
        if (temp_min < y_inicial): y_inicial = temp_min
        if (temp_max > y_final):   y_final   = temp_max
    
    # Writing GRACE ".agr" files ===============================================================

    BSE.write("# Grace project file \n")
    BSE.write("# ========================================================================== \n")
    BSE.write(f'# written using {VASProcar_name} \n')
    BSE.write(f'# {url_1} \n')
    BSE.write(f'# {url_2} \n') 
    BSE.write("# ========================================================================== \n")
    BSE.write("@version 50122 \n")
    BSE.write("@with g0 \n")
    BSE.write(f'@    world {x_inicial + dE_fermi}, {y_inicial}, {x_final + dE_fermi}, {y_final} \n')
    BSE.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    BSE.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    
    if (esc_fermi == 0): BSE.write(f'@    xaxis  label "E (eV)" \n')
    if (esc_fermi == 1): BSE.write(f'@    xaxis  label "E-Ef (eV)" \n')
    
    BSE.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    BSE.write(f'@    yaxis  label "Funcao Dieletrica (BSE)" \n')       

    BSE.write(f'@    legend loctype view \n')
    BSE.write(f'@    legend {fig_xmin}, {fig_ymax} \n')
    BSE.write(f'@    legend box fill pattern 4 \n')
    BSE.write(f'@    legend length 1 \n') 

    for j in range(5):
        BSE.write(f'@    s{j} type xy \n')
        BSE.write(f'@    s{j} line type 1 \n')
        BSE.write(f'@    s{j} line color {color[j]} \n')
        BSE.write(f'@    s{j} line linewidth 2.0 \n')
        # BSE.write(f'@    s{j} fill type 1 \n')
        # BSE.write(f'@    s{j} fill color {color[j]} \n')
        # BSE.write(f'@    s{j} fill pattern 4 \n')
        BSE.write(f'@    s{j} legend  "{rot[j]}" \n')

    BSE.write(f'@    s{j+1} type xy \n')
    BSE.write(f'@    s{j+1} line type 1 \n')
    BSE.write(f'@    s{j+1} line linestyle 3 \n')
    BSE.write(f'@    s{j+1} line linewidth 2.0 \n')
    BSE.write(f'@    s{j+1} line color 7 \n')
    
    BSE.write(f'@    s{j+2} type xy \n')
    BSE.write(f'@    s{j+2} line type 1 \n')
    BSE.write(f'@    s{j+2} line linestyle 3 \n')
    BSE.write(f'@    s{j+2} line linewidth 2.0 \n')
    BSE.write(f'@    s{j+2} line color 7 \n')
        
    BSE.write("@type xy")
    BSE.write(" \n")

    # Plot of the components of the Dielectric Function ===============

    for j in range(5):
        #---------------------------------------
        if (i == 0): temp = func_dielet[:,(j+1)]
        if (i == 1): temp = func_dielet[:,(j+6)]
        #---------------------------------------
        for k in range (passo):
            BSE.write(f'{energ[k] + dE_fermi} {temp[k]} \n')
        BSE.write(" \n")

    # Highlighting the Fermi energy in the Band structure =============
   
    BSE.write(f'{dest_fermi} {y_inicial} \n')
    BSE.write(f'{dest_fermi} {y_final} \n')
    BSE.write(" \n")
    
    # Highlighting the null value of the Dielectric Function ==========

    BSE.write(f'{x_inicial + dE_fermi} 0.0 \n')
    BSE.write(f'{x_final + dE_fermi} 0.0 \n')          
    BSE.write(" \n")

    #----------
    BSE.close()
    #----------
