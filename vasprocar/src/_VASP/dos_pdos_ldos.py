# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'DOS' exists --------------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/DOS'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/DOS')
#-------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#======================================================================
# Getting the number of orbitals present in the DOSCAR file ===========
#======================================================================

#----------------------------------------
doscar = open(dir_files + '/DOSCAR', "r")
#----------------------------------------

for i in range(5):
    VTemp = doscar.readline()

VTemp = doscar.readline().split()

E_max  = float(VTemp[0])
E_min  = float(VTemp[1])
NEDOS  = int(VTemp[2])
Efermi = float(VTemp[3])

energia = [0]*(NEDOS+1)  # Energia

for i in range (1,(NEDOS+1)):
      VTemp = doscar.readline().split()
      energia[i] = float(VTemp[0])

VTemp = doscar.readline()

VTemp = doscar.readline().split()
if (float(VTemp[0]) == energia[1]):
   n_columns = len(VTemp) -1

VTemp = doscar.readline().split()
if (float(VTemp[0]) != energia[2]):
   n_columns += len(VTemp)

#-------------
doscar.close()
#-------------


#------------------------------------------------------------------
if (lorbit == 10 and (n_columns == 3 or n_columns == 4) ):
   n_orb = int(n_columns)
if (lorbit >= 11 and (n_columns == 9 or n_columns == 16) ):
   n_orb = int(n_columns)
#------------------------------------------------------------------
if (lorbit == 10 and (n_columns == (4*3) or n_columns == (4*4)) ):
   n_orb = int(n_columns/4)
if (lorbit >= 11 and (n_columns == (4*9) or n_columns == (4*16)) ):
   n_orb = int(n_columns/4)
#------------------------------------------------------------------


#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("##################### Density of States: #####################")
print ("##############################################################") 
print (" ")

if (escolha == -1):

   print ("##############################################################") 
   print ("Do you want to change the DOS|lDOS|pDOS color default?        ")
   print ("[0] NOT                                                       ")
   print ("[1] YES                                                       ")
   print ("##############################################################") 
   esc_color = input (" "); esc_color = int(esc_color)
   print (" ")  

   if (esc_color == 1):

      print ("##############################################################")
      print ("Color code:                                                   ")
      print ("0  White   | 1  Black | 2  Red    | 3  Green  | 4  Blue       ")
      print ("5  Yellow  | 6  Borwn | 7  Grey   | 8  Violet | 9  Cyan       ")
      print ("10 Magenta |11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa   ")
      print ("15 Dark_Green                                                 ")
      print ("##############################################################")       
      print ("VASProcar color pattern:                                      ")
      print ("                                                              ")
      print ("total_DOS|lDOS:  7 13  (Grey, Maroon)                         ")
      print ("--------------------------------------------------------------") 
      print ("pdOS S|P|D|F:  4 2 3 10 (Blue, Red, Green, Magenta)           ")
      print ("--------------------------------------------------------------")      
      print ("pdOS Px|Py|Pz: 4 2 3    (Blue, Red, Green)                    ")
      print ("--------------------------------------------------------------") 
      print ("pdOS Dxy|Dyz|Dz2|Dxz|Dx2: 4 2 3 10 9                          ")
      print ("(Blue, Red, Green, Magenta, Cyan)                             ")
      print ("--------------------------------------------------------------")
      if (n_orb == 16): 
         print ("pdOS Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2: 4 2 3 10 9 5 11      ")
         print ("(Blue, Red, Green, Magenta, Cyan, Yellow, Orange)             ")
      print ("##############################################################") 
      print (" ")

      print ("==============================================================") 
      print ("Enter in sequence the colors of total_DOS and lDOS:           ")
      cor_orb = input ("Colors_DOS|lDOS: ")
      #---------------------
      tcor = cor_orb.split()
      c_DOS = int(tcor[0]); c_lDOS = int(tcor[1])
      #---------------------
      print (" ")

      print ("==============================================================") 
      print ("Type in sequence the colors of pDOS S|P|D|F:                  ")
      cor_orb = input ("Colors_of_Orbitals: ")
      #---------------------
      tcor = cor_orb.split()
      c_S = int(tcor[0]); c_P = int(tcor[1]); c_D = int(tcor[2]); c_F = int(tcor[3])
      #---------------------
      print (" ")
      
      if (n_orb >= 9):

         print ("==============================================================") 
         print ("Type in sequence the colors of pDOS Px|Py|Pzs                 ")
         cor_orb = input ("Colors_of_Orbitals: ")
         #---------------------
         tcor = cor_orb.split()
         c_Px = int(tcor[0]); c_Py = int(tcor[1]); c_Pz = int(tcor[2])
         #---------------------
         print (" ")
         
         print ("==============================================================") 
         print ("Type in sequence the colors of pDOS Dxy|Dyz|Dz2|Dxz|Dx2:      ")
         cor_orb = input ("Colors_of_Orbitals: ")
         #---------------------
         tcor = cor_orb.split()
         c_Dxy = int(tcor[0]); c_Dyz = int(tcor[1]); c_Dz2 = int(tcor[2]); c_Dxz = int(tcor[3]); c_Dx2 = int(tcor[4])
         #---------------------
         print (" ")

         if (n_orb == 16):
            print ("=============================================================================") 
            print ("Type in sequence the colors of pDOS Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2:      ")
            cor_orb = input ("Colors_of_Orbitals: ")
            #---------------------
            tcor = cor_orb.split()
            c_Fyx2 = int(tcor[0]); c_Fxyz = int(tcor[1]); c_Fyz2 = int(tcor[2]); c_Fzz2 = int(tcor[3])
            c_Fxz2 = int(tcor[4]); c_Fzx2 = int(tcor[5]); c_Fxx2 = int(tcor[6])
            #---------------------
            print (" ")   

   print ("##############################################################") 
   print ("with respect to energy, would you like? ======================")
   print ("[0] Use the default energy value from DFT output =============")
   print ("[1] Shift the Fermi level to 0.0 eV  =========================")
   print ("##############################################################")
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")    

   print ("##############################################################")
   print ("What do you want to Plot/Analyze? ============================")
   print ("[0] to analyze all ions in the lattice =======================")
   print ("[1] to analyze selected ions =================================")
   print ("##############################################################")
   esc = input (" "); esc = int(esc)
   print(" ")

   if (esc == 1):

      #-------------------------
      sim_nao = ["nao"]*(ni + 1)
      #-------------------------

      print ("##############################################################")
      print ("Choose the ranges of ions to be analyzed: =================== ")
      print ("Type as in the examples below =============================== ")
      print ("--------------------------------------------------------------")
      print ("The order in which ions are added does not change the result. ")
      print ("--------------------------------------------------------------")
      print ("ranges_of_ions: 1:5 7:7 11* 15:27                             ")          
      print ("ranges_of_ions: 7:49 50:53                                    ")
      print ("ranges_of_ions: 3* 8* 16:21                                   ")
      print ("##############################################################")
      ion_range = input ("ranges_of_ions: ")
      print (" ")
      #---------------------------------------------------------------------------------------
      selected_ions = ion_range.replace(':', ' ').replace('-', ' ').replace('*', ' *').split()
      loop = int(len(selected_ions)/2)
      #---------------------------------------------------------------------------------------
      
      for i in range (1,(loop+1)):
          #------------------------------------------------------
          loop_i = int(selected_ions[(i-1)*2])
          if (selected_ions[((i-1)*2) +1] == "*"):
             selected_ions[((i-1)*2) +1] = selected_ions[(i-1)*2]
          loop_f = int(selected_ions[((i-1)*2) +1])
          #----------------------------------------------------------------------
          if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
             print (" ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("ERROR: The informed ion values are incorrect %%%%%%%%%%%%%")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             confirmation = input (" ")
             exit()
          #----------------------------------------------------------------------           
          for j in range(loop_i, (loop_f + 1)):
              sim_nao[j] = "sim"  

      print (" ")

if (escolha == 1):
   esc_fermi = 1  
   esc = 0 

#----------------------------------------------------------------------
# Obtaining the results from DOSCAR -----------------------------------
#----------------------------------------------------------------------

# Initialization of Variables, Vectors and Matrices -------------------

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0 

#----------------------------------------------------------------------

dos_tot = [0.0]*(NEDOS+1)  # Total DOS

ldos    = [0.0]*(NEDOS+1)  # Local DOS

lpdos   = [[[0.0]*(NEDOS+1) for i in range(ni+1)] for j in range(n_orb+1)]  # Local and Projected DOS

pdos_S_tot = [0.0]*(NEDOS+1)  # Total pdos_S 
pdos_P_tot = [0.0]*(NEDOS+1)  # Total pdos_P
pdos_D_tot = [0.0]*(NEDOS+1)  # Total pdos_D
pdos_F_tot = [0.0]*(NEDOS+1)  # Total pdos_F

lpdos_S    = [0.0]*(NEDOS+1)  # Local pdos_S
lpdos_P    = [0.0]*(NEDOS+1)  # Local pdos_P
lpdos_D    = [0.0]*(NEDOS+1)  # Local pdos_D
lpdos_F    = [0.0]*(NEDOS+1)  # Local pdos_F

lpdos_tot = [[0.0]*(NEDOS+1) for i in range(n_orb+1)]  # Local Total-pdos

y_inicial = E_min
y_final   = E_max

x_inicial = +1000.0
x_final   = -1000.0

#-------------------------------------------------------------------------------------------------

#----------------------------------------
doscar = open(dir_files + '/DOSCAR', "r")
#----------------------------------------

for i in range(6):
    VTemp = doscar.readline()

for i in range (1,(NEDOS+1)):
    VTemp = doscar.readline()
      
for i in range (1,(ni+1)):
    if (esc == 1): temp_sn = sim_nao[i]
    #------------------------
    VTemp = doscar.readline()
    #----------------------------
    for j in range (1,(NEDOS+1)):

        VTemp = doscar.readline()
        #-----------------------------------------------------
        for k in range(10):
            VTemp = VTemp.replace(str(k) + '-', str(k) + 'E-')
            VTemp = VTemp.replace(str(k) + '+', str(k) + 'E+')
        VTemp = VTemp.split()    
        #-----------------------------------------------------

        if (len(VTemp) != (n_columns +1)):

           OTemp = [0.0]*(n_columns +1)

           for l in range (len(VTemp)):
               OTemp[l] = VTemp[l]

           ncTemp = len(VTemp)

           VTemp = doscar.readline()
           #-----------------------------------------------------
           for k in range(10):
               VTemp = VTemp.replace(str(k) + '-', str(k) + 'E-')
               VTemp = VTemp.replace(str(k) + '+', str(k) + 'E+')
           VTemp = VTemp.split()    
           #-----------------------------------------------------

           for l in range (len(VTemp)):
               OTemp[ncTemp +l] = VTemp[l]

           VTemp = OTemp

        for k in range(1,(n_orb+1)):

            #---------------------------------------------------------
            if (lorbit == 10 and (n_columns == 3 or n_columns == 4) ):
               passo = k
            if (lorbit >= 11 and (n_columns == 9 or n_columns == 16) ):
               passo = k
            #------------------------------------------------------------------
            if (lorbit == 10 and (n_columns == (4*3) or n_columns == (4*4)) ):
               passo = ((4*k) -3)
            if (lorbit >= 11 and (n_columns == (4*9) or n_columns == (4*16)) ):
               passo = ((4*k) -3)
            #------------------------------------------------------------------

            if (esc == 0 or (esc == 1 and temp_sn == "sim")):

               lpdos[k][i][j] = float(VTemp[passo])            
               lpdos_tot[k][j] = lpdos_tot[k][j] + lpdos[k][i][j]
               ldos[j] = ldos[j] + lpdos[k][i][j]

               #------------------------------------------ 
               if (k == 1):
                  lpdos_S[j] = lpdos_S[j] + lpdos[k][i][j]
               #------------------------------------------   
               if (lorbit == 10 and k == 2):
                  lpdos_P[j] = lpdos_P[j] + lpdos[k][i][j]
               #------------------------------------------                   
               if (lorbit == 10 and k == 3):
                  lpdos_D[j] = lpdos_D[j] + lpdos[k][i][j]
               #------------------------------------------                   
               if (lorbit == 10 and k == 4):
                  lpdos_F[j] = lpdos_F[j] + lpdos[k][i][j]
               #------------------------------------------                   
               if (lorbit >= 11 and (k == 2 or k == 3 or k == 4)):
                  lpdos_P[j] = lpdos_P[j] + lpdos[k][i][j]
               #------------------------------------------                   
               if (lorbit >= 11 and (k == 5 or k == 6 or k == 7 or k == 8 or k == 9)):
                  lpdos_D[j] = lpdos_D[j] + lpdos[k][i][j]           
               #------------------------------------------                   
               if (lorbit >= 11 and (k == 10 or k == 11 or k == 12 or k == 13 or k == 14 or k == 15 or k == 16)):
                  lpdos_F[j] = lpdos_F[j] + lpdos[k][i][j]
               #------------------------------------------ 
           
            dos_tot[j] = dos_tot[j] + float(VTemp[passo])                      

            #----------------------------------------------------- 
            if (k == 1):
               pdos_S_tot[j] = pdos_S_tot[j] + float(VTemp[passo])
            #-----------------------------------------------------                
            if (lorbit == 10 and k == 2):
               pdos_P_tot[j] = pdos_P_tot[j] + float(VTemp[passo])
            #-----------------------------------------------------                
            if (lorbit == 10 and k == 3):
               pdos_D_tot[j] = pdos_D_tot[j] + float(VTemp[passo])
            #-----------------------------------------------------                
            if (lorbit == 10 and k == 4):
               pdos_F_tot[j] = pdos_F_tot[j] + float(VTemp[passo])
            #-----------------------------------------------------                
            if (lorbit >= 11 and (k == 2 or k == 3 or k == 4)):
               pdos_P_tot[j] = pdos_P_tot[j] + float(VTemp[passo])
            #-----------------------------------------------------                
            if (lorbit >= 11 and (k == 5 or k == 6 or k == 7 or k == 8 or k == 9)):
               pdos_D_tot[j] = pdos_D_tot[j] + float(VTemp[passo])           
            #-----------------------------------------------------                
            if (lorbit >= 11 and (k == 10 or k == 11 or k == 12 or k == 13 or k == 14 or k == 15 or k == 16)):
               pdos_F_tot[j] = pdos_F_tot[j] + float(VTemp[passo]) 
            #----------------------------------------------------- 

        if (dos_tot[j] <= x_inicial): x_inicial = dos_tot[j]
        if (dos_tot[j] >= x_final):   x_final   = dos_tot[j]         
               
#-------------
doscar.close()
#-------------

#======================================================================
# Saving data to plot the DOS, pDOS e lDOS ============================
#======================================================================

#---------------------------------------------------------------------
dos_pdos_ldos = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.dat', 'w')
#---------------------------------------------------------------------

for k in range (1,(NEDOS+1)):
    #------------------------
    if (esc == 0):
       dos_pdos_ldos.write(f'{energia[k]} {dos_tot[k]} 0.0')
       dos_pdos_ldos.write(f' {pdos_S_tot[k]} 0.0 {pdos_P_tot[k]} 0.0 {pdos_D_tot[k]} 0.0 {pdos_F_tot[k]} 0.0')
    if (esc == 1):
       dos_pdos_ldos.write(f'{energia[k]} {dos_tot[k]} {ldos[k]}')
       dos_pdos_ldos.write(f' {pdos_S_tot[k]} {lpdos_S[k]} {pdos_P_tot[k]} {lpdos_P[k]} {pdos_D_tot[k]} {lpdos_D[k]} {pdos_F_tot[k]} {lpdos_F[k]}')
    if (n_orb >= 9):
       dos_pdos_ldos.write(f' {lpdos_tot[4][k]} {lpdos_tot[2][k]} {lpdos_tot[3][k]}')
       dos_pdos_ldos.write(f' {lpdos_tot[5][k]} {lpdos_tot[6][k]} {lpdos_tot[7][k]} {lpdos_tot[8][k]} {lpdos_tot[9][k]}')
       if (n_orb == 16):
          dos_pdos_ldos.write(f' {lpdos_tot[10][k]} {lpdos_tot[11][k]} {lpdos_tot[12][k]} {lpdos_tot[13][k]} {lpdos_tot[14][k]} {lpdos_tot[15][k]} {lpdos_tot[16][k]}')
    dos_pdos_ldos.write(f' \n')       

#--------------------
dos_pdos_ldos.close()
#--------------------

#========================================================================
#========================================================================
# DOS, pDOS e lDOS Plot using (GRACE) ===================================
#======================================================================== 
#========================================================================

if (save_agr == 1):

   print(" ")
   print ("============== Plotting DOS, pDOS, lDOS (Grace): ==============")
   
   execute_python_file(filename = 'plot/Grace/plot_dos_pdos_ldos.py')
   
   print ("DOS, pDOS, lDOS plot via Grace (.agr files) completed ---------")

#========================================================================
#========================================================================
# DOS, pDOS e lDOS Plot using (Matplotlib) ==============================
#========================================================================
#========================================================================

#------------------------------------------------------------------------
# Copy DOS_pDOS_lDOS.py to the output folder directory ------------------
#------------------------------------------------------------------------

try: f = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py'); f.close(); os.remove(dir_files + '/output/DOS/DOS_pDOS_lDOS.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_dos_pdos_ldos.py'
destination = dir_files + '/output/DOS/DOS_pDOS_lDOS.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py', 'r')
lines = file.readlines()
file.close()

linha = 4

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, f'# {VASProcar_name} \n')
linha += 1; lines.insert(linha, f'# {url_1} \n')
linha += 1; lines.insert(linha, f'# {url_2} \n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, '# Authors:                                                             \n')
linha += 1; lines.insert(linha, '# ==================================================================== \n')
linha += 1; lines.insert(linha, '# Augusto de Lelis Araujo                                              \n')
linha += 1; lines.insert(linha, '# Federal University of Uberlandia (Uberlândia/MG - Brazil)            \n')
linha += 1; lines.insert(linha, '# e-mail: augusto-lelis@outlook.com                                    \n')
linha += 1; lines.insert(linha, '# ==================================================================== \n')
linha += 1; lines.insert(linha, '# Renan da Paixao Maciel                                               \n')
linha += 1; lines.insert(linha, '# Uppsala University (Uppsala/Sweden)                                  \n')
linha += 1; lines.insert(linha, '# e-mail: renan.maciel@physics.uu.se                                   \n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, '\n')

linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# These are the parameters that allows the code to run separatedly === \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}; nk  = {nk}; x_inicial = {x_inicial}; x_final = {x_final}; energ_min = {y_inicial}; energ_max = {y_final}; lorbit = {lorbit}; n_orb = {n_orb}; esc = {esc} \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout file \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')

if (sum_save == 0): save_png = 1
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}  #  Plotting output format, onde [0] = NOT e [1] = YES \n')                       
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#======================================================================== \n')
linha += 1; lines.insert(linha, '# Color code:                                                             \n')
linha += 1; lines.insert(linha, '# 0  White  | 1  Black  | 2  Red    | 3  Green    | 4  Blue    | 5 Yellow \n')
linha += 1; lines.insert(linha, '# 6  Borwn  | 7  Grey   | 8  Violet | 9  Cyan     | 10 Magenta |          \n')
linha += 1; lines.insert(linha, '# 11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa | 15 Green   |          \n')
linha += 1; lines.insert(linha, '#------------------------------------------------------------------------ \n')
linha += 1; lines.insert(linha, '# Colors applied to DOS|lDOS|pDOS:                                        \n')
linha += 1; lines.insert(linha, f'c_DOS = {c_DOS}; c_lDOS = {c_lDOS}; c_S = {c_S}; c_P = {c_P}; c_D = {c_D}; c_F = {c_F} \n')
if (lorbit >= 11):
   linha += 1; lines.insert(linha, f'c_Px = {c_Px}; c_Py = {c_Py}; c_Pz = {c_Pz} \n')
   linha += 1; lines.insert(linha, f'c_Dxy = {c_Dxy}; c_Dyz = {c_Dyz}; c_Dz2 = {c_Dz2}; c_Dxz = {c_Dxz}; c_Dx2 = {c_Dx2} \n')
   if (n_orb == 16):
      linha += 1; lines.insert(linha, f'c_Fyx2 = {c_Fyx2}; c_Fxyz = {c_Fxyz}; c_Fyz2 = {c_Fyz2}; c_Fzz2 = {c_Fzz2}; c_Fxz2 = {c_Fxz2}; c_Fzx2 = {c_Fzx2}; c_Fxx2 = {c_Fxx2} \n')     
linha += 1; lines.insert(linha, '#=================================================================================== \n')

file = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py', 'w')
file.writelines(lines)
file.close()

#---------------------------------------------------------------
if (sum_save != 0):
   exec(open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py').read())
#---------------------------------------------------------------

#=======================================================================

print(" ")
print("================================================================")
print("= Edit the DOS Plot through the DOS_pDOS_lDOS.py or .agr =======")
print("= (via Grace) files generated in the output/DOS folder =========")   
print("================================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Completed =======================")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
