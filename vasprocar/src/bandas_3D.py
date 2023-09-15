# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import numpy as np

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'Bandas_3D' exists --------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Bandas_3D'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Bandas_3D')
#-------------------------------------------

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
print ("######################## 3D Band plot ########################")
print ("##############################################################")
print (" ")

if (escolha == -1):
   print ("##############################################################") 
   print ("with respect to energy, would you like? ======================")
   print ("[0] Use the default energy value from DFT output =============")
   print ("[1] Shift the Fermi level to 0.0 eV  =========================")
   print ("##############################################################")
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")

print ("##############################################################")
print ("Inform the Band interval to be plotted: ===================== ")
print ("--------------------------------------------------------------")
print ("Examples:                                                     ")
print ("Initial_band  Final_band: 5:15                                ")
print ("Initial_band  Final_band: 7:7   or   7*                       ")
print ("##############################################################")
bands_range = input ("Initial_band  Final_band: ")
print (" ")
#------------------------------------------------------------------------------------------
selected_bands = bands_range.replace(':', ' ').replace('-', ' ').replace('*', ' *').split()
#------------------------------------------------------------------------------------------
if (selected_bands[1] == "*"):
   Band_i = int(selected_bands[0])
   Band_f = Band_i
if (selected_bands[1] != "*"):
   Band_i = int(selected_bands[0])
   Band_f = int(selected_bands[1])
#---------------------------------

if (soma_1 == 2 or soma_2 == 2):
   #----------------------------------   
   if (soma_2 == 2 and escolha == -1):
      print ("##############################################################")
      print ("Would you like to choose k-axis units?                        ")
      print ("[1] (kx,ky,kz) 2pi/Param. (Param. in Angs.) ==================")
      print ("[2] (kx,ky,kz) 1/Angs. =======================================")
      print ("[3] (kx,ky,kz) 1/nm.   =======================================")   
   #----------------------------------
   if (soma_1 == 2 and soma_2 == 2 and escolha == -1):    
      print ("[4] (k1,k2,k3) Fractional coord: K = k1*B1 + k2*B2 + k3*B3 ===")    
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
   print("###############################################################")
   print("## Which pre-visualization plot mode would you like to use?  ##")
   print("## [1] Plotly (recommended option) ========================= ##")
   print("## [2] Matplotlib ========================================== ##")
   print("###############################################################")
   pacote = input (" "); pacote = int(pacote)
   if (pacote == 2):
      n_d = 101
   print (" ")

   print ("##############################################################")
   print ("## 3D plot customization  ================================= ##")
   print ("##############################################################")
   print ("## [0] Dotted plot (kpoint mesh grid as in DFT calculation) ##")
   if (pacote == 1): print ("## [1] Surface plot (Interpolation)  ====================== ##")
   if (pacote == 2): print ("## [1] Surface plot (Triangularization method) ============ ##")
   print ("## [2] Dotted plot + Surface plot ========================= ##")  
   print ("##############################################################") 
   tipo_plot = input (" "); tipo_plot = int(tipo_plot)
   print (" ")

   if (pacote == 1 and tipo_plot > 0):
      print ("##############################################################")
      print ("Choose the K-mesh grid (DxD) to be interpolated: =============")
      print ("Note:  The k-mesh grid used in your DFT calculation can be    ")
      print ("       used as a reference. You are free to increase/decrease ")
      print ("       the numberof kpoints to be interpolated.               ")
      print ("Hint:  use 101 (unless more precision is required).           ")
      print ("##############################################################") 
      n_d = input (" "); n_d = int(n_d)  
      print (" ")     

if (escolha == 1):
   esc_fermi = 1
   pacote = 1
   tipo_plot = 1
   n_d = 101

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0    

bands_range = '1:' + str(nb)

#======================================================================
# Obtaining the results from DFT outpout files ========================
#======================================================================
execute_python_file(filename = DFT + '_nscf.py')

#----------------------------------------------------------------------
Band_antes   = (Band_i - 1)               # This bands won't be plotted
Band_depois  = (Band_f + 1)               # This bands won't be plotted
#----------------------------------------------------------------------

#======================================================================
# Saving data to plot the bands =======================================
#======================================================================     

#-------------------------------------------------------------------
inform = open(dir_files + '/output/informacoes.txt', "r")
bandas = open(dir_files + '/output/Bandas.dat', "r") 
bandas_3D = open(dir_files + '/output/Bandas_3D/Bandas_3D.dat', 'w')
#-------------------------------------------------------------------

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
       bandas_3D.write(f'{kx} {ky} {kz} ')   
    if (Dimensao == 4):
       bandas_3D.write(f'{k1} {k2} {k3} ')

    VTemp = bandas.readline().split()
    for j in range (Band_i,(Band_f+1)):
        energ = float(VTemp[j])
        bandas_3D.write(f'{energ} ')
    bandas_3D.write("\n")

#----------------
inform.close()
bandas.close()
bandas_3D.close()
#----------------

os.remove(dir_files + '/output/Bandas.dat')

#-----------------------------------------------------------------------------------------------
# Copy Bandas_3D_matplotlib.py and Bandas_3D_plotly.py to the output folder directory  ---------
#-----------------------------------------------------------------------------------------------

try: f = open(dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py'); f.close(); os.remove(dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py')
except: 0 == 0

try: f = open(dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py'); f.close(); os.remove(dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_bandas_3D_plotly.py'
destination = dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py'
shutil.copyfile(source, destination)

source = main_dir + '/plot/plot_bandas_3D_matplotlib.py'
destination = dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
# Allowing the Plot to be executed separatedly -------------------------------------------------
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

for i in range (2):

    if (i == 0): file = open(dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py', 'r')
    if (i == 1): file = open(dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py', 'r')
    lines = file.readlines()
    file.close()

    if (i == 0): linha = 8
    if (i == 1): linha = 11

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
    linha += 1; lines.insert(linha, f'tipo_plot = {tipo_plot}  # [0] Dotted plot; [1] Surface plot; [2] Dotted + surface \n')   
    linha += 1; lines.insert(linha, f'Dimensao  = {Dimensao}   # [1] (kx,ky,kz) in 2pi/Param.; [2] (kx,ky,kz) in 1/Angs.; [3] (kx,ky,kz) in 1/nm.; [4] (k1,k2,k3) \n')
    linha += 1; lines.insert(linha, f'Plano_k   = {Plano_k}    # [1] kxky or k1k2; [2] kxkz or k1k3; [3] kykz or k2k3  \n')
    linha += 1; lines.insert(linha, f'Band_i    = {Band_i}     # Initial band to be plotted \n')
    linha += 1; lines.insert(linha, f'Band_f    = {Band_f}     # Final band to be plotted \n')
    linha += 1; lines.insert(linha, f'bands_range = "{bands_range}" \n')
    linha += 1; lines.insert(linha, f'Efermi    = {Efermi}     # Fermi energy from DFT outpout files \n')
    linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  # Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
    if (i == 0):
       linha += 1; lines.insert(linha, f'n_d = {n_d}  # Interpolation grid (DxD) \n')      
    if (i == 1):
       if ((sum_save == 0) and (pacote == 1)): save_png = 1
       linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}  # Plotting output format, where [0] = NOT and [1] = YES \n')
    linha += 1; lines.insert(linha, '\n')
    linha += 1; lines.insert(linha, '#===================================================================== \n')

    if (i == 0): file = open(dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py', 'w')
    if (i == 1): file = open(dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py', 'w')
    file.writelines(lines)
    file.close()

#----------------------------------------------------------------------------
if (pacote == 1):
   exec(open(dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py').read())
if (pacote == 2):
   exec(open(dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py').read())
#----------------------------------------------------------------------------

#=======================================================================
   
print(" ")
print("===========================================================")
print("= Edit Plot3D using the following files ===================")
print("= Bandas_3D_matplotlib.py and Bandas_3D_plotly.py generated")
print("= in the folder output/Bandas_3D ==========================")   
print("===========================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Completed =======================")
#-----------------------------------------------------------------
   
#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
