
#======================================================================
# Obtenção de alguns parâmetros de ajusto do Grafico (GRACE) ==========
#======================================================================    

x_inicial = xx[1][1]
x_final   = xx[n_procar][nk]
y_inicial = energ_min
y_final   = energ_max

#======================================================================

for t in range (1,(3+1)):            # Loop para a analise das Projecoes
        
#-----------------------------------------------------------------------

    if (t == 1):
       #-------------------------------------------------------------
       projection = open(dir_files + '/output/Spin/Spin_Sx.agr', 'w')
       #-------------------------------------------------------------
       print ("Analisando a Projecao Sx do Spin")
       letras = 'Sx'
    if (t == 2):
       #-------------------------------------------------------------
       projection = open(dir_files + '/output/Spin/Spin_Sy.agr', 'w')
       #-------------------------------------------------------------
       print ("Analisando a Projecao Sy do Spin")
       letras = 'Sy'
    if (t == 3):
       #-------------------------------------------------------------
       projection = open(dir_files + '/output/Spin/Spin_Sz.agr', 'w')
       #-------------------------------------------------------------
       print ("Analisando a Projecao Sz do Spin")
       letras = 'Sz'

# Escrita do arquivo ".agr" do GRACE ===================================

    projection.write("# Grace project file \n")
    projection.write("# ============================================================== \n")
    projection.write(f'# written using VASProcar version {version} - Python tools for VASP \n')
    projection.write(f'# {url_1} \n')
    projection.write(f'# {url_2} \n') 
    projection.write("# ============================================================== \n")
    projection.write("@version 50122 \n")   
    projection.write("@with g0 \n")
    projection.write(f'@    world {x_inicial}, {y_inicial + dE_fermi}, {x_final}, {y_final + dE_fermi} \n')
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
           projection.write(f'@    xaxis  ticklabel {i}, "{temp_r}" \n')
    
    projection.write(f'@    yaxis  tick major {escala_y:.2f} \n')

    if (esc_fermi == 0):
       projection.write(f'@    yaxis  label "E (eV)" \n')
    if (esc_fermi == 1):
       projection.write(f'@    yaxis  label "E-Ef (eV)" \n')
    
    projection.write(f'@    legend loctype world \n')
    projection.write(f'@    legend {x_inicial}, {y_final + dE_fermi} \n')
    projection.write(f'@    legend box fill pattern 4 \n')
    projection.write(f'@    legend length 1 \n')  

    for i in range (1,(3+1)):

        if (i == 1):
           grac='s0'; color = cor_spin[2]; legenda = letras + ' \\f{Symbol}\\c-\\C'   # Cor (Vermelho) da componente Up dos Spins Sx, Sy e Sz.
        if (i == 2):
           grac='s1'; color = cor_spin[3]; legenda = letras + ' \\f{Symbol}\\c/\\C'   # Cor (Azul) da componente Down dos Spins Sx, Sy e Sz.
        if (i == 3):
           grac='s2'; color = cor_spin[1]; legenda = ''                                    # Cor (Preto) da componente Nula dos Spins Sx, Sy e Sz.

        projection.write(f'@    {grac} type xysize \n')
        projection.write(f'@    {grac} symbol 1 \n')
        projection.write(f'@    {grac} symbol color {color} \n')
        projection.write(f'@    {grac} symbol fill color {color} \n')
        projection.write(f'@    {grac} symbol fill pattern 1 \n')
        projection.write(f'@    {grac} line type 0 \n')
        projection.write(f'@    {grac} line color {color} \n')
        if (i <= 3): projection.write(f'@    {grac} legend  "{legenda}" \n')

    for j in range(nb+1+contador2):

        if (j <= (nb-1)): color = 1 # cor Preta
        if (j == nb):     color = 2 # cor Vermelha
        if (j > nb):      color = 7 # Cor Cinza        
   
        projection.write(f'@    s{j+3} type xysize \n')
        projection.write(f'@    s{j+3} line type 1 \n')
        projection.write(f'@    s{j+3} line color {color} \n')         
           
    projection.write("@type xysize")
    projection.write(" \n")
                          
# Plot das Componentes de Spin (Sx,Sy,Sz) =============================

    for i in range (1,(3+1)):                                          # Busca em loop pelas componente up, down e nula (Sx,Sy,Sz)
      
#-----------------------------------------------------------------------

        for wp in range (1, (n_procar+1)):
            for point_k in range (1, (nk+1)):
                for Band_n in range (1, (nb+1)):
                    #----------------------------------
                    if (t == 1):
                       si = tot_sx[wp][point_k][Band_n]
                    if (t == 2):
                       si = tot_sy[wp][point_k][Band_n]
                    if (t == 3):
                       si = tot_sz[wp][point_k][Band_n]
                    #-------------------------------------------------------------------------------
                    if (wp == 1 and point_k == 1 and Band_n == 1):    
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n] + dE_fermi} 0.0 \n')                       
                    if (i == 1 and si > 0.0):
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n] + dE_fermi} {si} \n')
                    if (i == 2 and si < 0.0):
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n] + dE_fermi} {si} \n')
                    if (i == 3 and si == 0.0):
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n] + dE_fermi} {si} \n')
        #-------------------------------------------------------------------------------------------
        projection.write(" \n")  

# Plot da estrutura de Bandas =========================================
    
    for Band_n in range (1,(nb+1)):
        projection.write(" \n")
        for i in range (1,(n_procar+1)):
            for point_k in range (1,(nk+1)):
                projection.write(f'{xx[i][point_k]} {Energia[i][point_k][Band_n] + dE_fermi} 0.0 \n')
                
# Destacando a energia de Fermi no plot das Texturas ==================

    projection.write(" \n")
    projection.write(f'{xx[1][1]} {dest_fermi} 0.0 \n')
    projection.write(f'{xx[n_procar][nk]} {dest_fermi} 0.0 \n')

# Destacando pontos-k de interesse no plot das Texturas ===============

    if (dest_k > 0):
       for loop in range (contador2):
           projection.write(" \n")
           projection.write(f'{dest_pk[loop]} {energ_min + dE_fermi} 0.0 \n')
           projection.write(f'{dest_pk[loop]} {energ_max + dE_fermi} 0.0 \n')

    #-----------------
    projection.close()
    #-----------------
