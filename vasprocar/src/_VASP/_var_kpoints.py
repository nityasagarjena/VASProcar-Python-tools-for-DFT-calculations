# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#######################################################################
########################## PROCAR files Loop ##########################
#######################################################################

print("===========================")
print("Analyzing the k-points ====")
print("===========================")

# for wp in range(1, (n_procar+1)):
for wp in range(1, (1+1)):

    try: f = open(dir_files + '/PROCAR'); f.close(); teste = 'sim'
    except: teste = 'nao'   
   
    if (teste == 'sim' and n_procar == 1):
       procar = open(dir_files + '/PROCAR', "r")
      
    if (teste == 'nao' and n_procar >= 1):
       procar = open(dir_files + '/PROCAR.' + str(wp), "r")

    for n_spin in range(1,(ispin+1)):
     
        #######################################################################
        ############################ k-points loop ############################
        #######################################################################
        
        temp = 1.0; number = 0

        for point_k in range(1, (nk+1)):                                  

            #----------------------------------------------------------------------

            if (n_procar == 1 and point_k == 1 and n_spin == 1):
               print(" ")
               print("-------------------------")
               print("Analyzing the PROCAR file")
               print("-------------------------")

            if (n_procar > 1 and point_k == 1 and n_spin == 1):
               print(" ")
               print("----------------------------")
               print("Analyzing the PROCAR file",wp)
               print("----------------------------")

            if (ispin == 2 and point_k == 1):
               print(" ")
               print("----------------")
               print("Spin Component",n_spin)
               print("----------------")

            #----------------------------------------------------------------------
            # Calculating the PROCAR file reading percentage ----------------------
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
            # Reading the k1, k2 and k3 coordinates of each k-point ---------------
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
                                     #  Note: In VASP k1, k2 and k3 correspond to the direct coordinates of each k-point in the ZB, that is, 
               k1 = float(VTemp[3])  #  K = (k1*B1 + k2*B2 + k3*b3), its Cartesian coordinates are obtained through the relations below, 
               k2 = float(VTemp[4])  #  which give us kx = Coord_X, ky = Coord_Y and kz = Coord_Z, however, we should note that these kx, ky   
               k3 = float(VTemp[5])  #  and kz coordinates are written in units of 2pi/Network_parameter.
        
            VTemp = procar.readline()

            if (n_spin == 1):

               Coord_X = ((k1*B1x) + (k2*B2x) + (k3*B3x))
               Coord_Y = ((k1*B1y) + (k2*B2y) + (k3*B3y))
               Coord_Z = ((k1*B1z) + (k2*B2z) + (k3*B3z))

               #----------------------------------------------------------------------------
               # Test to verify the variation of coordinates k1, k2, k3, kx, ky and kz -----
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
            ############################# bands loop ##############################
            #######################################################################

            for Band_n in range (1, (int(nb/ispin) +1)):

                #-----------
                test = 'nao'
                #-----------
                while (test == 'nao'):             
                      VTemp = procar.readline().split()
                      #--------------------------------
                      if (len(VTemp) > 0 and VTemp[0] == 'band'):
                         test = 'sim'
                         #---------------------------------------              

                #-----------
                test = 'nao'
                #-----------
                while (test == 'nao'):             
                      VTemp = procar.readline().split()
                      #--------------------------------
                      if (len(VTemp) > 0 and VTemp[0] == 'ion'):
                         test = 'sim'                
                         #--------------------------------------
            
                #######################################################################
                ############################## ions loop ##############################
                #######################################################################

                #======================================================================
                #============== Ignoring the lines referring to Orbitals ==============
                #======================================================================

                for ion_n in range (1, (ni+1)):
                    VTemp = procar.readline()
                VTemp = procar.readline()

                if (LNC == 2):  #  Condition for calculation with Spin-orbit coupling
            
                   #======================================================================
                   #========== Ignoring lines referring to Spin's Sx component ===========
                   #======================================================================

                   for ion_n in range (1, (ni+1)):
                       VTemp = procar.readline()
                   VTemp = procar.readline()
               
                   #======================================================================
                   #========== Ignoring lines referring to Spin's Sy component ===========
                   #======================================================================

                   for ion_n in range (1, (ni+1)):
                       VTemp = procar.readline()
                   VTemp = procar.readline()

                   #======================================================================
                   #========== Ignoring lines referring to Spin's Sz component ===========
                   #======================================================================           

                   for ion_n in range (1, (ni+1)):
                       VTemp = procar.readline()
                   VTemp = procar.readline()          

                ##########################################################################
                ### End of the ions loop #################################################
            ### End of the bands loop ####################################################
        ### End of the k-points loop #####################################################
    ### End of the n_spin loop ###########################################################
    ######################################################################################
    
    #-------------
    procar.close()
    #-------------

#######################################################################
#################### End of the PROCAR files loop #####################
#######################################################################

print(" ")
