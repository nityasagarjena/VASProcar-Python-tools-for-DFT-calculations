# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import numpy as np

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#----------------------------------------------------------------------
# Check if "Plot_4D" folder exists ------------------------------------
#----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Plot_4D'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Plot_4D')
#-----------------------------------------

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

if (soma_1 != 3 and soma_2 != 3):
   print ("============================================================")
   print ("!!! ERROR !!!                                               ")
   print ("============================================================")
   print ("The calculation performed does not correspond to a GRID 3D  ")
   print ("in the BZ (GRID kxkykz or k1k2k3)                           ")
   print ("------------------------------------------------------------")
   print ("Please, use the option [665] to get the correct KPOINTS file")
   print ("============================================================")
   confirmation = input (" ")
   exit()

#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("###################### ISOSURFACE PLOT: ######################")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("What to do? ==================================================")
print ("[1] 3D energy dispersion of a specific band  =================")
print ("[2] Energy gap between two selected bands ====================")
print ("##############################################################") 
esc = input (" "); esc = int(esc)
print (" ")

if (esc == 1):
   print ("##############################################################")
   print ("Choose the band to be analyzed: ==============================")
   print ("##############################################################")
   n_band = input (" "); n_band = int(n_band)
   print (" ")
   #---------------------
   Band_1 = 0; Band_2 = 0
   #---------------------

   if (escolha == -1):
      print ("##############################################################") 
      print ("with respect to energy, would you like? ======================")
      print ("[0] Use the default energy value from DFT output =============")
      print ("[1] Shift the Fermi level to 0.0 eV  =========================")
      print ("##############################################################")
      esc_fermi = input (" "); esc_fermi = int(esc_fermi)
      print (" ")  

if (esc == 2):
   print ("##############################################################")
   print ("Inform the Band interval to be plotted: ===================== ")
   print ("--------------------------------------------------------------")
   print ("Examples:                                                     ")
   print ("Band_1 Band_2: 5:15                                           ")
   print ("Band_1 Band_2: 7:7   or   7*                                  ")
   print ("--------------------------------------------------------------")
   print ("##############################################################") 
   bands_range = input ("Band_1 Band_2: ")
   print (" ")
   #------------------------------------------------------------------------------------------
   selected_bands = bands_range.replace(':', ' ').replace('-', ' ').replace('*', ' *').split()
   #------------------------------------------------------------------------------------------
   if (selected_bands[1] == "*"):
      Band_1 = int(selected_bands[0])
      Band_2 = Band_1
   if (selected_bands[1] != "*"):
      Band_1 = int(selected_bands[0])
      Band_2 = int(selected_bands[1])
   #---------------------------------
   n_band = 0
   #---------

   if (escolha == -1):
      esc_fermi = 0  

#-----------------------------------------------------------------------------   

if (soma_1 == 3 or soma_2 == 3):
   #----------------------------------   
   if (soma_2 == 3 and escolha == -1):
      print ("##############################################################")
      print ("Would you like to choose k-axis units?                        ")
      print ("[1] (kx,ky,kz) 2pi/Param. (Param. in Angs.) ==================")
      print ("[2] (kx,ky,kz) 1/Angs. =======================================")
      print ("[3] (kx,ky,kz) 1/nm.   =======================================")     
   #----------------------------------
   if (soma_1 == 3 and soma_2 == 3 and escolha == -1):    
      print ("[4] (k1,k2,k3) Fractional coord: K = k1*B1 + k2*B2 + k3*B3 ===")  
   #----------------------------------
   if (soma_2 == 3 and escolha == -1): 
      print ("##############################################################") 
      Dimensao = input (" "); Dimensao = int(Dimensao)
      print (" ")
   #----------------------------------
   if (soma_2 != 3):
      Dimensao = 4
   #----------------------------------   
   if (soma_1 != 3 and escolha == 1):
      Dimensao = 1
   #----------------------------------   
   if (soma_1 == 3 and soma_2 == 3 and escolha == 1):
      Dimensao = 4

#-----------------------------------------------------------------------------       

if (escolha == -1):
   
   print ("##############################################################")
   print ("How many isosurfaces would you like to plot? =================")
   print ("Hint: use 15 (unless more precision is required) =============")
   print ("##############################################################") 
   n_iso = input (" "); n_iso = int(n_iso)
   print (" ")

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
   Dimensao = 4
   n_iso = 15
   n_d = 31

bands_range = '1:' + str(nb)

#----------------------------------------------------------------------
# Obtaining the results from DFT outpout files ------------------------
#----------------------------------------------------------------------
execute_python_file(filename = DFT + '_nscf.py')

#----------------------------
if (esc_fermi == 0):
   dE_fermi = 0.0
   dest_fermi = Efermi

if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1)
   dest_fermi = 0.0

#======================================================================
# Saving data to plot the bands =======================================
#====================================================================== 

#------------------------------------------------------------
inform = open(dir_files + '/output/informacoes.txt', "r")
bandas = open(dir_files + '/output/Bandas.dat', "r") 
plot4D = open(dir_files + '/output/Plot_4D/Plot_4d.dat', 'w')
#------------------------------------------------------------

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

    if (Dimensao < 4):
       plot4D.write(f'{kx} {ky} {kz} ')   
    if (Dimensao == 4):
       plot4D.write(f'{k1} {k2} {k3} ')

    VTemp = bandas.readline().split()

    if (esc == 1): 
       energ = float(VTemp[n_band])

    if (esc == 2): 
       energ = float(VTemp[Band_2]) - float(VTemp[Band_1])
       energ = (energ**2)**0.5 

    plot4D.write(f'{energ} \n')

#-------------
inform.close()
bandas.close()
plot4D.close()
#-------------

os.remove(dir_files + '/output/Bandas.dat')

#----------------------------------------------------------------------
# Copy Plot_4D.py to the output folder directory  ---------------------
#----------------------------------------------------------------------

try: f = open(dir_files + '/output/Plot_4D/Plot_4D.py'); f.close(); os.remove(dir_files + '/output/Plot_4D/Plot_4D.py')
except: 0 == 0
  
source = main_dir + '/plot/plot_bandas_4D_plotly.py'
destination = dir_files + '/output/Plot_4D/Plot_4D.py'
shutil.copyfile(source, destination)

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# Allowing the Plot to be executed separatedly -----------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

file = open(dir_files + '/output/Plot_4D/Plot_4D.py', 'r')
lines = file.readlines()
file.close()

linha = 8

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
linha += 1; lines.insert(linha, f'n_iso = {n_iso}    # Number of isosurfaces \n')
linha += 1; lines.insert(linha, f'n_d = {n_d}        # Interpolation grid (DxDxD) \n')
linha += 1; lines.insert(linha, f'Band = {n_band}    # The chosen band \n')
linha += 1; lines.insert(linha, f'Band_1 = {Band_1}  # 1nd band of the intervale \n')
linha += 1; lines.insert(linha, f'Band_2 = {Band_2}  # 2nd band of the intervale \n')
linha += 1; lines.insert(linha, f'bands_range = "{bands_range}" \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}        # Fermi energy from DFT outpout files \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  # Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
linha += 1; lines.insert(linha, f'Dimensao  = {Dimensao}      # [1] (kx,ky,kz) in 2pi/Param.; [2] (kx,ky,kz) in 1/Angs.; [3] (kx,ky,kz) in 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'esc = {esc}                 # Choose how much energy of the states (do not modify) \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Plot_4D/Plot_4D.py', 'w')
file.writelines(lines)
file.close()

#----------------------------------------------------------
exec(open(dir_files + '/output/Plot_4D/Plot_4D.py').read())
#----------------------------------------------------------

#=======================================================================

print(" ")
print("=========================================================")
print("= Edit Plot4D through the Plot_4D.py file generated in ==")
print("= the output/Plot_4D folder =============================")   
print("=========================================================")  

#-----------------------------------------------------------------
print(" ")
print("======================= Completed =======================")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
