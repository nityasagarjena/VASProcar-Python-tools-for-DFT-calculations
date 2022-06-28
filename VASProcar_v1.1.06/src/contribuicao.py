
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#======================================================================
# Get VASP/QE outpout files information ===============================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#======================================================================
# Getting the input parameters ========================================
#======================================================================

print ("##############################################################")
print ("################ Orbital & ions contribution: ################")
print ("##############################################################")
print (" ")

if (escolha == -1):

   print ("##############################################################")
   print ("Inform the Band interval to be analyzed: ==================== ")
   print ("--------------------------------------------------------------")
   print ("Examples:                                                     ")
   print ("Initial_band  Final_band: 5 15                                ")
   print ("Initial_band  Final_band: 7 7                                 ")
   print ("--------------------------------------------------------------")
   print ("##############################################################") 
   print (" ")
   Band_i, Band_f = input ("Initial_band  Final_band: ").split()
   Band_i = int(Band_i)
   Band_f = int(Band_f)
   print (" ") 

   print ("##############################################################")
   print ("Inform the k-point interval to be analyzed: ================= ")
   print ("--------------------------------------------------------------")
   print ("Examples:                                                     ")
   print ("Initial_K-point  Final_K-point: 90 250                        ")
   print ("Initial_K-point  Final_K-point: 75 75                         ")   
   print ("--------------------------------------------------------------")
   print ("##############################################################") 
   print (" ")
   point_i, point_f = input ("Initial_K-point  Final_K-point: ").split()
   point_i = int(point_i)
   point_f = int(point_f)
   print (" ")  

if (escolha == 1):
   point_i = 1
   point_f = nk
   Band_i = 1
   Band_f = nb

#*****************************************************************
# k-axis units ===================================================
# Dimensao = 1 >> 2pi/Param. (Param. in Angs.) *******************
# Dimensao = 2 >> 1/Angs. ****************************************
# Dimensao = 3 >> 1/nm *******************************************
#*****************************************************************
Dimensao = 1

#----------------------------------------------------------------------
# Obtaining the results from DFT outpout files ------------------------
#----------------------------------------------------------------------
read_orb = 1
execute_python_file(filename = DFT + '_nscf.py')

#----------------------------------------------------------------------
# Initialization of Variables, Vectors and Matrices -------------------
#----------------------------------------------------------------------

Band_antes   = (Band_i  -1)                    # Bands that will not be analyzed
Band_depois  = (Band_f  +1)                    # Bands that will not be analyzed
point_antes  = (point_i -1)                    # K-points that will not be analyzed
point_depois = (point_f +1)                    # K-points that will not be analyzed

atomo = [0]*(ni+1)

tot_ion = [[[[0]*(ni+1) for i in range(nb+1)] for j in range(nk+1)] for l in range(n_procar+1)]                        # tot_ion[n_procar][nk][nb][ni]
soma_orb = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(n_orb+1)] for k in range(n_procar+1)]                    # soma_orb[n_procar][n_orb][nk][nb]
total = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                                                 # tot[n_procar][nk][nb]
 
#  orb      = Orbital portion (S, P or D) referring to each "ni" ion
#  soma_orb = Orbital sum (S, P or D) over all selected "ni" ions
#  tot      = Sum over all orbitals and all ions

n_point_k = 0

linha_1 = "================================================"
linha_2 = "=========================================================================================================================================================================" 

###########################################################################
###########################################################################
###########################################################################

#--------------------------------------------------------------------
contrib_ions = open(dir_files + '/output/Contribuicao_ions.txt', 'w')
#----------------------------------------------------------------------------
contrib_orbitais = open(dir_files + '/output/Contribuicao_Orbitais.txt', 'w')
#----------------------------------------------------------------------------
  
contrib_ions.write("================================================================  \n")
contrib_ions.write("Note:                                                             \n")
contrib_ions.write("1) Ions with highest contribution are listed first                \n")
contrib_ions.write("2) Ions with zero contribution are not shown.                     \n")
contrib_ions.write("3) Ions with NO contribution are not listed.                      \n")
contrib_ions.write("================================================================  \n")
contrib_ions.write(" \n")

#######################################################################
############################# PROCAR loop #############################
#######################################################################

for wp in range(1, (n_procar+1)):

    if (n_procar > 1):
       
       contrib_ions.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
       contrib_ions.write(f'PROCAR nº {wp} \n')
       contrib_ions.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
       contrib_ions.write(" \n")

       contrib_orbitais.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
       contrib_orbitais.write(f'PROCAR nº {wp} \n')
       contrib_orbitais.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
       contrib_orbitais.write(" \n")       
      
    ###################################################################
    ####################### Loop over k-points: #######################
    ###################################################################

    for point_k in range(1, (nk+1)):
        
        # Criterion to define which k-points will be analyzed
        if (point_k > point_antes and point_k < point_depois):                      

           contrib_ions.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
           contrib_ions.write(f'K-point {point_k}: Direct coord. ({kb1[wp][point_k]}, {kb2[wp][point_k]}, {kb3[wp][point_k]}) \n')
           contrib_ions.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
           contrib_ions.write(" \n")

           contrib_orbitais.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
           contrib_orbitais.write(f'K-point {point_k}: Direct coord. ({kb1[wp][point_k]}, {kb2[wp][point_k]}, {kb3[wp][point_k]}) \n')
           contrib_orbitais.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
           contrib_orbitais.write(" \n")  

        ###############################################################
        ####################### Loop over Bands #######################
        ###############################################################

        for Band_n in range (1, (nb+1)):

            soma = 0.0
            
            # Criterion to define which bands will be analyzed 
            if ((point_k > point_antes and point_k < point_depois) and (Band_n > Band_antes and Band_n < Band_depois)):   

               contrib_ions.write(f'Band {Band_n} \n')
               contrib_ions.write(f'{linha_1}====== \n')

               contrib_orbitais.write(f'Band {Band_n:<3} \n')             
               
               if (lorbit >= 11): 
                  contrib_orbitais.write(f'{linha_2} \n')
               if (lorbit == 10):
                  contrib_orbitais.write(f'{linha_1}==== \n')                  
            
            ###########################################################
            ##################### Loop over Ions: #####################
            ###########################################################

            for ion_n in range (1, (ni+1)):
                atomo[ion_n] = ion_n                                     
                #------------------------------------------------------                                            
                for orb_n in range(1,(n_orb+1)):
                    tot_ion[wp][point_k][Band_n][ion_n]     =  tot_ion[wp][point_k][Band_n][ion_n]   +  orb[wp][orb_n][point_k][Band_n][ion_n]
                    soma_orb[wp][orb_n][point_k][Band_n]    =  soma_orb[wp][orb_n][point_k][Band_n]  +  orb[wp][orb_n][point_k][Band_n][ion_n]
                    total[wp][point_k][Band_n]              =  total[wp][point_k][Band_n]            +  orb[wp][orb_n][point_k][Band_n][ion_n]                    

            #----------------------------------------------------------           
            # End of the loop over ions -------------------------------
            #----------------------------------------------------------                 

            #=======================================================================
            # Normalizing the contribution to an individual k-point ================
            #=======================================================================
            
            if ((point_k > point_antes and point_k < point_depois) and (Band_n > Band_antes and Band_n < Band_depois)): 
               for ion_n in range (1, (ni+1)):
                   if (total[wp][point_k][Band_n] != 0.0):
                      tot_ion[wp][point_k][Band_n][ion_n]     =  ( tot_ion[wp][point_k][Band_n][ion_n]/total[wp][point_k][Band_n] )*100
                   for orb_n in range (1, (n_orb+1)):
                       if (total[wp][point_k][Band_n] != 0.0):
                          orb[wp][orb_n][point_k][Band_n][ion_n]  =  ( orb[wp][orb_n][point_k][Band_n][ion_n]/total[wp][point_k][Band_n] )*100

                   if (total[wp][point_k][Band_n] != 0 and lorbit >= 11):
                      #--------------------------------------------------
                      s   = orb[wp][1][point_k][Band_n][ion_n]
                      py  = orb[wp][2][point_k][Band_n][ion_n]
                      pz  = orb[wp][3][point_k][Band_n][ion_n]
                      px  = orb[wp][4][point_k][Band_n][ion_n]
                      p   = px + py + pz
                      dxy = orb[wp][5][point_k][Band_n][ion_n]
                      dyz = orb[wp][6][point_k][Band_n][ion_n]
                      dz2 = orb[wp][7][point_k][Band_n][ion_n]
                      dxz = orb[wp][8][point_k][Band_n][ion_n]
                      dx2 = orb[wp][9][point_k][Band_n][ion_n]
                      d   = dxy + dyz + dz2 + dxz + dx2
                      #--------------------------------------------------
                      contrib_orbitais.write(f'{rotulo[ion_n]:>2}: ion {atomo[ion_n]:<3} | S = {s:5,.2f}% | P = {p:5,.2f}% | D = {d:5,.2f}% | Px = {px:5,.2f}% | Py = {py:5,.2f}% ')
                      contrib_orbitais.write(f'| Pz = {pz:5,.2f}% | Dxy = {dxy:5,.2f}% | Dyz = {dyz:5,.2f}% | Dz2 = {dz2:5,.2f}% | Dxz = {dxz:5,.2f}% | Dx2 = {dx2:5,.2f}% |  \n')                     

                   if (total[wp][point_k][Band_n] != 0 and lorbit == 10):
                      #--------------------------------------------------
                      s = orb[wp][1][point_k][Band_n][ion_n]
                      p = orb[wp][2][point_k][Band_n][ion_n]
                      d = orb[wp][3][point_k][Band_n][ion_n]
                      #--------------------------------------------------
                      contrib_orbitais.write(f'{rotulo[ion_n]:>2}: ion {atomo[ion_n]:<3} | S = {s:5,.2f}% | P = {p:5,.2f}% | D = {d:5,.2f}% | \n')            

               for orb_n in range (1, (n_orb+1)):           
                   if (total[wp][point_k][Band_n] != 0.0):
                      soma_orb[wp][orb_n][point_k][Band_n]  =  ( soma_orb[wp][orb_n][point_k][Band_n]/total[wp][point_k][Band_n] )*100  

               if (lorbit >= 11):
                  #-------------------------------------------------------------- 
                  soma_s   = soma_orb[wp][1][point_k][Band_n]
                  soma_py  = soma_orb[wp][2][point_k][Band_n]
                  soma_pz  = soma_orb[wp][3][point_k][Band_n]
                  soma_px  = soma_orb[wp][4][point_k][Band_n]
                  soma_p   = soma_px + soma_py + soma_pz
                  soma_dxy = soma_orb[wp][5][point_k][Band_n]
                  soma_dyz = soma_orb[wp][6][point_k][Band_n]
                  soma_dz2 = soma_orb[wp][7][point_k][Band_n]
                  soma_dxz = soma_orb[wp][8][point_k][Band_n]
                  soma_dx2 = soma_orb[wp][9][point_k][Band_n]
                  soma_d   = soma_dxy + soma_dyz + soma_dz2 + soma_dxz + soma_dx2
                  #--------------------------------------------------------------               
                  contrib_orbitais.write(f'{linha_2} \n')
                  contrib_orbitais.write(f'Sum:        | S = {soma_s:5,.2f}% | P = {soma_p:5,.2f}% | D = {soma_d:5,.2f}% | Px = {soma_px:5,.2f}% | Py = {soma_py:5,.2f}% ')
                  contrib_orbitais.write(f'| Pz = {soma_pz:5,.2f}% | Dxy = {soma_dxy:5,.2f}% | Dyz = {soma_dyz:5,.2f}% | Dz2 = {soma_dz2:5,.2f}% | Dxz = {soma_dxz:5,.2f}% ')
                  contrib_orbitais.write(f'| Dx2 = {soma_dx2:5,.2f}% |  \n')
 
               if (lorbit == 10):
                  #-------------------------------------------------------------- 
                  soma_s = soma_orb[wp][1][point_k][Band_n]
                  soma_p = soma_orb[wp][2][point_k][Band_n]
                  soma_d = soma_orb[wp][3][point_k][Band_n]
                  #--------------------------------------------------------------                
                  contrib_orbitais.write(f'{linha_1}==== \n')
                  contrib_orbitais.write(f'Sum:        | S = {soma_s:5,.2f}% | P = {soma_p:5,.2f}% | D = {soma_d:5,.2f}% | \n')  

               ##################################################################
               ##################################################################
               ##################################################################               

               for j in range (1,(ni+1)):
                   rotulo_temp[j] = rotulo[j]

               nj = (ni - 1)
                
               for k in range (1,(nj+1)):
                   w = (ni - k)
                   for l in range (1,(w+1)):
                       if (tot_ion[wp][point_k][Band_n][l] < tot_ion[wp][point_k][Band_n][l+1]):
                          tp1 = tot_ion[wp][point_k][Band_n][l]
                          tot_ion[wp][point_k][Band_n][l] = tot_ion[wp][point_k][Band_n][l+1]
                          tot_ion[wp][point_k][Band_n][l+1] = tp1                        
                          #--------------------
                          tp2 = atomo[l]
                          atomo[l] = atomo[l+1]
                          atomo[l+1] = tp2                   
                          #--------------------
                          tp4 = rotulo_temp[l]
                          rotulo_temp[l] = rotulo_temp[l+1]
                          rotulo_temp[l+1] = tp4                          

               for ion_n in range (1,(ni+1)):
                   soma = soma + tot_ion[wp][point_k][Band_n][ion_n]               

                   if (total[wp][point_k][Band_n] != 0):
                      contrib_ions.write(f'{rotulo_temp[ion_n]:>2}: ion {atomo[ion_n]:<3} | Contributiono: {tot_ion[wp][point_k][Band_n][ion_n]:>6,.3f}% | Sum:  {soma:>7,.3f}% | \n')

               if (Band_n < (Band_f+1)):

                  contrib_ions.write(f'{linha_1}====== \n')
                  contrib_ions.write(" \n")

                  if (lorbit >= 11): 
                     contrib_orbitais.write(f'{linha_2} \n')
                  if (lorbit == 10):
                     contrib_orbitais.write(f'{linha_1}==== \n')

                  contrib_orbitais.write(" \n")
                  
        #----------------------------------------------------------
        # End of the loop over bands ------------------------------
        #----------------------------------------------------------      
    #----------------------------------------------------------
    # End of the loop over K-points ---------------------------
    #----------------------------------------------------------    
#----------------------------------------------------------
# End of the PROCAR loop ----------------------------------
#----------------------------------------------------------

#-------------------
contrib_ions.close()
#-----------------------
contrib_orbitais.close()
#-----------------------

#-----------------------------------------------------------------
print(" ")
print("====================== Finished ! =======================")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
