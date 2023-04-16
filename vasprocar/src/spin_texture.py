# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import numpy as np

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'Spin_Texture' exists -----------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Spin_Texture'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Spin_Texture')
#----------------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#======================================================================
# Analyzing the variation of the coordinates of the K-points ==========
#======================================================================
execute_python_file(filename = DFT + '_var_kpoints.py')

soma_1 = dk[0] + dk[1] + dk[2]
soma_2 = dk[3] + dk[4] + dk[5]

#======================================================================
# Get the input from user =============================================
#======================================================================
 
print ("##############################################################")
print ("What do you want to analyze regarding Spin's texture proj.? ##")
print ("## -------------------------------------------------------- ##")
print ("## [1] 2D projection of the SiSj vector and the Sx|Sy|Sz    ##")
print ("##     components on the kikj plane of ZB                   ##")
print ("## [2] 3D projection of the SxSySz vector and the Sx|Sy|Sz  ##")
print ("##     components on the grid [ki, kj, E(eV)]               ##") 
print ("## [3] 3D projection of the SxSySz vector and the Sx|Sy|Sz  ##")
print ("##     components on the grid [kx,ky,kz] or [k1,k2,k3]      ##")
print ("## [4] Isosurfaces of the Sx|Sy|Sz components in the grid   ##")
print ("##     [kx,ky,kz] or [k1,k2,k3]                             ##")
print ("##############################################################") 
escolha_d = input (" "); escolha_d = int(escolha_d)  
print (" ")

if (escolha_d < 0): escolha_d = (escolha_d**2)**0.5

if (escolha_d <= 2): number = 2
if (escolha_d > 2):  number = 3
   
if (soma_1 != number and soma_2 != number):
   print ("============================================================")
   print ("!!! ERROR !!!                                               ")
   print ("============================================================")
   if (escolha_d <= 2):
      print ("The calculation performed does not correspond to a 2D plan  ")
      print ("in the BZ. kikj-plan (i,j = x,y,z or i,j = 1,2,3)           ")
   if (escolha_d > 2):
      print ("The calculation performed does not correspond to a GRID 3D  ")
      print ("in the BZ (GRID kxkykz or k1k2k3)                           ")
   print ("------------------------------------------------------------")
   print ("Please, use the option [665] to get the correct KPOINTS file")
   print ("============================================================")
   confirmation = input (" ")
   exit()   

print ("##############################################################")
print ("Which band do you want to analyze? ===========================")
print ("##############################################################") 
n_band = input (" "); n_band = int(n_band)
print (" ")

if (escolha == -1):
   
   if (escolha_d == 2):
      print ("##############################################################") 
      print ("with respect to energy, would you like? ======================")
      print ("[0] Use the default energy value from DFT output =============")
      print ("[1] Shift the Fermi level to 0.0 eV  =========================")
      print ("##############################################################")
      esc_fermi = input (" "); esc_fermi = int(esc_fermi)
      print (" ")

   if (escolha_d != 2):
      esc_fermi = 1  
   
   print ("##############################################################")
   print ("What do you want to Plot/Analyze? ============================")
   print ("[0] to analyze all ions in the lattice =======================")
   print ("[1] to analyze selected ions =================================")
   print ("##############################################################")
   esc_ions = input (" "); esc_ions = int(esc_ions)
   print(" ")

   if (esc_ions == 1):

      #-------------------------
      sim_nao = ["nao"]*(ni + 1)  
      #-------------------------

      print ("################################################################")
      print ("Choose the intervals_of_ions to be analyzed: ===================")
      print ("Type as in the examples below ==================================")
      print ("----------------------------------------------------------------")
      print ("The order in which the ions are added does not change the result")
      print ("----------------------------------------------------------------")
      print ("intervals_of_ions  1:5 3:9 11* 15:27                            ")          
      print ("intervals_of_ions  7:49 50:53                                   ")
      print ("intervals_of_ions  3* 9* 15:17                                  ")
      print ("################################################################")
      ion_range = input ("intervals_of_ions  ")
      print (" ")
      #----------------------------------------------------------------------------------------
      selected_ions = ion_range.replace(':', ' ').replace('-', ' ').replace('*', ' *').split( )
      loop = int(len(selected_ions)/2)
      #----------------------------------------------------------------------------------------
      
      for i in range (1,(loop+1)):
          #------------------------------------------------------
          loop_i = int(selected_ions[(i-1)*2])
          if (selected_ions[((i-1)*2) +1] == "*"):
             selected_ions[((i-1)*2) +1] = selected_ions[(i-1)*2]
          loop_f = int(selected_ions[((i-1)*2) +1])
          #----------------------------------------------------------------------------------------
          if ((loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0) or (loop_i > loop_f)):
             print (" ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("ERROR: The informed ion values are incorrect %%%%%%%%%%%%%")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             confirmation = input (" ")
             exit()
          #----------------------------------------------------------------------           
          for j in range(loop_i, (loop_f + 1)):
              sim_nao[j] = "sim" 

if (escolha == -1 and escolha_d == 4): 
   print ("##############################################################")
   print ("How many isosurfaces would you like to plot? =================")
   print ("Hint: use 15 (unless more precision is required) =============")
   print ("##############################################################") 
   n_iso = input (" "); n_iso = int(n_iso)
   print (" ")

#-----------------------------------------------------------------------------

if (soma_1 == number or soma_2 == number):
   #----------------------------------   
   if (soma_2 == number and escolha == -1):
      print ("##############################################################")
      print ("Would you like to choose k-axis units?                        ")
      print ("[1] (kx,ky,kz) 2pi/Param. (Param. in Angs.) ==================")
      print ("[2] (kx,ky,kz) 1/Angs. =======================================")
      print ("[3] (kx,ky,kz) 1/nm.   =======================================")  
   #----------------------------------
   if (soma_1 == number and soma_2 == number and escolha == -1):    
      print ("[4] (k1,k2,k3) Fractional coord: K = k1*B1 + k2*B2 + k3*B3 ===")
   #----------------------------------
   if (soma_2 == number and escolha == -1): 
      print ("##############################################################") 
      Dimensao = input (" "); Dimensao = int(Dimensao)
      print (" ")
   #----------------------------------
   if (soma_2 != number):
      Dimensao = 4
   #----------------------------------   
   if (soma_1 != number and escolha == 1):
      Dimensao = 1
   #----------------------------------   
   if (soma_1 == number and soma_2 == number and escolha == 1):
      Dimensao = 4
   #----------------------------------

   if (escolha_d <= 2):   
      #----------------------------------
      if (Dimensao < 4):
         if (dk[3] == 1 and dk[4] == 1): Plano_k = 1  #  kxky-plan
         if (dk[3] == 1 and dk[5] == 1): Plano_k = 2  #  kxkz-plan
         if (dk[4] == 1 and dk[5] == 1): Plano_k = 3  #  kykz-plan
   
      if (Dimensao == 4):
         if (dk[0] == 1 and dk[1] == 1): Plano_k = 1  #  k1k2-plan
         if (dk[0] == 1 and dk[2] == 1): Plano_k = 2  #  k1k3-plan
         if (dk[1] == 1 and dk[2] == 1): Plano_k = 3  #  k2k3-plan   

#-----------------------------------------------------------------------------   

if (escolha == -1):

   if (escolha_d == 1):
      print ("##############################################################")  
      print ("Enter [0] if you want to keep the density of Spin vectors.    ")
      print ("==============================================================")
      print ("If you want to reduce the density, enter an integer > 0, -----")
      print ("corresponding to the number of skipped Spin vectors ----------")
      print ("interspersed along the ZB plane. -----------------------------") 
      print ("##############################################################") 
      pulo = input (" "); pulo = int(pulo)  
      print (" ")
      #----------------------
      if (pulo < 0): pulo = 0

      print ("##############################################################")  
      print ("To keep the length of Spin vectors, Enter 1.0                 ")
      print ("To increase the length, Enter a Positive value > 1.0          ")
      print ("To decrease the length, enter a Negative value < -1.0         ")
      print ("==============================================================")
      print ("These values correspond to how many times the length of the   ") 
      print ("array will be multiplied (increased) or divided (decreased).  ")
      print ("##############################################################")    
      fator = input (" "); fator = float(fator)  
      print (" ")    
   
   if (escolha_d == 2):     
      print ("##############################################################")
      print ("Choose the K-mesh grid (DxD) to be interpolated: =============")
      print ("Note:  The k-mesh grid used in your DFT calculation can be    ")
      print ("       used as a reference. You are free to increase/decrease ")
      print ("       the numberof kpoints to be interpolated.               ")
      print ("Hint:  use 101 (unless more precision is required).           ")
      print ("##############################################################")
      n_d = input (" "); n_d = int(n_d)  
      print (" ")
      
   if (escolha_d == 4):
      
      print ("##############################################################")
      print ("Choose the K-mesh grid (DxDxD) to be interpolated: ===========")
      print ("Note:  The k-mesh grid used in your DFT calculation can be    ")
      print ("       used as a reference you are free to increase/decrease  ")
      print ("       the number of kpoints to be interpolated               ")
      print ("Hint:  use 31 (unless more precision is required)             ")
      print ("##############################################################") 
      n_d = input (" "); n_d = int(n_d)  
      print (" ")     

if (escolha == 1):
   esc_fermi = 1   
   esc_ions = 0
   Dimensao = 1
   #-------------------
   if (escolha_d == 1):   
      pulo = 0
      fator = 1.0
   if (escolha_d == 2):
      n_d = 101
   if (escolha_d == 4):
      n_d = 31; n_iso = 15

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0       

bands_range = '1:' + str(nb)

#======================================================================
# Obtaining the results from DFT outpout files ========================
#======================================================================
read_spin = 1
execute_python_file(filename = DFT + '_nscf.py')   

#======================================================================
# Saving data to plot the Spin Texture ================================
#======================================================================

bandas = np.loadtxt(dir_files + '/output/Bandas.dat') 
bandas.shape

energia = bandas[:,n_band]

#----------------------------------------------------------------------------
inform = open(dir_files + '/output/informacoes.txt', "r")
spin = open(dir_files + '/output/Spin.dat', "r")
spin_texture = open(dir_files + '/output/Spin_Texture/Spin_Texture.dat', 'w')
#----------------------------------------------------------------------------

palavra = 'k-points |'                          

for line in inform:   
    if palavra in line: 
       break

VTemp = inform.readline()
VTemp = inform.readline()
       
for i in range (n_procar*nk):
    VTemp = inform.readline().split()
    k1 = float(VTemp[1]); k2 = float(VTemp[2]); k3 = float(VTemp[3])
    kx = float(VTemp[4]); ky = float(VTemp[5]); kz = float(VTemp[6])

    for j in range (1,(nb+1)):
        VTemp = spin.readline().split()
        if (j == n_band):
           Sx = float(VTemp[2]) + float(VTemp[3])
           Sy = float(VTemp[4]) + float(VTemp[5])
           Sz = float(VTemp[6]) + float(VTemp[7])

    if (Dimensao != 4):
       spin_texture .write(f'{kx} {ky} {kz} {energia[i]} {Sx} {Sy} {Sz} \n')      
    if (Dimensao == 4):
       spin_texture .write(f'{k1} {k2} {k3} {energia[i]} {Sx} {Sy} {Sz} \n')

#-------------------
inform.close()
spin.close()
spin_texture.close()
#-------------------

os.remove(dir_files + '/output/Bandas.dat')
os.remove(dir_files + '/output/Spin.dat')

#======================================================================
# Copy Spin_Texture_?D.py to the output folder directory ==============
#======================================================================

if (escolha_d == 1):
   name = '2D'
   
if (escolha_d == 2):
   name = '3D'
   
if (escolha_d == 3):
   name = '4D'
   
if (escolha_d == 4):
   name = '4D_[iso]'

try: f = open(dir_files + '/output/Spin_Texture/Spin_Texture_' + name + '.py'); f.close(); os.remove(dir_files + '/output/Spin_Texture/Spin_Texture_' + name + '.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_spin_texture_' + name + '.py'
destination = dir_files + '/output/Spin_Texture/Spin_Texture_' + name + '.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/Spin_Texture/Spin_Texture_' + name + '.py', 'r')
lines = file.readlines()
file.close()

if (escolha_d == 1):
   linha = 12
if (escolha_d == 2):
   linha = 7
if (escolha_d == 3):
   linha = 7
if (escolha_d == 4):
   linha = 7

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, f'# {VASProcar_name} Copyright (C) 2023 \n')
linha += 1; lines.insert(linha, f'# GNU GPL-3.0 license \n')
linha += 1; lines.insert(linha, f'# {url_1} \n')
linha += 1; lines.insert(linha, f'# {url_2} \n')
linha += 1; lines.insert(linha, f'# {url_3} \n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, '# Authors:                                                             \n')
linha += 1; lines.insert(linha, '# ==================================================================== \n')
linha += 1; lines.insert(linha, '# Augusto de Lelis Araujo                                              \n')
linha += 1; lines.insert(linha, '# [2022-2023] CNPEM|Ilum|LNNano (Campinas-SP/Brazil)                   \n')
linha += 1; lines.insert(linha, '# [2007-2022] Federal University of Uberlandia (Uberlândia-MG/Brazil)  \n')
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
if (escolha_d == 1):
   linha += 1; lines.insert(linha, f'fator = {fator}  #  Factor by which the length of the spin vectors will be increased or decreased \n')   
   linha += 1; lines.insert(linha, f'pulo = {pulo}    #  Number of spin vectors to be ignored interleaved in the ZB plane \n')
linha += 1; lines.insert(linha, f'bands_range = "{bands_range}" \n')
if (escolha_d == 2): 
   linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout files \n')
   linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
   linha += 1; lines.insert(linha, f'n_d = {n_d}              #  Interpolation grid (DxD) \n') 
if (escolha_d == 4):
   linha += 1; lines.insert(linha, f'n_d = {n_d}          #  Interpolation grid (DxDxD) \n') 
   linha += 1; lines.insert(linha, f'n_iso = {n_iso}      #  Number of isosurfaces in the plot \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}   #  [1] (kx,ky,kz) in 2pi/Param.; [2] (kx,ky,kz) in 1/Angs.; [3] (kx,ky,kz) in 1/nm.; [4] (k1,k2,k3) \n')
if (escolha_d < 3):
   linha += 1; lines.insert(linha, f'Plano_k = {Plano_k}  #  [1] kxky or k1k2; [2] kxkz or k1k3; [3] kykz or k2k3  \n')
if (escolha_d != 4):
   linha += 1; lines.insert(linha, f'nk = {nk}  #  Total Number of k-points \n')
if (escolha_d == 1):
   if (sum_save == 0): save_png = 1 
   linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}  #  Plotting output format, where [0] = NOT and [1] = YES \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Spin_Texture/Spin_Texture_' + name + '.py', 'w')
file.writelines(lines)
file.close()

#--------------------------------------------------------------------------------
if (escolha_d == 1):
   exec(open(dir_files + '/output/Spin_Texture/Spin_Texture_2D.py').read())
   
if (escolha_d == 2):
   exec(open(dir_files + '/output/Spin_Texture/Spin_Texture_3D.py').read())
   
if (escolha_d == 3):
   exec(open(dir_files + '/output/Spin_Texture/Spin_Texture_4D.py').read())
   
if (escolha_d == 4):
   exec(open(dir_files + '/output/Spin_Texture/Spin_Texture_4D_[iso].py').read())
#--------------------------------------------------------------------------------

#=======================================================================  

print(" ")

if (escolha_d == 1):
   print("=====================================================================")
   print("= Edit the generated vectors, modifying the value of the variables ==")
   print("= [factor], [thickness] and [length] in the Spin_Texture_2D.py file =")
   print("= generated in the output/Spin_Texture folder. ======================")   
   print("=====================================================================")

if (escolha_d == 2):
   print("===========================================================")
   print("= Edit the generated vectors, modifying the value of the ==")
   print("= [sizeref] variable in the Spin_Texture_3D.py file =======")
   print("= generated in the output/Spin_Texture folder. ============")   
   print("===========================================================") 

if (escolha_d == 3):
   print("===========================================================")
   print("= Edit the generated vectors, modifying the value of the ==")
   print("= [sizeref] variable in the Spin_Texture_4D.py file =======")
   print("= generated in the output/Spin_Texture folder. ============")   
   print("===========================================================")

if (escolha_d == 4):
   print("===============================================================")
   print("= Edit the generated vectors, modifying the value of the ======")
   print("= [sizeref] variable in the Spin_Texture_4D_[iso].py file =====")
   print("= generated in the output/Spin_Texture folder. ================")   
   print("===============================================================")
   
#-----------------------------------------------------------------
print(" ")
print("======================= Completed =======================")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
