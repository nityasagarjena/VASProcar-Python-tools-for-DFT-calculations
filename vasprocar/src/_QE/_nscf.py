# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

print('TESTE4')

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

execute_python_file(filename = DFT + '_info.py')

print('TESTE5')

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

if (read_orb == 1):
   
   orb = [[[[[0]*(ni+1) for i in range((nb)+1)] for j in range(nk+1)] for k in range(9+1)] for l in range(n_procar+1)]  

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

print('TESTE6')

#######################################################################
########################### Loop dos ?????? ###########################
#######################################################################

for wp in range(1,(n_procar+1)):

   #===================================================================
   # Obtenção dos autovalores de energia ==============================
   # Obtenção das simetrias dos autovalores e dos pontos-k ============
   #===================================================================

   print('TESTE7')

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
             #--------------------------------
             VTemp = bands.readline()
             VTemp = VTemp.replace('e(','e( ').replace(")","")
             VTemp = VTemp.split()
             #--------------------------------
             
             if (len(VTemp) >= 9):
                #---------------------------------
                if (VTemp[8] == '-->'): delta = 0
                if (VTemp[7] == '-->'): delta = -1
                #---------------------------------
                band_i = int(VTemp[1])
                #--------------------------------------------------------------          
                band_f = str(VTemp[3 + delta]); band_f = band_f.replace("-","")
                band_f = int(band_f)
                #--------------------------------------------------------------
                energ = float(VTemp[5 + delta])
                #---------------------------------------
                irrep_temp = str(VTemp[9 + delta])
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
      project = open(dir_files + '/projwfc.in', "r")
      #---------------------------------------------

      test = 'null'

      while (test != 'filproj'): 
          #--------------------------------
          VTemp = project.readline()
          VTemp = VTemp.replace('=', ' = ')
          VTemp = VTemp.replace(',', ' , ')
          VTemp = VTemp.replace("'", "")
          VTemp = VTemp.split()
          #---------------------------------------------
          if (len(VTemp) > 0 and VTemp[0] == 'filproj'):
             filproj = str(VTemp[2])
             test = VTemp[0]

      #--------------
      project.close()
      #--------------

      #===================================================================

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
          #---------------------------------
          ion_n = int(VTemp[1])
          rotulo_ion = str(VTemp[2])
          rotulo_orb = str(VTemp[3])
          t_orb_L = int(VTemp[5])  # Numero quântico L: L = 0 (Orbital S); L = 1 (Orbital P); L = 2 (Orbital D)
          t_orb_M = int(VTemp[6])
          #----------------------
          if (lorbit == 10):
             t_orb = t_orb_L + 1
          #----------------------   
          if (lorbit >= 11):
             if (t_orb_L == 0):    t_orb = 1  # Orbital S
             if (t_orb_L == 1):
                if (t_orb_M == 1): t_orb = 2  # Orbital Pz
                if (t_orb_M == 2): t_orb = 3  # Orbital Px
                if (t_orb_M == 3): t_orb = 4  # Orbital Py 
             if (t_orb_L == 2):
                if (t_orb_M == 1): t_orb = 5  # Orbital Dz2
                if (t_orb_M == 2): t_orb = 6  # Orbital Dxz
                if (t_orb_M == 3): t_orb = 7  # Orbital Dyz
                if (t_orb_M == 4): t_orb = 8  # Orbital Dx2
                if (t_orb_M == 5): t_orb = 9  # Orbital Dxy
             
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
