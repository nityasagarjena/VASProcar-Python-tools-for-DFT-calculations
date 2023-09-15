# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import numpy as np

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'Orbital_Texture' exists ---------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Orbital_Texture'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Orbital_Texture')
#------------------------------------------------- 

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

if (soma_1 != 2 and soma_2 != 2):
   print ("============================================================")
   print ("!!! ERROR !!!                                               ")
   print ("============================================================")
   print ("The calculation performed does not correspond to a 2D plan  ")
   print ("in the BZ. kikj-plan (i,j = x,y,z or i,j = 1,2,3)           ")
   print ("------------------------------------------------------------")
   print ("Please, use the option [665] to get the correct KPOINTS file")
   print ("============================================================")
   confirmation = input (" ")
   exit()

#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("#################### Orbital Texture Plot ####################")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("Which band do you want to analyze? ===========================")
print ("##############################################################") 
n_band = input (" "); n_band = int(n_band)
print (" ")

print ("##############################################################")
print ("Enter the number of Orbital intensity contours ===============")
print ("##############################################################")
n_contour = input (" "); n_contour = int(n_contour)
if (n_contour <= 0): n_contour = 1
print(" ")

print ("##############################################################")
print ("Enter the number of Energy contours ==========================")
print ("##############################################################")
n_contour_energ = input (" "); n_contour_energ = int(n_contour_energ)
if (n_contour_energ <= 0): n_contour_energ = 0
print(" ")

tipo_contour = 0

if (escolha == -1):

   print ("##############################################################")
   print ("What do you want to analyze? =================================")
   print ("[0] Analyze all ions in the lattice ==========================")
   print ("[1] Analyze selected Ions ====================================")
   print ("##############################################################")
   esc_ions = input (" "); esc_ions = int(esc_ions)
   print(" ")

   if (esc_ions == 1):
      
      #-------------------------
      sim_nao = ["nao"]*(ni + 1)  #  sim_nao vector initialization
      #-------------------------

      if (len(inputs) == 0):
         print ("################################################################")
         print ("Choose the ions_ranges to be analyzed: ======================== ")
         print ("Type as in the examples below ================================= ")
         print ("----------------------------------------------------------------")
         print ("The order in which the ions are added does not change the result")
         print ("----------------------------------------------------------------")
         print ("ions_ranges  1:5 3:9 11* 15:27                                  ")
         print ("ions_ranges  7:49 50:53                                         ")
         print ("ions_ranges  1* 3* 6:9                                          ")
         print ("################################################################")
         ion_range = input ("ions_ranges  ")
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

#-----------------------------------------------------------------------------

if (soma_1 == 2 or soma_2 == 2):
   #----------------------------------   
   if (soma_2 == 2 and escolha == -1):
      print ("##############################################################")
      print (" Would you like to choose k-axis units?                       ")
      print (" [1] (kx,ky,kz) 2pi/Param. (Param. in Angs.) =================")
      print (" [2] (kx,ky,kz) 1/Angs. ======================================")
      print (" [3] (kx,ky,kz) 1/nm.   ======================================")   
   #----------------------------------
   if (soma_1 == 2 and soma_2 == 2 and escolha == -1):    
      print (" [4] (k1,k2,k3) Fractional coord: K = k1*B1 + k2*B2 + k3*B3 ==")   
   #----------------------------------
   if (soma_2 == 2 and escolha == -1): 
      print ("##############################################################") 
      Dimensao = input (" "); Dimensao = int(Dimensao)
      print (" ")
   #----------------------------------
   if (soma_2 != 2):
      Dimensao = 4
   #----------------------------------   
   if (soma_1 != 2 and escolha == 1):
      Dimensao = 1
   #----------------------------------   
   if (soma_1 == 2 and soma_2 == 2 and escolha == 1):
      Dimensao = 4
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

   print ("##############################################################")
   print ("Choose the K-mesh grid (DxD) to be interpolated: =============")
   print ("Note:  The k-mesh grid used in your VASP calculation can be   ")
   print ("       used as a reference. You are free to increase/decrease ")
   print ("       the numberof kpoints to be interpolated.               ")
   print ("Hint:  use 101 (unless more precision is required).           ")
   print ("##############################################################")  
   n_d = input (" "); n_d = int(n_d)  
   print (" ")

   print ("##############################################################")
   print ("Enter the transparency value [0.0 to 1.0] to be applied to the")
   print ("gradient of the Orbital Contours, the lower|higher the value, ")
   print ("the more smoother|intense the colors will be                  ")
   print ("##############################################################")
   transp = input (" "); transp = float(transp)
   print(" ")

esc_fermi = 1

if (escolha == 1):
   esc_ions = 0
   esc_fermi = 1
   n_d = 101
   transp = 1.0

esc_fermi = 1

if (esc_fermi == 0): dE_fermi = 0.0
if (esc_fermi == 1): dE_fermi = (Efermi)*(-1)   

bands_range = '1:' + str(nb)

#======================================================================
# Obtaining the results from DFT outpout files ========================
#======================================================================
read_orb = 1
execute_python_file(filename = DFT + '_nscf.py')  

#======================================================================
# Saving data to plot the Orbital Countour ============================
#======================================================================       

bandas = np.loadtxt(dir_files + '/output/Bandas.dat') 
bandas.shape

#------------------------------------------------------------------------------
inform = open(dir_files + '/output/informacoes.txt', "r")
countour = open(dir_files + '/output/Orbital_Texture/Orbital_Texture.dat', 'w')
orbitais = open(dir_files + '/output/Orbitais.dat', "r") 
#------------------------------------------------------------------------------

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

    if (Dimensao != 4):
       countour.write(f'{kx} {ky} {kz} ')   
    if (Dimensao == 4):
       countour.write(f'{k1} {k2} {k3} ')

    for j in range (1,(nb+1)):
        VTemp = orbitais.readline().split()
        if (j == n_band):
           #--------------------
           energia = bandas[:,j]
           countour.write(f'{energia[i]} ')
           #-------------------------------
           for k in range(len(VTemp)-2):
              orb = float(VTemp[k+2])
              countour.write(f'{orb} ')
           countour.write(f' \n')

#---------------
inform.close()
orbitais.close()
countour.close()
#---------------

os.remove(dir_files + '/output/Bandas.dat')
os.remove(dir_files + '/output/Orbitais.dat')

#--------------------------------------------------------------------------------------
# Copy Orbital_Texture.py to the output folder directory  ------------------------------
#--------------------------------------------------------------------------------------

try: f = open(dir_files + '/output/Orbital_Texture/Orbital_Texture.py'); f.close(); os.remove(dir_files + '/output/Orbital_Texture/Orbital_Texture.py')
except: 0 == 0
 
source = main_dir + '/plot/plot_orbital_texture.py'
destination = dir_files + '/output/Orbital_Texture/Orbital_Texture.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
# Allowing the Plot to be executed separatedly -------------------------------------------------
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

file = open(dir_files + '/output/Orbital_Texture/Orbital_Texture.py', 'r')
lines = file.readlines()
file.close()

linha = 11

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
linha += 1; lines.insert(linha, f'Dimensao  = {Dimensao}  #  [1] (kx,ky,kz) in 2pi/Param.; [2] (kx,ky,kz) in 1/Angs.; [3] (kx,ky,kz) in 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'Plano_k   = {Plano_k}   #  [1] kxky or k1k2; [2] kxkz or k1k3; [3] kykz or k2k3  \n')
linha += 1; lines.insert(linha, f'Banda = {n_band}         #  Band to be analyzed \n')
linha += 1; lines.insert(linha, f'bands_range = "{bands_range}" \n')
linha += 1; lines.insert(linha, f'n_d = {n_d}             #  Interpolation grid (DxD) \n')
linha += 1; lines.insert(linha, f'transp = {transp}       #  Transparency applied to the color gradient of the contours 2D plot \n')
linha += 1; lines.insert(linha, f'tipo_contour = {tipo_contour}  #  How to obtain the energies of the Orbital Curves: Where [0] is automatic; [1] energy range and [2] entered manually \n')
linha += 1; lines.insert(linha, f'n_contour = {n_contour}              #  Number of Orbital intensity contours \n')
linha += 1; lines.insert(linha, f'n_contour_energ = {n_contour_energ}  #  Number of Energy contours \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}              #  Fermi energy from DFT outpout files \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}        #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')

if (sum_save == 0): save_png = 1
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}  #  Plotting output format, where [0] = NOT and [1] = YES \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Orbital_Texture/Orbital_Texture.py', 'w')
file.writelines(lines)
file.close()

#--------------------------------------------------------------------------
exec(open(dir_files + '/output/Orbital_Texture/Orbital_Texture.py').read())
#--------------------------------------------------------------------------

#=======================================================================
   
print(" ")
print("=========================================================")
print("= Edit the Plots through the Orbital_Texture.py file ====")
print("= generated in the output/Orbital_Texture folder ========")   
print("=========================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Completed =======================")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
