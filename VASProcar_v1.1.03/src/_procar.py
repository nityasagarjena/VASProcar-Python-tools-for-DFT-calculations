
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

execute_python_file(filename = '_informacoes.py')

#--------------------------------------------------------
inform = open(dir_files + '/output/informacoes.txt', "a")
#--------------------------------------------------------

#*****************************************************************
# Dimensao = 1 >> k em unidades de 2pi/Param com Param em Angs. **
# Dimensao = 2 >> k em unidades de 1/Angs. ***********************
# Dimensao = 3 >> K em unidades de 1/nm **************************
#*****************************************************************

if (Dimensao == 1 or Dimensao == 4):
   fator_zb = 1.0

if (Dimensao == 2):
   fator_zb = (2*3.1415926535897932384626433832795)/Parametro

if (Dimensao == 3):
   fator_zb = (10*2*3.1415926535897932384626433832795)/Parametro

B1x = B1x*fator_zb
B1y = B1y*fator_zb
B1z = B1z*fator_zb
B2x = B2x*fator_zb
B2y = B2y*fator_zb
B2z = B2z*fator_zb
B3x = B3x*fator_zb
B3y = B3y*fator_zb
B3z = B3z*fator_zb

#----------------------------------------------------------------------

inform.write("***************************************************** \n")
inform.write("*********** Pontos-k na Zona de Brillouin *********** \n")
inform.write("***************************************************** \n")
inform.write(" \n")
      
if (Dimensao == 1 or Dimensao == 4):
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |   Separacao (2Pi/Param) \n")
if (Dimensao == 2):
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |   Separacao (1/Angs.) \n")
if (Dimensao == 3):
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |   Separacao (1/nm) \n")

inform.write("         |          K =  k1*B1 + k2*B2 + k3*B3          | \n")
inform.write(" \n")

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------

n_point_k = 0        # Variavel com alguma função de controle
energ_max = -1000.0  # Valor inicial para determinar o maior valor de Energia
energ_min = +1000.0  # Valor inicial para determinar o menor valor de Energia
                                              
xx  = [[0]*(nk+1) for i in range(n_procar+1)]  # xx[n_procar][nk] 
kx  = [[0]*(nk+1) for i in range(n_procar+1)]  # kx[n_procar][nk]
ky  = [[0]*(nk+1) for i in range(n_procar+1)]  # ky[n_procar][nk]
kz  = [[0]*(nk+1) for i in range(n_procar+1)]  # kz[n_procar][nk]
kb1 = [[0]*(nk+1) for i in range(n_procar+1)]  # kb1[n_procar][nk]
kb2 = [[0]*(nk+1) for i in range(n_procar+1)]  # kb2[n_procar][nk]
kb3 = [[0]*(nk+1) for i in range(n_procar+1)]  # kb3[n_procar][nk]

separacao = [[0]*(nk+1) for i in range(n_procar+1)]  # separacao[n_procar][nk]
Energia = [[[0]*((nb)+1) for i in range(nk+1)] for j in range(n_procar+1)]  # Energia[n_procar][nk][nb]

#======================================================================================================

if (lorbit >= 11): 
   n_orb = 9  # Número de elementos a serem lidos na linha dos Orbitais ou Componentes de Spin para lorbit = 11 ou 12
if (lorbit == 10): 
   n_orb = 3  # Número de elementos a serem lidos na linha dos Orbitais ou Componentes de Spin para lorbit = 10

if (read_orb == 1):
   
   if (lorbit >= 11): 
      orb = [[[[[0]*(ni+1) for i in range((nb)+1)] for j in range(nk+1)] for k in range(9+1)] for l in range(n_procar+1)]  
   if (lorbit == 10): 
      orb = [[[[[0]*(ni+1) for i in range((nb)+1)] for j in range(nk+1)] for k in range(3+1)] for l in range(n_procar+1)]  

   #  orb[n_procar][1][nk][nb][ni] = Contribuição de cada ion "ni" para o orbital S em uma dada banda e ponto-k.
   #  orb[n_procar][2][nk][nb][ni] = Contribuição de cada ion "ni" para o orbital Py ou P (lorbit = 10) em uma dada banda e ponto-k.
   #  orb[n_procar][3][nk][nb][ni] = Contribuição de cada ion "ni" para o orbital Pz ou D (lorbit = 10) em uma dada banda e ponto-k.
   #  orb[n_procar][4][nk][nb][ni] = Contribuição de cada ion "ni" para o orbital Px em uma dada banda e ponto-k.
   #  orb[n_procar][5][nk][nb][ni] = Contribuição de cada ion "ni" para o orbital Dxy em uma dada banda e ponto-k.
   #  orb[n_procar][6][nk][nb][ni] = Contribuição de cada ion "ni" para o orbital Dyz em uma dada banda e ponto-k.
   #  orb[n_procar][7][nk][nb][ni] = Contribuição de cada ion "ni" para o orbital Dz2 em uma dada banda e ponto-k.
   #  orb[n_procar][8][nk][nb][ni] = Contribuição de cada ion "ni" para o orbital Dxz em uma dada banda e ponto-k.
   #  orb[n_procar][9][nk][nb][ni] = Contribuição de cada ion "ni" para o orbital Dx2 em uma dada banda e ponto-k.

   tot = [[[[0]*(ni+1) for i in range((nb)+1)] for i in range(nk+1)] for j in range(n_procar+1)]
   # tot[n_procar][nk][nb][ni] = Soma de todos os orbitais (S,P,D) para um dado ion. 

#===================================================================================================================================

if (read_spin == 1):

   if (SO == 2):
      if (lorbit != 10): 
         Sx = [[[[[0]*(ni+1) for i in range((nb)+1)] for j in range(nk+1)] for k in range(9+1)] for l in range(n_procar+1)]  
         Sy = [[[[[0]*(ni+1) for i in range((nb)+1)] for j in range(nk+1)] for k in range(9+1)] for l in range(n_procar+1)]  
         Sz = [[[[[0]*(ni+1) for i in range((nb)+1)] for j in range(nk+1)] for k in range(9+1)] for l in range(n_procar+1)]  
      if (lorbit == 10): 
         Sx = [[[[[0]*(ni+1) for i in range((nb)+1)] for j in range(nk+1)] for k in range(3+1)] for l in range(n_procar+1)]  
         Sy = [[[[[0]*(ni+1) for i in range((nb)+1)] for j in range(nk+1)] for k in range(3+1)] for l in range(n_procar+1)]  
         Sz = [[[[[0]*(ni+1) for i in range((nb)+1)] for j in range(nk+1)] for k in range(3+1)] for l in range(n_procar+1)]  

   #  Sx[n_procar][1][nk][nb][ni] = Contrinuição de cada ion "ni" para o orbital S de Sx em uma dada banda e ponto-k.
   #  Sx[n_procar][2][nk][nb][ni] = Contrinuição de cada ion "ni" para o orbital Py ou P (lorbit = 10) de Sx em uma dada banda e ponto-k.
   #  Sx[n_procar][3][nk][nb][ni] = Contrinuição de cada ion "ni" para o orbital Pz ou D (lorbit = 10) de Sx em uma dada banda e ponto-k.
   #  Sx[n_procar][4][nk][nb][ni] = Contrinuição de cada ion "ni" para o orbital Px de Sx em uma dada banda e ponto-k.
   #  Sx[n_procar][5][nk][nb][ni] = Contrinuição de cada ion "ni" para o orbital Dxy de Sx em uma dada banda e ponto-k.
   #  Sx[n_procar][6][nk][nb][ni] = Contrinuição de cada ion "ni" para o orbital Dyz de Sx em uma dada banda e ponto-k.
   #  Sx[n_procar][7][nk][nb][ni] = Contrinuição de cada ion "ni" para o orbital Dz2 de Sx em uma dada banda e ponto-k.
   #  Sx[n_procar][8][nk][nb][ni] = Contrinuição de cada ion "ni" para o orbital Dxz de Sx em uma dada banda e ponto-k.
   #  Sx[n_procar][9][nk][nb][ni] = Contrinuição de cada ion "ni" para o orbital Dx2 de Sx em uma dada banda e ponto-k.

#========================================================================================================================================

#######################################################################
########################### Loop dos PROCAR ###########################
#######################################################################

for wp in range(1, (n_procar+1)):

    try: f = open(dir_files + '/PROCAR'); f.close(); teste = 'sim'
    except: teste = 'nao'   
   
    if (teste == 'sim' and n_procar == 1):
       procar = open(dir_files + '/PROCAR', "r")
      
    if (teste == 'nao' and n_procar >= 1):
       procar = open(dir_files + '/PROCAR.' + str(wp), "r")

    for n_spin in range(1,(ispin+1)):

        for i in range(4 - n_spin):
            VTemp = procar.readline()
      
        #######################################################################
        ########################## Loop dos Pontos_k ##########################
        #######################################################################
        
        temp = 1.0; number = 0

        for point_k in range(1, (nk+1)):                                  

            #----------------------------------------------------------------------

            if (n_procar == 1 and point_k == 1 and n_spin == 1):
               print("===========================")
               print("Analisando o arquivo PROCAR")
               print("===========================")

            if (n_procar > 1 and point_k == 1 and n_spin == 1):
               print(" ")
               print("==============================")
               print("Analisando o arquivo PROCAR",wp)
               print("==============================")

            if (ispin == 2 and point_k == 1):
               print("----------------")
               print("Spin Component",n_spin)
               print("----------------")

            #----------------------------------------------------------------------
            # Calculando a porcentagem de leitura do arquivo PROCAR ---------------
            #----------------------------------------------------------------------

            porc = (point_k/nk)*100        

            if (porc >= temp):
               print(f'Processado {porc:>3,.0f}%')                 
               number += 1
               if (number == 1):
                  temp = 10.0
               if (number == 2):
                  temp = 25.0
               if (number >= 3):
                  temp = temp + 25.0
              
            #----------------------------------------------------------------------
            # Leitura das coordenadas k1, k2 e k3 de cada ponto-k -----------------
            #---------------------------------------------------------------------- 

            VTemp = procar.readline()
            #--------------------------------------------------------------------
            teste = VTemp.split()           
            if (len(teste) < 9):
               for i in range(10):
                   VTemp = VTemp.replace('-' + str(i) + '.', ' -' + str(i) + '.')
            VTemp = VTemp.split()
            #--------------------------------------------------------------------

            if (n_spin == 1):          
                                     #  Observacao: No VASP k1, k2 e k3 correspondem as coordenadas diretas de cada ponto-k na ZB, ou seja
               k1 = float(VTemp[3])  #  K = (k1*B1 + k2*B2 + k3*b3), suas coordenadas cartesianas sao obtidas por meio das relacoes abaixo,
               k2 = float(VTemp[4])  #  os quais nos fornecem kx = Coord_X, ky = Coord_Y e kz = Coord_Z, entretanto, devemos observar que  
               k3 = float(VTemp[5])  #  estas coordenadas kx, ky e kz estao escritas em unidades de 2pi/Parametro_de_rede.
       
               kb1[wp][point_k] = k1
               kb2[wp][point_k] = k2
               kb3[wp][point_k] = k3
        
            VTemp = procar.readline()

            if (n_spin == 1):

               #----------------------------------------------------------------------
               # Obtenção da distancia de separacao entre os pontos-k ----------------
               #----------------------------------------------------------------------

               Coord_X = ((k1*B1x) + (k2*B2x) + (k3*B3x))
               Coord_Y = ((k1*B1y) + (k2*B2y) + (k3*B3y))
               Coord_Z = ((k1*B1z) + (k2*B2z) + (k3*B3z))

               kx[wp][point_k] = Coord_X       
               ky[wp][point_k] = Coord_Y
               kz[wp][point_k] = Coord_Z   

               if (wp == 1) and (point_k == 1):
                  comp = 0.0
                  xx[wp][point_k] = comp 

               if (wp != 1) or (point_k != 1):
                  delta_X = Coord_X_antes - Coord_X
                  delta_Y = Coord_Y_antes - Coord_Y
                  delta_Z = Coord_Z_antes - Coord_Z
                  comp = (delta_X**2 + delta_Y**2 + delta_Z**2)**0.5
                  comp = comp + comp_antes
                  xx[wp][point_k] = comp

               Coord_X_antes = Coord_X
               Coord_Y_antes = Coord_Y
               Coord_Z_antes = Coord_Z
               comp_antes = comp
        
               separacao[wp][point_k] = comp

               n_point_k = n_point_k + 1   

               inform.write(f'{n_point_k:>4}{k1:>19,.12f}{k2:>17,.12f}{k3:>17,.12f}   {comp:.12f} \n')
          
            #######################################################################
            ########################### Loop dos Bandas ###########################
            #######################################################################

            for Band_n in range (1, (int(nb/ispin) +1)):

                Band = Band_n + (n_spin - 1)*int(nb/ispin)

                VTemp = procar.readline().split()
                energ =  float(VTemp[4])

               #-------------------------------------------------------------------
               # Ajuste das energias para múltiplos arquivos PROCAR ---------------
               #-------------------------------------------------------------------        

                if (wp == 1):                                             # Energia(1,1,1)                                      
                   Energia[wp][point_k][Band] = energ
                   auto_valor = Energia[wp][point_k][Band]

                if (wp != 1):                                             # Energia(wp,1,1)
                   if ((point_k == 1) and (Band == 1) and (n_spin == 1)):
                      dE  = Energia[wp-1][nk][1] - energ                                   
                   Energia[wp][point_k][Band] = energ + dE
                   auto_valor = Energia[wp][point_k][Band]

                #------------------------------------------------------------------

                if (energ_max < auto_valor):                              # Calculo do maior auto-valor de energia.
                   energ_max = auto_valor

                if (energ_min > auto_valor):                              # Calculo do menor auto-valor de energia.
                   energ_min = auto_valor
              
                VTemp = procar.readline()
                VTemp = procar.readline()               
            
                #######################################################################
                ############################ Loop dos ions ############################
                #######################################################################

                #======================================================================
                #========================== Lendo os Orbitais =========================
                #======================================================================

                if (read_orb == 0):
                   for ion_n in range (1, (ni+1)):
                       VTemp = procar.readline()
                   VTemp = procar.readline()

                if (read_orb == 1):
                   for ion_n in range (1, (ni+1)):
                       VTemp = procar.readline().split()
                       #-------------------------------------------------------------------------                                        
                       for i in range(1,(n_orb+1)):
                           orb[wp][i][point_k][Band][ion_n] = float(VTemp[i])
                       #-------------------------------------------------------------------------                     
                       tot[wp][point_k][Band][ion_n] = float(VTemp[n_orb+1])
                       #-------------------------------------------------------------------------
                   VTemp = procar.readline()
           
                #======================================================================
                #============ Analisando as componentes Sx, Sy e Sz do Spin ===========
                #======================================================================

                if (SO == 2):                                             # Condicao para calculo com acoplamento Spin-orbita
            
                   #======================================================================
                   #==================== Lendo a componente Sx do Spin ===================
                   #======================================================================

                   if (read_spin == 0): 
                      for ion_n in range (1, (ni+1)):
                          VTemp = procar.readline()
                      VTemp = procar.readline()

                   if (read_spin == 1): 
                      for ion_n in range (1, (ni+1)):
                          VTemp = procar.readline().split()
                          #------------------------------------------------------                 
                          for i in range(1,(n_orb+1)):
                              Sx[wp][i][point_k][Band][ion_n] = float(VTemp[i])                                                   
                          #------------------------------------------------------
                      VTemp = procar.readline()
               
                   #======================================================================
                   #==================== Lendo a componente Sy do Spin ===================
                   #======================================================================

                   if (read_spin == 0): 
                      for ion_n in range (1, (ni+1)):
                          VTemp = procar.readline()
                      VTemp = procar.readline()

                   if (read_spin == 1): 
                      for ion_n in range (1, (ni+1)):
                          VTemp = procar.readline().split()
                          #------------------------------------------------------                 
                          for i in range(1,(n_orb+1)):
                              Sy[wp][i][point_k][Band][ion_n] = float(VTemp[i])                                                   
                          #------------------------------------------------------
                      VTemp = procar.readline()

                   #======================================================================
                   #==================== Lendo a componente Sz do Spin ===================
                   #======================================================================            

                   if (read_spin == 0): 
                      for ion_n in range (1, (ni+1)):
                          VTemp = procar.readline()
                      VTemp = procar.readline()

                   if (read_spin == 1): 
                      for ion_n in range (1, (ni+1)):
                          VTemp = procar.readline().split()
                          #------------------------------------------------------                 
                          for i in range(1,(n_orb+1)):
                              Sz[wp][i][point_k][Band][ion_n] = float(VTemp[i])                                                   
                          #------------------------------------------------------
                      VTemp = procar.readline()         

                #----------------------------------------------------------------------
                # Pulando as linhas referente a fase (LORBIT 12) ----------------------
                #---------------------------------------------------------------------- 
 
                #=========== Pulando as linhas referente a fase (LORBIT 12) ===========

                if (lorbit == 12):
                   temp2 = ((2*ni) + 2)
                   for i in range (1, (temp2 + 1)):
                       VTemp = procar.readline()

                if (lorbit != 12):
                   VTemp = procar.readline()

                ###########################################################
                ################## Fim do Loop dos ions ###################
                ###########################################################                
                  
            ###############################################################
            ################### Fim do Loop das Bandas ####################
            ###############################################################

            #----------------------------------------------------------------------
            # Ignorando a linha ao final de cada ponto-k --------------------------
            #---------------------------------------------------------------------- 

            if (point_k < nk):
               VTemp = procar.readline()
        
        ###################################################################
        #################### Fim do Loop dos pontos-k #####################
        ###################################################################

    ###################################################################
    ###################### Fim do Loop do n_spin ######################
    ###################################################################

    #-------------
    procar.close()
    #-------------

#######################################################################
################### Fim do Loop dos arquivos PROCAR ###################
#######################################################################

#----------------------------------------------------------------------
# Fim da escrita do arquivo "informacoes.txt" -------------------------
#---------------------------------------------------------------------- 

inform.write(" \n")

if (Dimensao == 1 or Dimensao == 4):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao (2Pi/Param) \n")
   inform.write("         |                  (2Pi/Param)                 | \n")
if (Dimensao == 2):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao (1/Angs.) \n")
   inform.write("         |                   (1/Angs.)                  | \n")
if (Dimensao == 3):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao (1/nm) \n")
   inform.write("         |                    (1/nm)                    | \n")
 
inform.write(" \n")

n_point_k = 0

for i in range (1,(n_procar+1)):
    for j in range (1, (nk+1)):
        n_point_k += 1
        inform.write(f'{n_point_k:>4}{kx[i][j]:>19,.12f}{ky[i][j]:>17,.12f}{kz[i][j]:>17,.12f}   {separacao[i][j]:.12f} \n')

#-------------
inform.close()
#-------------
