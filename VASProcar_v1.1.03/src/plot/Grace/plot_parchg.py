
for l in range(1,(3+1)):

    if (l == 1):      
       print ("Analisando a direcao-X ==================================")
       name = 'Densidade_x'; eixo = 'X '; t_grid = Grid_x; coord = ion_x
       dx = fator_x/20; x_inicial = (0.0 - dx); x_final = (fator_x + dx)
       dy = (max(Vx) - min(Vx))/20; y_inicial = (min(Vx) - dy); y_final = (max(Vx) + dy)      
       
    if (l == 2):
       print ("Analisando a direcao-Y ==================================")      
       name = 'Densidade_y'; eixo = 'Y '; t_grid = Grid_y; coord = ion_y
       dx = fator_y/20; x_inicial = (0.0 - dx); x_final = (fator_y + dx)
       dy = (max(Vy) - min(Vy))/20; y_inicial = (min(Vy) - dy); y_final = (max(Vy) + dy)
       
    if (l == 3):
       print ("Analisando a direcao-Z ==================================")      
       name = 'Densidade_z'; eixo = 'Z '; t_grid = Grid_z; coord = ion_z
       dx = fator_z/20; x_inicial = (0.0 - dx); x_final = (fator_z + dx)
       dy = (max(Vz) - min(Vz))/20; y_inicial = (min(Vz) - dy); y_final = (max(Vz) + dy)

    #-------------------------------------------------------------------------------------
    densidade = open(dir_files + '/output/Densidade_Carga_Parcial/' + name + '.agr', "w")
    #-------------------------------------------------------------------------------------

    densidade.write("# Grace project file \n")
    densidade.write("# ============================================================== \n")
    densidade.write(f'# written using VASProcar version {version} - Python tools for VASP \n')
    densidade.write(f'# {url_1} \n')
    densidade.write(f'# {url_2} \n') 
    densidade.write("# ============================================================== \n")
    densidade.write("@version 50122 \n")
    densidade.write("@with g0 \n")
    densidade.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
    # densidade.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    densidade.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    if (Dimensao == 1):
       label = eixo + '(Angs.)'
       densidade.write(f'@    xaxis  label "{label}" \n') 
    if (Dimensao == 2):
       label = eixo + '(nm)'
       densidade.write(f'@    xaxis  label "{label}" \n') 
 
    densidade.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    densidade.write(f'@    yaxis  label "Densidade de Carga Parcial" \n')

    #======================================================================

    if (destaque == 0): ni = 0
    if (destaque == 1): ni = ni
    
    for i in range(1,((ni+1)+1)):

        if (destaque == 1 and i <= ni): color = 7 # cor Cinza
        if (i > ni): color = 2  # cor Vermelha
   
        densidade.write(f'@    s{i-1} type xy \n')
        densidade.write(f'@    s{i-1} line type 1 \n')
        densidade.write(f'@    s{i-1} line color {color} \n')
        
        if (i <= ni):
           densidade.write(f'@    s{i-1} line linestyle 1 \n')        
           densidade.write(f'@    s{i-1} line linewidth 0.5 \n')
        if (i > ni):
           densidade.write(f'@    s{i-1} line linestyle 1 \n')        
           densidade.write(f'@    s{i-1} line linewidth 2.0 \n')
           
    densidade.write(f'@type xy \n')

    # Destacando as coordenadas dos ions da rede:
            
    if (destaque == 1): 
       for i in range (ni):
           densidade.write(f'{coord[i]} {y_inicial} \n')
           densidade.write(f'{coord[i]} {y_final} \n')     
           densidade.write(" \n")    
    
    # Plot do valor médio da densidade de carga parcial em uma dada direção:
    
    for i in range (t_grid):
       
        if (l == 1):
           X[i] = (float(i)/(float(Grid_x) - 1.0))*fator_x
           densidade.write(f'{X[i]} {Vx[i]} \n')

        if (l == 2):
           Y[i] = (float(i)/(float(Grid_y) - 1.0))*fator_y
           densidade.write(f'{Y[i]} {Vy[i]} \n')

        if (l == 3):
           Z[i] = (float(i)/(float(Grid_z) - 1.0))*fator_z
           densidade.write(f'{Z[i]} {Vz[i]} \n')           

    #----------------
    densidade.close()
    #----------------
    
