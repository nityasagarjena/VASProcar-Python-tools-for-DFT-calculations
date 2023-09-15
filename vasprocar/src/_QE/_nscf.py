# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

execute_python_file(filename = DFT + '_info.py')

#--------------------------------------------------------
inform = open(dir_files + '/output/informacoes.txt', "a")
#--------------------------------------------------------
file_bands = open(dir_files + '/output/Bandas.dat', "w")
#----------------------------------------------------------
if (read_projwfc_up == 1):
   file_orb = open(dir_files + '/output/Orbitais.dat', "w")
#----------------------------------------------------------
if (read_reg == 1):
   file_reg = open(dir_files + '/output/Localizacao/Localizacao.dat', 'w')
   reg = [[[[0.0]*(nb+1) for j in range(nk+1)] for l in range(6+1)] for k in range(n_procar+1)] 


#-------------------------------------------------------------------------

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

"""
B1x = B1x*fator_zb
B1y = B1y*fator_zb
B1z = B1z*fator_zb
B2x = B2x*fator_zb
B2y = B2y*fator_zb
B2z = B2z*fator_zb
B3x = B3x*fator_zb
B3y = B3y*fator_zb
B3z = B3z*fator_zb
"""

#----------------------------------------------------------------------

inform.write("***************************************************** \n")
inform.write("*********** Pontos-k na Zona de Brillouin *********** \n")
inform.write("***************************************************** \n")
inform.write(" \n")
      
if (Dimensao == 1 or Dimensao == 4):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao      | Symmetry \n")
   inform.write("         |                  (2Pi/Param)                 |   (2Pi/Param)    |          \n")
if (Dimensao == 2):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao      | Symmetry \n")
   inform.write("         |                   (1/Angs.)                  |   (1/Angs.)      |          \n")
if (Dimensao == 3):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao      | Symmetry \n")
   inform.write("         |                    (1/nm)                    |   (1/nm)         |          \n")

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
# kb1 = [[0]*(nk+1) for i in range(n_procar+1)]  # kb1[n_procar][nk]
# kb2 = [[0]*(nk+1) for i in range(n_procar+1)]  # kb2[n_procar][nk]
# kb3 = [[0]*(nk+1) for i in range(n_procar+1)]  # kb3[n_procar][nk]

separacao = [[0]*(nk+1) for i in range(n_procar+1)]  # separacao[n_procar][nk]
Energia = [[[0]*((nb)+1) for i in range(nk+1)] for j in range(n_procar+1)]  # Energia[n_procar][nk][nb]

#======================================================================================================

num_bands = 0
bands_sn = ["nao"]*(nb + 1)
selected_bands = bands_range.replace(':', ' ').replace('-', ' ').split()
loop = int(len(selected_bands)/2)
    
for i in range (1,(loop+1)):
    #-----------------------------------------
    loop_i = int(selected_bands[(i-1)*2])
    loop_f = int(selected_bands[((i-1)*2) +1])
    #----------------------------------------------------------------------------------------
    if ((loop_i > nb) or (loop_f > nb) or (loop_i < 0) or (loop_f < 0) or (loop_i > loop_f)):
       print (" ")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       print ("ERROR: The values of the informed bands are incorrect %%%%")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       confirmacao = input (" ")
       exit()
    #----------------------------------------------------------------------     
    for j in range(loop_i, (loop_f + 1)):
        num_bands += 1
        bands_sn[j] = "sim" 

#======================================================================================================

if (read_orb == 1):
   
   orb = [[[[[0]*(ni+1) for i in range((nb)+1)] for j in range(nk+1)] for k in range(n_orb+1)] for l in range(n_procar+1)]
   # orb[n_procar][no][nk][nb][ni]

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

irrep = [[[0]*(nb+1) for j in range(nk+1)] for l in range(n_procar+1)]  #  irrep[n_procar][nk][nb]
symmetry = [[0]*(nk+1) for j in range(n_procar+1)]  #  symmetry[n_procar][nk]

#========================================================================================================================================

#######################################################################
########################### Loop dos ?????? ###########################
#######################################################################

for wp in range(1,(n_procar+1)):

   #===================================================================
   # Obtenção dos autovalores de energia ==============================
   # Obtenção das simetrias dos autovalores e dos pontos-k ============
   #===================================================================

   #------------------------------------------
   bands = open(dir_files + '/bands.out', 'r')
   #------------------------------------------

   for line in bands:
       if 'xk=(' in line:
          break

   for point_k in range(1,(nk+1)):

       n_nb = 0
       test = 'null' 

       while (test != 'Band'):             
             #-------------------------------
             VTemp = bands.readline().split()
             #-------------------------------
             if (len(VTemp) > 0):
                test = VTemp[0]
             #-------------------------------------------------------------------
             if (len(VTemp) > 1 and VTemp[0] == 'point' and VTemp[1] == 'group'):
                symmetry[wp][point_k] = str(VTemp[2])
                symmetry[wp][point_k] = symmetry[wp][point_k].replace("_", "")
                #-------------------------------
                VTemp = bands.readline().split()
                n_classes = int(VTemp[2])
                n_irreps = n_classes
             #-------------------------------------------------------------------       
             if (len(VTemp) > 1 and VTemp[0] == 'double' and VTemp[1] == 'point'):
                symmetry[wp][point_k] = str(VTemp[3])
                symmetry[wp][point_k] = symmetry[wp][point_k].replace("_", "")
                #-------------------------------
                VTemp = bands.readline().split()
                n_classes = int(VTemp[2])
                n_irreps = int(VTemp[5])
             #----------------------------------------------------------------------
             if (len(VTemp) > 1 and VTemp[0] == 'Band' and VTemp[1] == 'symmetry,'):
                symmetry[wp][point_k] = str(VTemp[2])
                symmetry[wp][point_k] = symmetry[wp][point_k].replace("_", "")

       #=============================================================================

       VTemp = bands.readline()

       n_spin = 1  # ????????????????????????????????????????????????????????????????

       while (n_nb < nb): 
             #------------------------------------------------------------------------------------------------------
             VTemp = bands.readline().replace("(", " ( ").replace(")", " ) ").replace("-  ", "-").replace("- ", "-")
             VTemp = VTemp.split()
             #--------------------
             
             if (len(VTemp) >= 9):
                #---------------------
                band_i = str(VTemp[2])
                band_i = int(band_i)
                #--------------------------------------          
                band_f = str(VTemp[3]).replace("-", "")
                band_f = int(band_f)
                #----------------------
                energ = float(VTemp[6])
                #-------------------------------------------------
                if (len(VTemp) == 11): irrep_temp = str(VTemp[10])
                if (len(VTemp) == 12): irrep_temp = str(VTemp[11])
                irrep_temp = irrep_temp.replace("_", "")
                #---------------------------------------
                n_nb = band_f
         
                for band_s in range(band_i,(band_f+1)):

                    #-----------------------------------------
                    band = band_s + (n_spin - 1)*int(nb/ispin)
                    #-----------------------------------------

                    #------------------------------------------------------------------
                    # Ajuste das energias para múltiplos arquivos ?????? --------------
                    #------------------------------------------------------------------        

                    if (wp == 1):  # Energia(1,1,1)                                      
                       Energia[wp][point_k][band] = energ
                       auto_valor = Energia[wp][point_k][band]

                    if (wp != 1):  # Energia(wp,1,1)
                       if ((point_k == 1) and (band == 1) and (n_spin == 1)):
                          dE  = Energia[wp-1][nk][1] - energ                                   
                       Energia[wp][point_k][band] = energ + dE
                       auto_valor = Energia[wp][point_k][band]

                    #---------------------------------------------------------------------

                    if (energ_max < auto_valor):  # Calculo do maior auto-valor de energia
                       energ_max = auto_valor

                    if (energ_min > auto_valor):  # Calculo do menor auto-valor de energia
                       energ_min = auto_valor
                       
                    #---------------------------------------------------------------------
                       
                    irrep[wp][point_k][band] = irrep_temp
               
       #----------------------------------------------------------------------------------

       if (i != nk):
          for i in range(5):
              VTemp = bands.readline()        

   #------------
   bands.close()
   #------------

   #===================================================================
   # Obtenção das coordenadas dos pontos-k ============================
   #===================================================================

   #-------------------------------------------
   bands = open(dir_files + '/' + filband, 'r')
   #-------------------------------------------

   if (nb % 10 == 0.0):
      nloop = int(nb/10)
   if (nb % 10 != 0.0):
      nloop = int(nb/10) + 1

   VTemp = bands.readline()

   for point_k in range(1,(nk+1)):
    
       VTemp = bands.readline().split()
    
       Coord_X = float(VTemp[0])*fator_zb
       Coord_Y = float(VTemp[1])*fator_zb
       Coord_Z = float(VTemp[2])*fator_zb

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

       inform.write(f'{n_point_k:>4}{Coord_X:>19,.12f}{Coord_Y:>17,.12f}{Coord_Z:>17,.12f}   {comp:.12f}   {symmetry[wp][point_k]} \n')

       for j in range(nloop):
           VTemp = bands.readline()

   #------------
   bands.close()
   #-------------
   inform.close()
   #-------------




   #===================================================================
   # Obtenção da informação dos Orbitais ==============================
   #===================================================================

   if (read_orb == 1):

      #---------------------------------------------
      projwfc = open(dir_files + '/projwfc.in', "r")
      #---------------------------------------------

      filpdos = 'a'
      filproj = 'a'

      for i in range(1000):
          #----------------------------------------------------------------------------------
          VTemp = projwfc.readline().replace('=', ' = ').replace(',', ' , ').replace("'", "")
          VTemp = VTemp.split()
          #--------------------
          if (len(VTemp) >= 3):
             if (VTemp[0] == 'prefix'):  prefix  = str(VTemp[2])
             if (VTemp[0] == 'filpdos'): filpdos = str(VTemp[2])
             if (VTemp[0] == 'filproj'): filproj = str(VTemp[2])

      #--------------
      projwfc.close()
      #--------------

      if (filpdos == 'a'): filpdos = prefix
      if (filproj == 'a'): filproj = prefix

      #===================================================================

      #----------------------------------------------
      projwfc = open(dir_files + '/projwfc.out', "r")
      #----------------------------------------------

      test = 'null' 

      while (test != 'Calling'):             
            #---------------------------------
            VTemp = projwfc.readline().split()
            if (len(VTemp) > 0): test = str(VTemp[0])
            #----------------------------------------

      for ii in range(4):
          VTemp = projwfc.readline()

      test = 'state'

      n_wfc = 0

      while (test == 'state'):             
            #-------------------------------------------------------------------------------------
            VTemp = projwfc.readline().replace(":", " : ").replace("(", " ( ").replace(")", " ) ")
            VTemp = VTemp.split()
            #--------------------
            if (len(VTemp) > 0):
               test = str(VTemp[0])
               if (test == 'state'):
                  n_wfc += 1
            if (len(VTemp) == 0):
               test = 'null'
            #--------------------

      projwfc.close()

   #===================================================================

   if (read_projwfc_up == 1):

      #-------------------------------------------------------------
      project = open(dir_files + '/' + filproj + '.projwfc_up', 'r')
      #-------------------------------------------------------------

      for i in range(7 + types + ni):
          VTemp = project.readline()

      VTemp = project.readline().split()
      no = int(VTemp[0])

      VTemp = project.readline()

      number_P = 0
      number_D = 0

      #------------------
      for i in range(no):
      #------------------
                  
          VTemp = project.readline().split()
          #-------------------------
          ion_n = int(VTemp[1])
          rotulo_ion = str(VTemp[2])
          rotulo_orb = str(VTemp[3])
          t_orb = int(VTemp[5])    # Numero quântico l: 0 = Orbital_S; 1 = Orbital_P; 2 = Orbital_D
          t_orb = t_orb + 1
          #-------------------------         
             
          #------------------------------
          for point_k in range(1,(nk+1)):
          #------------------------------
              #---------------------------
              for Band in range(1,(nb+1)):
              #---------------------------

                  VTemp = project.readline().split()
                  orb[wp][t_orb][point_k][Band][ion_n] = orb[wp][t_orb][point_k][Band][ion_n] + float(VTemp[2])
                  tot[wp][point_k][Band][ion_n] = tot[wp][point_k][Band][ion_n] + float(VTemp[2])

      #--------------
      project.close()
      #--------------


      #====================================================================== 
      # Initialization of Variables, Vectors and Matrices ===================
      #====================================================================== 
   
      soma_orb = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(n_orb+1)] for k in range(n_procar+1)]                    # soma_orb[n_procar][n_orb][nk][nb]
      total = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                                                 # tot[n_procar][nk][nb]
 
      #  orb      = Orbital portion (S, P or D) referring to each "ni" ion
      #  soma_orb = Orbital sum (S, P or D) over all selected "ni" ions
      #  tot      = Sum over all orbitals and all ions

      color_SPD  = [0]*n_procar*nk*nb  # color_SPD[n_procar*nk*nb]
      color_P    = [0]*n_procar*nk*nb  # color_P[n_procar*nk*nb]
      color_D    = [0]*n_procar*nk*nb  # color_D[n_procar*nk*nb]

      orb_S   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
      orb_P   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
      orb_D   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]

      #======================================================================
      # Calculo do peso (% de contribuição) de cada orbital =================
      #====================================================================== 

      for wp in range(1, (n_procar+1)):
          for point_k in range(1, (nk+1)):                                  
              for Band_n in range (1, (nb+1)):
                  for ion_n in range (1, (ni+1)):            
                      #------------------------------------------------------                
                      if (esc_ions == 1):
                         temp_sn = sim_nao[ion_n]
                      #------------------------------------------------------                              
                      for orb_n in range(1,(n_orb+1)):
                          total[wp][point_k][Band_n] = total[wp][point_k][Band_n] + orb[wp][orb_n][point_k][Band_n][ion_n]
                          if (esc_ions == 0 or (esc_ions == 1 and temp_sn == "sim")):
                             soma_orb[wp][orb_n][point_k][Band_n] = soma_orb[wp][orb_n][point_k][Band_n] + orb[wp][orb_n][point_k][Band_n][ion_n]                    

              #----------------------------------------------------------
              # End of the loop over bands ------------------------------
              #----------------------------------------------------------      
          #----------------------------------------------------------
          # End of the loop over K-points ---------------------------
          #----------------------------------------------------------    
      #----------------------------------------------------------
      # End of the PROCAR loop ----------------------------------
      #----------------------------------------------------------

      #======================================================================
      # Calculo do peso de cada REGIAO da Rede sobre os estados =============
      #====================================================================== 

      if (read_reg == 1):
         for wp in range(1, (n_procar+1)):
             for point_k in range(1, (nk+1)):                                  
                 for Band_n in range (1, (nb+1)):
                     for p in range(1,(n_reg+1)):
                         for ion_n in range (1, (ni+1)):
                             if (ion_n == 1): reg[wp][p][point_k][Band_n] = 0.0 
                             for orbital in range(1,(n_orb+1)):
                                 if (ion_orb[p][ion_n][orbital] == 1):
                                    reg[wp][p][point_k][Band_n] += orb[wp][orbital][point_k][Band_n][ion_n]

#=========================================================================================
# Bands.dat file writing =================================================================
#=========================================================================================

for wp in range(1, (n_procar+1)):
    for point_k in range(1, (nk+1)):
        file_bands.write(f'{separacao[wp][point_k]} ') 
        for Band in range (1, (nb+1)):
            file_bands.write(f'{Energia[wp][point_k][Band]} ')
        file_bands.write(f' \n')

#-----------------
file_bands.close()
#-----------------

#=========================================================================================
# Orbitais.dat file writing ==============================================================
#=========================================================================================

if (read_projwfc_up == 1):
   for wp in range(1, (n_procar+1)):
       for point_k in range(1, (nk+1)):
           for Band_n in range (1, (nb+1)):
               if (bands_sn[Band_n] == "sim"):
                  file_orb.write(f'{separacao[wp][point_k]} {Energia[wp][point_k][Band_n]} {soma_orb[wp][1][point_k][Band_n]} {soma_orb[wp][2][point_k][Band_n]} ')
                  file_orb.write(f'{soma_orb[wp][3][point_k][Band_n]} {0.0} \n')

   #---------------
   file_orb.close()
   #---------------

#=========================================================================================
# Localizacao.dat file writing ===========================================================
#=========================================================================================


if (read_reg == 1):
   for wp in range(1, (n_procar+1)):
       for point_k in range(1, (nk+1)):
           for Band_n in range (1, (nb+1)):
               if (bands_sn[Band_n] == "sim"):
                  for p in range (1,(n_reg+1)):
                      if (reg[wp][p][point_k][Band_n] < contrib_min):
                         reg[wp][p][point_k][Band_n] = 0.0
                  file_reg.write(f'{separacao[wp][point_k]} {Energia[wp][point_k][Band_n]} {reg[wp][1][point_k][Band_n]} {reg[wp][2][point_k][Band_n]} ')
                  file_reg.write(f'{reg[wp][3][point_k][Band_n]} {reg[wp][4][point_k][Band_n]} {reg[wp][5][point_k][Band_n]} {reg[wp][6][point_k][Band_n]} \n')


   #---------------
   file_reg.close()
   #---------------
