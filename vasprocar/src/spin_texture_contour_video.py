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

#-----------------------------------------------------------------------
# Check whether the folder 'figures' exists ----------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Spin_Texture/figures'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Spin_Texture/figures')
#------------------------------------------------------  

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
   confirmacao = input (" ")
   exit()

#======================================================================
# Getting the input parameters ========================================
#======================================================================

print ("##############################################################")
print ("## Which Spin component or vector should be analyzed? ===== ##")
print ("##############################################################")
print ("## [1] Sx     [2] Sy     [3] Sz =========================== ##")
print ("## [4] SxSy   [5] SxSz   [6] SySz ========================= ##")
print ("##############################################################") 
tipo_spin = input (" "); tipo_spin = int(tipo_spin)
print (" ")

print ("##############################################################")
print ("Which band do you want to analyze? ===========================")
print ("##############################################################") 
n_band = input (" "); n_band = int(n_band)
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
print ("What is the number of Level Contours you want to obtain? =====")
print ("##############################################################")
n_contour = input (" "); n_contour = int(n_contour)
print(" ")

if (n_contour <= 0):
   n_contour = 1

print ("##############################################################")
print ("Regarding the energies of the Level Contours: ================")
print ("[0] Must be obtained automatically by code ===================")
print ("[1] Must sweep a certain range of energy =====================")
print ("[2] I want to specify each energy value manually =============")
print ("##############################################################")
tipo_contour = input (" "); tipo_contour = int(tipo_contour)
print(" ")

if (tipo_contour == 1):
   print ("##############################################################")
   print ("Choose the Energy range to be analyzed: ===================== ")
   print ("Type as in the examples below =============================== ")
   print ("--------------------------------------------------------------")
   print ("Initial_energ Final_Energ: -4.5 6.9                           ")
   print ("Initial_energ Final_Energ:  0.0 5.5                           ")
   print ("##############################################################")
   print (" ")
   energ_i, energ_f = input ("Initial_energ Final_Energ: ").split()
   energ_i = float(energ_i)
   energ_f = float(energ_f)
   print (" ")

if (tipo_contour == 2):
   #-------------------------
   levels_n = [0.0]*n_contour
   #-------------------------
   print ("##############################################################")
   print ("Enter Energy values as in the examples below ================ ")
   print ("--------------------------------------------------------------")
   print ("Energies: -4.5 -2.0 -1.0  0.0  1.0  3.0 5.0                   ")
   print ("Energies:  0.2  0.5  0.78 1.23 9.97                           ")
   print ("--------------------------------------------------------------")
   print ("!!! important note !!! ====================================== ")
   print ("Always enter energy values in ascending order =============== ")
   print ("##############################################################") 
   print (" ")
   levels_n = input ("Energies: ").split()
   for i in range(n_contour):
       levels_n[i] = float(levels_n[i])
   print (" ") 

#--------------------------------------------------------------------------   

if (escolha == -1):

   print ("##############################################################")
   print ("What do you want to analyze? =================================")
   print ("[0] Analyze all ions in the lattice ==========================")
   print ("[1] Analyze selected Ions ====================================")
   print ("##############################################################")
   esc_ions = input (" "); esc_ions = int(esc_ions)
   print (" ")

   if (esc_ions == 1):

      #-------------------------
      sim_nao = ["nao"]*(ni + 1)
      #-------------------------

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
             confirmacao = input (" ")
             exit()
          #----------------------------------------------------------------------           
          for j in range(loop_i, (loop_f + 1)):
              sim_nao[j] = "sim"  

#-----------------------------------------------------------------------------

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

print ("##############################################################")
print ("How many figures should appear per second (fps) in the video? ")
print ("tip 1: =======================================================")
print ("Choose between 1 and 30 figures ==============================")
print ("tip 2: =======================================================")
print ("The greater the number of images and the greater the number of")
print ("images per second (fps), the smoother the video.              ")
print ("##############################################################")
n_fig = input (" "); n_fig = int(n_fig)  
print (" ")
#-------------------------
if (n_fig <= 0): n_fig = 1
#-------------------------   
save_png = 1
save_pdf = 0
save_eps = 0
save_svg = 0

#-----------------------------------------------------------------------------

if (escolha == -1):  

   print ("##############################################################")
   print ("Choose the K-mesh grid (DxD) to be interpolated: =============")
   print ("Note:  The k-mesh grid used in your DFT calculation can be    ")
   print ("       used as a reference. You are free to increase/decrease ")
   print ("       the numberof kpoints to be interpolated.               ")
   print ("Hint:  use 101 (unless more precision is required).           ")
   print ("##############################################################")
   n_d = input (" "); n_d = int(n_d)  
   print (" ")

   print ("##############################################################")
   print ("Enter [0] if you want to keep the density of Spin vectors.    ")
   print ("==============================================================")
   print ("If you want to reduce the density, enter an integer > 0, -----")
   print ("corresponding to the number of skipped Spin vectors ----------")
   print ("interspersed along the path of the band contour. -------------")
   print ("##############################################################")
   pulo = input (" "); pulo = int(pulo)  
   print (" ")
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

   print ("##############################################################")
   print ("Enter the transparency value [0.0 to 1.0] to be applied to the")
   print ("Spin vectors, the lower the value the smoother the colors will")
   print ("be, the higher the more intense they will be. ----------------")
   print ("##############################################################")
   transp = input (" "); transp = float(transp)
   print(" ")

if (escolha == 1):
   esc_fermi = 1
   esc_ions = 0
   n_d = 101
   pulo = 0
   fator = 1.0
   transp = 1.0

if (esc_fermi == 0): dE_fermi = 0.0
if (esc_fermi == 1): dE_fermi = (Efermi)*(-1)   

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
# Copy Spin_Texture_Video.py to the output folder directory ===========
#======================================================================

try: f = open(dir_files + '/output/Spin_Texture/Spin_Texture_Video.py'); f.close(); os.remove(dir_files + '/output/Spin_Texture/Spin_Texture_Video.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_spin_texture_contour_video.py'
destination = dir_files + '/output/Spin_Texture/Spin_Texture_Video.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/Spin_Texture/Spin_Texture_Video.py', 'r')
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
linha += 1; lines.insert(linha, f'nk = {nk}        #  Total Num. of k-points \n')
linha += 1; lines.insert(linha, f'Banda = {n_band}  #  Band being analyzed \n')
linha += 1; lines.insert(linha, f'fator = {fator}  #  Factor by which the length of the spin vectors will be increased or decreased \n')
linha += 1; lines.insert(linha, f'pulo = {pulo}    #  Number of spin vectors to be ignored interleaved along the path of the band contour \n')
linha += 1; lines.insert(linha, f'n_d = {n_d}      #  Interpolation grid (DxD) \n') 
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}  #  [1] (kx,ky,kz) 2pi/Param.; [2] (kx,ky,kz)  1/Angs.; [3] (kx,ky,kz) 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'Plano_k = {Plano_k}    #  [1] kxky or k1k2; [2] kxkz or k1k3; [3] kykz or k2k3  \n')
linha += 1; lines.insert(linha, f'transp = {transp}      #  Transparency applied to the color gradient of the contours 2D plot \n')
linha += 1; lines.insert(linha, f'tipo_spin = {tipo_spin}        #  Component or Spin Vector to be analyzed, where: [1] Sx; [2] Sy; [3] Sz; [4] SxSy; [5] SxSz; [6] SySz \n')
linha += 1; lines.insert(linha, f'tipo_contour = {tipo_contour}  #  How to obtain the energies of the Level Curves: Where [0] is automatic; [1] energy range and [2] entered manually \n')
linha += 1; lines.insert(linha, f'n_contour = {n_contour}        #  Number of Level Contours to be obtained \n')
linha += 1; lines.insert(linha, f'bands_range = "{bands_range}" \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout files \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
#--------------------------------
if (tipo_contour == 1):
   linha += 1; lines.insert(linha, f'energ_i = {energ_i}; energ_f = {energ_f}  #  Starting and ending energy of the Energy Range in the Level Contours plot \n')
if (tipo_contour == 2):
   linha += 1; lines.insert(linha, f'levels_n = {levels_n}  #  Energy values specified manually in the plot of Level Contours \n')
if (tipo_contour < 2):
   linha += 1; lines.insert(linha, f'levels_n = [0.0, 0.0, 0.0, 0.0, 0.0]  #  Values of the Level Contours specified manually \n')
#--------------------------------
linha += 1; lines.insert(linha, f'n_fig = {n_fig}  #  Number of figures that appear in the video per second (fps) \n')

if (sum_save == 0): save_png = 1
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}  #  Plotting output format, where [0] = NO and [1] = YES \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Spin_Texture/Spin_Texture_Video.py', 'w')
file.writelines(lines)
file.close()

#--------------------------------------------------------------------------
exec(open(dir_files + '/output/Spin_Texture/Spin_Texture_Video.py').read())
#--------------------------------------------------------------------------

#==========================================================================
   
print(" ")
print("=====================================================================")
print("= Edit the generated vectors, modifying the value of the variables ==")
print("= [factor], [thickness] and [length] in the Spin_Texture_Contour.py =")
print("= file generated in the output/Spin_Texture folder. =================")
print("=====================================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Completed =======================")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
