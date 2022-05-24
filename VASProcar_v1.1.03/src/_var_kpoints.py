
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#######################################################################
########################### Loop dos PROCAR ###########################
#######################################################################

print("===========================")
print("Analisando os pontos-k ====")
print("===========================")
print(" ")

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
               print("Analisando o arquivo PROCAR")
               print("---------------------------")

            if (n_procar > 1 and point_k == 1 and n_spin == 1):
               print("Analisando o arquivo PROCAR",wp)
               print("------------------------------")

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
        
            VTemp = procar.readline()

            if (n_spin == 1):

               Coord_X = ((k1*B1x) + (k2*B2x) + (k3*B3x))
               Coord_Y = ((k1*B1y) + (k2*B2y) + (k3*B3y))
               Coord_Z = ((k1*B1z) + (k2*B2z) + (k3*B3z))

               #----------------------------------------------------------------------------
               # Teste para verificar a variacao das coordenadas k1, k2, k3, kx, ky e kz ---
               #----------------------------------------------------------------------------

               if (wp == 1 and point_k == 1):
                  k1_i = k1; k2_i = k2; k3_i = k3
                  kx_i = Coord_X; ky_i = Coord_Y; kz_i = Coord_Z         
                  dk = [0]*6

               if (wp != 1 or (wp == 1 and point_k != 1)):
                  #---------------------------------
                  if (k1 != k1_i):      dk[0] = 1
                  if (k2 != k2_i):      dk[1] = 1
                  if (k3 != k3_i):      dk[2] = 1
                  if (Coord_X != kx_i): dk[3] = 1
                  if (Coord_Y != ky_i): dk[4] = 1
                  if (Coord_Z != kz_i): dk[5] = 1
           
            #######################################################################
            ########################### Loop dos Bandas ###########################
            #######################################################################

            for Band_n in range (1, (int(nb/ispin) +1)):

                VTemp = procar.readline()             
                VTemp = procar.readline()
                VTemp = procar.readline()               
            
                #######################################################################
                ############################ Loop dos ions ############################
                #######################################################################

                #======================================================================
                #============ Ignorando as linhas referentes aos Orbitais =============
                #======================================================================

                for ion_n in range (1, (ni+1)):
                    VTemp = procar.readline()
                VTemp = procar.readline()

                if (SO == 2):  #  Condicao para calculo com acoplamento Spin-orbita
            
                   #======================================================================
                   #======= Ignorando as linhas referentes a componente Sx do Spin =======
                   #======================================================================

                   for ion_n in range (1, (ni+1)):
                       VTemp = procar.readline()
                   VTemp = procar.readline()
               
                   #======================================================================
                   #======= Ignorando as linhas referentes a componente Sy do Spin =======
                   #======================================================================

                   for ion_n in range (1, (ni+1)):
                       VTemp = procar.readline()
                   VTemp = procar.readline()

                   #======================================================================
                   #======= Ignorando as linhas referentes a componente Sz do Spin =======
                   #======================================================================           

                   for ion_n in range (1, (ni+1)):
                       VTemp = procar.readline()
                   VTemp = procar.readline()          

                #----------------------------------------------------------------------
                # Pulando as linhas referente a fase (LORBIT 12) ----------------------
                #---------------------------------------------------------------------- 
 
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

print(" ")
