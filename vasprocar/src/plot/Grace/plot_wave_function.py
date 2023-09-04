# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

for l in range(1,(3+1)):  

    if (l == 1):      
       name = 'Wave_Function_X'; eixo = 'X '; t_grid = Grid_x; coord = ion_x
       dx = fator_x/20; x_inicial = (0.0 - dx); x_final = (fator_x + dx)
       dy = (max(Vx) - min(Vx))/20; y_inicial = (min(Vx) - dy); y_final = (max(Vx) + dy)      
       
    if (l == 2):   
       name = 'Wave_Function_Y'; eixo = 'Y '; t_grid = Grid_y; coord = ion_y
       dx = fator_y/20; x_inicial = (0.0 - dx); x_final = (fator_y + dx)
       dy = (max(Vy) - min(Vy))/20; y_inicial = (min(Vy) - dy); y_final = (max(Vy) + dy)
       
    if (l == 3):      
       name = 'Wave_Function_Z'; eixo = 'Z '; t_grid = Grid_z; coord = ion_z
       dx = fator_z/20; x_inicial = (0.0 - dx); x_final = (fator_z + dx)
       dy = (max(Vz) - min(Vz))/20; y_inicial = (min(Vz) - dy); y_final = (max(Vz) + dy)

    #------------------------------------------------------------------------------
    wave_function = open(dir_files + '/output/Wave_Function/' + name + '.agr', "w")
    #------------------------------------------------------------------------------

    wave_function.write("# Grace project file \n")
    wave_function.write("# ========================================================================== \n")
    wave_function.write(f'# written using {VASProcar_name} \n')
    wave_function.write(f'# {url_1} \n')
    wave_function.write(f'# {url_2} \n') 
    wave_function.write("# ========================================================================== \n")
    wave_function.write("@version 50122 \n")
    wave_function.write("@with g0 \n")
    wave_function.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
    # wave_function.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    wave_function.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    if (Dimensao == 1):
       label = eixo + '(Angs.)'
       wave_function.write(f'@    xaxis  label "{label}" \n') 
    if (Dimensao == 2):
       label = eixo + '(nm)'
       wave_function.write(f'@    xaxis  label "{label}" \n') 
 
    wave_function.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    wave_function.write(f'@    yaxis  label "Wave Function" \n')

    #======================================================================

    if (destaque == 0): ni = 0
    if (destaque == 1): ni = ni
    
    for i in range(1,((ni+1)+1)):

        if (destaque == 1 and i <= ni): color = 7  # Gray color
        if (i > ni): color = 2                     # Red color
   
        wave_function.write(f'@    s{i-1} type xy \n')
        wave_function.write(f'@    s{i-1} line type 1 \n')
        wave_function.write(f'@    s{i-1} line color {color} \n')
        
        if (i <= ni):
           wave_function.write(f'@    s{i-1} line linestyle 1 \n')        
           wave_function.write(f'@    s{i-1} line linewidth 0.5 \n')
        if (i > ni):
           wave_function.write(f'@    s{i-1} line linestyle 1 \n')        
           wave_function.write(f'@    s{i-1} line linewidth 2.0 \n')
           
    wave_function.write(f'@type xy \n')

    # Highlighting the coordinates of the lattice ions:
            
    if (destaque == 1): 
       for i in range (ni):
           wave_function.write(f'{coord[i]} {y_inicial} \n')
           wave_function.write(f'{coord[i]} {y_final} \n')     
           wave_function.write(" \n")    
    
    # Plot of average partial load Wave_Function value in a given direction:
    
    for i in range (t_grid):      
        if (l == 1): wave_function.write(f'{X[i]} {Vx[i]} \n')
        if (l == 2): wave_function.write(f'{Y[i]} {Vy[i]} \n')
        if (l == 3): wave_function.write(f'{Z[i]} {Vz[i]} \n')          

    #--------------------
    wave_function.close()
    #--------------------  
