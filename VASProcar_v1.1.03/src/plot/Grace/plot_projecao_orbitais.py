
#======================================================================
# Obtenção de alguns parâmetros de ajusto do Grafico (GRACE) ==========
#======================================================================    

x_inicial = xx[1][1]
x_final   = xx[n_procar][nk]
y_inicial = energ_min
y_final   = energ_max
                          
if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

# Rotulo dos Orbitais ================================================= 

t_orb = [0]*(12)
t_orb[1] = 'S'; t_orb[2] = 'P'; t_orb[3] = 'D'; t_orb[4] = 'Px'; t_orb[5] = 'Py'; t_orb[6] = 'Pz'
t_orb[7] = 'Dxy'; t_orb[8] = 'Dyz'; t_orb[9] = 'Dz2'; t_orb[10] = 'Dxz'; t_orb[11] = 'Dx2'

#======================================================================

print (" ")          
print ("============================================")

for i in range (1,(loop+1)):     # Loop para a analise das Projecoes
        
#-----------------------------------------------------------------------

    if (i == 1):
       #----------------------------------------------------------------------
       projection = open(dir_files + '/output/Orbitais/Orbitais_SPD.agr', 'w')
       #----------------------------------------------------------------------
       print ("Analisando a Projecao dos Orbitais (S, P, D)")        
       s = 1; t = (3+1)
       
    if (i == 2):
       #--------------------------------------------------------------------
       projection = open(dir_files + '/output/Orbitais/Orbitais_P.agr', 'w')     
       #--------------------------------------------------------------------
       print ("Analisando a Projecao dos Orbitais (Px, Py, Pz)") 
       s = 4; t = (6+1)
       
    if (i == 3):
       #--------------------------------------------------------------------
       projection = open(dir_files + '/output/Orbitais/Orbitais_D.agr', 'w')
       #--------------------------------------------------------------------
       print ("Analisando a Projecao dos Orbitais (Dxy, Dyz, Dz2, Dxz, Dx2)") 
       s = 7; t = (11+1)   

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
       
    for j in range (s,t):
          
        if (j == (s+0)): grac='s0'; color = cor_orb[j]        # Cor dos Orbitais (S,Px,Dxy)
        if (j == (s+1)): grac='s1'; color = cor_orb[j]        # Cor dos Orbitais (P,Py,Dyz)
        if (j == (s+2)): grac='s2'; color = cor_orb[j]        # Cor dos Orbitais (D,Pz,Dz2)
        if (j == (s+3)): grac='s3'; color = cor_orb[j]        # Cor do Orbital Dxz
        if (j == (s+4)): grac='s4'; color = cor_orb[j]        # Cor do Orbital Dx2
           
        projection.write(f'@    {grac} type xysize \n')
        projection.write(f'@    {grac} symbol 1 \n')
        projection.write(f'@    {grac} symbol color {color} \n')
        projection.write(f'@    {grac} symbol fill color {color} \n')
        projection.write(f'@    {grac} symbol fill pattern 1 \n')
        projection.write(f'@    {grac} line type 0 \n')
        projection.write(f'@    {grac} line color {color} \n')
        projection.write(f'@    {grac} legend  "{t_orb[j]}" \n')

    for j in range(nb+1+contador2):

        if (j <= (nb-1)): color = 1 # cor Preta
        if (j == nb):     color = 2 # cor Vermelha
        if (j > nb):      color = 7 # Cor Cinza
   
        projection.write(f'@    s{j+(t-s)} type xysize \n')
        projection.write(f'@    s{j+(t-s)} line type 1 \n')
        projection.write(f'@    s{j+(t-s)} line color {color} \n') 

    projection.write("@type xysize")
    projection.write(" \n")
      
# Plot dos Orbitais ===================================================

    for j in range (s,t):      
        for wp in range (1, (n_procar+1)):
            for point_k in range (1, (nk+1)):
                for Band_n in range (1, (nb+1)):
                    
                    #------------------------------------------------------
                    if (j == 1): # Orbital S
                       orbital = soma_orb[wp][1][point_k][Band_n]
                       orb_S[wp][point_k][Band_n] = orbital
                       orbital_S[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    #-------------------- lorbit = 10 ---------------------
                    if (j == 2 and lorbit == 10): # Orbital P
                       orbital = soma_orb[wp][2][point_k][Band_n]
                       orb_P[wp][point_k][Band_n] = orbital
                       orbital_P[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 3 and lorbit == 10): # Orbital D
                       orbital = soma_orb[wp][3][point_k][Band_n]
                       orb_D[wp][point_k][Band_n] = orbital
                       orbital_D[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    #-------------------- lorbit >= 11 --------------------                     
                    if (j == 2 and lorbit >= 11): # Orbital P = Px + Py + Pz
                       orbital = soma_orb[wp][2][point_k][Band_n] + soma_orb[wp][3][point_k][Band_n] + soma_orb[wp][4][point_k][Band_n]
                       orb_P[wp][point_k][Band_n] = orbital
                       orbital_P[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 3 and lorbit >= 11): # Orbital D = Dxy + Dyz + Dz2 + Dxz + Dx2
                       orbital = soma_orb[wp][5][point_k][Band_n] + soma_orb[wp][6][point_k][Band_n] + soma_orb[wp][7][point_k][Band_n] + soma_orb[wp][8][point_k][Band_n] + soma_orb[wp][9][point_k][Band_n]
                       orb_D[wp][point_k][Band_n] = orbital
                       orbital_D[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    #------------------------------------------------------
                    if (j == 4): # Orbital Px 
                       orbital = soma_orb[wp][4][point_k][Band_n]
                       orb_Px[wp][point_k][Band_n] = orbital
                       orbital_Px[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 5): # Orbital Py 
                       orbital = soma_orb[wp][2][point_k][Band_n]
                       orb_Py[wp][point_k][Band_n] = orbital
                       orbital_Py[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 6): # Orbital pz 
                       orbital = soma_orb[wp][3][point_k][Band_n]
                       orb_Pz[wp][point_k][Band_n] = orbital
                       orbital_Pz[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    #------------------------------------------------------
                    if (j == 7): # Orbital Dxy 
                       orbital = soma_orb[wp][5][point_k][Band_n]
                       orb_Dxy[wp][point_k][Band_n] = orbital
                       orbital_Dxy[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 8): # Orbital Dyz 
                       orbital = soma_orb[wp][6][point_k][Band_n]
                       orb_Dyz[wp][point_k][Band_n] = orbital
                       orbital_Dyz[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 9): # Orbital Dz2 
                       orbital = soma_orb[wp][7][point_k][Band_n]
                       orb_Dz2[wp][point_k][Band_n] = orbital
                       orbital_Dz2[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 10): # Orbital Dxz 
                       orbital = soma_orb[wp][8][point_k][Band_n]
                       orb_Dxz[wp][point_k][Band_n] = orbital
                       orbital_Dxz[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 11): # Orbital Dx2 
                       orbital = soma_orb[wp][9][point_k][Band_n]
                       orb_Dx2[wp][point_k][Band_n] = orbital
                       orbital_Dx2[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    #------------------------------------------------------                       
                    if (wp == 1 and point_k == 1 and Band_n == 1):    
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n] + dE_fermi} 0.0 \n')
                    if (orbital > 0.0):    
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n] + dE_fermi} {orbital} \n')

        projection.write(" \n")
       
# Plot da estrutura de Bandas =========================================
    
    for Band_n in range (1,(nb+1)):
        projection.write(" \n")
        for i in range (1,(n_procar+1)):
            for point_k in range (1,(nk+1)):
                projection.write(f'{xx[i][point_k]} {Energia[i][point_k][Band_n] + dE_fermi} 0.0 \n')

# Destacando a energia de Fermi na estrutura de Bandas ================

    projection.write(" \n")
    projection.write(f'{xx[1][1]} {dest_fermi} 0.0 \n')
    projection.write(f'{xx[n_procar][nk]} {dest_fermi} 0.0 \n')

# Destacando pontos-k de interesse na estrutura de Bandas =============

    if (dest_k > 0):
       for loop in range (contador2):
           projection.write(" \n")
           projection.write(f'{dest_pk[loop]} {energ_min + dE_fermi} 0.0 \n')
           projection.write(f'{dest_pk[loop]} {energ_max + dE_fermi} 0.0 \n')

    #-----------------
    projection.close()
    #-----------------
    
