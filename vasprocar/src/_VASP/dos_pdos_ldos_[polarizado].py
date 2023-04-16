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
n_orb = int((len(VTemp) -1)/2)

#-------------
doscar.close()
#-------------

#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("############# Density of States (Polarized Spin) #############")
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
      print ("pDOS Px|Py|Pz:  4 2 3  (Blue, Red, Green)                     ")
      print ("--------------------------------------------------------------") 
      print ("pDOS Dxy|Dyz|Dz2|Dxz|Dx2: 4 2 3 10 9                          ")
      print ("(Blue, Red, Green, Magenta, Cyan)                             ")
      print ("--------------------------------------------------------------")
      if (n_orb == 16): 
         print ("pDOS Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2: 4 2 3 10 9 5 11      ")
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
      print ("Enter in sequence the colors of pdOS S|P|D:                   ")
      cor_orb = input ("Colors_pdOS_S|P|D: ")
      #---------------------
      tcor = cor_orb.split()
      c_S = int(tcor[0]); c_P = int(tcor[1]); c_D = int(tcor[2])
      #---------------------
      print (" ")
      
      if (n_orb >= 9):

         print ("==============================================================") 
         print ("Enter in sequence the colors of pdOS Px|Py|Pz:                ")
         cor_orb = input ("Colors_pdOS_Px|Py|Pz: ")
         #---------------------
         tcor = cor_orb.split()
         c_Px = int(tcor[0]); c_Py = int(tcor[1]); c_Pz = int(tcor[2])
         #---------------------
         print (" ")
         
         print ("==============================================================") 
         print ("Enter in sequence the colors of pDOS Dxy|Dyz|Dz2|Dxz|Dx2:     ")
         cor_orb = input ("Colors_pDOS_Dxy|Dyz|Dz2|Dxz|Dx2: ")
         #---------------------
         tcor = cor_orb.split()
         c_Dxy = int(tcor[0]); c_Dyz = int(tcor[1]); c_Dz2 = int(tcor[2]); c_Dxz = int(tcor[3]); c_Dx2 = int(tcor[4])
         #---------------------
         print (" ")

         if (n_orb == 16):
            print ("=============================================================================") 
            print ("Enter in sequence the colors of pDOS Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2:     ")
            cor_orb = input ("Colors_dos_Orbitais: ")
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

#----------------------------------------
doscar = open(dir_files + '/DOSCAR', "r")
#----------------------------------------

for i in range(6):
    VTemp = doscar.readline().split()

E_max = float(VTemp[0])
E_min = float(VTemp[1])
NEDOS = int(VTemp[2])
Efermi = float(VTemp[3])

#----------------------------------------------------------------------

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0 

#----------------------------------------------------------------------
# Initialization of Variables, Vectors and Matrices -------------------
#----------------------------------------------------------------------

dos_u_tot = [0.0]*(NEDOS+1)  # Total DOS (Up)
dos_d_tot = [0.0]*(NEDOS+1)  # Total DOS (Down)

ldos_u    = [0.0]*(NEDOS+1)  # Local DOS (Up)
ldos_d    = [0.0]*(NEDOS+1)  # Local DOS (Down)

lpdos_u   = [[[0.0]*(NEDOS+1) for i in range(ni+1)] for j in range(n_orb+1)]  # Local and Projected DOS (Up)
lpdos_d   = [[[0.0]*(NEDOS+1) for i in range(ni+1)] for j in range(n_orb+1)]  # Local and Projected DOS (Down)

pdos_u_S_tot = [0.0]*(NEDOS+1)  # Total pdos_S (Up)
pdos_d_S_tot = [0.0]*(NEDOS+1)  # Total pdos_S (Down)
pdos_u_P_tot = [0.0]*(NEDOS+1)  # Total pdos_P (Up)
pdos_d_P_tot = [0.0]*(NEDOS+1)  # Total pdos_P (Down)
pdos_u_D_tot = [0.0]*(NEDOS+1)  # Total pdos_D (Up)
pdos_d_D_tot = [0.0]*(NEDOS+1)  # Total pdos_D (Down)
pdos_u_F_tot = [0.0]*(NEDOS+1)  # Total pdos_F (Up)
pdos_d_F_tot = [0.0]*(NEDOS+1)  # Total pdos_F (Down)

lpdos_u_S    = [0.0]*(NEDOS+1)  # Local pdos_S (Up)
lpdos_d_S    = [0.0]*(NEDOS+1)  # Local pdos_S (Down)
lpdos_u_P    = [0.0]*(NEDOS+1)  # Local pdos_P (Up)
lpdos_d_P    = [0.0]*(NEDOS+1)  # Local pdos_P (Down)
lpdos_u_D    = [0.0]*(NEDOS+1)  # Local pdos_D (Up)
lpdos_d_D    = [0.0]*(NEDOS+1)  # Local pdos_D (Down)
lpdos_u_F    = [0.0]*(NEDOS+1)  # Local pdos_F (Up)
lpdos_d_F    = [0.0]*(NEDOS+1)  # Local pdos_F (Down)

lpdos_u_tot = [[0.0]*(NEDOS+1) for i in range(n_orb+1)]  # Local Total pdos (Up)
lpdos_d_tot = [[0.0]*(NEDOS+1) for i in range(n_orb+1)]  # Local Total pdos (Down)

y_inicial = E_min
y_final   = E_max

x_inicial = 0.0
x_final   = 0.0

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

        for k in range(1,(n_orb+1)):

            if (esc == 0 or (esc == 1 and temp_sn == "sim")):

               lpdos_u[k][i][j] = float(VTemp[(2*k) -1])
               lpdos_d[k][i][j] = float(VTemp[2*k])*(-1)
               
               lpdos_u_tot[k][j] = lpdos_u_tot[k][j] + lpdos_u[k][i][j]
               lpdos_d_tot[k][j] = lpdos_d_tot[k][j] + lpdos_d[k][i][j]

               ldos_u[j] = ldos_u[j] + lpdos_u[k][i][j]
               ldos_d[j] = ldos_d[j] + lpdos_d[k][i][j]

               if (k == 1):
                  lpdos_u_S[j] = lpdos_u_S[j] + lpdos_u[k][i][j]
                  lpdos_d_S[j] = lpdos_d_S[j] + lpdos_d[k][i][j]
           
               if (lorbit == 10 and k == 2):
                  lpdos_u_P[j] = lpdos_u_P[j] + lpdos_u[k][i][j]
                  lpdos_d_P[j] = lpdos_d_P[j] + lpdos_d[k][i][j]
               
               if (lorbit == 10 and k == 3):
                  lpdos_u_D[j] = lpdos_u_D[j] + lpdos_u[k][i][j]
                  lpdos_d_D[j] = lpdos_d_D[j] + lpdos_d[k][i][j]

               if (lorbit == 10 and k == 4):
                  lpdos_u_F[j] = lpdos_u_F[j] + lpdos_u[k][i][j]
                  lpdos_d_F[j] = lpdos_d_F[j] + lpdos_d[k][i][j]
               
               if (lorbit >= 11 and (k == 2 or k == 3 or k == 4)):
                  lpdos_u_P[j] = lpdos_u_P[j] + lpdos_u[k][i][j]
                  lpdos_d_P[j] = lpdos_d_P[j] + lpdos_d[k][i][j]
               
               if (lorbit >= 11 and (k == 5 or k == 6 or k == 7 or k == 8 or k == 9)):
                  lpdos_u_D[j] = lpdos_u_D[j] + lpdos_u[k][i][j]
                  lpdos_d_D[j] = lpdos_d_D[j] + lpdos_d[k][i][j]

               if (lorbit >= 11 and (k == 10 or k == 11 or k == 12 or k == 13 or k == 14 or k == 15 or k == 16)):
                  lpdos_u_F[j] = lpdos_u_F[j] + lpdos_u[k][i][j]
                  lpdos_d_F[j] = lpdos_d_F[j] + lpdos_d[k][i][j]

            dos_u_tot[j] = dos_u_tot[j] + float(VTemp[(2*k) -1])
            dos_d_tot[j] = dos_d_tot[j] + float(VTemp[2*k])*(-1)

            #------------------------------------------------------------
            if (k == 1):
               pdos_u_S_tot[j] = pdos_u_S_tot[j] + float(VTemp[(2*k) -1])
               pdos_d_S_tot[j] = pdos_d_S_tot[j] + float(VTemp[2*k])*(-1)
            #------------------------------------------------------------                
            if (lorbit == 10 and k == 2):
               pdos_u_P_tot[j] = pdos_u_P_tot[j] + float(VTemp[(2*k) -1])
               pdos_d_P_tot[j] = pdos_d_P_tot[j] + float(VTemp[2*k])*(-1)
            #------------------------------------------------------------                
            if (lorbit == 10 and k == 3):
               pdos_u_D_tot[j] = pdos_u_D_tot[j] + float(VTemp[(2*k) -1])
               pdos_d_D_tot[j] = pdos_d_D_tot[j] + float(VTemp[2*k])*(-1)
            #------------------------------------------------------------                
            if (lorbit == 10 and k == 4):
               pdos_u_F_tot[j] = pdos_u_F_tot[j] + float(VTemp[(2*k) -1])
               pdos_d_F_tot[j] = pdos_d_F_tot[j] + float(VTemp[2*k])*(-1)
            #------------------------------------------------------------                
            if (lorbit >= 11 and (k == 2 or k == 3 or k == 4)):
               pdos_u_P_tot[j] = pdos_u_P_tot[j] + float(VTemp[(2*k) -1])
               pdos_d_P_tot[j] = pdos_d_P_tot[j] + float(VTemp[2*k])*(-1)
            #------------------------------------------------------------                
            if (lorbit >= 11 and (k == 5 or k == 6 or k == 7 or k == 8 or k == 9)):
               pdos_u_D_tot[j] = pdos_u_D_tot[j] + float(VTemp[(2*k) -1])
               pdos_d_D_tot[j] = pdos_d_D_tot[j] + float(VTemp[2*k])*(-1)
            #------------------------------------------------------------                
            if (lorbit >= 11 and (k == 10 or k == 11 or k == 12 or k == 13 or k == 14 or k == 15 or k == 16)):
               pdos_u_F_tot[j] = pdos_u_F_tot[j] + float(VTemp[(2*k) -1])
               pdos_d_F_tot[j] = pdos_d_F_tot[j] + float(VTemp[2*k])*(-1)
            #------------------------------------------------------------

        if (dos_u_tot[j] >= x_final):   x_final   = dos_u_tot[j]
        if (dos_d_tot[j] <= x_inicial): x_inicial = dos_d_tot[j] 
               
#-------------
doscar.close()
#-------------

#====================================================================================
# Saving data to plot the DOS, pDOS e lDOS (Up Component) ===========================
#====================================================================================

#------------------------------------------------------------------------
dos_pdos_ldos = open(dir_files + '/output/DOS/DOS_pDOS_lDOS_up.dat', 'w')
#------------------------------------------------------------------------

for k in range (1,(NEDOS+1)):
    #--------------------------------------------------------------------------------
    if (esc == 0):
       dos_pdos_ldos.write(f'{energia[k]} {dos_u_tot[k]} 0.0')
       dos_pdos_ldos.write(f' {pdos_u_S_tot[k]} 0.0 {pdos_u_P_tot[k]} 0.0 {pdos_u_D_tot[k]} 0.0 {pdos_u_F_tot[k]} 0.0')
    if (esc == 1):
       dos_pdos_ldos.write(f'{energia[k]} {dos_u_tot[k]} {ldos_u[k]}')
       dos_pdos_ldos.write(f' {pdos_u_S_tot[k]} {lpdos_u_S[k]} {pdos_u_P_tot[k]} {lpdos_u_P[k]} {pdos_u_D_tot[k]} {lpdos_u_D[k]} {pdos_u_F_tot[k]} {lpdos_u_F[k]}')
    if (n_orb >= 9):
       dos_pdos_ldos.write(f' {lpdos_u_tot[4][k]} {lpdos_u_tot[2][k]} {lpdos_u_tot[3][k]}')
       dos_pdos_ldos.write(f' {lpdos_u_tot[5][k]} {lpdos_u_tot[6][k]} {lpdos_u_tot[7][k]} {lpdos_u_tot[8][k]} {lpdos_u_tot[9][k]}')
       if (n_orb == 16):
          dos_pdos_ldos.write(f' {lpdos_u_tot[10][k]} {lpdos_u_tot[11][k]} {lpdos_u_tot[12][k]} {lpdos_u_tot[13][k]} {lpdos_u_tot[14][k]} {lpdos_u_tot[15][k]} {lpdos_u_tot[16][k]}')
    dos_pdos_ldos.write(f' \n')       

#--------------------
dos_pdos_ldos.close()
#--------------------

#====================================================================================
# Saving data to plot the DOS, pDOS e lDOS (Down Component) =========================
#====================================================================================

#--------------------------------------------------------------------------
dos_pdos_ldos = open(dir_files + '/output/DOS/DOS_pDOS_lDOS_down.dat', 'w')
#--------------------------------------------------------------------------s

for k in range (1,(NEDOS+1)):
    #--------------------------------------------------------------------------------
    if (esc == 0):
       dos_pdos_ldos.write(f'{energia[k]} {dos_d_tot[k]} 0.0')
       dos_pdos_ldos.write(f' {pdos_d_S_tot[k]} 0.0 {pdos_d_P_tot[k]} 0.0 {pdos_d_D_tot[k]} 0.0 {pdos_d_F_tot[k]} 0.0')
    if (esc == 1):
       dos_pdos_ldos.write(f'{energia[k]} {dos_d_tot[k]} {ldos_d[k]}')
       dos_pdos_ldos.write(f' {pdos_d_S_tot[k]} {lpdos_d_S[k]} {pdos_d_P_tot[k]} {lpdos_d_P[k]} {pdos_d_D_tot[k]} {lpdos_d_D[k]} {pdos_d_F_tot[k]} {lpdos_d_F[k]}')
    if (lorbit > 10):
       dos_pdos_ldos.write(f' {lpdos_d_tot[4][k]} {lpdos_d_tot[2][k]} {lpdos_d_tot[3][k]}')
       dos_pdos_ldos.write(f' {lpdos_d_tot[5][k]} {lpdos_d_tot[6][k]} {lpdos_d_tot[7][k]} {lpdos_d_tot[8][k]} {lpdos_d_tot[9][k]}')
       if (n_orb == 16): 
          dos_pdos_ldos.write(f' {lpdos_d_tot[10][k]} {lpdos_d_tot[11][k]} {lpdos_d_tot[12][k]} {lpdos_d_tot[13][k]} {lpdos_d_tot[14][k]} {lpdos_d_tot[15][k]} {lpdos_d_tot[16][k]}')
    dos_pdos_ldos.write(f' \n')        

#--------------------
dos_pdos_ldos.close()
#--------------------

"""
#====================================================================================
#====================================================================================
# DOS, pDOS e lDOS Plot using (GRACE) ===============================================
#==================================================================================== 
#====================================================================================

if (save_agr == 1):

   print(" ")
   print ("============== Plotting DOS, pDOS, lDOS (Grace): ==============")
   
   execute_python_file(filename = 'plot/Grace/plot_dos_pdos_ldos_[polarizado].py')  
   execute_python_file(filename = 'plot/Grace/plot_dos_pdos_ldos_[polarizado_delta].py')

   print ("DOS, pDOS, lDOS plot via Grace (.agr files) completed ---------")
"""

#====================================================================================
#====================================================================================
# DOS, pDOS e lDOS Plot using (Matplotlib) ==========================================
#====================================================================================
#====================================================================================

#------------------------------------------------------------------------
# Copy DOS_pDOS_lDOS.py to the output folder directory ------------------
#------------------------------------------------------------------------

try: f = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py'); f.close(); os.remove(dir_files + '/output/DOS/DOS_pDOS_lDOS.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_dos_pdos_ldos_[polarizado].py'
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
linha += 1; lines.insert(linha, '# Color code:                                                        \n')
linha += 1; lines.insert(linha, '# 0  White  | 1  Black  | 2  Red    | 3  Green    | 4  Blue    | 5 Yellow \n')
linha += 1; lines.insert(linha, '# 6  Borwn  | 7  Grey   | 8  Violet | 9  Cyan     | 10 Magenta |          \n')
linha += 1; lines.insert(linha, '# 11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa | 15 Green   |          \n')
linha += 1; lines.insert(linha, '#------------------------------------------------------------------------ \n')
linha += 1; lines.insert(linha, '# Colors applied to DOS|lDOS|pDOS:                                        \n')
linha += 1; lines.insert(linha, f'c_DOS = {c_DOS}; c_lDOS = {c_lDOS}; c_S = {c_S}; c_P = {c_P}; c_D = {c_D} \n')
if (lorbit >= 11):
   linha += 1; lines.insert(linha, f'c_Px = {c_Px}; c_Py = {c_Py}; c_Pz = {c_Pz} \n')
   linha += 1; lines.insert(linha, f'c_Dxy = {c_Dxy}; c_Dyz = {c_Dyz}; c_Dz2 = {c_Dz2}; c_Dxz = {c_Dxz}; c_Dx2 = {c_Dx2} \n')    
   if (n_orb == 16):
      linha += 1; lines.insert(linha, f'c_Fyx2 = {c_Fyx2}; c_Fxyz = {c_Fxyz}; c_Fyz2 = {c_Fyz2}; c_Fzz2 = {c_Fzz2}; c_Fxz2 = {c_Fxz2}; c_Fzx2 = {c_Fzx2}; c_Fxx2 = {c_Fxx2} \n')
linha += 1; lines.insert(linha, '#======================================================================== \n')

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
