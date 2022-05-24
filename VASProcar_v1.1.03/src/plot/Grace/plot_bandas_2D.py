
#======================================================================
# Obtenção de alguns parâmetros de ajusto do Grafico (GRACE) ==========
#======================================================================    

x_inicial = xx[1][1]
x_final   = xx[n_procar][nk]
y_inicial = energ_min
y_final   = energ_max

#----------------------------------------------------------
bandas = open(dir_files + '/output/Bandas/Bandas.agr', 'w')
#----------------------------------------------------------

bandas.write("# Grace project file \n")
bandas.write("# ============================================================== \n")
bandas.write(f'# written using VASProcar version {version} - Python tools for VASP \n')
bandas.write(f'# {url_1} \n')
bandas.write(f'# {url_2} \n') 
bandas.write("# ============================================================== \n")
bandas.write("@version 50122 \n")
bandas.write("@with g0 \n")
bandas.write(f'@    world {x_inicial}, {y_inicial + dE_fermi}, {x_final}, {y_final + dE_fermi} \n')
bandas.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

escala_x = (x_final - x_inicial)/5
escala_y = (y_final - y_inicial)/5

bandas.write(f'@    xaxis  tick major {escala_x:.2f} \n')

palavra = '"\\f{Symbol}2p/\\f{Times-Italic}a"'

if (Dimensao == 1 and dest_k != 2): bandas.write(f'@    xaxis  label {palavra} \n') 
if (Dimensao == 2 and dest_k != 2): bandas.write(f'@    xaxis  label "1/Angs." \n') 
if (Dimensao == 3 and dest_k != 2): bandas.write(f'@    xaxis  label "1/nm" \n')

if (dest_k == 2):
   bandas.write(f'@    xaxis  tick spec type both \n')
   bandas.write(f'@    xaxis  tick spec {contador2} \n')
   for i in range (contador2):   
       bandas.write(f'@    xaxis  tick major {i}, {dest_pk[i]} \n')
       temp_r = label_pk[i]
       for j in range(34):
           if (temp_r == '#' + str(j+1)): temp_r = r_grace[j]                  
       bandas.write(f'@    xaxis  ticklabel {i}, "{temp_r}" \n')    
 
bandas.write(f'@    yaxis  tick major {escala_y:.2f} \n')

if (esc_fermi == 0):
   bandas.write(f'@    yaxis  label "E (eV)" \n')
if (esc_fermi == 1):
   bandas.write(f'@    yaxis  label "E-Ef (eV)" \n')

bandas.write(f'@    legend loctype world \n')
bandas.write(f'@    legend {x_inicial}, {y_final + dE_fermi} \n')
bandas.write(f'@    legend box fill pattern 4 \n')
bandas.write(f'@    legend length 1 \n')   
   
#======================================================================

for i in range(nb + 1 + contador2):

    if (ispin == 1):
       if (i <= (nb-1)): color = 1 # cor Preta
       if (i == nb):     color = 2 # cor Vermelha

    if (ispin == 2):
       if (i <= ((nb/2)-1)):                 color = 2 # cor Vermelha
       if (i > ((nb/2)-1) and i <= (nb-1)):  color = 4 # cor Azul
       if (i == nb):                         color = 7 # cor Cinza
     
    if (i > nb):      color = 7 # Cor Cinza  
   
    bandas.write(f'@    s{i} type xy \n')
    bandas.write(f'@    s{i} line type 1 \n')
    bandas.write(f'@    s{i} line color {color} \n')
    
    if (ispin == 2 and i == ((nb/2)-1)):  bandas.write(f'@    s{i} legend  "Spin 1" \n') 
    if (ispin == 2 and i == (nb-1)):      bandas.write(f'@    s{i} legend  "Spin 2" \n')
    
bandas.write(f'@type xy \n')    

# Plot das Bandas =====================================================

for Band_n in range (1,(nb+1)):
    bandas.write(" \n")
    for j in range (1,(n_procar+1)):
        for point_k in range (1,(nk+1)):
            bandas.write(f'{xx[j][point_k]} {Energia[j][point_k][Band_n] + dE_fermi} \n')

# Destacando a energia de Fermi na estrutura de Bandas ================
      
bandas.write(" \n")
bandas.write(f'{xx[1][1]} {dest_fermi} \n')
bandas.write(f'{xx[n_procar][nk]} {dest_fermi} \n')

# Destacando pontos-k de interesse na estrutura de Bandas =============

if (dest_k > 0):
   for loop in range (contador2):
       bandas.write(" \n")
       bandas.write(f'{dest_pk[loop]} {energ_min + dE_fermi} \n')
       bandas.write(f'{dest_pk[loop]} {energ_max + dE_fermi} \n')     

#-------------
bandas.close()
#-------------
