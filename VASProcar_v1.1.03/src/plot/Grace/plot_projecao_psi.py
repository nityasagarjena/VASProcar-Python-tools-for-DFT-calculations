
#======================================================================
# Obtenção de alguns parâmetros de ajusto do Grafico (GRACE) ==========
#======================================================================    

x_inicial = xx[1][1]
x_final   = xx[n_procar][nk]
y_inicial = energ_min
y_final   = energ_max

#======================================================================

#----------------------------------------------------------------
projection = open(dir_files + '/output/Psi/Estados_Psi.agr', 'w')    
#----------------------------------------------------------------      

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

for j in range (1,(n_psi+1)):

    legend = l_psi[j]; color = cor_orb[j+6]  #  Cor do estado Psi
    grac = 's' + str(j-1)
          
    projection.write(f'@    {grac} type xysize \n')
    projection.write(f'@    {grac} symbol 1 \n')
    projection.write(f'@    {grac} symbol color {color} \n')
    projection.write(f'@    {grac} symbol fill color {color} \n')
    projection.write(f'@    {grac} symbol fill pattern 1 \n')
    projection.write(f'@    {grac} line type 0 \n')
    projection.write(f'@    {grac} line color {color} \n')   
    projection.write(f'@    {grac} legend  "{legend}" \n')
                     
number = 0

for j in range(nb+1+contador2):

    number += 1

    if (j <= (nb-1)): color = 1 # cor Preta
    if (j == nb):     color = 2 # cor Vermelha
    if (j > nb):      color = 7 # Cor Cinza
   
    projection.write(f'@    s{j + n_psi} type xysize \n')
    projection.write(f'@    s{j + n_psi} line type 1 \n')
    projection.write(f'@    s{j + n_psi} line color {color} \n') 

projection.write("@type xysize")
projection.write(" \n")
      
# Plot dos estados Psi ================================================

for j in range (1,(n_psi+1)):      
    for wp in range (1,(n_procar+1)):
        for point_k in range (1,(nk+1)):
            for Band_n in range (1,(nb+1)):
                #----------------------------------------------------------------     
                estado = psi[j][wp][point_k][Band_n]
                est_psi[j][wp][point_k][Band_n] = estado
                estado_psi[j][wp][point_k][Band_n] = ((dpi*estado)**2)*peso_total         
                #----------------------------------------------------------------          
                if (wp == 1 and point_k == 1 and Band_n == 1):    
                   projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n] + dE_fermi} 0.0 \n')
                if (estado > 0.0):    
                   projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n] + dE_fermi} {estado} \n')

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
