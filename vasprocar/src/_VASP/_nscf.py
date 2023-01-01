# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

execute_python_file(filename = DFT + '_info.py')

#-------------------------------------------------------------------------
inform = open(dir_files + '/output/informacoes.txt', "a")
#-------------------------------------------------------------------------
file_bands = open(dir_files + '/output/Bandas.dat', "w")
#-------------------------------------------------------------------------
if (read_orb == 1):
   file_orb = open(dir_files + '/output/Orbitais.dat', "w")
#-------------------------------------------------------------------------
if (read_spin == 1):
   file_spin = open(dir_files + '/output/Spin.dat', "w")
#-------------------------------------------------------------------------
if (read_psi == 1):
   file_psi = open(dir_files + '/output/Psi/Psi.dat', 'w')
   psi = [0.0]*(6+1)
#-------------------------------------------------------------------------
if (read_reg == 1):
   file_reg = open(dir_files + '/output/Localizacao/Localizacao.dat', 'w')
   reg = [0.0]*(6+1)
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
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |    |        Coord. Cartesianas kx, ky e kz        |   Separacao (2Pi/Param) \n")
   inform.write("         |          K =  k1*B1 + k2*B2 + k3*B3          |    |                  (2Pi/Param)                 | \n")
if (Dimensao == 2):
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |    |        Coord. Cartesianas kx, ky e kz        |   Separacao (1/Angs.) \n")
   inform.write("         |          K =  k1*B1 + k2*B2 + k3*B3          |    |                   (1/Angs.)                  | \n")
if (Dimensao == 3):
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |    |        Coord. Cartesianas kx, ky e kz        |   Separacao (1/nm) \n")
   inform.write("         |          K =  k1*B1 + k2*B2 + k3*B3          |    |                    (1/nm)                    | \n")

inform.write(" \n")

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------

n_point_k = 0        # Variavel com alguma função de controle
comp_k = [0]*(nk+1)  # Vetor que contem as coordenadas dos pontos-k
energ_max = -1000.0  # Valor inicial para determinar o maior valor de Energia
energ_min = +1000.0  # Valor inicial para determinar o menor valor de Energia

separacao = [[0]*(nk+1) for i in range(n_procar+1)]  # separacao[n_procar][nk]
Energia = [[[0]*((nb)+1) for i in range(nk+1)] for j in range(n_procar+1)]  # Energia[n_procar][nk][nb]
                                         
#----------------------------------------------------------------------

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
       print ("ERRO: Os valores das bandas informadas estao incorretos %%")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       confirmacao = input (" ")
       exit()
    #----------------------------------------------------------------------     
    for j in range(loop_i, (loop_f + 1)):
        num_bands += 1
        bands_sn[j] = "sim" 

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

            #-----------
            test = 'nao'
            #-----------
            while (test == 'nao'):             
                  #------------------------
                  VTemp = procar.readline()
                  Teste = VTemp.split() 
                  #---------------------------------------------
                  if (len(Teste) > 0 and Teste[0] == 'k-point'):
                     test = 'sim'
                     for i in range(10):
                         VTemp = VTemp.replace('-' + str(i) + '.', ' -' + str(i) + '.')
                     VTemp = VTemp.split()                         
                     #-----------------------------------------------------------------

            if (n_spin == 1):          
                                     #  Observacao: No VASP k1, k2 e k3 correspondem as coordenadas diretas de cada ponto-k na ZB, ou seja
               k1 = float(VTemp[3])  #  K = (k1*B1 + k2*B2 + k3*b3), suas coordenadas cartesianas sao obtidas por meio das relacoes abaixo,
               k2 = float(VTemp[4])  #  os quais nos fornecem kx = Coord_X, ky = Coord_Y e kz = Coord_Z, entretanto, devemos observar que  
               k3 = float(VTemp[5])  #  estas coordenadas kx, ky e kz estao escritas em unidades de 2pi/Parametro_de_rede.

            VTemp = procar.readline()

            if (n_spin == 1): 
 
               #----------------------------------------------------------------------
               # Obtenção da distancia de separacao entre os pontos-k ----------------
               #----------------------------------------------------------------------

               Coord_X = ((k1*B1x) + (k2*B2x) + (k3*B3x))
               Coord_Y = ((k1*B1y) + (k2*B2y) + (k3*B3y))
               Coord_Z = ((k1*B1z) + (k2*B2z) + (k3*B3z))

               if (wp == 1) and (point_k == 1):
                  comp = 0.0

               if (wp != 1) or (point_k != 1):
                  delta_X = Coord_X_antes - Coord_X
                  delta_Y = Coord_Y_antes - Coord_Y
                  delta_Z = Coord_Z_antes - Coord_Z
                  comp = (delta_X**2 + delta_Y**2 + delta_Z**2)**0.5
                  comp = comp + comp_antes

               Coord_X_antes = Coord_X
               Coord_Y_antes = Coord_Y
               Coord_Z_antes = Coord_Z
               comp_antes = comp

               separacao[wp][point_k] = comp

               n_point_k = n_point_k + 1

               #----------------------------------------------------------------------
               # Escrita das informacoes nos arquivos de saida -----------------------
               #----------------------------------------------------------------------   

               inform.write(f'{n_point_k:>4}{k1:>19,.12f}{k2:>17,.12f}{k3:>17,.12f} {Coord_X:>17,.12f}{Coord_Y:>17,.12f}{Coord_Z:>17,.12f}   {comp:.12f} \n')
          
            #######################################################################
            ########################### Loop dos Bandas ###########################
            #######################################################################

            for Band_n in range (1, (int(nb/ispin) +1)):
                #-----------------------------------------
                Band = Band_n + (n_spin - 1)*int(nb/ispin)
                #-----------------------------------------

                #-----------
                test = 'nao'
                #-----------
                while (test == 'nao'):             
                      VTemp = procar.readline().split()
                      #------------------------------------------
                      if (len(VTemp) > 0 and VTemp[0] == 'band'):
                         test = 'sim'
                         #---------------------------------------

                energ =  float(VTemp[4])
                Energia[wp][point_k][Band] = energ

                #-------------------------------------------------------------------
                # Ajuste das energias para múltiplos arquivos PROCAR ---------------
                #-------------------------------------------------------------------        

                if (wp != n_procar and point_k == nk):
                   temp_E = energ

                if (wp != 1):                                             # Energia(wp,1,1)
                   if ((point_k == 1) and (Band == 1) and (n_spin == 1)):
                      dE  = temp_E - energ  
                      energ = energ + dE
                      Energia[wp][point_k][Band] = energ
                                             
                #------------------------------------------------------------------

                if (energ_max < energ):    # Calculo do maior auto-valor de energia
                   energ_max = energ

                if (energ_min > energ):    # Calculo do menor auto-valor de energia
                   energ_min = energ
              
                #-----------
                test = 'nao'
                #-----------
                while (test == 'nao'):             
                      VTemp = procar.readline().split()
                      #-----------------------------------------
                      if (len(VTemp) > 0 and VTemp[0] == 'ion'):
                         test = 'sim'              
                         #--------------------------------------
            
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

                       #--------------------------------------------------------------------------
                       # Zerando as variaveis ao inicio de cada loop dos ions --------------------
                       #--------------------------------------------------------------------------

                       if (ion_n == 1 and lorbit < 11):
                          Orb_S   = 0.0
                          Orb_P   = 0.0
                          Orb_D   = 0.0
                          Orb_F   = 0.0
                          #------------
                          Orb_tot = 0.0

                       if (ion_n == 1 and lorbit >= 11):
                          Orb_S    = 0.0
                          Orb_P    = 0.0
                          Orb_D    = 0.0
                          Orb_F    = 0.0
                          #-------------
                          Orb_Px   = 0.0
                          Orb_Py   = 0.0
                          Orb_Pz   = 0.0
                          #-------------
                          Orb_Dxy  = 0.0
                          Orb_Dyz  = 0.0
                          Orb_Dz2  = 0.0
                          Orb_Dxz  = 0.0
                          Orb_Dx2  = 0.0
                          #-------------
                          Orb_Fyx2 = 0.0
                          Orb_Fxyz = 0.0
                          Orb_Fyz2 = 0.0
                          Orb_Fzz2 = 0.0
                          Orb_Fxz2 = 0.0
                          Orb_Fzx2 = 0.0
                          Orb_Fxx2 = 0.0                        
                          #-------------
                          Orb_tot  = 0.0

                       #--------------------------------------------------------------------------
                       # Somando a contribuicao orbital de cada ion selecionado ------------------
                       #--------------------------------------------------------------------------
           
                       if (esc_ions == 1):
                          temp_sn = sim_nao[ion_n]

                       if (esc_ions == 0 or (esc_ions == 1 and temp_sn == "sim")):                

                          # Ordem dos Orbitais
                          #       1 | 2  | 3  | 4  |  5  |  6  |  7  |  8  |  9  |  10  |  11  |  12  |  13  |  14  |  15  |  16  |
                          # VASP: S | Py | Pz | Px | Dxy | Dyz | Dz2 | Dxz | Dx2 | Fyx2 | Fxyz | Fyz2 | Fzz2 | Fxz2 | Fzx2 | Fxx2 |
                          # QE:   S | Pz | Px | Py | Dz2 | Dxz | Dyz | Dx2 | Dxy | ???? | ???? | ???? | ???? | ???? | ???? | ???? |

                          if (n_orb <= 4):
                             Orb_S += float(VTemp[1])
                             Orb_P += float(VTemp[2])
                             Orb_D += float(VTemp[3])
                             #-----------------------
                             if (n_orb == 4):
                                Orb_F += float(VTemp[4])

                          if (n_orb >= 9):
                             Orb_S   += float(VTemp[1])
                             Orb_Py  += float(VTemp[2])
                             Orb_Pz  += float(VTemp[3])
                             Orb_Px  += float(VTemp[4])
                             Orb_P   += float(VTemp[2]) + float(VTemp[3]) + float(VTemp[4])
                             Orb_Dxy += float(VTemp[5])
                             Orb_Dyz += float(VTemp[6])
                             Orb_Dz2 += float(VTemp[7])
                             Orb_Dxz += float(VTemp[8])
                             Orb_Dx2 += float(VTemp[9])
                             Orb_D   += float(VTemp[5]) + float(VTemp[6]) + float(VTemp[7]) + float(VTemp[8]) + float(VTemp[9])  
                             #-------------------------------------------------------------------------------------------------         
                             if (n_orb == 16):
                                Orb_Fyx2 += float(VTemp[10])
                                Orb_Fxyz += float(VTemp[11])
                                Orb_Fyz2 += float(VTemp[12])
                                Orb_Fzz2 += float(VTemp[13])
                                Orb_Fxz2 += float(VTemp[14])
                                Orb_Fzx2 += float(VTemp[15])
                                Orb_Fxx2 += float(VTemp[16]) 
                                Orb_F += float(VTemp[10]) + float(VTemp[11]) + float(VTemp[12]) + float(VTemp[13]) + float(VTemp[14]) + float(VTemp[15]) + float(VTemp[16])

                       for orb in range(1,(n_orb+1)):
                           Orb_tot += float(VTemp[orb])

                       if (read_psi == 1):
                          if (ion_n == 1): 
                             for p in range(1,(n_psi+1)):
                                 psi[p] = 0.0
                          for p in range(1,(n_psi+1)):
                              for orb in range(1,(n_orb+1)):
                                  if (ion_orb[p][ion_n][orb] == 1):
                                     psi[p] += float(VTemp[orb])

                       if (read_reg == 1):
                          if (ion_n == 1): 
                             for p in range(1,(n_reg+1)):
                                 reg[p] = 0.0
                          for p in range(1,(n_reg+1)):
                              for orb in range(1,(n_orb+1)):
                                  if (ion_orb[p][ion_n][orb] == 1):
                                     reg[p] += float(VTemp[orb])

                   #--------------------------------------------------------------------------
                   # Calculando a proporcao de cada Orbital ----------------------------------
                   #--------------------------------------------------------------------------
                   
                   if (Orb_tot > 0.01 and DFT == '_VASP/'):
                      if (n_orb <= 4):
                         Orb_S = Orb_S/Orb_tot
                         Orb_P = Orb_P/Orb_tot
                         Orb_D = Orb_D/Orb_tot
                         Orb_F = Orb_F/Orb_tot

                      if (n_orb >= 9):
                         Orb_S    = Orb_S/Orb_tot
                         Orb_P    = Orb_P/Orb_tot
                         Orb_D    = Orb_D/Orb_tot
                         Orb_F    = Orb_F/Orb_tot
                         #------------------------
                         Orb_Px   = Orb_Px/Orb_tot
                         Orb_Py   = Orb_Py/Orb_tot
                         Orb_Pz   = Orb_Pz/Orb_tot
                         #-------------------------
                         Orb_Dxy  = Orb_Dxy/Orb_tot
                         Orb_Dyz  = Orb_Dyz/Orb_tot
                         Orb_Dz2  = Orb_Dz2/Orb_tot
                         Orb_Dxz  = Orb_Dxz/Orb_tot
                         Orb_Dx2  = Orb_Dx2/Orb_tot
                         #--------------------------
                         Orb_Fyx2 = Orb_Fyx2/Orb_tot
                         Orb_Fxyz = Orb_Fxyz/Orb_tot
                         Orb_Fyz2 = Orb_Fyz2/Orb_tot
                         Orb_Fzz2 = Orb_Fzz2/Orb_tot
                         Orb_Fxz2 = Orb_Fxz2/Orb_tot
                         Orb_Fzx2 = Orb_Fzx2/Orb_tot
                         Orb_Fxx2 = Orb_Fxx2/Orb_tot

                      if (read_psi == 1):
                         for p in range (1,(n_psi+1)):
                             psi[p] = psi[p]/Orb_tot

                      if (read_reg == 1):
                         for p in range (1,(n_reg+1)):
                             reg[p] = reg[p]/Orb_tot

                   VTemp = procar.readline()

                if (read_orb == 1and bands_sn[Band_n] == "sim"):
                   file_orb.write(f'{separacao[wp][point_k]} {energ} {Orb_S} {Orb_P} {Orb_D} {Orb_F} ')
                   if (n_orb >= 9):
                      file_orb.write(f'{Orb_Px} {Orb_Py} {Orb_Pz} {Orb_Dxy} {Orb_Dyz} {Orb_Dz2} {Orb_Dxz} {Orb_Dx2} ')
                      file_orb.write(f'{Orb_Fyx2} {Orb_Fxyz} {Orb_Fyz2} {Orb_Fzz2} {Orb_Fxz2} {Orb_Fzx2} {Orb_Fxx2} \n')
                   file_orb.write(f' \n')

                if (read_psi == 1 and bands_sn[Band_n] == "sim"):
                   for p in range (1,(n_psi+1)):
                       if (psi[p] < contrib_min):
                          psi[p] = 0.0
                   file_psi.write(f'{separacao[wp][point_k]} {energ} {psi[1]} {psi[2]} {psi[3]} {psi[4]} {psi[5]} {psi[6]} \n')

                if (read_reg == 1 and bands_sn[Band_n] == "sim"):
                   for p in range (1,(n_reg+1)):
                       if (reg[p] < contrib_min):
                          reg[p] = 0.0
                   file_reg.write(f'{separacao[wp][point_k]} {energ} {reg[1]} {reg[2]} {reg[3]} {reg[4]} {reg[5]} {reg[6]} \n')

                #======================================================================
                #============ Analisando as componentes Sx, Sy e Sz do Spin ===========
                #======================================================================

                if (LNC == 2):      # Condicao para calculo com acoplamento Spin-orbita
            
                   #======================================================================
                   #==================== Lendo a componente Sx do Spin ===================
                   #======================================================================

                   if (read_spin == 0): 
                      for ion_n in range (1, (ni+1)):
                          VTemp = procar.readline()
                      VTemp = procar.readline()

                   if (read_spin == 1): 
                      for ion_n in range (1, (ni+1)):
                          #----------------------------------------------------------                          
                          if (ion_n == 1):
                             Sx = 0.0
                          #----------------------------------------------------------                             
                          VTemp = procar.readline().split()
                          #----------------------------------------------------------
                          for m in range(2):
                              if (len(VTemp) == 0): VTemp = procar.readline().split()
                          #----------------------------------------------------------
                          if (esc_ions == 1):
                             temp_sn = sim_nao[ion_n]
                          #----------------------------------------------------------
                          if (esc_ions == 0 or (esc_ions == 1 and temp_sn == "sim")):  
                             #-------------------------------------------------------  
                             for i in range(1,(n_orb+1)):
                                 Sx += float(VTemp[i])                                                   
                             #---------------------------

                      if (Sx >= 0.0):
                         Sx_up = Sx; Sx_down = 0.0 

                      if (Sx <= 0.0):
                         Sx_down = Sx; Sx_up = 0.0

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
                          #----------------------------------------------------------                          
                          if (ion_n == 1):
                             Sy = 0.0
                          #----------------------------------------------------------                             
                          VTemp = procar.readline().split()
                          #----------------------------------------------------------
                          for m in range(2):
                              if (len(VTemp) == 0): VTemp = procar.readline().split()
                          #----------------------------------------------------------
                          if (esc_ions == 1):
                             temp_sn = sim_nao[ion_n]
                          #----------------------------------------------------------
                          if (esc_ions == 0 or (esc_ions == 1 and temp_sn == "sim")):  
                             #------------------------------------------------------- 
                             for i in range(1,(n_orb+1)):
                                 Sy += float(VTemp[i])                                                   
                             #---------------------------

                      if (Sy >= 0.0):
                         Sy_up = Sy; Sy_down = 0.0 

                      if (Sy <= 0.0):
                         Sy_down = Sy; Sy_up = 0.0

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
                          #----------------------------------------------------------                          
                          if (ion_n == 1):
                             Sz = 0.0
                          #----------------------------------------------------------                             
                          VTemp = procar.readline().split()
                          #----------------------------------------------------------
                          for m in range(2):
                              if (len(VTemp) == 0): VTemp = procar.readline().split()
                          #----------------------------------------------------------
                          if (esc_ions == 1):
                             temp_sn = sim_nao[ion_n]
                          #----------------------------------------------------------
                          if (esc_ions == 0 or (esc_ions == 1 and temp_sn == "sim")):  
                             #-------------------------------------------------------    
                             for i in range(1,(n_orb+1)):
                                 Sz += float(VTemp[i])                                                   
                             #---------------------------

                      if (Sz >= 0.0):
                         Sz_up = Sz; Sz_down = 0.0 

                      if (Sz <= 0.0):
                         Sz_down = Sz; Sz_up = 0.0

                      VTemp = procar.readline()         

                if (read_spin == 1 and LNC == 2 and bands_sn[Band_n] == "sim"):
                   file_spin.write(f'{separacao[wp][point_k]} {energ} {Sx_up} {Sx_down} {Sy_up} {Sy_down} {Sz_up} {Sz_down} \n')

                ########################################################################## 
                ### Fim do Loop dos ions #################################################
            ### Fim do Loop das Bandas ###################################################     
        ### Fim do Loop dos pontos-k #####################################################
    ### Fim do Loop do n_spin ############################################################
    ###################################################################################### 

    #-------------
    procar.close()
    #-------------

##########################################################################################
### Fim do Loop dos arquivos PROCAR ######################################################
##########################################################################################

#=========================================================================================
# Escrita do arquivo Bands.dat ===========================================================
#=========================================================================================

for wp in range(1, (n_procar+1)):
    for point_k in range(1, (nk+1)):
        file_bands.write(f'{separacao[wp][point_k]} ') 
        for Band in range (1, (nb+1)):
            file_bands.write(f'{Energia[wp][point_k][Band]} ')
        file_bands.write(f' \n')

#=========================================================================================
# Fechando arquivos temporarios ==========================================================
#=========================================================================================

#-------------------
inform.close()
#-------------------
file_bands.close()
#-------------------
if (read_orb == 1):
   file_orb.close()
#-------------------
if (read_spin == 1):
   file_spin.close()
#-------------------
if (read_psi == 1):
   file_psi.close()
#-------------------
if (read_reg == 1):
   file_reg.close()
#-------------------