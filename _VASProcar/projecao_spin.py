#########################################################################################
## VASProcar -- https://github.com/Augusto-Dlelis/VASProcar-Tools-Python ################
## Autores: #############################################################################
## =================================================================================== ##
## Augusto de Lelis Araujo - Federal University of Uberlandia (Uberlândia/MG - Brazil) ##
## e-mail: augusto-lelis@outlook.com                                                   ##
## =================================================================================== ##
## Renan da Paixão Maciel - Uppsala University (Uppsala/Sweden) #########################
## e-mail: renan.maciel@physics.uu.se                           #########################
#########################################################################################

#---------------------------------------------
exec(open("_VASProcar/informacoes.py").read())
#---------------------------------------------

#======================================================================
# Obtenção dos parâmetros de input por interação com usuário ==========
#======================================================================

print ("##############################################################")
print ("######## Projecao das Componentes de Spin (Sx,Sy,Sz): ########")
print ("##############################################################") 
print (" ")

if (escolha == -3):
   
   print ("##############################################################")
   print ("Escolha a dimensao do eixo-k: ================================")
   print ("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. =")
   print ("Utilize 2 para k em unidades de 1/Angs. ======================")
   print ("Utilize 3 para k em unidades de 1/nm. ========================")
   print ("##############################################################")
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print(" ")

   print ("##############################################################")
   print ("Digite o peso/tamanho das esferas na projecao: ===============")
   print ("Digite um valor entre 0.0 e 1.0 ==============================")
   print ("##############################################################")
   peso_total = input (" "); peso_total = float(peso_total)
   print(" ")

   print ("##############################################################")
   print ("O que vc deseja Plotar/Analisar? =============================")
   print ("Digite 0 para analisar todos os ions da rede =================")
   print ("Digite 1 para analisar ions selecionados =====================")
   print ("##############################################################")
   esc = input (" "); esc = int(esc)

   if (esc == 1):

      sim_nao = ["nao"]*(ni + 1)             # Inicialização do vetor sim_nao
      
      print (" ")
      print ("##############################################################")
      print ("Especifique os ions selecionados em intervalos ===============")
      print ("Quantos intervalos de ions ira fornecer abaixo? ==============")
      print ("##############################################################")
      loop = input (" "); loop = int(loop)
      for i in range (1,(loop+1)):
          print (" ")
          print (f'{i} intervalo: ==============================================')
          print ("Digite o ion inicial do intervalo ============================")
          loop_i = input (" "); loop_i = int(loop_i)
          print ("Digite o ion final do intervalo ==============================")
          loop_f = input (" "); loop_f = int(loop_f)
          if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
             print ("")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("   ERRO: Os valores de ions informados estao incorretos   ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("")
          for i in range(loop_i, (loop_f + 1)):
              sim_nao[i] = "sim"                              # Escolha se serão Plotados/Analisados todos os ions ou não, nas projeções.

   print(" ")

if (escolha == 3):   
   Dimensao = 1
   peso_total = 1.0
   esc = 0
   
#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------

#---------------------------------------------
exec(open("_VASProcar/procar.py").read())
#---------------------------------------------   

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------

soma_sx = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(3+1)] for k in range(n_procar+1)]  # soma_sx[n_procar][3][nk][nb]
soma_sy = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(3+1)] for k in range(n_procar+1)]  # soma_sy[n_procar][3][nk][nb]
soma_sz = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(3+1)] for k in range(n_procar+1)]  # soma_sz[n_procar][3][nk][nb]    

tot_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sx[n_procar][nk][nb]
tot_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sy[n_procar][nk][nb]
tot_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sz[n_procar][nk][nb]

total_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sx[n_procar][nk][nb]
total_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sy[n_procar][nk][nb]
total_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sz[n_procar][nk][nb]

#  soma_sx[n_procar][1][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital S de Sx
#  soma_sx[n_procar][2][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Py ou P (lorbit = 10) de Sx
#  soma_sx[n_procar][3][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Pz ou D (lorbit = 10) de Sx
#  soma_sx[n_procar][4][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Px de Sx
#  soma_sx[n_procar][5][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dxy de Sx
#  soma_sx[n_procar][6][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dyz de Sx
#  soma_sx[n_procar][7][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dz2 de Sx
#  soma_sx[n_procar][8][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dxz de Sx
#  soma_sx[n_procar][9][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dx2 de Sx
#  tot_sx   = Soma de todos os orbitais (para ions selecionados) de Sx
#  total_sx = Soma de todos os orbitais (para todos os ions) de Sx

#----------------------------------------------------------------------

for wp in range(1, (n_procar+1)):
    for point_k in range(1, (nk+1)):                                  
        for Band_n in range (1, (nb+1)):
            for ion_n in range (1, (ni+1)):              
                #------------------------------------------------------ 
                if (esc == 1):
                   temp_sn = sim_nao[ion_n]
                #------------------------------------------------------ 
                for orb_n in range(1,(n_orb+1)):
                    if (esc == 0 or (esc == 1 and temp_sn == "sim")):
                       tot_sx[wp][point_k][Band_n] = ( tot_sx[wp][point_k][Band_n] + Sx[wp][orb_n][point_k][Band_n][ion_n] )
                       tot_sy[wp][point_k][Band_n] = ( tot_sy[wp][point_k][Band_n] + Sy[wp][orb_n][point_k][Band_n][ion_n] )
                       tot_sz[wp][point_k][Band_n] = ( tot_sz[wp][point_k][Band_n] + Sz[wp][orb_n][point_k][Band_n][ion_n] )
            #----------------------------------------------------------           
            # Fim do Loop dos ions ------------------------------------
            #----------------------------------------------------------                 
        #----------------------------------------------------------
        # Fim do Loop das Bandas ----------------------------------
        #----------------------------------------------------------      
    #----------------------------------------------------------
    # Fim do Loop dos pontos-k --------------------------------
    #----------------------------------------------------------    
#----------------------------------------------------------
# Fim do Loop dos arquivos PROCAR -------------------------
#----------------------------------------------------------
 
#======================================================================
# Obtenção de alguns parâmetros de ajusto do Grafico (GRACE) ==========
#======================================================================    

x_inicial = xx[1][1]
x_final   = xx[n_procar][nk]
y_inicial = energ_min
y_final   = energ_max

#======================================================================
# Obtendo pontos-k de interesse na estrutura de Bandas ================
#======================================================================

#------------------------------------------
inform = open("saida/informacoes.txt", "r")
#------------------------------------------

palavra = 'Pontos-k |'                          

for line in inform:   
    if palavra in line: 
       break

VTemp = inform.readline()
VTemp = inform.readline()
       
nk_total = nk*n_procar

contador2 = 0
dest_pk = [0]*(100)                    # Inicialização do vetor dest_pk de dimensão 100.

for i in range (1, (nk_total+1)):
    VTemp = inform.readline().split()
    r1 = int(VTemp[0]); r2 = float(VTemp[1]); r3 = float(VTemp[2]); r4 = float(VTemp[3]); comprimento = float(VTemp[4])
    if (i != 1) and (i != (nk_total+1)):  
       dif = comprimento - comprimento_old     
       if(dif == 0.0):
          contador2 += 1
          dest_pk[contador2] = comprimento
          
    comprimento_old = comprimento

#-------------
inform.close()
#-------------

#======================================================================
# Plot das Projeções das Componentes de Spin (Sx,Sy,Sz) (GRACE) =======
#======================================================================            

print (" ")          
print ("==================================")
print (" ")

for t in range (1,(3+1)):            # Loop para a analise das Projecoes
        
#-----------------------------------------------------------------------

    if (t == 1):
       #--------------------------------------------------
       projection = open("saida/Spin_Sx.agr", "w")
       #--------------------------------------------------
       print ("Analisando a Projecao Sx do Spin")
    if (t == 2):
       #--------------------------------------------------
       projection = open("saida/Spin_Sy.agr", "w")
       #--------------------------------------------------
       print (" ")
       print ("Analisando a Projecao Sy do Spin")          
    if (t == 3):
       #--------------------------------------------------
       projection = open("saida/Spin_Sz.agr", "w")
       #--------------------------------------------------
       print (" ")
       print ("Analisando a Projecao Sz do Spin")

#-----------------------------------------------------------------------
# Escrita do arquivo ".agr" do GRACE -----------------------------------
#-----------------------------------------------------------------------

    projection.write("# Grace project file \n")
    projection.write("# \n")
    projection.write("@version 50122 \n")   
    projection.write("@with string \n")                 
    projection.write("@    string on \n")
    projection.write(f'@    string {fig_xmin}, {fig_ymax + 0.01} \n')
    projection.write(f'@    string def "E(eV)" \n')
    projection.write("@with string \n")
    projection.write("@    string on \n")

    if (Dimensao == 1):
       projection.write(f'@    string {fig_xmax - 0.14}, {fig_ymin - 0.058} \n')
       projection.write(f'@    string def "(2pi/Param.)" \n')
    if (Dimensao == 2):
       projection.write(f'@    string {fig_xmax - 0.10}, {fig_ymin - 0.058} \n')
       projection.write(f'@    string def "(1/Angs.)" \n')
    if (Dimensao == 3):
       projection.write(f'@    string {fig_xmax - 0.07}, {fig_ymin - 0.058} \n')
       projection.write(f'@    string def "(1/nm)" \n')

    projection.write("@with g0 \n")
    projection.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
    projection.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    projection.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    projection.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    projection.write(f'@    legend {fig_xmax + 0.025}, {fig_ymax} \n')   

    for i in range (1,(3+1)):

        if (i == 1):
           grac='s0'; color = cor[2]; legenda = 'Up'          # Cor (Vermelho) da componente Up dos Spins Sx, Sy e Sz.
        if (i == 2):
           grac='s1'; color = cor[3]; legenda = 'Down'         # Cor (Azul) da componente Down dos Spins Sx, Sy e Sz.
        if (i == 3):
           grac='s2'; color = cor[1]; legenda = 'Nulo'       # Cor (Preto) da componente Nula dos Spins Sx, Sy e Sz.

        projection.write(f'@    {grac} type xysize \n')
        projection.write(f'@    {grac} symbol 1 \n')
        projection.write(f'@    {grac} symbol color {color} \n')
        projection.write(f'@    {grac} symbol fill color {color} \n')
        projection.write(f'@    {grac} symbol fill pattern 1 \n')
        projection.write(f'@    {grac} line type 0 \n')
        projection.write(f'@    {grac} line color {color} \n')
        projection.write(f'@    {grac} legend  "{legenda}" \n')
           
    projection.write("@type xysize")
    projection.write(" \n")
                          
#======================================================================
# Plot das Componentes de Spin (Sx,Sy,Sz) =============================
#======================================================================

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
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} 0.0 \n')                       
                    if (i == 1 and si > 0.0):
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} {si} \n')
                    if (i == 2 and si < 0.0):
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} {si} \n')
                    if (i == 3 and si == 0.0):
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} {si} \n')
        #-------------------------------------------------------------------------------------------
        projection.write(" \n")  

#======================================================================
# Plot da estrutura de Bandas =========================================
#==================================================================
    
    # Plot da Estrutura de Bandas. 
    for Band_n in range (1,(nb+1)):
        projection.write(" \n")
        for i in range (1,(n_procar+1)):
            for point_k in range (1,(nk+1)):
                projection.write(f'{xx[i][point_k]} {Energia[i][point_k][Band_n]} 0.0 \n')
                
#======================================================================
# Destacando a energia de Fermi na estrutura de Bandas ================
#======================================================================

    # Destacando a Energia de Fermi, no plot das Texturas.
    projection.write(" \n")
    projection.write(f'{xx[1][1]} 0.0 0.0 \n')
    projection.write(f'{xx[n_procar][nk]} 0.0 0.0 \n')

#======================================================================
# Destacando pontos-k de interesse na estrutura de Bandas =============
#======================================================================

    # Destacando pontos-k de interesse na Estrutura de Bandas.
    for loop in range (1,(contador2+1)):
        projection.write(" \n")
        projection.write(f'{dest_pk[loop]} {energ_min} 0.0 \n')
        projection.write(f'{dest_pk[loop]} {energ_max} 0.0 \n')

    #-----------------
    projection.close()
    #-----------------

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################